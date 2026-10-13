# Plugin: fiskus

Jahresunabhängiger Steuer-Workflow für Landwirtschaft, Vermietung, Freiberuf und PV-Anlagen.

## Skills

| Skill | Zweck |
|---|---|
| `start` | Einrichtung des Steuerprofils, Einstieg am gespeicherten Stand, Anlage des neuen Steuerjahrs |
| `belege` | Belege benennen, drehen, in die WISO-Struktur sortieren, DATEV-Ausgang bereitstellen |
| `online-rechnungen` | Rechnungen aus Amazon und eBay für Betriebe und Werbungskosten laden (erst Gmail mit Label für den Export im Mail-Programm, danach Chrome als Vollständigkeitsprüfung), benennen, ablegen |
| `schaetzung` | Steuerlast des Jahres schätzen, Szenarien vergleichen |
| `ust` | Umsatzsteuer-Jahreserklärung inkl. PV-Anlagen und Optionsbindung |

## Persönliche Daten

Das Plugin enthält keine persönlichen Daten. Name, Steuernummern, Objekte, Präfixe, Entscheidungen und Vorjahreswerte stehen in einer separaten Datei `Steuerprofil.md` im Steuer-Ordner oder Projekt. Eine Vorlage liegt unter `skills/belege/references/profil-vorlage.md`.

## Benutzung

0. Den Steuerordner einmal pro Sitzung freigeben, `start` fragt danach und fordert den Zugriff an.
1. Beim ersten Mal und zu jedem neuen Steuerjahr: "Starte Steuer {JAHR}" (Skill `start`). Er legt das Steuerprofil an oder setzt am gespeicherten Stand an. Der Stand steht im Abschnitt "Stand Steuerjahr {JAHR}" des `Steuerprofil.md`.
2. Ordner "Steuer {JAHR}" mit der Struktur aus `skills/belege/references/ordnerstruktur.md` verbinden.
3. Anfrage stellen, z. B. "Sortiere den Eingang für 2027" oder "Schätze die Steuerlast 2027".

## Hinweis

Die Skills liefern Schätzungen und Vorbereitung, keine Steuerberatung.
