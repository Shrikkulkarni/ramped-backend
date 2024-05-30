import os

import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.job_search
collection = db.jobs

# Load sample job posting data
url = "https://docs.google.com/spreadsheets/d/1b0c1fbBuq4WNejtBi6IdPodOx74BG2-VwI1nGbyPHck/export?format=csv"
data = pd.read_csv(url)

# Clear existing data
collection.delete_many({})

# Insert data into MongoDB
collection.insert_many(data.to_dict("records"))

print("Data imported successfully.")
