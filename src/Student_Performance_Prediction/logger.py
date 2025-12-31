import logging 
import os
from datetime import datetime

Log_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", Log_FILE)
os.makedirs(logs_path, exist_ok=True)

Log_FILE_PATH = os.path.join(logs_path, Log_FILE)

logging.basicConfig(
    filename=Log_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s",
    level=logging.INFO,
)