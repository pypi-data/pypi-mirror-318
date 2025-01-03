import re
import os
import sys
import subprocess
import requests


def sort_version(version):
    # Sort package versions from highest to lowest semantic version.
    # Dev versions are also sorted from highest to lowest and published
    # versions are sorted above their corresponding dev versions.
    # e.g. ['2.0.9', '2.0.9.dev1', '2.0.9.dev0', '2.0.8', '2.0.7']
    parts = version.split('.')
    major = int(parts[0])
    minor = int(parts[1])
    patch = int(parts[2])

    if len(parts) == 4:
        dev_rank = int(parts[3].split('dev')[1])
    else:
        dev_rank = float('inf')
    
    return (major, minor, patch, dev_rank)

def get_pkg_versions(from_jenkins, args):
    artifactory_url = ""
    
    if from_jenkins:
        auth = (args[0].split('=')[1], args[1].split('=')[1])
        artifactory_url = f'{args[2].split("=")[1]}/api/storage/{args[3].split("=")[1]}/{args[4].split("=")[1]}'
    else:
        username = os.environ.get('ARTIFACTORY_USER')
        password = os.environ.get('ARTIFACTORY_PWD')

        artifactory_base_url = os.environ.get('ARTIFACTORY_BASE_URL')
        arfifactory_repo = os.environ.get('ARTIFACTORY_REPO')
        artifactory_pkg = os.environ.get('ARTIFACTORY_PKG')

        if not username or not password or not artifactory_base_url or not arfifactory_repo or not artifactory_pkg:
            print("\nTo run this script, you need to add artifactory credentials and\n"
            "information about your artifactory package. This will allow the script to\n"
            "determine if there are any potential version conflicts with packages already\n"
            "published to artifactory. Add this information by running the following commands:\n\n"
            "  - export ARTIFACTORY_USER=artifactory_user\n"
            "  - export ARTIFACTORY_PWD=artifactory_pwd\n"
            "  - export ARTIFACTORY_BASE_URL=artifactory_base_url\n"
            "  - export ARTIFACTORY_REPO=artifactory_repo\n"
            "  - export ARTIFACTORY_PKG=artifactory_pkg\n"
            )
            sys.exit(1)
        else:
            auth = (os.environ['ARTIFACTORY_USER'], os.environ['ARTIFACTORY_PWD'])
            artifactory_url = f'{os.environ["ARTIFACTORY_BASE_URL"]}/api/storage/{os.environ["ARTIFACTORY_REPO"]}/{os.environ["ARTIFACTORY_PKG"]}'

    response = requests.get(artifactory_url, auth=auth).json()["children"]

    versions = [item["uri"][1:] for item in response]
    return sorted(versions, key=sort_version, reverse=True)

def has_open_pr(branch):
    github_org = os.environ.get('GITHUB_ORG')
    github_repo = os.environ.get('GITHUB_REPO')
    github_pat = os.environ.get('GITHUB_PAT')

    if not github_org or not github_repo or not github_pat:
        print("\nTo run this script, you need to add your GitHub Personal Access Token as\n"
        "well as information about your Github repository. This will allow the script to\n"
        "determine if there is an open PR for your branch and apply the vesrion bump rules\n"
        "accordingly. Add this information by running the following commands:\n\n"
        "  - export GITHUB_ORG=your_org"
        "  - export GITHUB_REPO=your_repo"
        "  - export GITHUB_PAT=your_token"
        )
        sys.exit(1)
    else:
        github_url = f'https://api.github.com/repos/{os.environ["GITHUB_ORG"]}/{os.environ["GITHUB_REPO"]}/pulls?state=open'

        headers = {
            'Authorization': f'token {os.environ["GITHUB_PAT"]}',
            'Accept': 'application/vnd.github.v3+json'
        }

        params = {
            'head': f'{os.environ["GITHUB_ORG"]}:{branch}',
            'state': 'open'
        }

        response = requests.get(github_url, headers=headers, params=params)
        return response.status_code == 200 and response.json()

def is_higher_semantic_version(old_version, new_version):
    old_version = old_version.split('.dev')[0]
    new_version = new_version.split('.dev')[0]

    old_version_components = list(map(int, old_version.split('.')))
    new_version_components = list(map(int, new_version.split('.')))
    return new_version_components > old_version_components

def get_valid_bump_versions(version):
    valid_versions = {
        'Major': f"{str(int(version.split('.')[0]) + 1)}.0.0",
        'Minor': f"{version.split('.')[0]}.{str(int(version.split('.')[1]) + 1)}.0",
        'Patch': f"{version.split('.')[0]}.{version.split('.')[1]}.{str(int(version.split('.')[2]) + 1)}"
    }

    return valid_versions

