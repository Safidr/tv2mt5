from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Test URL (GET)
@app.route('/', methods=['GET'])
def home():
    return "✅ Render Webhook is running"

# Webhook endpoint (POST from TradingView)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print("📩 Received from TradingView:", data)

    # VPS IP and Port
    vps_url = "http://147.93.186.31:5000/signal"  # ← Remplace si ton IP change

    try:
        response = requests.post(vps_url, json=data, timeout=5)
        print("↪️ Sent to VPS:", response.text)
    except Exception as e:
        print("❌ Failed to send to VPS:", str(e))

    return jsonify({"status": "received"}), 200

# Flask entrypoint for Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
