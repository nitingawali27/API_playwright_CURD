import logging
import os
from datetime import datetime

# Create Logs folder if it doesn't exist
log_folder = r"D:\Playwright_Automation\Logs"
os.makedirs(log_folder, exist_ok=True)

# Generate log file name with date & time
log_file = os.path.join(log_folder, f"api_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Create logger
logger = logging.getLogger("API_Logger")
logger.setLevel(logging.INFO)  # Set minimum log level

# Create file handler to save logs to the file
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Create simple formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
if not logger.handlers:
    logger.addHandler(file_handler)

# Optional: print the log file path
print("Logs will be saved at:", log_file)
