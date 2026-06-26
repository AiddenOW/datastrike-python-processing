import os
import sys
from threading import Thread
from flask import Flask

# Mini serveur pour valider Render gratuitement
app = Flask('')

@app.route('/')
def home():
    return "Backend Datastrike en cours d'exécution (Mode Local)"

@app.route('/healthz')
def health():
    return "OK", 200

def run_fake_server():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    print("Démarrage du serveur de contournement Render...")
    # Lance Flask sur un autre fil
    Thread(target=run_fake_server).start()
    print("Serveur Web actif sur le port configuré.")
    
    # Ici, le script principal reste vivant sans chercher à appeler Kafka
    print("En attente de traitement des logs ScrimTime...")
