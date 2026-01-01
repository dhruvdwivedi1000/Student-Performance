from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
import sys
from src.Student_Performance_Prediction.components.data_ingestion import DataIngestion
from src.Student_Performance_Prediction.components.data_ingestion import DataIngestionConfig
if __name__ == "__main__":
    logging.info("Application started")
    # Your application code here
    logging.info("Application finished")

try:
    #data_ingestion_config = DataIngestionConfig()
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()

   
except Exception as e:
    logging.info("Custom exception is being raised")
    raise CustomException(e, sys)