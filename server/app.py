from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS
import database as db


load_dotenv()

db = db.dbConnect()


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "¡Funciona!"


if __name__ == '__main__':
    app.run(debug=True, port=5003)