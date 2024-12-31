# File: cli.py
import os
import subprocess
import sys
import shutil
import tempfile
import re
from pathlib import Path
from importlib import resources  # Python 3.9+

def read_existing_env(env_path):
    existing_vars = {}
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    existing_vars[key.strip()] = value.strip()
    return existing_vars

def validate_port(port):
    try:
        port = int(port)
        return 1024 <= port <= 65535
    except ValueError:
        return False

def validate_hostname(hostname):
    if not hostname:
        return False
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}|[a-zA-Z0-9\.-]+$')
    return bool(ip_pattern.match(hostname))

def prompt_for_three_vars(existing_vars):
    """Prompt ONLY for NODE_PORT, NODE_TCP_PORT, ADVERTISE_IP.
    If user hits Enter, keep existing .env value or use defaults."""

    # 1) NODE_PORT
    default_node_port = existing_vars.get('NODE_PORT', '8000')
    while True:
        node_port = input(
            f"Enter NODE_PORT (press Enter for default {default_node_port}): "
        ).strip()
        if not node_port:
            node_port = default_node_port
        if validate_port(node_port):
            existing_vars["NODE_PORT"] = node_port
            break
        print("Invalid port! Must be between 1024 and 65535.")

    # 2) NODE_TCP_PORT
    default_tcp_port = existing_vars.get('NODE_TCP_PORT', '8500')
    while True:
        node_tcp_port = input(
            f"Enter NODE_TCP_PORT (press Enter for default {default_tcp_port}): "
        ).strip()
        if not node_tcp_port:
            node_tcp_port = default_tcp_port
        if validate_port(node_tcp_port):
            existing_vars["NODE_TCP_PORT"] = node_tcp_port
            break
        print("Invalid port! Must be between 1024 and 65535.")

    # 3) ADVERTISE_IP
    default_ip = existing_vars.get('ADVERTISE_IP', 'localhost')
    while True:
        advertise_ip = input(
            f"Enter ADVERTISE_IP (e.g., example.com) [default {default_ip}]: "
        ).strip()
        if not advertise_ip:
            advertise_ip = default_ip
        if validate_hostname(advertise_ip):
            existing_vars["ADVERTISE_IP"] = advertise_ip
            break
        print("Invalid hostname/IP! Please enter a valid hostname or IP address.")

def write_env(env_path, vars_dict):
    try:
        with open(env_path, 'w') as f:
            for k, v in vars_dict.items():
                f.write(f"{k}={v}\n")
    except Exception as e:
        print(f"Error writing .env: {e}")
        sys.exit(1)

def up(detached=False):
    """
    Bring up Docker containers. If detached=True, run docker compose in '-d' mode.
    """
    print("\nSetting up environment variables...")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Copy Dockerfile + docker-compose.yml from inside the package
        docker_dir = resources.files("sokoweb.docker")
        shutil.copyfile(docker_dir / "Dockerfile", temp_path / "Dockerfile")
        shutil.copyfile(docker_dir / "docker-compose.yml", temp_path / "docker-compose.yml")

        # Now handle the .env. If the user already has .env in their project,
        # copy it in if it exists:
        env_path = temp_path / ".env"
        user_env = Path.cwd() / ".env"
        if user_env.exists():
            shutil.copyfile(user_env, env_path)

        existing_vars = read_existing_env(env_path)
        # Prompt ONLY for the 3 required variables (others remain from .env)
        prompt_for_three_vars(existing_vars)

        # 1) If ADVERTISE_IP == 'localhost', set BOOTSTRAP_NODES to an empty string
        if existing_vars.get("ADVERTISE_IP", "") == "localhost":
            existing_vars["BOOTSTRAP_NODES"] = ""

        # Write them back to .env
        write_env(env_path, existing_vars)

        print("\nUpdated environment variables (from .env in the temp directory):")
        for k, v in existing_vars.items():
            print(f"{k}={v}")

        # Start Docker
        print("\nStarting Docker containers...")
        compose_cmd = ["docker", "compose", "-f", "docker-compose.yml", "up", "--build"]
        if detached:
            compose_cmd.append("-d")
        try:
            process = subprocess.run(
                compose_cmd,
                check=True,
                cwd=str(temp_path)
            )
            if process.returncode == 0:
                if detached:
                    print("Successfully started Docker containers in detached mode.")
                else:
                    print("Successfully started Docker containers.")
        except subprocess.CalledProcessError as e:
            print(f"Error starting Docker containers (exit code={e.returncode})")
            sys.exit(e.returncode)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            sys.exit(1)

def down():
    """
    Stop/remove containers (and volumes). For simplicity, look for a docker-compose.yml
    in the current directory or let user specify.
    """
    print("Stopping Docker containers and removing volumes...")
    # This function might assume there's a docker-compose.yml in the current directory
    # or rely on a known path. Adapt as needed:
    docker_compose_file = Path.cwd() / "docker-compose.yml"
    if not docker_compose_file.exists():
        print("No docker-compose.yml found in the current directory.")
        return

    try:
        subprocess.run(
            ["docker", "compose", "-f", str(docker_compose_file), "down", "-v"],
            check=True
        )
        print("Successfully stopped and removed containers/volumes.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping Docker containers (exit code={e.returncode})")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    """
    If someone calls python cli.py [options], we’ll parse arguments quickly:
    -d or --detached to run up() in detached mode
    down to run down()
    """
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "down":
            down()
        elif arg in ["-d", "--detached"]:
            up(detached=True)
        else:
            # fallback, maybe they want up with no special arguments
            up(detached=False)
    else:
        # default
        up(detached=False)