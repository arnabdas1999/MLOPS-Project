import os
import sys
import json
from dotenv import load_dotenv
import certifi
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()

import pymongo
import pandas as pd
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict('records')
            return records 
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def push_data_to_mongodb(self, records, database, collection):
        try:
            self.database  = database
            self.records = records
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = r"Network_Data\\phisingData.csv"
    DATABASE = "ArnabAI"
    collection  = "networkData"
    networkObject = NetworkDataExtract()
    records = networkObject.csv_to_json(FILE_PATH)
    no_of_records = networkObject.push_data_to_mongodb(records, DATABASE, collection)             
    print(f"Number of records inserted to Mongodb Atlas: {no_of_records}")