def check_bump_from_dev_version(old_version, new_version, latest_dev_version, latest_published_version):
    valid_release_version = old_version.split('.dev')[0]
    if 'dev' in new_version:
        # Example: 2.0.9.dev2 -> 2.0.9.dev3
        if new_version.split('.dev')[0] == valid_release_version:
            if int(new_version.split('.dev')[1]) == int(latest_dev_version.split('.dev')[1]) + 1:
                print("Version bumped successfully!")
            elif old_version != latest_dev_version and int(new_version.split('.dev')[1]) == int(old_version.split('.dev')[1]) + 1:
                print("\nThe version from your previous commit failed to upload to artifactory.\n"
                "This could occur due to various reasons such as syntax errors in Jenkinsfile_lib\n"
                "or if Artifactory was down during the previous publish attempt. Please revert your\n"
                "version bump and push your branch again so we can re-publish the failed version.\n"
                )
            else:
                print_error_message('invalid_bump_from_dev', old_version, latest_published_version)
        else:
            print_error_message('invalid_bump_from_dev', old_version, latest_published_version)
    else:
        # Example: 2.0.9.dev2 -> 2.0.9 
        if new_version == valid_release_version:
            if is_higher_semantic_version(new_version, latest_published_version):
                print_error_message('conflicting_bump_from_dev', old_version, latest_published_version)

            print("Version bumped successfully!")
            sys.exit(0)
        elif is_higher_semantic_version(valid_release_version, latest_published_version) and new_version in get_valid_bump_versions(latest_published_version).values():
            print("Version bumped successfully!")
            sys.exit(0)
        else:
            print_error_message('invalid_bump_from_dev', old_version, latest_published_version)

def check_bump_from_master_version(old_version, new_version, current_branch, highest_open_version):
    # Example: 2.0.8 -> 2.0.9.dev0
    if is_higher_semantic_version(old_version, new_version) and (new_version.endswith('.dev0') or '.dev' not in new_version):
        if not is_higher_semantic_version(highest_open_version, new_version):
            print_error_message('conflicting_bump_from_master', old_version, highest_open_version)
        else:
            print("Version bumped successfully!")
            sys.exit(0)
    else:
        highest_open_version = new_version if is_higher_semantic_version(highest_open_version, new_version) else highest_open_version
        print_error_message('invalid_bump_from_master', old_version, highest_open_version)

def print_error_message(error_type, old_version, potential_conflict_version):
    if "missing" in error_type:
        print("Oops! You forgot to bump the package version.")
    elif "invalid" in error_type:
        print("Oops! You didn't bump the package version correctly.")
    elif error_type == "conflicting_bump_from_master":
        print("Uh-oh! It looks like there's another branch already using that version.\n"
              "Additionaly, other branches might be using other versions above your desired version.")
    else:
        print("Uh-oh! The latest published package version is higher than your current version.")
    
    print("\nPlease bump your package as follows:")

    if "master" in error_type:
        version_to_bump = old_version

        if is_higher_semantic_version(old_version, potential_conflict_version):
            version_to_bump = potential_conflict_version

            # Precautionary message to alert the user of a potential conflict if they
            # don't currently have the conflicing version error
            if "conflicting" not in error_type:
                print("\n** NOTE: There is a higher package version in either master and/or another\n"
                "branch. The new bump versions reflect that to avoid a version mismatch. **\n")

        for version_type, valid_version in get_valid_bump_versions(version_to_bump).items():
            print(f"  - {version_type} changes to test: {old_version} -> {valid_version}.dev0")
            print(f"  - {version_type} changes ready to merge: {old_version} -> {valid_version}")
    
    elif "conflicting" in error_type:
        for version_type, valid_version in get_valid_bump_versions(potential_conflict_version).items():
            print(f"  - {version_type} changes ready to merge: {old_version} -> {valid_version}")
    else:
        new_dev_version = old_version.split('.dev')[0] + '.dev' + str(int(old_version.split('.dev')[1]) + 1)
        new_release_version = old_version.split('.dev')[0]

        print(f"  - New dev changes to test: {old_version} -> {new_dev_version}")
        if is_higher_semantic_version(new_release_version, potential_conflict_version):
            print("\n** NOTE: The package version in master is higher than your current version.\n"
            "The new release versions reflects that update to avoid a version mismatch with master. **\n")

            for version_type, valid_version in get_valid_bump_versions(potential_conflict_version).items():
                print(f"  - {version_type} changes ready to merge: {old_version} -> {valid_version}")
        else:
            print(f"  - Changes ready to merge: {old_version} -> {new_release_version}")

    print("\nOnce you have fixed the version, update your commit by running:\n"
          "  - git add pyproject.toml\n"
          "  - git commit --amend --no-edit\n\n"
          "Then push your branch again.\n\n"
          "If you are confident your version change is correct, you can skip this check\n"
          "by setting skip_check at the end of the script to True. In particular, this\n"
          "check may be incorrect after resolving a merge conflict. After setting\n"
          "skip_check to True, update your commit by running:\n"
          "  - git add check_version_bump.py\n"
          "  - git commit --amend --no-edit\n\n"
          "Then push your branch again."
    )
    sys.exit(1)

