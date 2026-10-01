# Flask brauchen wir, um einen kleinen Webserver zu erstellen
from flask import Flask, request


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

    # Antwort an die Kamera schicken
    return {"status": "Daten empfangen"}


# Server starten
app.run(host="0.0.0.0", port=5000)