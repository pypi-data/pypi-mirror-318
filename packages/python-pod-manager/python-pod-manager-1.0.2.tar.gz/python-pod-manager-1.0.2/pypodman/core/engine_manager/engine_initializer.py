from colorama import Fore, init
import subprocess
import logging
import shutil
import os
import grp

init(autoreset=True)

# Supported and exempted container engines
SUPPORTED_ENGINES = ["podman", "docker"]
EXEMPT_ENGINES = ["podman"]  # Engines that don't require a service or group

class EngineInitializer:
    """Initialize and check the status of the container engine."""

    def __init__(self, config: dict):
        self.engine_name = config.get("name").lower()

    def initialize_engine(self) -> bool:
        """Initialize the Container Engine based on the configuration."""
        if not self.is_engine_installed(self.engine_name):
            logging.error(f"{self.engine_name.capitalize()} is not installed.")
            print(Fore.RED + f"{self.engine_name.capitalize()} is not installed.")
            return False

        # Skip group and service checks for exempted engines like podman
        if self.engine_name not in EXEMPT_ENGINES and not self.has_access_to_engine(self.engine_name):
            logging.error(f"{self.engine_name.capitalize()} is installed but you lack access permissions.")
            print(Fore.YELLOW + f"{self.engine_name.capitalize()} is installed but you lack access permissions.")
            print(Fore.CYAN + f"Add your user to the '{self.engine_name}' group and log out/back in to gain access.")
            return False

        if self.is_engine_running(self.engine_name):
            logging.info(f"{self.engine_name.capitalize()} is installed, accessible, and running.")
            print(Fore.GREEN + f"{self.engine_name.capitalize()} is installed, accessible, and running.")
            return True
        else:
            logging.warning(f"{self.engine_name.capitalize()} is installed but not running.")
            print(Fore.YELLOW + f"{self.engine_name.capitalize()} is installed but not running.")
            
            if self.engine_name in EXEMPT_ENGINES:
                logging.info(f"{self.engine_name.capitalize()} does not require a running service.")
                print(Fore.GREEN + f"{self.engine_name.capitalize()} does not require a running service.")
                return True  # For engines like Podman, not needing a service is normal.

            response = input(Fore.YELLOW + f"Would you like to try starting {self.engine_name}? (Y/n): ").strip().lower() or 'y'
            if response == 'y':
                if self.try_start_engine(self.engine_name):
                    logging.info(f"{self.engine_name.capitalize()} has been started successfully.")
                    print(Fore.GREEN + f"{self.engine_name.capitalize()} has been started successfully.")
                    return True
                else:
                    logging.error(f"Failed to start {self.engine_name}. Please check the service manually.")
                    print(Fore.RED + f"Failed to start {self.engine_name}. Please check the service manually.")
                    return False
            else:
                logging.info("User chose not to attempt starting the engine.")
                print(Fore.CYAN + "User chose not to attempt starting the engine.")
                return False

    def is_engine_installed(self, engine_name: str) -> bool:
        """Check if the specified container engine is installed."""
        if engine_name not in SUPPORTED_ENGINES:
            logging.error(f"Unsupported engine '{engine_name}' specified.")
            print(Fore.RED + f"Unsupported engine '{engine_name}' specified.")
            return False

        if shutil.which(engine_name) is None:
            return False
        return True

    def has_access_to_engine(self, engine_name: str) -> bool:
        """Check if the current user has access to the container engine."""
        if engine_name in EXEMPT_ENGINES:
            return True  # Engines like Podman don't require a specific user group

        try:
            user_groups = [grp.getgrgid(g).gr_name for g in os.getgroups()]
            required_group = engine_name
            if required_group in user_groups:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"Error checking access permissions for {engine_name}: {e}")
            print(Fore.RED + f"Error checking access permissions for {engine_name}: {e}")
            return False

    def is_engine_running(self, engine_name: str) -> bool:
        """Check if the container engine is running."""
        if engine_name in EXEMPT_ENGINES:
            return True  # Podman doesn't require a running service for its CLI

        try:
            result = subprocess.run(
                [engine_name, "ps"], capture_output=True, text=True
            )
            if result.returncode == 0:
                return True
            else:
                # If ps fails, try checking if the service is running (for engines like Docker)
                return self.is_service_running(engine_name)
        except Exception as e:
            logging.error(f"Error checking {engine_name} status: {e}")
            print(Fore.RED + f"Error checking {engine_name} status: {e}")
            return False

    def is_service_running(self, engine_name: str) -> bool:
        """Check if the service for an engine like Docker is running."""
        try:
            result = subprocess.run(
                ["systemctl", "is-active", "--quiet", f"{engine_name}.service"], capture_output=True
            )
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            logging.error(f"Error checking service status for {engine_name}: {e}")
            return False

    def try_start_engine(self, engine_name: str) -> bool:
        """Try to start the container engine service."""
        if engine_name in EXEMPT_ENGINES:
            logging.info(f"{engine_name.capitalize()} does not require starting a service.")
            print(Fore.GREEN + f"{engine_name.capitalize()} does not require starting a service.")
            return True  # Podman doesn't require a service

        try:
            subprocess.run(["systemctl", "start", f"{engine_name}.service"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to start {engine_name}: {e}")
            print(Fore.RED + f"Failed to start {engine_name}: {e}")
            return False
