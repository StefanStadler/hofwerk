---
name: start
description: Einstieg in das Plugin aktien: richtet beim ersten Mal den Ordner Aktien-Briefing mit Stand und Verlauf in Google Drive ein, zeigt später den letzten Lauf und den Stand. Verwenden bei der ersten Anfrage nach der Installation, bei "Aktien einrichten", "fang an", "wo stehe ich bei den Aktien", "letzter Lauf", "Stand Aktien" oder wenn ein anderer Skill des Plugins keinen Ordner Aktien-Briefing findet.
---

# Einrichtung und Stand

Das Plugin selbst speichert nichts. Stand und Verlauf liegen in Google Drive im Ordner `Aktien-Briefing` (Aufbau, Finden und Schreiben: `../../references/stand-und-verlauf.md`, zuerst lesen). Die Skills `momentum`, `value` und `briefing` lesen den letzten Lauf und schreiben ihren Lauf zurück.

## Ablauf

1. **Konnektor prüfen.** Gibt es Werkzeuge mit dem Präfix `mcp__Google_Drive__`? Wenn nicht: sagen, dass der Konnektor Google Drive fehlt und das Plugin ohne Verlauf läuft (kein `Neu`/`Wdh.`), und den Nutzer bitten, ihn zu verbinden. Nicht weiter einrichten.
2. **Ordner suchen** wie in der Referenz beschrieben.
3. **Ordner vorhanden:** Den Stand in wenigen Zeilen zusammenfassen: Datum des letzten Laufs, die Momentum- und Value-Auswahl mit Rang und Status, die Zahl der Verlaufseinträge, offene Punkte aus dem `Stand`. Dann fragen, was geändert werden soll (Einstellungen, Depot-Kontext, Filter). Nichts erneut abfragen, was im `Stand` schon steht.
4. **Ordner fehlt, erster Lauf:** Nach kurzer Ansage `Aktien-Briefing`, darin `Verlauf` anlegen und ein Doc `Stand` mit dem Inhalt aus der Referenz. Kurze Auswahlfragen, gebündelt:
   - Welche Werte oder Branchen sollen in den News zählen (Depot-Kontext, ohne Beträge)?
   - Sind Google Alerts angelegt (Gmail-Konnektor, Absender `googlealerts-noreply@google.com`)?
   - Welche Konnektoren hängen an der geplanten Aufgabe, zu welcher Uhrzeit läuft sie?
   Vorschläge aus dem, was erkennbar ist (verfügbare Werkzeuge), zur Bestätigung vorlegen statt zu erfragen.
5. **Erster Lauf anschließen:** Auf Wunsch gleich den Skill `briefing` ausführen. Er schreibt dann den ersten Verlaufseintrag.

## Regeln

- Keine Kontonummern, Kontostände oder Stückzahlen im `Stand` oder im Verlauf.
- Vor jedem neuen `Stand` zeigen, was sich ändert.
- Bei einem unbeaufsichtigten Lauf nicht nachfragen: fehlende Ordner anlegen und weitermachen.
