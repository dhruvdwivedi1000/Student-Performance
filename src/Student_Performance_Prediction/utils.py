import os
import sys

import sklearn
from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

import numpy as np
import pymysql

# Load environment variables
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')   # should be "student_perfromance" in your .env

def read_sql_data():
    logging.info("Establishing connection to the database")
    try:
        # Create connection
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info(f"Connection established successfully: {mydb}")

        # Use pandas to read SQL query
        query = "SELECT * FROM student_perfromance"   # ✅ using old table name
        df = pd.read_sql_query(query, mydb)

        logging.info("Data fetched successfully from student_perfromance table")
        print(df.head())
        return df

    except Exception as ex:
        raise CustomException(ex, sys)

    finally:
        # Always close connection
        if 'mydb' in locals() and mydb.open:
            mydb.close()
            logging.info("Database connection closed")

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)