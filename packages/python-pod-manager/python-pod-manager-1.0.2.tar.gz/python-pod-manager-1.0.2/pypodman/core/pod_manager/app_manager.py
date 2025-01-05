import subprocess
import logging
import time
import atexit
import sys
from ..engine_manager.swarm_initializer import SwarmInitializer

class AppManager:
    def __init__(self, config: dict):
        """Initialize AppManager with configuration settings and setup cleanup."""
        try:
            self.config = config
            self.stack_name = self.config.get("stack_name")
            self.deployment_mode = self.config.get("deployment_mode")
            self.compose_file = self.config.get("compose_file")
            self.retry_attempts = self.config.get("retry_attempts", 3)
            self.retry_interval = self.config.get("retry_interval", 5)  # seconds

            self.app_started = False
            self.interrupt_count = 0

            atexit.register(self.stop_app)
        except Exception as e:
            logging.error(f"Initialization failed: {e}")
            sys.exit(1)

    def start_app(self):
        """Start the application using Docker Stack or Docker Compose based on configuration."""
        try:
            logging.info("Starting services...")
            self.app_started = True
            
            if self.deployment_mode == "stack":
                self._init_swarm_and_deploy()
            elif self.deployment_mode == "compose":
                self._run_subprocess(["docker", "compose", "-f", self.compose_file, "up", "-d"], "Starting with Docker Compose")

            self.wait_for_services()
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to start application: {e}")
        except KeyboardInterrupt:
            self.handle_interrupt()

    def stop_app(self):
        """Stop the application using Docker Stack or Docker Compose."""
        try:
            if not self.app_started:
                logging.info("Application was not started.")
                return
            logging.info("Stopping the application...")
            if self.deployment_mode == "stack":
                self._run_subprocess(["docker", "stack", "rm", self.stack_name], "Stopping Docker Stack")
                SwarmInitializer().leave_swarm()
                logging.info("Successfully left Docker Swarm.")
            elif self.deployment_mode == "compose":
                self._run_subprocess(["docker", "compose", "-f", self.compose_file, "down"], "Stopping Docker Compose")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to stop application: {e}")
        except KeyboardInterrupt:
            self.handle_interrupt()

    def restart_app(self):
        """Restart the application."""
        self.stop_app()
        self.start_app()

    def wait_for_services(self):
        """Wait and check if all services are running, retrying if necessary."""
        self._retry(self.check_services_status, self.retry_attempts, self.retry_interval)

    def check_services_status(self):
        """Check the status of services and return if all are running and their statuses."""
        service_status = {}
        try:
            if self.deployment_mode == "stack":
                return self._check_stack_services(service_status)
            elif self.deployment_mode == "compose":
                return self._check_compose_services(service_status)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to check services status: {e}")
            return False, service_status
        except KeyboardInterrupt:
            self.handle_interrupt()

    def handle_interrupt(self):
        """Handle KeyboardInterrupt gracefully."""
        self.interrupt_count += 1
        if self.interrupt_count == 1:
            logging.warning("Ctrl+C detected. Shutting down... (Press Ctrl+C again to force shutdown)")
            self.stop_app()
            sys.exit(0)
        elif self.interrupt_count >= 2:
            logging.critical("Force shutdown detected. Exiting immediately.")
            sys.exit(1)

    def _init_swarm_and_deploy(self):
        """Initialize Docker Swarm and deploy the stack."""
        SwarmInitializer().init_swarm()
        self._run_subprocess(
            ["docker", "stack", "deploy", "-c", self.compose_file, self.stack_name],
            "Starting with Docker Stack"
        )

    def _run_subprocess(self, command, action_desc, capture_output=False):
        """Utility method to run a subprocess command."""
        try:
            return subprocess.run(
                command,
                check=True,
                capture_output=capture_output,
                text=True
            )
        except subprocess.CalledProcessError as e:
            logging.error(f"{action_desc} failed: {e}")
            raise

    def _retry(self, func, attempts, interval, *args, **kwargs):
        """Retry a function a given number of times."""
        for attempt in range(1, attempts + 1):
            success, result = func(*args, **kwargs)
            if success:
                logging.info("All services started successfully.")
                return result
            else:
                logging.warning(f"Attempt {attempt}/{attempts}: Services not running.")
                time.sleep(interval)
        logging.error("Some services failed to start after multiple attempts.")
        return result

    def _check_stack_services(self, service_status):
        """Check the status of Docker Stack services."""
        result = self._run_subprocess(["docker", "service", "ls", "--format", "{{.Name}} {{.Replicas}}"], "Checking Docker Stack services", capture_output=True)
        services_status = result.stdout.strip().split("\n")
        for status in services_status:
            name, replicas = status.split()
            service_status[name] = replicas
            if self.stack_name in name and not replicas.startswith("1/1"):
                return False, service_status
        return True, service_status

    def _check_compose_services(self, service_status):
        """Check the status of Docker Compose services."""
        result = self._run_subprocess(["docker", "compose", "-f", self.compose_file, "ps"], "Checking Docker Compose services", capture_output=True)
        services_status = result.stdout.strip().split("\n")[2:]  # Skip headers
        for status in services_status:
            columns = status.split()
            service_name = columns[0]
            service_state = columns[-1]
            service_status[service_name] = service_state
            if "Up" not in service_state:
                return False, service_status
        return True, service_status