pr_input_message = '''
You are in the initial development stage. You can exit the initial development stage if you
are ready to test your and/or get feedback. Do you want to open a PR for your branch? (y/n):
'''

def main(from_jenkins, args):
    current_branch = subprocess.check_output(['git', 'branch', '--show-current'], universal_newlines=True).strip()
    pkg_versions = get_pkg_versions(from_jenkins, args)

    latest_published_version = next((version for version in pkg_versions if 'dev' not in version), "0.0.0")

    # Compare the version from the latest pushed state of your branch or master if your branch
    # has not been pushed to remote yet.
    try:
        if from_jenkins:
            # Since jenkins runs immediately after a new commit, we will need to compare that commit
            # to the commit before if to get the correct diff
            last_two_commits = subprocess.check_output(['git', 'log', '--format=%H', "-n", "2"], universal_newlines=True).splitlines()
            pyproject_diff = subprocess.check_output(['git', 'diff', last_two_commits[0], last_two_commits[1], '--', 'pyproject.toml'], universal_newlines=True)
        else:
            pyproject_diff = subprocess.check_output(['git', 'diff', current_branch, f'origin/{current_branch}', '--', 'pyproject.toml'], universal_newlines=True)
    except subprocess.CalledProcessError:
        pyproject_diff = subprocess.check_output(['git', 'diff', current_branch, 'origin/master', '--', 'pyproject.toml'], universal_newlines=True)

    if '+version' in pyproject_diff:
        old_version = re.search(r'\+version = "([^"]+)"', pyproject_diff).group(1) 
        new_version = re.search(r'\-version = "([^"]+)"', pyproject_diff).group(1)

        if from_jenkins or has_open_pr(current_branch):
            if 'dev' in old_version:
                latest_dev_version = next((version for version in pkg_versions if old_version.split('dev')[0] + 'dev' in version), old_version.split('dev')[0] + 'dev-1')
                check_bump_from_dev_version(old_version, new_version, latest_dev_version, latest_published_version)
            else:
                check_bump_from_master_version(old_version, new_version, current_branch, pkg_versions[0])
        else:
            # Attaches prompt to the user's dev terminal.
            with open('/dev/tty', 'r+') as tty:
                tty.write(pr_input_message)
                while True:
                    answer = tty.read(1)

                    if answer.lower() == 'y':
                        check_bump_from_master_version(old_version, new_version, current_branch, pkg_versions[0])
                    elif answer.lower() == 'n':
                        print("Oops! You changed the package version too early. Please undo the\n"
                              "version bump and wait until exiting the inital development stage\n"
                              "before bumping the version.\n")
                        sys.exit(1)
                    else:
                        tty.write("Invalid input. Please enter 'y' or 'n'.")
    else:
        with open('pyproject.toml', 'r') as f:
            content = f.read()
        current_version = re.search(r'version = "([^"]+)"', content).group(1)

        if from_jenkins or has_open_pr(current_branch):
            if current_version not in pkg_versions:
                # Addresses edge case where the package from the previous commit failed to publish
                # and the user thus needs to publish the same version again. This can occur for
                # example if the previous commit had syntax errors in Jenkinsfile_lib or if
                # Artifactory was down during the previous publish attempt.
                print("Version not bumped as expected.")
                sys.exit(0)
            else:
                print_error_message('missing_bump_from_dev', current_version, latest_published_version)
        else:
            highest_open_version = current_version if is_higher_semantic_version(pkg_versions[0], current_version) else pkg_versions[0]
            with open('/dev/tty', 'r+') as tty:
                tty.write(pr_input_message)
                while True:
                    answer = tty.read(1)

                    if answer.lower() == 'y':
                        print_error_message('missing_bump_from_master', current_version, highest_open_version)
                    elif answer.lower() == 'n':
                        print("Version not bumped in initial development stage as expected.")
                        sys.exit(0)
                    else:
                        tty.write("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    # Set this to True if you want to skip this check both locally and in Jenkins.
    skip_check = False

    if skip_check:
        print("Skipping the version bump check")
        sys.exit(0)
    else:
        args = sys.argv[1:]
        main(bool(args), args)
