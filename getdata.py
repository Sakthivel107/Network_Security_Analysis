import os
import sys
import json


from dotenv import load_dotenv
load_dotenv()
Mongo_db_url=os.getenv('MONGODB_url')
print(Mongo_db_url)
import certifi
ca=certifi.where()
import numpy as np
import pandas as pd
