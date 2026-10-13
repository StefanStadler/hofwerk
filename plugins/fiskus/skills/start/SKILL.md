---
name: start
description: Einstieg in das Plugin fiskus: fragt nach Steuerjahr und Vorgehen, richtet beim ersten Mal Steuerprofil und Eingang ein, setzt sonst am gespeicherten Stand an und legt zum Jahreswechsel das neue Jahr an. Verwenden bei der ersten Anfrage nach der Installation, bei "Steuerprofil anlegen", "Einrichtung", "neues Steuerjahr", "wo stehe ich bei der Steuer", "Stand Steuer 20xx", "fang an" oder wenn ein anderer Skill des Plugins kein Steuerprofil findet.
---

# Einstieg und Stand

Das Plugin selbst speichert nichts. Der Stand liegt im `Steuerprofil.md` im Steuer-Ordner oder Projekt des Nutzers, im Abschnitt „Stand Steuerjahr {JAHR}“. Alle Skills des Plugins lesen ihn zuerst und schreiben bestätigte Ergebnisse zurück. Arbeitsdaten (CSV, Skripte) liegen weiter in `9_Archiv/Arbeitsdateien/`.

## Ablauf

0. **Verzeichnis klären.** Zuerst prüfen, ob der Steuerordner (der Oberordner, in dem `Steuer {JAHR}` und das `Steuerprofil.md` liegen) mit dem Steuerprofil in dieser Sitzung erreichbar ist. Wenn nicht: den Pfad aus den Projektnotizen vorschlagen, sonst den Nutzer danach fragen und den Pfad ausdrücklich im Chat wiederholen, damit er in den Projektnotizen landet. Dann den Zugriff anfordern. Der Nutzer bestätigt, die Freigabe gilt nur für diese Sitzung. In einem neuen Chat genügt deshalb dieselbe eine Bestätigung. Der Pfad wird nie im Plugin gespeichert. Ist kein Zugriff möglich, mit den Anhängen im Chat weiterarbeiten und sagen, dass Originale und Stand noch nicht abgelegt werden können.
1. **Steuerjahr und Vorgehen abfragen** (kurze Auswahlfragen, nur was noch offen ist): Für welches Steuerjahr? Wie soll es weitergehen: Eingang sortieren, Online-Rechnungen holen, Steuerlast schätzen, USt vorbereiten oder alles der Reihe nach? `{JAHR}` kommt vom Nutzer, nie raten.
2. **Steuerprofil suchen** (verbundener Ordner, Projekt) und je Fall vorgehen:

**A. Profil und Stand für das Jahr vorhanden.** Den Stand in wenigen Zeilen zusammenfassen: pro Bereich (Belege, Online-Rechnungen, Schätzung, USt) Datum der letzten Bearbeitung und Ergebnis, dazu die offenen Punkte. Den nächsten sinnvollen Schritt vorschlagen (Reihenfolge: Online-Rechnungen holen, Belege sortieren, Steuerlast schätzen, USt vorbereiten) und fragen, wo es weitergeht. Keine bekannten Angaben erneut abfragen.

**B. Profil vorhanden, aber noch kein Abschnitt für dieses Jahr (Jahreswechsel).**
   - Ordner `Steuer {JAHR}` nach `skills/belege/references/ordnerstruktur.md` anlegen (erst die geplante Struktur nennen), darunter der Eingang `1_Eingang`, in dem alle Dateien aus dem Chat als unveränderte Originale landen (siehe Skill `belege`, Abschnitt Dokumenteingang).
   - Den Stand des Vorjahres zu einer Zeile unter „Vorjahreswerte“ verdichten und einen leeren Abschnitt „Stand Steuerjahr {JAHR}“ anlegen.
   - Die festen Entscheidungen des Vorjahres einzeln nennen und fragen, welche weiter gelten. Nur Änderungen erfragen, den Rest übernehmen.
   - Offene Punkte des Vorjahres übernehmen, die noch zutreffen.

**C. Kein Profil.** Vorlage `../belege/references/profil-vorlage.md` kopieren und in Blöcken ausfüllen: Person, Steuernummern, Einkunftsarten und Objekte, USt-Form und Optionsbindung, Bereiche mit Präfix und Gmail-Unterlabel (aus den Einkunftsarten als Vorschlag ableiten), Händlerregeln (zunächst leer, wächst später), Konten, feste Entscheidungen, Vorjahreswerte. Fragen bündeln. Angaben, die in vorhandenen Bescheiden, Belegen oder Notizen stehen, als Vorschlag zur Bestätigung vorlegen, statt sie zu erfragen. Danach wie unter B den Ordner anlegen.

3. **Nächsten Schritt starten** und am Ende der Sitzung den Stand sichern (siehe jeweiliger Skill).

## Regeln

- Persönliche Daten stehen nur im Steuerprofil des Nutzers, nie im Plugin.
- Entscheidungen des Nutzers gelten als gesetzt, bis er sie ändert.
- Vor jedem Überschreiben von Angaben im Profil zeigen, was sich ändert.
