import os
import sys
import logging

# Define the logging format:
# - %(asctime)s: Timestamp of the log entry
# - %(levelname)s: Logging level (e.g., INFO, DEBUG, ERROR)
# - %(module)s: Module where the log entry was generated
# - %(message)s: The actual log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory where log files will be stored
log_dir = "logs"

# Construct the full file path for the log file (running_logs.log)
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Specify the format for log messages
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages to a file
        logging.StreamHandler(sys.stdout)  # Also output log messages to the console
    ]
)

# Create a logger object named "cnnProjectLogger" for consistent logging across the project
logger = logging.getLogger("cnnProjectLogger")

# Example usage of the logger to verify setup
logger.info("Logging setup complete. Logs will be saved to %s", log_filepath)

# Check logging is working:
if __name__=='__main__':
    logging.info("Logging is working")
