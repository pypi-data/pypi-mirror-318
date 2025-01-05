import yaml
import logging
import os
from typing import List, Dict, Any, Optional


class ConfigLoader:
    """Class to load and manage configuration settings from a YAML file."""
    REQUIREMENTS_KEY = 'requirements_file'

    DEFAULT_CONFIG = {
        'engine': {
            'name': 'docker',
            'rebuild': True
        },
        'isolation': {
            'enabled': True,
            'name': 'Code-Runner',
            'version': 'latest',
            'base_image': 'python:3.13-slim',
            'working_dir': '/app',
            'commands': [
                {
                    'name': 'COPY',
                    'command': '. /app'
                }
            ]
        },
        'library_pod': {
            'base_image': 'python:3.13-slim',
            'working_dir': '/app',
            'version': 'latest',
            'dedicated_pod': False,
            'pod_name': 'my_pod'
        },
        'commands': [
            {
                'name': 'RUN',
                'command': 'pip install {libraries} --target /app/lib'
            },
            {
                'name': 'CMD',
                'command': '["tail", "-f", "/dev/null"]'
            }
        ],
        'mount': {
            'host_mount_path': '~/Pypodmanager/lib',
            'pod_mount_path': '/app/lib'
        },
        'deployment': {
            'deployment_mode': 'compose',
            'stack_name': 'my_stack',
            'compose_file': 'docker-compose.yml',
            'retry_attempts': 3,
            'retry_interval': 5
        },
        'additional': {
            'logging': {
                'log_level': 'FATAL',
                'log_path': '~/Pypodmanager/logs',
                'log_file': 'Python_Pod_Manager.log'
            }
        }
    }

    def __init__(self, config_path: Optional[str] = None, cwd: Optional[str] = None):
        """Initialize the ConfigLoader with the path to the configuration file."""
        self.config_path = config_path or os.path.join(cwd or os.getcwd(), "config.yaml")
        self.config = self.load_config(self.config_path)
        self.config = self.merge_with_defaults(self.config, self.DEFAULT_CONFIG)
        
        self.check_critical_files()

    def check_critical_files(self):
        """Exit if both the configuration file and the requirements file are missing."""
        config_exists = os.path.isfile(self.config_path)
        requirements_exists = os.path.isfile(
            os.path.join(os.getcwd(), self.DEFAULT_CONFIG.get('libraries', {}).get(self.REQUIREMENTS_KEY, 'requirements.txt'))
        )

        if not config_exists and not requirements_exists:
            logging.error(f"Critical error: Neither configuration file nor requirements file found!")
            exit(1)
        elif not config_exists:
            logging.warning(f"Configuration file not found.")
        elif not requirements_exists:
            logging.warning(f"Requirements file not found.")

    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from a YAML file."""
        if not os.path.isfile(config_path):
            return {}

        try:
            with open(config_path, "r") as file:
                config_data = yaml.safe_load(file) or {}
                logging.info(f"Configuration loaded successfully from {config_path}")
                return config_data
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML configuration file at {config_path}: {e}")
            return {}

    def merge_with_defaults(self, user_config: Dict[str, Any], default_config: Dict[str, Any]) -> Dict[str, Any]:
        """Merge user configuration with default values recursively."""
        merged_config = default_config.copy()

        for key, value in user_config.items():
            if isinstance(value, dict) and key in default_config:
                merged_config[key] = self.merge_with_defaults(value, default_config[key])
            else:
                merged_config[key] = value

        return merged_config

    def get_library_names(self) -> List[str]:
        """Get library names and versions from the config, handling both list format and requirements files."""
        libraries = self.config.get("libraries", {})
        names = []

        if isinstance(libraries, dict):
            # Attempt to read libraries from a requirements file if specified
            names = self._get_libraries_from_requirements(libraries)
            if names:
                return names  # Return early if successful

        elif isinstance(libraries, list):
            # Process the libraries list if provided as dictionaries
            names = self._get_libraries_from_list(libraries)

        else:
            logging.warning("Unexpected format for 'libraries' section in the config.")
        
        return names

    def _get_libraries_from_requirements(self, libraries: Dict[str, Any]) -> List[str]:
        """Try to read libraries from a requirements file."""
        # First, check if a requirements file is specified in the config
        if self.REQUIREMENTS_KEY in libraries:
            path = libraries.get('path', os.getcwd())
            requirements_file_path = os.path.join(path, libraries[self.REQUIREMENTS_KEY])
            names = self._read_requirements_file(requirements_file_path)
            if names:
                return names  # Return early if successful

        # Fallback to the default requirements file in the current directory
        default_requirements_file = os.path.join(os.getcwd(), libraries.get(self.REQUIREMENTS_KEY, "requirements.txt"))
        return self._read_requirements_file(default_requirements_file)

    def _get_libraries_from_list(self, libraries: List[Dict[str, Any]]) -> List[str]:
        """Extract library names and versions from a list format."""
        names = []
        for lib in libraries:
            if isinstance(lib, dict):
                name = lib.get("name")
                version = lib.get("version")
                if name:
                    names.append(f"{name}=={version}" if version else name)
        return names

    def _read_requirements_file(self, filepath: str) -> List[str]:
        """Read a requirements file and return the list of libraries."""
        if os.path.isfile(filepath):
            try:
                with open(filepath, "r") as file:
                    libraries = [line.strip() for line in file if line.strip() and not line.startswith("#")]
                    logging.info(f"Successfully read libraries from {filepath}")
                    return libraries
            except IOError as e:
                logging.error(f"Error reading requirements file at {filepath}: {e}")
        else:
            logging.error(f"Requirements file not found at {filepath}")
        return []

    def get_deployment_config(self) -> Dict[str, Any]:
        """Get the deployment configuration from the main config."""
        return self.config.get("deployment")

    def get_additional_config(self) -> Dict[str, Any]:
        """Get the additional configuration from the main config."""
        return self.config.get("additional")

    def get_engine_config(self) -> Dict[str, Any]:
        """Get the engine configuration from the main config."""
        return self.config.get("engine")

    def get_isolation_config(self) -> Dict[str, Any]:
        """Get the isolation configuration from the main config."""
        return self.config.get("isolation")

    def validate_config(self) -> bool:
        """Validate the config to ensure necessary keys are present."""
        required_sections = ['libraries']
        missing_sections = [section for section in required_sections if section not in self.config]

        if missing_sections:
            logging.error(f"Missing required configuration sections: {', '.join(missing_sections)}")
            return False
        return True