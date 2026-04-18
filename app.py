from flask import Flask, request, jsonify
from flask_cors import CORS   # 👈 ADD THIS

app = Flask(__name__)
CORS(app)   # 👈 ADD THIS

@app.route('/')
def home():
    return "Backend Running 🚀"

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    print(data)
    return jsonify({"message": "Booking received"})
