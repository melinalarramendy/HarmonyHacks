from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def dbConnect():
    try:
        client = MongoClient(os.getenv("MONGO_URI"), connectTimeoutMS=5000, serverSelectionTimeoutMS=5000)
        print("Conexión exitosa a la base de datos")
        db = client["harmonyhacks_db"]
        return db
    except ConnectionError as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise
    
