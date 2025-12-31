from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
import sys
if __name__ == "__main__":
    logging.info("Application started")
    # Your application code here
    logging.info("Application finished")

try:
    # Simulating an error for demonstration
    a=1 / 0
except Exception as e:
    logging.info("Custom exception is being raised")
    raise CustomException(e, sys)