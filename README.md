#Da ich alle meine Bausteine kostenlos zur Verfügung stelle und ich das auch gerne beibehalten möchte, würde ich mich über eine kleine Paypal Spende freuen. Vielen Dank für deine Unterstützung.


[Spende eine kleine Aufwandsentschädigung](https://www.paypal.com/donate/?hosted_button_id=SHU2PHYACRRMN)

# Fahrzeugstatusüberwachungs Skript für Divera 24/7

Dieses Python-Skript überwacht den Status von Fahrzeugen und benachrichtigt Benutzer per Divera Mitteilung,
wenn ein Fahrzeugstatus wechselt. Es gibt verschiedene Modis um das versenden der Mitteilung anzustoßen:

Modus 1 = Wenn sich der Status von 6 auf ungleich 6 oder von ungleich 6 auf 6 ändert wird eine Mitteilung gesendet.

Modus 2 = Bei jeder Statusänderung eine Mitteilung senden.

Modus 3 = Sendet eine Mitteilung, wenn ein bestimmter Zielstatus erreicht wird.

## Voraussetzungen
Python 3

Module: urllib, json, os, datetime, time, logging, websockets, aiohttp, asyncio, subprocess

## Konfiguration
Das Skript erwartet eine Konfigurationsdatei config.json, in der die erforderlichen Informationen wie API-Schlüssel, Empfängergruppen etc. festgelegt sind.
Eine config-example.json ist dem Repository beigefügt.
Im Repository ist eine setup.py enthalten die dir bei der erstellung der Konfigurationsdatei hilft.

Das Script läuft auf einem Linux basiertem System wie zb. ein Raspberry Pi.
Um das Script zu konfigurieren führe folgende Befehle aus:

```bash
apt install git

git clone https://github.com/Sleepwalker86/Divera_FMS_Status_to_Message.git

cd Divera_FMS_Status_to_Message

sudo python3 setup.py

```

Die Konfigurationsdatei wird nach Abschluss des Setups im Verzeichnis Divera erstellt.
Wenn Mitteilungen ausgelöst wurden finden Sie diese im Scriptverzeichnis in der Datei log.txt

## Verwendung
Das Script wird als service im Autostart hinterlegt und nimmt in Echtzeit den Fahrzeugstatus entgegen.
Das Script wird somit einmal über den Service gestartet und läuft dann permanent im Hintergrund.

```bash
# Script starten
service divera_websocket start

# Scrip stoppen
service divera_websocket stop

# Script neustarten
service divera_websocket restart

# Script status
service divera_websocket status
```

# Vehicle Status Monitoring Script for Divera 24/7

This Python script monitors the status of vehicles and notifies users via Divera messages when a vehicle status changes. There are different modes to trigger the message sending:

Mode 1 = Sends a message when the status changes from 6 to not equal 6 or from not equal 6 to 6.

Mode 2 = Sends a message for every status change.

Mode 3 = Sends a message when a specific target status is reached.

## Requirements
Python 3

Modules: urllib, json, os, datetime, time, logging, websockets, aiohttp, asyncio, subprocess

## Configuration
The script expects a configuration file config.json, where necessary information such as API keys, recipient groups, etc., are defined.
A config-example.json is included in the repository.
The repository contains a setup.py that assists you in creating the configuration file.

The script runs on a Linux-based system such as a Raspberry Pi.
To configure the script, execute the following commands:

```bash
apt install git

git clone https://github.com/Sleepwalker86/Divera_FMS_Status_to_Message.git

cd Divera_FMS_Status_to_Message

sudo python3 setup.py
```
