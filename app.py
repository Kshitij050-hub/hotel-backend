from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend Running"

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    print(data)
    return jsonify({"message": "Booking received"})

if __name__ == '__main__':
    app.run()