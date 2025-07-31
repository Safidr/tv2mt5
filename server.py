
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ✅ Route GET pour vérifier si Render est en ligne
@app.route('/')
def home():
    return "✅ Render Webhook is running"

# ✅ Route POST utilisée par TradingView
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print("📩 Received from TradingView:", data)

    # ✅ Adresse publique et route correcte du VPS
    vps_url = "http://147.93.186.31:5000/signal"  # Change IP si besoin

    try:
        response = requests.post(vps_url, json=data, timeout=5)
        print("✅ Sent to VPS:", response.text)
    except Exception as e:
        print("❌ Failed to send to VPS:", str(e))

    return jsonify({"status": "received"}), 200

# ✅ Lancement sur Render (le port est imposé par Render via variable d'environnement)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
