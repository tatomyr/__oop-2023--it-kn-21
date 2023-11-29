from flask import Flask, jsonify
from mongoengine import connect
from config import Config

app = Flask(__name__)
connect(Config.DB_NAME, host=Config.DB_CONN_STRING)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Everything is fine"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=Config.PORT)
