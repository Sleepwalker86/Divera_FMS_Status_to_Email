import urllib.request
import json
import os
from datetime import datetime
import logging
import time

# Logger konfigurieren
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Erhalte den absoluten Pfad zur aktuellen Datei
current_directory = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(current_directory, 'config.json')

def load_config():
    if not os.path.exists(CONFIG_FILE):
        logger.info("Die Konfigurationsdatei '{}' existiert nicht.".format(CONFIG_FILE))
        logger.info("Bitte erstellen Sie eine Konfigurationsdatei mit den erforderlichen Informationen.")
        logger.info("Ein Beispiel für die Konfigurationsdatei könnte wie folgt aussehen:")
        logger.info("{")
        logger.info("    \"api_key\": \"YOUR-API-KEY\",")
        logger.info("    \"auto_archiv\": \"1\",")
        logger.info("    \"autoarchive_days\": 1,")
        logger.info("    \"autoarchive_hours\": 0,")
        logger.info("    \"autoarchive_minutes\": 0,")
        logger.info("    \"autoarchive_seconds\": 0,")
        logger.info("    \"send_push\": \"1\",")
        logger.info("    \"send_mail\": \"0\",")
        logger.info("    \"notification_type\": \"4\",")
        logger.info("    \"private_mode\": \"1\",")
        logger.info("    \"users_primaerschluessel\": [")
        logger.info("        \"User-Primärschlüssel\"")
        logger.info("    ],")
        logger.info("    \"groups_divera\": [")
        logger.info("        \"Gruppen-ID\"")
        logger.info("    ],")
        logger.info("    \"message_titel\": \"Änderung Fahrzeugstatus!\",")
        logger.info("    \"status_dict\": {}")
        logger.info("}")
        exit(1)
    with open(CONFIG_FILE) as f:
        config = json.load(f)
    return config

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def send_message(title, text, private_mode, notification_type, send_push, send_mail, ts_publish, archive, ts_archive, group, users_fremdschluessel, api_key):
    message_data = {
        "News": {
            "title": title,
            "text": text,
            "private_mode": private_mode,
            "notification_type": notification_type,
            "send_push": send_push,
            "send_mail": send_mail,
            "ts_publish": ts_publish,
            "archive": archive,
            "ts_archive": ts_archive,
            "group": group,
            "user_cluster_relation": users_fremdschluessel
        }
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    # URL für das senden der Nachricht definieren.
    message_url = f"https://app.divera247.com/api/v2/news?accesskey={api_key}"

    # Nachricht an DIVERA API senden.
    try:
        req = urllib.request.Request(message_url, method='POST', headers=headers)
        data = json.dumps(message_data).encode('utf-8')
        response = urllib.request.urlopen(req, data=data)
        result = json.loads(response.read().decode('utf-8'))
        if 'success' in result and result['success']:
            logging.info("Meldung erfolgreich gesendet.")
        else:
            logging.error("Fehler beim senden der Meldung. Antwort: %s", result)
    except Exception as e:
        logging.error("Es ist ein Fehler beim senden der Meldung aufgetreten: %s", e)

def archive_time(autoarchive_days, autoarchive_hours, autoarchive_minutes, autoarchive_seconds):
    if autoarchive_days == 0 and autoarchive_hours == 0 and autoarchive_minutes == 0 and autoarchive_seconds == 0:
        ts_archive = int(time.time()) + autoarchive_days * 86400 + 24 * 3600 + autoarchive_minutes * 60 + autoarchive_seconds
    else:
        ts_archive = int(time.time()) + autoarchive_days * 86400 + autoarchive_hours * 3600 + autoarchive_minutes * 60 + autoarchive_seconds

    return ts_archive

def main():
    # Parameter aus der config.json lesen
    config = load_config()
    api_key = config["api_key"]
    mode = config.get("mode", 1)
    destination_fms = config.get("destination_fms", 3)
    auto_archiv = config["auto_archiv"]
    autoarchive_days = config.get('autoarchive_days', 0)
    autoarchive_hours = config.get('autoarchive_hours', 0)
    autoarchive_minutes = config.get('autoarchive_minutes', 0)
    autoarchive_seconds = config.get('autoarchive_seconds', 0)
    send_push = config["send_push"]
    send_mail = config["send_mail"]
    private_mode = config["private_mode"]
    notification_type = config.get("notification_type", 4)
    users_primaerschluessel = config.get("users_primaerschluessel", [])
    groups_divera = config.get("groups_divera", [])
    message_titel = config["message_titel"]
    ts_publish = int(time.time())  # Aktueller Unix-Zeitstempel

    # Status jeder ID speichern
    status_dict = config.get("status_dict", {})

    # URL für den Abruf der Fahrzeugstatus definieren.
    url = f"https://app.divera247.com/api/v2/pull/vehicle-status?accesskey={api_key}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            for item in data["data"]:
                id = str(item["id"])  # ID als Zeichenkette speichern.
                fullname = item["fullname"]
                shortname = item["shortname"]
                fmsstatus = item["fmsstatus"]

                # Wenn die ID noch nicht im status_dict ist, wird sie hinzugefügt.
                if id not in status_dict:
                    status_dict[id] = fmsstatus
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Fahrzeug: {shortname} wurde hinzugefügt. Aktueller Status:", status_dict[id])
                else:
                    if mode == 1:
                        # Wenn sich der Status von 6 auf != 6 oder von !=6 auf 6 ändert, sende eine Mitteilung und aktualisiere den Status.
                        if (status_dict[id] == 6 and fmsstatus != 6) or (status_dict[id] != 6 and fmsstatus == 6):
                            logger.info("Mode: " + str(mode))
                            message = f"Das Fahrzeug ({shortname}) hat in den Status: {fmsstatus} gewechselt.\n Fahrzeugname: {fullname},\n Kurzname: {shortname},\n FMS Status: {fmsstatus}\n"
                            logger.info(message)
                            # Funktion zum senden der Mitteilung aufrufen.
                            send_message(message_titel, message, private_mode, notification_type, send_push, send_mail, ts_publish, auto_archiv, archive_time(autoarchive_days, autoarchive_hours, autoarchive_minutes, autoarchive_seconds), groups_divera, users_primaerschluessel, api_key)
                    elif mode == 2:
                        # Bei jeder Statusänderung eine Mitteilung senden.
                        if fmsstatus != status_dict[id]:
                            logger.info("Mode: " + str(mode))
                            message = f"Das Fahrzeug ({shortname}) hat in den Status: {fmsstatus} gewechselt.\n Fahrzeugname: {fullname},\n Kurzname: {shortname},\n FMS Status: {fmsstatus}\n"
                            logger.info(message)
                            # Funktion zum senden der Mitteilung aufrufen.
                            send_message(message_titel, message, private_mode, notification_type, send_push, send_mail, ts_publish, auto_archiv, archive_time(autoarchive_days, autoarchive_hours, autoarchive_minutes, autoarchive_seconds), groups_divera, users_primaerschluessel, api_key)
                    elif mode == 3:
                        # Wenn in den wunsch Status gewechselt wird.
                        if fmsstatus != status_dict[id] and fmsstatus == destination_fms:
                            logger.info("Mode: " + str(mode))
                            message = f"Das Fahrzeug ({shortname}) hat in den Status: {fmsstatus} gewechselt.\n Fahrzeugname: {fullname},\n Kurzname: {shortname},\n FMS Status: {fmsstatus}\n"
                            logger.info(message)
                            # Funktion zum senden der Mitteilung aufrufen.
                            send_message(message_titel, message, private_mode, notification_type, send_push, send_mail, ts_publish, auto_archiv, archive_time(autoarchive_days, autoarchive_hours, autoarchive_minutes, autoarchive_seconds), groups_divera, users_primaerschluessel, api_key)
                    # Aktualisiere den Status für die ID in der config.json.
                    status_dict[id] = fmsstatus

            # Speichere den Status in der Konfigurationsdatei config.json.
            config["status_dict"] = status_dict
            save_config(config)

    except Exception as e:
        logger.error("Fehler beim Abrufen der Daten:", e)

if __name__ == "__main__":
    main()
    logger.info("Script erfolgreich ausgeführt!")