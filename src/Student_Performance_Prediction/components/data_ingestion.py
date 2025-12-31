import os
import sys
from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
import pandas as pd
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            #Reading code
            logging.info("Reading from MySQL database")
            os.mkdir(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to

            pass 
        except Exception as e:
            
            raise CustomException(e, sys)
        

