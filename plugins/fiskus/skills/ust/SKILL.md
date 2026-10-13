---
name: ust
description: Bereitet die Umsatzsteuer-Jahreserklärung eines Steuerjahrs vor, insbesondere mit PV-Anlagen (Einspeisung, Anschaffung, Vorsteuer), Land-/Forstwirtschaft nach § 24 UStG und Freiberuf, und prüft die Optionsbindung zur Regelbesteuerung. Verwenden bei "Umsatzsteuer", "USt-Jahreserklärung", "Voranmeldung", "PV Umsatzsteuer", "Option Regelbesteuerung", "Kleinunternehmer wechseln" oder "Vorsteuer PV".
---

# Umsatzsteuer-Jahreserklärung

Eigener Arbeitsschritt neben der Einkommensteuer, weil PV-Anlagen ertragsteuerfrei sein können (§ 3 Nr. 72 EStG), umsatzsteuerlich aber relevant bleiben. Du bist kein Steuerberater. Rechtliche Details bei Unsicherheit per Websuche gegen aktuelle Quellen prüfen und die Unsicherheit im Chat benennen.

Persönliche Angaben (Steuernummern, Anlagen, Besteuerungsform, Optionsbindung) stehen im `Steuerprofil.md`. Zuerst lesen.

## Vorgehen

1. **Besteuerungsform je Bereich klären**: Regelbesteuerung, Durchschnittssatzbesteuerung nach § 24 UStG (Land-/Forstwirtschaft), Kleinunternehmer. Das Profil gibt die Vorgabe, Abweichungen im Chat ansprechen.
2. **Einnahmen je PV-Anlage** aus Kontoauszügen und Abrechnungen des Netzbetreibers erfassen (Einspeisevergütung brutto/netto, Eigenverbrauch).
3. **Vorsteuer** aus Anschaffung, Wartung, Versicherung und laufenden Kosten je Anlage zuordnen. Gemischt genutzte Kosten sachgerecht aufteilen.
4. **Zahllast** aus Umsatzsteuer abzüglich Vorsteuer und abzüglich geleisteter Vorauszahlungen berechnen. Spanne konservativ/wahrscheinlich, wenn Daten fehlen. Fälligkeit nennen.
5. **Optionsbindung prüfen**: Bindungsfrist je Objekt laut Profil, frühester Wechsel, Folgen eines Wechsels (u. a. Vorsteuerberichtigung). Entscheidung gehört dem Nutzer, Optionen mit Zahlen gegenüberstellen.
6. **Steuernummern abgleichen**: Die USt-Erklärung wird unter der im Profil genannten USt-Nummer abgegeben, nicht unter der ESt- oder EÜR-Nummer. Auf Verwechslung in WISO/ELSTER achten.
7. **Belege ablegen** nach `13_Umsatzsteuer` (Unterordner je Anlage) und als Kopie in das DATEV-Fach für PV-Anlagen (siehe Skill `belege`).

## Ausgabe

Im Chat: Tabelle je Anlage mit Umsatzsteuer, Vorsteuer, Saldo, darunter Gesamt-Zahllast und Fälligkeit, dann offene Punkte. Dokumente für den Steuerberater enthalten nur Zahlen und Tabellen, keine Hinweise oder Begründungen.

## Dateien aus dem Chat

Dateien, die der Nutzer im Chat schickt, kommen zuerst unverändert in den Eingang (`1_Eingang`, siehe Skill `belege`, Abschnitt Dokumenteingang). Danach wird mit Kopien gearbeitet.

## Stand sichern

Gestartet wird am gespeicherten Stand im `Steuerprofil.md` (Abschnitt „Stand Steuerjahr {JAHR}“). Fehlt das Profil oder das Jahr, zuerst den Skill `start` ausführen. Nach der Bestätigung des Ergebnisses durch den Nutzer die Zeile „USt“ in diesem Abschnitt aktualisieren: Besteuerungsform je Bereich, Zahllast mit Fälligkeit, geleistete Vorauszahlungen, Stand der Optionsbindung. Nur die eigene Zeile ändern, vorher zeigen, was sich ändert. Neue Entscheidungen des Nutzers unter „Feste Entscheidungen“ eintragen.
