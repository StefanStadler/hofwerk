---
name: start
description: Einstieg in das Plugin postfach: richtet beim ersten Mal die Regeldatei ein, gleicht sie mit den vorhandenen Gmail-Labels ab und setzt später am gespeicherten Stand an. Verwenden bei der ersten Anfrage nach der Installation, bei "Postfachregeln einrichten", "Mail-Regeln anlegen", "fang an", "wo stehe ich beim Postfach", "Regeln prüfen" oder wenn ein anderer Skill des Plugins keine Postfachregeln findet.
---

# Einrichtung und Stand

Das Plugin selbst speichert nichts. Die Regeln und der Stand liegen in der Datei `Postfachregeln.md` im Ordner des Nutzers. Alle Skills des Plugins lesen sie zuerst und schreiben bestätigte Ergebnisse zurück.

## Ablauf

0. **Gmail prüfen.** Ist der Gmail-Connector nicht verbunden, den Nutzer darauf hinweisen und hier stoppen. Ohne Postfach gibt es nichts zu sortieren.
1. **Verzeichnis klären.** Prüfen, ob der Ordner mit der `Postfachregeln.md` in dieser Sitzung erreichbar ist. Wenn nicht: den Pfad aus den Projektnotizen vorschlagen, sonst den Nutzer danach fragen und den Pfad ausdrücklich im Chat wiederholen, damit er in den Projektnotizen landet. Dann den Zugriff anfordern. Die Freigabe gilt nur für diese Sitzung. Der Pfad wird nie im Plugin gespeichert. Ist kein Zugriff möglich, die Regeln im Chat ausgeben und den Nutzer bitten, die Datei selbst abzulegen.
2. **Datei vorhanden:** Den Stand in wenigen Zeilen zusammenfassen: Datum des letzten Laufs, Anzahl Regeln, offene Fragen. Fragen, was jetzt passieren soll (Posteingang sortieren, Regel ändern). Keine bekannten Angaben erneut abfragen.
3. **Datei fehlt:** Vorlage `references/regeln-vorlage.md` kopieren und in Blöcken ausfüllen.
   - Mit `list_labels` die vorhandenen Gmail-Labels lesen und als Vorschlag für die Label-Struktur vorlegen, statt eine neue zu erfinden.
   - Aus Projektnotizen oder früheren Entscheidungen bekannte Regeln als Vorschlag zur Bestätigung vorlegen, nicht einzeln erfragen.
   - Fragen bündeln, mit Auswahlantworten wo möglich: Was bleibt immer im Posteingang? Was darf in den Papierkorb? Welche Absender haben feste Labels?
4. **Ersten Lauf klein halten.** Danach Skill `sortieren` mit etwa 20 Threads starten, das Ergebnis gemeinsam prüfen und erst dann größere Mengen angehen.

## Regeln

- Die Regeldatei gehört in den Ordner des Nutzers, nie in das Plugin-Repository (steht in der `.gitignore`).
- Keine Passwörter, Kontonummern oder Aktenzeichen in die Datei schreiben. Absender, Stichworte und Labelnamen genügen.
- Vor jedem Überschreiben von Angaben in der Datei zeigen, was sich ändert.
