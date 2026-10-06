# Wir brauchen json, um Daten schön anzuzeigen
import json

# Wir brauchen time, damit wir 3 Sekunden warten
import time

# Damit bekommen wir die aktuelle Uhrzeit
from datetime import datetime

# Damit können wir Daten über HTTP senden
import requests


# Adresse von unserem Edge Processor
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

    # Die Daten im Terminal anzeigen
    print(json.dumps(data, indent=2))

    try:

        # Die Daten an den Edge Processor senden
        response = requests.post(
            processor_url,
            json=data,
            timeout=5
        )

        # Antwort des Edge Processors anzeigen
        print("Antwort vom Processor:", response.json())

    except requests.exceptions.RequestException as error:

        # Falls der Edge nicht erreichbar ist
        print("Edge Processor nicht erreichbar!")
        print(error)

    # 3 Sekunden warten
    time.sleep(3)