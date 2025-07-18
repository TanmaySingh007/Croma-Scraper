from flask import Flask, jsonify
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/scraped-content", methods=["GET"])
def get_scraped_content():
    data = r.get("scraped_content")
    if data is not None:
        if isinstance(data, bytes):
            data = data.decode("utf-8")
        if not isinstance(data, str):
            return jsonify({"success": False, "message": "Unexpected data type from Redis."}), 500
        return jsonify({"success": True, "data": json.loads(data)})
    else:
        return jsonify({"success": False, "message": "No data found"}), 404

@app.route("/products", methods=["GET"])
def get_products():
    data = r.get("products")
    if data is not None:
        if isinstance(data, bytes):
            data = data.decode("utf-8")
        if not isinstance(data, str):
            return jsonify({"success": False, "message": "Unexpected data type from Redis."}), 500
        return jsonify({"success": True, "products": json.loads(data)})
    else:
        return jsonify({"success": False, "message": "No products found"}), 404



if __name__ == "__main__":
    app.run(debug=True)