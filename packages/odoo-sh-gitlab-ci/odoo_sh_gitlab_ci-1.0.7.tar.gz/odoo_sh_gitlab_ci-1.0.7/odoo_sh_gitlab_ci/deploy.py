import os
import subprocess
import argparse


def check_env_vars(required_vars):
    """Verifica que todas las variables de entorno necesarias estén definidas."""
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        print("Missing required environment variables:")
        for var in missing_vars:
            print(f"- {var}: Define it using 'export {var}=<value>'")
        exit(1)


def initialize_environment():
    """Inicializa el agente SSH y realiza las configuraciones globales necesarias."""
    try:
        # Verifica si ssh-agent está disponible, si no, instala OpenSSH
        subprocess.run("command -v ssh-agent >/dev/null || ( apk add --update openssh )", shell=True, check=True)

        # Inicia el agente SSH
        ssh_agent_output = subprocess.check_output("eval $(ssh-agent -s)", shell=True, text=True)
        print(ssh_agent_output)

        # Asegúrate de que la variable PRIVATE_DEPLOY_KEY esté definida
        private_key = os.environ.get("PRIVATE_DEPLOY_KEY", "")
        if not private_key:
            raise ValueError("PRIVATE_DEPLOY_KEY is not set or empty.")

        # Añade la llave privada al agente SSH
        subprocess.run(f"echo \"{private_key}\" | tr -d '\\r' | ssh-add -", shell=True, check=True)
        print("SSH key added successfully.")

        # Configuración de SSH y Git
        os.makedirs(os.path.expanduser("~/.ssh"), exist_ok=True)
        os.chmod(os.path.expanduser("~/.ssh"), 0o700)
        subprocess.run("ssh-keyscan github.com git.jarsa.com git.vauxoo.com >> ~/.ssh/known_hosts", shell=True, check=True)
        os.chmod(os.path.expanduser("~/.ssh/known_hosts"), 0o644)
        subprocess.run("git config --global user.email 'jarsabot@jarsa.com'", shell=True, check=True)
        subprocess.run("git config --global user.name 'Jarsabot'", shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error initializing environment: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)


def deploy():
    """Lógica principal para manejar el despliegue en Odoo.sh."""
    required_vars = [
        "PRIVATE_DEPLOY_KEY", "GITHUB_REPO", "GITHUB_REPO_NAME",
        "CI_COMMIT_REF_NAME", "CI_PROJECT_NAME", "CI_REPOSITORY_URL",
        "VERSION", "CI_SERVER_HOST", "CI_PROJECT_PATH"
    ]

    # Verifica las variables de entorno
    check_env_vars(required_vars)

    try:
        # Clonar y actualizar submódulos
        subprocess.run(f"git clone --recurse-submodules -b production {os.environ['GITHUB_REPO']}", shell=True, check=True)
        os.chdir(os.environ["GITHUB_REPO_NAME"])
        subprocess.run("git submodule update --init --recursive", shell=True, check=True)
        subprocess.run("git submodule update --remote --force", shell=True, check=True)

        # Actualización de submódulos y commit
        updated_submodules = subprocess.check_output("git submodule status --recursive | awk '/^[+-]/ {print $2}'", shell=True).decode()
        commit_message = f"""Update submodules

Updated submodules:

{updated_submodules}"""
        subprocess.run(f"git commit -am \"{commit_message}\"", shell=True, check=True)
        subprocess.run("git push -f origin HEAD", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}")
        exit(1)


def main():
    parser = argparse.ArgumentParser(description="Manage Odoo.sh deployment.")
    parser.add_argument("--initialize", action="store_true", help="Initialize the environment (SSH agent, known hosts, Git config).")
    args = parser.parse_args()

    if args.initialize:
        initialize_environment()
    else:
        deploy()


if __name__ == "__main__":
    main()
