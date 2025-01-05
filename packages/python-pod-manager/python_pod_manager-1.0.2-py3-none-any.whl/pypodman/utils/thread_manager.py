from threading import Thread
from typing import Callable, Optional, Tuple, List
import logging
import sys
import time


class ThreadManager:
    def __init__(self):
        """Initialize the ThreadManager."""
        self.exit_flag = False
        self.threads = []

    def start_thread(self, target: Callable, args: Tuple = (), on_finish: Optional[Callable] = None) -> None:
        """
        Start a thread with the given target function and arguments.

        :param target: The function to run in the thread.
        :param args: Arguments to pass to the target function.
        :param on_finish: Optional callback to execute after the thread finishes.
        """
        def wrapper():
            try:
                if not self.exit_flag:
                    target(*args)
            except Exception as e:
                logging.error(f"Error in thread {target.__name__}: {e}")
            finally:
                if on_finish:
                    try:
                        on_finish()
                    except Exception as e:
                        logging.error(f"Error in on_finish callback: {e}")

        try:
            thread = Thread(target=wrapper)
            thread.daemon = True  # Daemon threads exit when the main program exits
            thread.start()
            self.threads.append(thread)
        except Exception as e:
            logging.error(f"Failed to start thread for {target.__name__}: {e}")
            sys.exit(1)  # Exit immediately if thread cannot be started

    def stop_threads(self) -> None:
        """
        Signal all threads to stop and clear the thread list.
        This sets the `exit_flag` to True, which threads should respect.
        """
        self.exit_flag = True
        for thread in self.threads:
            if thread.is_alive():
                logging.info(f"Stopping thread {thread.name}")
        self.threads.clear()

    def are_threads_alive(self) -> bool:
        """
        Check if any threads are still alive.

        :return: True if any threads are alive, False otherwise.
        """
        return any(thread.is_alive() for thread in self.threads)

    def join_threads(self, timeout: Optional[float] = None) -> None:
        """
        Wait for all threads to finish.

        :param timeout: Optional timeout in seconds to wait for each thread.
        """
        for thread in self.threads:
            try:
                thread.join(timeout=timeout)
            except Exception as e:
                logging.error(f"Error while joining thread {thread.name}: {e}")

    def run_threaded_tasks(self, tasks: List[dict]) -> None:
        """
        Run multiple tasks concurrently with optional finish functions.

        :param tasks: A list of dictionaries containing:
                      - 'target': The target function to run.
                      - 'args': Arguments for the function (default: []).
                      - 'on_finish': Optional callback when the thread finishes (default: None).
        """
        for task in tasks:
            try:
                target = task.get('target')
                args = task.get('args', [])
                on_finish = task.get('on_finish', None)
                self.start_thread(target, tuple(args), on_finish=on_finish)
            except Exception as e:
                logging.error(f"Failed to start task: {e}")
                sys.exit(1)  # Exit immediately if a task cannot be started

    def wait_for_threads(self) -> None:
        """Wait for all threads to finish."""
        try:
            for thread in self.threads:
                thread.join()
        except KeyboardInterrupt:
            logging.warning("KeyboardInterrupt detected. Stopping all threads...")
            self.handle_exit()

    def handle_exit(self):
        """
        Handle program exit gracefully by stopping all threads.
        Ensure immediate exit with `sys.exit(1)` to avoid continuation.
        """
        logging.info("Exiting program. Cleaning up threads...")
        self.stop_threads()
        self.join_threads()
        sys.exit(1)
