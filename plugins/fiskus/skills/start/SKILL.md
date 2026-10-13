---
name: start
description: Einstieg in den Steuer-Workflow: richtet beim ersten Mal das Steuerprofil ein, setzt sonst am gespeicherten Stand des Steuerjahrs an und legt zum Jahreswechsel das neue Steuerjahr an. Verwenden bei "Steuerprofil anlegen", "Einrichtung", "neues Steuerjahr", "wo stehe ich bei der Steuer", "Stand Steuer 20xx", "fang an" oder wenn ein anderer Skill des Plugins kein Steuerprofil findet.
---

# Einstieg und Stand

Das Plugin selbst speichert nichts. Der Stand liegt im `Steuerprofil.md` im Steuer-Ordner oder Projekt des Nutzers, im Abschnitt „Stand Steuerjahr {JAHR}“. Alle Skills des Plugins lesen ihn zuerst und schreiben bestätigte Ergebnisse zurück. Arbeitsdaten (CSV, Skripte) liegen weiter in `9_Archiv/Arbeitsdateien/`.

## Ablauf

1. **Steuerjahr klären.** `{JAHR}` kommt vom Nutzer, bei Unklarheit nachfragen.
2. **Steuerprofil suchen** (verbundener Ordner, Projekt) und je Fall vorgehen:

**A. Profil und Stand für das Jahr vorhanden.** Den Stand in wenigen Zeilen zusammenfassen: pro Bereich (Belege, Online-Rechnungen, Schätzung, USt) Datum der letzten Bearbeitung und Ergebnis, dazu die offenen Punkte. Den nächsten sinnvollen Schritt vorschlagen (Reihenfolge: Online-Rechnungen holen, Belege sortieren, Steuerlast schätzen, USt vorbereiten) und fragen, wo es weitergeht. Keine bekannten Angaben erneut abfragen.

**B. Profil vorhanden, aber noch kein Abschnitt für dieses Jahr (Jahreswechsel).**
   - Ordner `Steuer {JAHR}` nach `skills/belege/references/ordnerstruktur.md` anlegen (erst die geplante Struktur nennen).
   - Den Stand des Vorjahres zu einer Zeile unter „Vorjahreswerte“ verdichten und einen leeren Abschnitt „Stand Steuerjahr {JAHR}“ anlegen.
   - Die festen Entscheidungen des Vorjahres einzeln nennen und fragen, welche weiter gelten. Nur Änderungen erfragen, den Rest übernehmen.
   - Offene Punkte des Vorjahres übernehmen, die noch zutreffen.

**C. Kein Profil.** Vorlage `../belege/references/profil-vorlage.md` kopieren und in Blöcken ausfüllen: Person, Steuernummern, Einkunftsarten und Objekte, USt-Form und Optionsbindung, Bereichs-Präfixe, Konten, feste Entscheidungen, Vorjahreswerte. Fragen bündeln. Angaben, die in vorhandenen Bescheiden, Belegen oder Notizen stehen, als Vorschlag zur Bestätigung vorlegen, statt sie zu erfragen. Danach wie unter B den Ordner anlegen.

3. **Nächsten Schritt starten** und am Ende der Sitzung den Stand sichern (siehe jeweiliger Skill).

## Regeln

- Persönliche Daten stehen nur im Steuerprofil des Nutzers, nie im Plugin.
- Entscheidungen des Nutzers gelten als gesetzt, bis er sie ändert.
- Vor jedem Überschreiben von Angaben im Profil zeigen, was sich ändert.
