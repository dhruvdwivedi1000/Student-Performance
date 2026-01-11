from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
import sys
from src.Student_Performance_Prediction.components.data_ingestion import DataIngestion
from src.Student_Performance_Prediction.components.data_ingestion import DataIngestionConfig
from src.Student_Performance_Prediction.components.data_transformation import DataTransformation
from src.Student_Performance_Prediction.components.model_trainer import ModelTrainer, ModelTrainerConfig

if __name__ == "__main__":
    logging.info("Application started")
    # Your application code here
    logging.info("Application finished")

try:
    #data_ingestion_config = DataIngestionConfig()
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
    
    #Model Trainer
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))

   
except Exception as e:
    logging.info("Custom exception is being raised")
    raise CustomException(e, sys)