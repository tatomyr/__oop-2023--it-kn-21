from flask import Flask, jsonify
from models import User
from mongoengine import connect
from config import Config
from routes import equipment_bp

app = Flask(__name__)
connect(Config.DB_NAME, host=Config.DB_CONN_STRING)

if __name__ == '__main__':
    app.register_blueprint(equipment_bp, url_prefix='/equipment')
    app.run(debug=True, port=Config.PORT)
