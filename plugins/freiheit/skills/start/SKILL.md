---
name: start
description: Richtet das Finanzprofil beim ersten Mal ein und setzt bei späteren Läufen am gespeicherten Stand an, statt von vorn zu beginnen. Verwenden bei "Finanzprofil anlegen", "Einrichtung", "fang an", "wo stehe ich", "Stand aktualisieren", "Profil prüfen" oder wenn ein anderer Skill des Plugins kein Finanzprofil findet.
---

# Einrichtung und Stand

Das Plugin selbst speichert nichts. Der Stand liegt in der Datei `Finanzprofil.md` im Finanzordner oder Projekt des Nutzers. Alle Skills des Plugins lesen sie zuerst und schreiben bestätigte Ergebnisse zurück.

## Ablauf

1. **Profil suchen** (verbundener Finanzordner, Projekt). 
2. **Profil vorhanden:** Den Stand in wenigen Zeilen zusammenfassen: Datum der letzten Auswertung, Bedarf pro Monat, Deckungsgrad, offene Punkte. Zeitraum der gespeicherten Kontoauszüge nennen und nur einen Export ab dem letzten Datum anfordern. Dann fragen, was aktualisiert werden soll (neue Kontoauszüge, geänderte Beträge, neue Entscheidung). Nicht von vorn beginnen und keine bekannten Angaben erneut abfragen.
3. **Kein Profil:** Vorlage `../bedarf/references/profil-vorlage.md` kopieren und in Blöcken ausfüllen: Haushalt, Konten, passives Einkommen, Kredite, Annahmen ohne Gehalt, feste Entscheidungen. Fragen bündeln (mehrere auf einmal, mit Auswahlantworten wo möglich). Angaben, die in vorhandenen Dokumenten, Projektnotizen oder Kontoauszügen stehen, als Vorschlag zur Bestätigung vorlegen, statt sie zu erfragen.
4. **Erste Auswertung anschließen:** Kontoexport anfordern, mit `--ablegen` in `<Finanzordner>/Kontoauszuege/<Konto>/` sichern (siehe Skill `bedarf`), Skill `bedarf` ausführen, danach `deckung`. Das Ergebnis im Profil sichern.

## Regeln

- Das Profil gehört in den Finanzordner des Nutzers, nie in das Plugin-Repository (steht in der `.gitignore`).
- Keine IBANs, Kontonummern oder Kreditaktenzeichen speichern. Banknamen und Verwendungszweck der Konten genügen.
- Vor jedem Überschreiben von Angaben im Profil zeigen, was sich ändert.
