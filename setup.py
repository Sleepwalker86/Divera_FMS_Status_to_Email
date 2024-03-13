import json

def create_config():
    config = {}
    print("DIVERA 24/7 Setup Hilfe.")
    print("Dieses Setup hilft dir die korrekte Config Datei für das Divera Script zu erstellen. Bitte trage deine Daten Schritt für Schritt ein.")
    # Die folgende Zeile setzt den Standardwert auf "DEIN-API-KEY", falls keine Eingabe erfolgt
    config["api_key"] = input("Bitte geben Sie den Privaten API-Schlüssel aus deinem Divera Account ein. (default: DEIN-API-KEY): ") or "DEIN-API-KEY"
    print("Modus 1 = Wenn sich der Status von 6 auf != 6 oder von !=6 auf 6 eine Mitteilung senden.")
    print("Modus 2 = Bei jeder Statusänderung eine Mitteilung senden.")
    print("Modus 3 = Wenn in den wunsch Status gewechselt wird.")
    # Die folgende Zeile setzt den Standardwert auf 2, falls keine Eingabe erfolgt
    config["mode"] = int(input("Bitte wählen Sie einen Modus. (default: 2): ") or 2)
    print("Bitte wählen deinen Ziel Status falls du Modus 3 gewählt hast.")
    # Die folgende Zeile setzt den Standardwert auf 2, falls keine Eingabe erfolgt
    config["destination_fms"] = int(input("Bitte geben Sie den Ziel-FMS-Status ein. (default: 2): ") or 2)
    # Die folgende Zeile setzt den Standardwert auf False, falls keine Eingabe erfolgt
    config["auto_archiv"] = input("Soll die Autoarchivierung für die Mitteilungen aktiviert werden? (true/false, default: false): ").lower() == "true"
    # Die folgende Zeile setzt den Standardwert auf 1, falls keine Eingabe erfolgt
    config["autoarchive_days"] = int(input("Bitte geben Sie die Anzahl der Tage für die Autoarchivierung ein. (default: 1): ") or 1)
    # Die folgende Zeile setzt den Standardwert auf 0, falls keine Eingabe erfolgt
    config["autoarchive_hours"] = int(input("Bitte geben Sie die Anzahl der Stunden für die Autoarchivierung ein. (default: 0): ") or 0)
    # Die folgende Zeile setzt den Standardwert auf 0, falls keine Eingabe erfolgt
    config["autoarchive_minutes"] = int(input("Bitte geben Sie die Anzahl der Minuten für die Autoarchivierung ein. (default: 0): ") or 0)
    # Die folgende Zeile setzt den Standardwert auf 0, falls keine Eingabe erfolgt
    config["autoarchive_seconds"] = int(input("Bitte geben Sie die Anzahl der Sekunden für die Autoarchivierung ein. (default: 0): ") or 0)
    # Die folgende Zeile setzt den Standardwert auf True, falls keine Eingabe erfolgt
    config["send_push"] = input("Soll das Senden von Push-Benachrichtigungen aktiviert werden? (true/false, default: false): ").lower() == "true"
    # Die folgende Zeile setzt den Standardwert auf False, falls keine Eingabe erfolgt
    config["send_mail"] = input("Soll das Senden von E-Mails aktiviert werden? (true/false, default: false): ").lower() == "true"
    print("Benachrichtigungs ID")
    print("3 = Ausgewählte Gruppen, 4 = Ausgewählte Benutzer")
    # Die folgende Zeile setzt den Standardwert auf 4, falls keine Eingabe erfolgt
    config["notification_type"] = input("Bitte geben Sie den Benachrichtigungstyp ein (default: 4): ") or "4"
    # Die folgende Zeile setzt den Standardwert auf True, falls keine Eingabe erfolgt
    config["private_mode"] = input("Soll der private Modus für die Mitteilung aktiviert werden? (true/false, default: false): ").lower() == "true"
    # Die folgende Zeile setzt den Standardwert auf ["220053"], falls keine Eingabe erfolgt
    config["users_primaerschluessel"] = [input("Bitte geben Sie den Primärschlüssel des Benutzers ein. (default: 220053): ") or "220053"]
    # Die folgende Zeile setzt den Standardwert auf ["138728"], falls keine Eingabe erfolgt
    config["groups_divera"] = [input("Bitte geben Sie die Divera-Gruppen-ID ein. (default: 138728): ") or "138728"]
    # Die folgende Zeile setzt den Standardwert auf "Änderung Fahrzeugstatus!", falls keine Eingabe erfolgt
    config["message_titel"] = input("Bitte geben Sie den Titel der Nachricht ein. (default: Änderung Fahrzeugstatus!): ") or "Änderung Fahrzeugstatus!"
    config["status_dict"] = {}

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    create_config()
