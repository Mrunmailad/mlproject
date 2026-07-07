import logging
import os
from datetime import datetime

# 1. Create a unique string for the file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Point directly to a central 'logs' directory in your root folder
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# 3. Combine the logs directory path with your specific filename
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True # <--- CRITICAL: Prevents duplicate logging handlers during multi-file execution
)

if __name__ == "__main__":
    logging.info("Logging has started successfully.")