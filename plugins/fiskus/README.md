# Plugin: fiskus

Jahresunabhängiger Steuer-Workflow für Landwirtschaft, Vermietung, Freiberuf und PV-Anlagen.

## Skills

| Skill | Zweck |
|---|---|
| `belege` | Belege benennen, drehen, in die WISO-Struktur sortieren, DATEV-Ausgang bereitstellen |
| `online-rechnungen` | Rechnungen aus Amazon und eBay für Betriebe und Werbungskosten laden, benennen, ablegen |
| `schaetzung` | Steuerlast des Jahres schätzen, Szenarien vergleichen |
| `ust` | Umsatzsteuer-Jahreserklärung inkl. PV-Anlagen und Optionsbindung |

## Persönliche Daten

Das Plugin enthält keine persönlichen Daten. Name, Steuernummern, Objekte, Präfixe, Entscheidungen und Vorjahreswerte stehen in einer separaten Datei `Steuerprofil.md` im Steuer-Ordner oder Projekt. Eine Vorlage liegt unter `skills/belege/references/profil-vorlage.md`.

## Benutzung

1. Steuerprofil anlegen oder aktualisieren.
2. Ordner "Steuer {JAHR}" mit der Struktur aus `skills/belege/references/ordnerstruktur.md` verbinden.
3. Anfrage stellen, z. B. "Sortiere den Eingang für 2027" oder "Schätze die Steuerlast 2027".

## Hinweis

Die Skills liefern Schätzungen und Vorbereitung, keine Steuerberatung.
