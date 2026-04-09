from flask import Flask, request, jsonify
from main import process_identity

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    result = process_identity(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
