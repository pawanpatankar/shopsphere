from flask import Flask, jsonify
from common_lib.logger import log

app = Flask(__name__)

@app.route("/")
def home():
    log("User Service called")
    return jsonify(service="user-service", status="running")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
