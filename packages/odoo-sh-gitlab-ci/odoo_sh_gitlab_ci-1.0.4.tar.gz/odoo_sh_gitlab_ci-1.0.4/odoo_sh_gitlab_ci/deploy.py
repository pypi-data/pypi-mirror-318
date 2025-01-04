import os
import subprocess
import logging
import tempfile

_logger = logging.getLogger(__name__)

def check_env_vars(required_vars):
    """Verifica que todas las variables de entorno necesarias estén definidas."""
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        _logger.error("Missing required environment variables:")
        for var in missing_vars:
            _logger.error(f"- {var}: Define it using 'export {var}=<value>'")
        exit(1)

def initialize_ssh_agent():
    """Inicia el agente SSH y añade la llave privada."""
    try:
        # Inicia el agente SSH
        ssh_agent_output = subprocess.check_output("eval $(ssh-agent -s)", shell=True, text=True)
        _logger.info(f"SSH agent output: {ssh_agent_output}")

        # Escribe la llave privada en un archivo temporal
        private_key = os.environ.get("PRIVATE_DEPLOY_KEY", "")
        if not private_key:
            raise ValueError("PRIVATE_DEPLOY_KEY is not set or empty.")

        with tempfile.NamedTemporaryFile(delete=False, mode="w") as key_file:
            key_file.write(private_key)
            key_file_name = key_file.name

        # Ajusta los permisos del archivo temporal
        os.chmod(key_file_name, 0o600)

        # Añade la llave privada desde el archivo temporal
        subprocess.run(f"ssh-add {key_file_name}", shell=True, check=True)
        _logger.info("SSH key added successfully.")

        # Elimina el archivo temporal
        os.unlink(key_file_name)
    except subprocess.CalledProcessError as e:
        _logger.error(f"Error initializing SSH agent: {e}")
        exit(1)
    except ValueError as e:
        _logger.error(f"Error: {e}")
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
        _logger.error(f"Error during deployment: {e}")
        exit(1)
