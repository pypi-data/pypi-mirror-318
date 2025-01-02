from datetime import datetime
import inspect, os

# Log level constants
DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3

def add_call_info(func):
    """Decorator to add filename, function name, and line number to log messages."""
    def wrapper(self, message, *args):
        caller_frame = inspect.currentframe().f_back
        full_path = caller_frame.f_code.co_filename
        filename = os.path.basename(full_path)
        function_name = caller_frame.f_code.co_name
        line_number = caller_frame.f_lineno
        # Append call info to the message
        enhanced_message = (
            f"(File: {filename}, Function: {function_name}, Line: {line_number}) {message}"
        )
        return func(self, enhanced_message, *args)
    return wrapper

class Logger:
    def __init__(self, level=INFO, app="Application"):
        """
        Initialize the Logger.

        :param level: Logging level (default is INFO)
        :param app: Name of the application (default is "Application")
        """
        self.level = level
        self.app = app
        self.log_messages = []

    def set_level(self, level):
        """
        Set the logging level.

        :param level: New logging level
        """
        self.level = level

    def _log(self, level_name, level, message):
        """
        Internal method to log a message if the level is appropriate.

        :param level_name: Name of the log level (e.g., "DEBUG")
        :param level: Numeric log level
        :param message: Log message
        """
        if self.level <= level:
            timestamp = datetime.now().isoformat()
            log_entry = f"{timestamp} {level_name} [{self.app}] {message}"
            self.log_messages.append(log_entry)

    @add_call_info
    def debug(self, message, *args):
        """Log a debug message."""
        self._log("DEBUG", DEBUG, message.format(*args))

    @add_call_info
    def info(self, message, *args):
        """Log an info message."""
        self._log("INFO", INFO, message.format(*args))

    @add_call_info
    def warn(self, message, *args):
        """Log a warning message."""
        self._log("WARN", WARN, message.format(*args))

    @add_call_info
    def error(self, message, *args):
        """Log an error message."""
        self._log("ERROR", ERROR, message.format(*args))

    def __str__(self):
        """Return all log messages as a single string."""
        return "\n".join(self.log_messages)

# Example usage
if __name__ == "__main__":
    # Create a logger instance
    logger = Logger(level=INFO, app="MyApp")

    # Log messages
    logger.debug("This is a debug message: {}", 42)  # Will not log (level too low)
    logger.info("This is an info message")
    logger.warn("This is a warning")
    logger.error("This is an error: {}", "something went wrong")

    # Change log level
    logger.set_level(DEBUG)
    logger.debug("Now debugging is enabled!")

    # Print all logs
    print(logger)
