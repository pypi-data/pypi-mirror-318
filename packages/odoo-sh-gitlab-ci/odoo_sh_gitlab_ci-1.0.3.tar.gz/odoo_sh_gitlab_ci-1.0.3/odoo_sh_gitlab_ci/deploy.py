import os
import subprocess

def check_env_vars(required_vars):
    """Verifica que todas las variables de entorno necesarias estén definidas."""
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        print("Missing required environment variables:")
        for var in missing_vars:
            print(f"- {var}: Define it using 'export {var}=<value>'")
        exit(1)

def initialize_ssh_agent():
    """Inicia el agente SSH y añade la llave privada, replicando la lógica del archivo .gitlab-ci.yml."""
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
    except subprocess.CalledProcessError as e:
        print(f"Error initializing SSH agent: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

def odoo_sh_deploy():
    """Lógica principal para manejar el despliegue en Odoo.sh."""
    required_vars = [
        "PRIVATE_DEPLOY_KEY", "GITHUB_REPO", "GITHUB_REPO_NAME",
        "CI_COMMIT_REF_NAME", "CI_PROJECT_NAME", "CI_REPOSITORY_URL",
        "VERSION", "CI_SERVER_HOST", "CI_PROJECT_PATH"
    ]

    # Verifica las variables de entorno
    check_env_vars(required_vars)

    # Inicializa el agente SSH
    initialize_ssh_agent()

    try:
        # Configuración de SSH conocido
        os.makedirs(os.path.expanduser("~/.ssh"), exist_ok=True)
        os.chmod(os.path.expanduser("~/.ssh"), 0o700)
        subprocess.run("ssh-keyscan github.com >> ~/.ssh/known_hosts", shell=True, check=True)
        os.chmod(os.path.expanduser("~/.ssh/known_hosts"), 0o644)

        # Configuración de usuario Git
        subprocess.run("git config --global user.email 'info@jarsa.com'", shell=True, check=True)
        subprocess.run("git config --global user.name 'Jarsa'", shell=True, check=True)

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
