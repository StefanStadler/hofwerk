---
name: belege
description: Sammelt, benennt, dreht und sortiert Steuerbelege eines Steuerjahrs in die WISO-Struktur und stellt am Ende den DATEV-Ausgang für den Steuerberater bereit. Verwenden bei "Belege sortieren", "Steuerunterlagen", "Eingang einsortieren", "DATEV-Upload vorbereiten", "Beleg benennen", "Steuerberater-Übersicht" oder wenn Scans, Fotos, Kontoauszüge oder Rechnungen für ein Steuerjahr verarbeitet werden sollen.
---

# Steuer-Belege: Eingang → WISO → DATEV

Das Steuerjahr `{JAHR}` kommt vom Nutzer. Bei Unklarheit nachfragen, nie raten. Persönliche Daten (Name, Steuernummern, Objekte, Präfixe, feste Entscheidungen) stehen im Steuerprofil des Nutzers. Zuerst die Datei `Steuerprofil.md` im verbundenen Ordner bzw. Projekt lesen. Fehlt sie, die Vorlage `references/profil-vorlage.md` zeigen und gemeinsam ausfüllen. Persönliche Daten nie in dieses Plugin schreiben.

## Ordnerstruktur im verbundenen Ordner "Steuer {JAHR}"

Struktur und DATEV-Fächer stehen in `references/ordnerstruktur.md`. Lies sie vor dem ersten Einsortieren.

Ablauf: `1_Eingang` → (benennen, drehen, prüfen) → `2_Steuererklaerung_Wiso` → am Ende als Kopie nach `3_Ausgang_DATEV`. Originale in `1_Eingang` bleiben unverändert, es wird nur kopiert oder innerhalb des Ordners verschoben. Belege, die erst im Folgejahr zählen, kommen nach `9_Archiv/Folgejahr_{JAHR+1}`.

## Dokumenteingang

Jede Datei, die der Nutzer im Chat schickt (Scan, Foto, PDF, Kontoauszug, Bescheid), wird als Erstes unverändert in den Eingang des Steuerordners kopiert, bevor etwas damit passiert: `1_Eingang/<Unterordner>` (Kontoauszuege/<Konto>, Scans_Fotos, Mail_Downloads, Online_Bestellungen). Liegen Mail-Anhänge in Unterordnern von `Mail_Downloads` (je Bereich), ist der Ordnername ein Bereichsvorschlag, keine Entscheidung. Originalname und Inhalt bleiben, nichts wird gedreht, umbenannt oder geändert. Gleiche Inhalte (Hash) nicht doppelt ablegen. Danach arbeiten alle Skills mit Kopien. Dem Nutzer in einem Satz sagen, wo das Original liegt. Ist kein Steuerordner verbunden, trotzdem verarbeiten und darauf hinweisen, dass das Original noch nicht abgelegt ist.

## Dateinamen

`<Bereich>_<JJJJ-MM-TT>_<Beschreibung>_<Aussteller>_<Betrag>EUR.pdf`

Beispiel: `LuF_2026-03-30_Hauskosten-Mischbatterie-Altenteiler_Dietrich-R26-000018_583,34EUR.pdf`

Die Bereichs-Präfixe stehen im Steuerprofil. Wo eine Journal-Zuordnung besteht, kommt die Belegnummer (3-stellig, ggf. mit Buchstaben-Suffix) als Präfix davor. Kein "Zur_Pruefung"-Präfix verwenden.

## Arbeitsregeln

1. Rückmeldungen und offene Punkte nur im Chat. Keine zusätzliche Excel-Auswertung, außer sie ist ausdrücklich gewünscht.
2. Flache Ablage je Zielordner, keine Unterordner über die vorgegebene Struktur hinaus.
3. Gescannte oder fotografierte Belege müssen für Menschen lesbar gedreht sein. Vor der Auslieferung die Rotation stichprobenartig visuell prüfen. EXIF orientation=6: nur `exif_transpose`. orientation=1: `exif_transpose` plus `rotate(-90, expand=True)`.
4. Texterkennung aus Fotos kann Zeilen verschieben (Off-by-one). Bei Unstimmigkeit das Originalfoto ansehen, nicht der CSV vertrauen.
5. Kategorisierung im Zweifel zugunsten des Nutzers, soweit steuerlich vertretbar.
6. Keine Hinweise an den Steuerberater in Dokumenten (keine Prüf-, Klärungs- oder Warnhinweise, Empfehlungen oder rechtlichen Begründungen). Dokumente enthalten nur Zahlen, Tabellen und Belege. Offene Punkte nur im Chat.
7. Dubletten (Rechnung plus Zahlungsbeleg) gehen nur einmal in die Summen, beide Belege werden aber abgelegt.
8. Erstattungen (z. B. Zahnarzt/Krankenversicherung, Rechtsschutz) vor dem Ansatz als Ausgabe gegen die Kontoumsätze prüfen.
9. Löschen im verbundenen Ordner ist standardmäßig gesperrt. Erst Löschrecht anfragen, sonst in `_to_delete/` verschieben und dem Nutzer sagen, welche Dateien dort liegen.
10. Arbeitsdaten (CSV, JSON, Skripte) in `9_Archiv/Arbeitsdateien/` sichern, damit Folgesitzungen darauf aufbauen können.
11. Steuerbescheide (egal welches Jahr) gesondert ablegen, nicht in die Jahreskategorien zwingen.

## Ausgaben

- **Steuerberater-Übersicht** (PDF, DOCX oder XLSX, je nach Wunsch): fortlaufend nummerierte Belege je Bereich, nur Zahlen und Tabellen.
- **DATEV-Upload**: alle Belege als Einzeldateien in die Fächer unter `3_Ausgang_DATEV/` einsortiert. Ein Ordner- oder ZIP-Upload ist im Portal nicht möglich.

Am Ende kurz im Chat zusammenfassen: Anzahl einsortierter Belege je Bereich, offene Punkte, Belege fürs Folgejahr.

## Stand sichern

Gestartet wird am gespeicherten Stand im `Steuerprofil.md` (Abschnitt „Stand Steuerjahr {JAHR}“). Fehlt das Profil oder das Jahr, zuerst den Skill `start` ausführen. Nach der Bestätigung des Ergebnisses durch den Nutzer die Zeile „Belege“ in diesem Abschnitt aktualisieren: Datum der letzten Verarbeitung, Anzahl einsortierter Belege je Bereich, Belege fürs Folgejahr, ob der DATEV-Ausgang vollständig ist. Nur die eigene Zeile ändern, vorher zeigen, was sich ändert. Neue Entscheidungen des Nutzers unter „Feste Entscheidungen“ eintragen.
