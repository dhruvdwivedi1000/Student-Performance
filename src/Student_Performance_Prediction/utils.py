import os
import sys
from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
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