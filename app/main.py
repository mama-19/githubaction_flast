from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"status": "ok it work"})

@app.route("/health")
def health():
    return jsonify({"db_url": os.getenv("DATABASE_URL", "not set")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)