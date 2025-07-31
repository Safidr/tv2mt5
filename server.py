

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Serveur Webhook actif"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print("📩 Données reçues de TradingView :", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
