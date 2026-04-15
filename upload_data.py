from pymongo import MongoClient
import pandas as pd

# Read CSV
df = pd.read_csv("pollution.csv")

# Convert to dictionary
data = df.to_dict(orient="records")

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["pollution_db"]
collection = db["pollution"]

# Insert data
collection.insert_many(data)

print("✅ Data inserted successfully!")