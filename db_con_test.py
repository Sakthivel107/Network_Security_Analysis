
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url= "mongodb+srv://Sakthivel:8072656893@mlcluster.33fsw.mongodb.net/?retryWrites=true&w=majority&appName=MLcluster"

# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)