
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ✅ Route GET simple pour vérifier que Render est actif
@app.route('/')
def home():
    return "✅ Render bot is online (route = /signal)", 200

# ✅ Route POST appelée par TradingView
@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json(force=True)
    print("📩 Signal reçu de TradingView :", data)

    # 🔁 Relai vers le VPS
    vps_url = "http://147.93.186.31:5000/signal"  # 🔁 Modifie l’IP si besoin

    try:
        response = requests.post(vps_url, json=data, timeout=5)
        print("✅ Signal transmis au VPS :", response.text)
    except Exception as e:
        print("❌ Échec de l’envoi au VPS :", str(e))
        return jsonify({"error": "Transmission échouée", "details": str(e)}), 500

    return jsonify({"status": "reçu", "forwarded_to": "VPS"}), 200

# ▶️ Lancement obligatoire sur Render (port défini par variable d’environnement)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
