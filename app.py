from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Connection URI
MONGO_URI = "mongodb+srv://Harsha1234:Harsha1234@cluster1.nwz3t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

try:
    client = MongoClient(MONGO_URI)
    db = client["user_db"]
    user_collection = db["user_data"]
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    client = None

@app.route("/add_user", methods=["POST"])
def add_user():
    if client is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    # Get data from the Unity request (JSON)
    user_data = request.json
    try:
        # Insert the data into MongoDB
        user_collection.insert_one(user_data)
        return jsonify({"message": "User data added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to add user: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
