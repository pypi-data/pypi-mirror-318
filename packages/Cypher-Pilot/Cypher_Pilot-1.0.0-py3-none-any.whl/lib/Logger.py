import logging
import os

class Logger:
    _instance = None  # Class-level variable to store the singleton instance

    def __new__(cls, *args, **kwargs):
        """This method ensures only one instance of the Logger class exists."""
        if cls._instance is None:
            # If no instance exists, create it
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger(*args, **kwargs)
        return cls._instance

    def _initialize_logger(self, name="Log_File", log_file=None, level=logging.DEBUG):
        """Initialize the logger only once."""
        # Create a logger with the provided name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Define the log format
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(log_format)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Default log file in the root directory of the project (current working directory)
        if log_file is None:
            log_file = os.path.join(os.getcwd(), 'log.log')  # Default log path in current working directory

        # If a log file is provided, create a file handler
        if log_file:
            # Ensure the directory exists
            log_dir = os.path.dirname(log_file)
            if not os.path.exists(log_dir) and log_dir != '':  # Don't create a directory if the path is just a filename
                os.makedirs(log_dir)  # Create directory if it doesn't exist

            # Create and add file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        """Return the logger instance."""
        return self.logger
