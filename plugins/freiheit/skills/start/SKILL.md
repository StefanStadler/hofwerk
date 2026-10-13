---
name: start
description: Einstieg in das Plugin freiheit: fragt beim ersten Mal nach dem Vorgehen, richtet Finanzprofil und Eingang ein und setzt später am gespeicherten Stand an. Verwenden bei der ersten Anfrage nach der Installation, bei "Finanzprofil anlegen", "Einrichtung", "fang an", "wo stehe ich", "Stand aktualisieren", "Profil prüfen" oder wenn ein anderer Skill des Plugins kein Finanzprofil findet.
---

# Einrichtung und Stand

Das Plugin selbst speichert nichts. Der Stand liegt in der Datei `Finanzprofil.md` im Finanzordner oder Projekt des Nutzers. Alle Skills des Plugins lesen sie zuerst und schreiben bestätigte Ergebnisse zurück.

## Ablauf

0. **Verzeichnis klären.** Zuerst prüfen, ob der Finanzordner mit dem `Finanzprofil.md` in dieser Sitzung erreichbar ist. Wenn nicht: den Pfad aus den Projektnotizen vorschlagen, sonst den Nutzer danach fragen und den Pfad ausdrücklich im Chat wiederholen, damit er in den Projektnotizen landet. Dann den Zugriff anfordern. Der Nutzer bestätigt, die Freigabe gilt nur für diese Sitzung. In einem neuen Chat genügt deshalb dieselbe eine Bestätigung. Der Pfad wird nie im Plugin gespeichert. Ist kein Zugriff möglich, mit den Anhängen im Chat weiterarbeiten und sagen, dass Originale und Stand noch nicht abgelegt werden können.
1. **Profil und Eingang suchen** (verbundener Finanzordner, Projekt). Fehlt der Ordner `1_Eingang` mit den Unterordnern `Kontoauszuege/<Konto>`, `Bescheide_Vertraege` und `Sonstiges`, ihn nach kurzer Ansage anlegen. Dort landen alle Dateien aus dem Chat unverändert (siehe Skill `bedarf`, Abschnitt Dokumenteingang).
2. **Beim ersten Mal das Vorgehen abfragen** (kurze Auswahlfragen): Was soll zuerst passieren (Profil einrichten, Kontoauszüge auswerten, Deckungsgrad prüfen, alles der Reihe nach)? Welche Konten gibt es? Danach nicht mehr fragen, was das Profil schon weiß.
3. **Profil vorhanden:** Den Stand in wenigen Zeilen zusammenfassen: Datum der letzten Auswertung, Bedarf pro Monat, Deckungsgrad, offene Punkte. Zeitraum der gespeicherten Kontoauszüge nennen und nur einen Export ab dem letzten Datum anfordern. Dann fragen, was aktualisiert werden soll (neue Kontoauszüge, geänderte Beträge, neue Entscheidung). Nicht von vorn beginnen und keine bekannten Angaben erneut abfragen.
4. **Kein Profil:** Vorlage `../bedarf/references/profil-vorlage.md` kopieren und in Blöcken ausfüllen: Haushalt, Konten, passives Einkommen, Kredite, Annahmen ohne Gehalt, feste Entscheidungen. Fragen bündeln (mehrere auf einmal, mit Auswahlantworten wo möglich). Angaben, die in vorhandenen Dokumenten, Projektnotizen oder Kontoauszügen stehen, als Vorschlag zur Bestätigung vorlegen, statt sie zu erfragen.
5. **Erste Auswertung anschließen:** Kontoexport anfordern, mit `--ablegen` als Original in `1_Eingang/Kontoauszuege/<Konto>/` sichern, Skill `bedarf` ausführen, danach `deckung`. Das Ergebnis im Profil sichern.

## Regeln

- Das Profil gehört in den Finanzordner des Nutzers, nie in das Plugin-Repository (steht in der `.gitignore`).
- Keine IBANs, Kontonummern oder Kreditaktenzeichen speichern. Banknamen und Verwendungszweck der Konten genügen.
- Vor jedem Überschreiben von Angaben im Profil zeigen, was sich ändert.
