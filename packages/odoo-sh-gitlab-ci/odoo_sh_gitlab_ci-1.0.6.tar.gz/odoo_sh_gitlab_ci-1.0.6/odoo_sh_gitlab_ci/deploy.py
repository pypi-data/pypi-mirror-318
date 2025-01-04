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

def odoo_sh_deploy():
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
        _logger.error(f"Error during deployment: {e}")
        exit(1)
