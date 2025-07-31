from flask import Flask, request, jsonify

app = Flask(__name__)

# Route GET pour vérifier que le serveur fonctionne
@app.route('/', methods=['GET'])
def home():
    return "Serveur en ligne ✅"

# Route POST pour recevoir les alertes TradingView
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("✅ Alerte reçue :", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
