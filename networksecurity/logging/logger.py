import logging
import os
from datetime import datetime

# 1. Define the log file name
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# 2. Define the directory where logs will be stored
# This will create a 'logs' folder inside your current working directory 
LOG_DIR = os.path.join(os.getcwd(), 'logs')

# 3. Create the logs directory if it doesn't exist
# We only need to pass the directory path to os.makedirs
os.makedirs(LOG_DIR, exist_ok=True) 

# 4. Define the final, full path for the log file
# Join the directory path and the file name
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE) 

# 5. Configure logging with the correct file path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s  - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("NetworkSecurityLogger")