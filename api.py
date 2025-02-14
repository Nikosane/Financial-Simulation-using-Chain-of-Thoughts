from flask import Flask, request, jsonify
import requests
from config import CONFIG

app = Flask(__name__)

@app.route("/trade", methods=["POST"])
def trade():
    data = request.json
    trader_name = data.get("trader")
    decision = data.get("decision")
    asset = data.get("asset")
    quantity = data.get("quantity")
    price = data.get("price")
    
    if not all([trader_name, decision, asset, quantity, price]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    response_message = f"{trader_name} decided to {decision} {quantity} of {asset} at {price}"
    return jsonify({"message": response_message})

@app.route("/analyze_market", methods=["GET"])
def analyze_market():
    response = requests.get(CONFIG["deepseek_api"]["endpoint"])
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
