import os
import sys
import json

import pymongo
from dotenv import load_dotenv
load_dotenv()
Mongo_db_url=os.getenv('MONGODB_url')
print(Mongo_db_url)
import certifi
ca=certifi.where()
import numpy as np
import pandas as pd
from NetworkSecurity.exception.exception import MyException
from NetworkSecurity.logger.logger import logging
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise MyException(e,sys)
    def CovertsIntoJson(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise MyException(e,sys)
    def PushingDataIntoMongoDB(self,records,database,collection):
        try:
            self.records=records
            self.database=database
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(Mongo_db_url)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise MyException(e,sys)
if __name__=="__main__":
    FILE_PATH='Network_data\\NetworkData.csv'
    DATABASE="mlcluster"
    COLLECTION="NETWORK_SEQURITY"
    networkobj=NetworkDataExtract()
    records= networkobj.CovertsIntoJson(FILE_PATH)
    no_of_records=networkobj.PushingDataIntoMongoDB(records,DATABASE,COLLECTION)
    print(no_of_records)