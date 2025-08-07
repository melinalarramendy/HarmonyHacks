from flask import Flask
from flask_cors import CORS
import database as db

db = db.dbConnect()

app = Flask(__name__)
CORS(app)



if __name__ == '__main__':
    app.run(debug=True, port=5003)