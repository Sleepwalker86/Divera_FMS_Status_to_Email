# Fahrzeugstatusüberwachungs Skript für Divera 24/7

Dieses Python-Skript überwacht den Status von Fahrzeugen und benachrichtigt Benutzer per Divera Mitteilung,
wenn ein Fahrzeugstatus wechselt. Es gibt verschiedene Modis um das versenden der Mitteilung anzustoßen:

Modus 1 = Wenn sich der Status von 6 auf ungleich 6 oder von ungleich 6 auf 6 ändert wird eine Mitteilung gesendet.

Modus 2 = Bei jeder Statusänderung eine Mitteilung senden.

Modus 3 = Sendet eine Mitteilung, wenn ein bestimmter Zielstatus erreicht wird.

## Voraussetzungen
Python 3

Module: urllib.request, json, os, datetime, time, logging

## Konfiguration
Das Skript erwartet eine Konfigurationsdatei config.json, in der die erforderlichen Informationen wie API-Schlüssel, Empfängergruppen etc. festgelegt sind.
Eine config-example.json ist dem Repository beigefügt.

Im Repository ist eine setup.py enthalten die dir bei der erstellung der Konfigurationsdatei hilft.

Die setup.py fordert folgende Infos:
```
DIVERA 24/7 Setup Hilfe.
Dieses Setup hilft dir die korrekte Config Datei für das Divera Skript zu erstellen. Bitte trage deine Daten Schritt für Schritt ein.

Bitte geben Sie den Privaten API-Schlüssel aus deinem Divera Account ein. (default: DEIN-API-KEY):
Bitte wählen Sie einen Modus. (default: 2):
Bitte geben Sie den Ziel-FMS-Status ein. (default: 2):
Soll die Autoarchivierung für die Mitteilungen aktiviert werden? (true/false, default: false):
Bitte geben Sie die Anzahl der Tage für die Autoarchivierung ein. (default: 1):
Bitte geben Sie die Anzahl der Stunden für die Autoarchivierung ein. (default: 0):
Bitte geben Sie die Anzahl der Minuten für die Autoarchivierung ein. (default: 0):
Bitte geben Sie die Anzahl der Sekunden für die Autoarchivierung ein. (default: 0):
Soll das Senden von Push-Benachrichtigungen aktiviert werden? (true/false, default: false):
Soll das Senden von E-Mails aktiviert werden? (true/false, default: false):
Bitte geben Sie den Benachrichtigungstyp ein (default: 4):
Soll der private Modus für die Mitteilung aktiviert werden? (true/false, default: false):
Bitte geben Sie den Primärschlüssel des Benutzers ein. (default: 220053):
Bitte geben Sie die Divera-Gruppen-ID ein. (default: 138728):
Bitte geben Sie den Titel der Nachricht ein. (default: Änderung Fahrzeugstatus!):
```

Das Script läuft auf einem Linux basiertem System wie zb. ein Raspberry Pi.
Um das Script zu konfigurieren führe folgende Befehle aus:

```bash
apt install git

mkdir Divera

cd Divera

git clone https://github.com/Sleepwalker86/Divera_FMS_Status_to_Message.git

python3 setup.py

```

Die Konfigurationsdatei wird nach Abschluss des Setups im Verzeichnis Divera erstellt.

## Verwendung
Führen Sie das Skript aus, und verwenden Sie einen Cronjob, um regelmäßig den Fahrzeugstatus zu überprüfen.

```bash
crontab -e

# Diese Zeile am Ende der Datei einfügen und mit strg+o speichern und dann mit strg+x die Datei verlassen.
*/5 * * * * /usr/bin/python3 /home/pi/Divera/Divera_FMS_Status_to_Message/main.py >> /home/pi/Divera/Divera_FMS_Status_to_Message/log.txt 2>&1

# Hiermit wird einmal im Jahr das Logfile gelöscht.
0 0 1 10 * rm /home/pi/Divera_FMS_Status_to_Message/log.txt

```

Dieser Cronjob überprüft alle 5 Minuten den Fahrzeugstatus und protokolliert die Ausgabe in die Datei log.txt.


# Vehicle Status Monitoring Script for Divera 24/7

This Python script monitors the status of vehicles and notifies users via Divera message when a vehicle status changes. There are different modes to trigger the sending of the message:

Mode 1 = Sends a message when the status changes from 6 to not equal to 6 or from not equal to 6 to 6.

Mode 2 = Sends a message for every status change.

Mode 3 = Sends a message when a specific target status is reached.
## Requirements
Python 3

Modules: urllib.request, json, os, datetime, time, logging

## Configuration
The script expects a configuration file config.json, where the necessary information such as API keys, recipient groups, etc. are set. A config-example.json is included in the repository.

The repository contains a setup.py that assists you in creating the configuration file.

The script runs on a Linux-based system such as a Raspberry Pi.

To configure the script, execute the following commands:

```bash
apt install git

mkdir Divera

cd Divera

git clone https://github.com/Sleepwalker86/Divera_FMS_Status_to_Message.git

python3 setup.py
```
The configuration file will be created in the Divera directory upon completion of the setup.

## Usage

Execute the script and use a cron job to regularly check the vehicle status.

```bash
crontab -e

# Add this line at the end of the file, then save with ctrl+o and exit with ctrl+x.
*/5 * * * * /usr/bin/python3 /home/pi/Divera/Divera_FMS_Status_to_Message/main.py >> /home/pi/Divera/Divera_FMS_Status_to_Message/log.txt 2>&1

# with this code the logfile is deleted once a year
0 0 1 10 * rm /home/pi/Divera_FMS_Status_to_Message/log.txt
```
This cron job checks the vehicle status every 5 minutes and logs the output to the file log.txt.

