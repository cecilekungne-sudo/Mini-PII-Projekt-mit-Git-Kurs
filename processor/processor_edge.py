# Flask brauchen wir, um einen kleinen Webserver zu erstellen
from flask import Flask, request

# Damit können wir Daten an die Cloud senden
import requests


# Adresse von unserer Cloud
cloud_url = "http://127.0.0.1:6000/data"


# Unsere Webanwendung erstellen
app = Flask(__name__)


# Diese Funktion wird aufgerufen,
# wenn Daten an /data geschickt werden
@app.route("/data", methods=["POST"])
def receive_data():

    # Die gesendeten Daten lesen
    data = request.json

    # Die Daten anzeigen
    print("Daten von der Kamera:")
    print(data)

    # Wir prüfen die Sicherheit der Erkennung
    if data["confidence"] >= 0.80:

        # Die Erkennung ist ausreichend sicher
        data["edge_status"] = "Person erkannt"

    else:

        # Die Erkennung ist nicht sicher genug
        data["edge_status"] = "Unsichere Erkennung"

    # Daten an die Cloud weiterleiten
    response = requests.post(
        cloud_url,
        json=data
    )

    # Antwort von der Cloud anzeigen
    print("Antwort von der Cloud:")
    print(response.json())

    # Antwort an die Kamera schicken
    return {"status": "Daten empfangen"}


# Server starten
app.run(host="0.0.0.0", port=5000)