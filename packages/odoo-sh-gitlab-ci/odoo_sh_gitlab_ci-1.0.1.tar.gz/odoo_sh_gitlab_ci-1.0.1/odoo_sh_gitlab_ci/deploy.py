import os
import subprocess

def check_env_vars(required_vars):
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        print("Missing required environment variables:")
        for var in missing_vars:
            print(f"- {var}: Define it using 'export {var}=<value>'")
        exit(1)

def odoo_sh_deploy():
    required_vars = [
        "PRIVATE_DEPLOY_KEY", "GITHUB_REPO", "GITHUB_REPO_NAME",
        "CI_COMMIT_REF_NAME", "CI_PROJECT_NAME", "CI_REPOSITORY_URL",
        "VERSION", "CI_SERVER_HOST", "CI_PROJECT_PATH"
    ]

    check_env_vars(required_vars)

    try:
        # Initialize SSH agent and add private key
        subprocess.run("command -v ssh-agent >/dev/null || ( apk add --update openssh )", shell=True, check=True)
        subprocess.run("eval $(ssh-agent -s)", shell=True, check=True)
        subprocess.run(f"echo \"$PRIVATE_DEPLOY_KEY\" | tr -d '\\r' | ssh-add -", shell=True, check=True)

        # Configure SSH known hosts
        os.makedirs(os.path.expanduser("~/.ssh"), exist_ok=True)
        os.chmod(os.path.expanduser("~/.ssh"), 0o700)
        subprocess.run("ssh-keyscan github.com >> ~/.ssh/known_hosts", shell=True, check=True)
        os.chmod(os.path.expanduser("~/.ssh/known_hosts"), 0o644)

        # Configure Git user
        subprocess.run("git config --global user.email 'info@jarsa.com'", shell=True, check=True)
        subprocess.run("git config --global user.name 'Jarsa'", shell=True, check=True)

        # Clone and update submodules
        subprocess.run(f"git clone --recurse-submodules -b production {os.environ['GITHUB_REPO']}", shell=True, check=True)
        os.chdir(os.environ["GITHUB_REPO_NAME"])
        subprocess.run("git submodule update --init --recursive", shell=True, check=True)
        subprocess.run("git submodule update --remote --force", shell=True, check=True)

        # Update submodules and commit changes
        updated_submodules = subprocess.check_output("git submodule status --recursive | awk '/^[+-]/ {print $2}'", shell=True).decode()
        commit_message = f"""Update submodules

Updated submodules:

{updated_submodules}"""
        subprocess.run(f"git commit -am \"{commit_message}\"", shell=True, check=True)
        subprocess.run("git push -f origin HEAD", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}")
        exit(1)
