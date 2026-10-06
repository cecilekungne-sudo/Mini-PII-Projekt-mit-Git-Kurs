# Flask brauchen wir für unseren kleinen Cloud-Webserver
from flask import Flask, request


# Unsere Webanwendung erstellen
app = Flask(__name__)

# Hier speichern wir die empfangenen Ereignisse
events = []

# Diese Funktion wird aufgerufen,
# wenn der Edge Daten an /data schickt
@app.route("/data", methods=["POST"])
def receive_data():

    # Die Daten vom Edge lesen
    data = request.json

    # Die Daten anzeigen
    print("Daten vom Edge:")
    print(data)

    # Ereignis in unserer Liste speichern
    events.append(data)

    # Anzahl der gespeicherten Ereignisse anzeigen
    print("Gespeicherte Ereignisse:", len(events))

    # Antwort an den Edge schicken
    return {"status": "Daten von Cloud empfangen"}


# Cloud-Server starten
app.run(host="0.0.0.0", port=6000)