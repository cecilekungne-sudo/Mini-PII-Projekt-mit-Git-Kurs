# Wir brauchen json, um Daten schön anzuzeigen
import json

# Wir brauchen time, damit wir 3 Sekunden warten
import time

# Damit bekommen wir die aktuelle Uhrzeit
from datetime import datetime

# Damit können wir Daten über HTTP senden
import requests


# Adresse von unserem Processor
processor_url = "http://127.0.0.1:5000/data"


# Diese Schleife läuft immer weiter
while True:

    # Wir erstellen die Daten unserer Kamera
    data = {
        # Name der Kamera
        "device": "keenet-camera-01",

        # Aktuelle Uhrzeit
        "timestamp": datetime.now().isoformat(),

        # Was die Kamera erkannt hat
        "object": "person",

        # Sicherheit der Erkennung: 92 %
        "confidence": 0.92
    }

    # Die Daten werden weiterhin im Terminal angezeigt
    print(json.dumps(data, indent=2))

    # Die Daten werden an den Processor gesendet
    response = requests.post(processor_url, json=data)

    # Wir zeigen die Antwort des Processors an
    print("Antwort vom Processor:", response.json())

    # Wir warten 3 Sekunden
    time.sleep(3)