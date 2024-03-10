# Divera FMS Status Fahrzeugstatusüberwachungs Skript Divera 24/7

Dieses Python-Skript überwacht den Status von Fahrzeugen und benachrichtigt Benutzer per E-Mail und Push-Nachricht, wenn ein Fahrzeugstatus von oder zu 6 wechselt.

Voraussetzungen
Python 3
Module: urllib.request, json, smtplib, email.mime, os, datetime, logging
Konfiguration
Das Skript erwartet eine Konfigurationsdatei config.json, in der die erforderlichen Informationen wie API-Schlüssel, E-Mail-Einstellungen und Empfängeradressen festgelegt sind. Eine Beispieldatei example-config.json ist im Repository enthalten. Sie müssen diese Datei kopieren und entsprechend Ihren Informationen anpassen.

cp example-config.json config.json


Verwendung
Führen Sie das Skript aus, und verwenden Sie einen Cronjob, um regelmäßig den Fahrzeugstatus zu überprüfen.

*/5 * * * * /usr/bin/python3 /home/pi/Divera_FMS/main.py >> /home/pi/Divera_FMS/log.txt 2>&1

Dieser Cronjob überprüft alle 5 Minuten den Fahrzeugstatus und protokolliert die Ausgabe in die Datei log.txt.



