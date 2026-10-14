# Stand und Verlauf in Google Drive

Das Plugin speichert nichts selbst. Stand und Verlauf liegen im Google Drive des Nutzers, weil auch ein geplanter Lauf in der Cloud dort lesen und schreiben kann. Voraussetzung ist der Konnektor Google Drive (Werkzeuge mit dem Präfix `mcp__Google_Drive__`). Fehlt er, laufen alle Skills wie bisher ohne Verlauf. Die Status `⚡ Neu` und `📌 Wdh.` sind dann nicht belegt und werden durch `k.A.` ersetzt.

## Struktur

```
Aktien-Briefing/        Ordner im Stammverzeichnis von My Drive
  Stand                  Google Doc: Einstellungen und Depot-Kontext
  Verlauf/               Unterordner
    2026-10-14 Lauf      Google Doc, ein Eintrag pro Lauf
    2026-10-13 Lauf
```

## Finden

1. `search_files` mit `title = 'Aktien-Briefing' and mimeType = 'application/vnd.google-apps.folder' and owner = 'me'`.
2. Im Ordner `Stand` suchen (`parentId = '<Ordner-ID>' and title = 'Stand'`) und den Unterordner `Verlauf`.
3. Den jüngsten Eintrag im Verlauf finden: `parentId = '<Verlauf-ID>'`, Titel beginnt mit dem Datum, der größte Wert gewinnt. Mit `read_file_content` lesen.
4. Gibt es den Ordner nicht: Skill `start` ausführen (bei einem geplanten, unbeaufsichtigten Lauf stattdessen Ordner und Unterordner selbst anlegen, siehe unten).

Dateien nie nur nach dem Titel raten: immer die ID aus `search_files` nehmen.

## Schreiben

Die Drive-Werkzeuge können Dateien anlegen und umbenennen oder verschieben, aber keinen Inhalt ändern. Deshalb:

- **Verlauf:** Je Lauf ein neues Doc mit `create_file` (`contentMimeType` `text/plain`, wird zum Google Doc), Titel `JJJJ-MM-TT Lauf`, `parentId` = Verlauf-Ordner. Gibt es für das Datum schon ein Doc (zweiter Lauf am selben Tag), Titel `JJJJ-MM-TT Lauf 2`.
- **Stand:** Ändert sich etwas, das alte Doc mit `update_file` in `Stand (alt JJJJ-MM-TT)` umbenennen und ein neues `Stand` anlegen. Lesen immer nur das Doc mit dem Titel genau `Stand`.
- Ordner mit `create_file` und `mimeType` `application/vnd.google-apps.folder` anlegen.
- Nichts löschen, nichts teilen, nichts verschieben außer dem Umbenennen des alten Stands.

## Inhalt eines Verlaufseintrags

```
Lauf: 2026-10-14
Marktlage: ein Satz

Momentum
| Rang | Ticker | Firma | Kurs | RSI | Status | Trigger |
...
Value
| Rang | Ticker | Firma | Kurs | Rabatt z. IV | Status | Katalysator |
...
CEO-Signale: Firma/Ticker, Aussage in eigenen Worten, Datum, Link
Hinweise: nicht abrufbare Quellen, fehlende Daten
```

Kurz halten, nur Tabellen und Stichpunkte, keine ausformulierten Begründungen.

## Wie der Status entsteht

- `📌 Wdh.`: Der Ticker stand im Verlauf der letzten 14 Tage in der jeweiligen Liste (Momentum oder Value). Zusätzlich die Zahl der Tage in Folge nennen, z. B. `📌 Wdh. (3 Tage)`.
- `⚡ Neu`: Der Ticker stand in den letzten 14 Tagen nicht in dieser Liste.
- Gab es keinen Verlauf (erster Lauf oder kein Drive): keinen dieser beiden Status setzen, sondern `k.A.`.
- Fällt ein Ticker gegenüber dem letzten Lauf heraus, im Verlaufseintrag unter `Hinweise` mit Grund festhalten (z. B. RSI über 75, Trend gebrochen).

## Stand (Inhalt)

```
Stand vom: 2026-10-14
Depot-Kontext: Werte oder Branchen, die in der Auswahl der News zählen (keine Beträge)
Google Alerts: angelegt ja/nein, Zustellzeit
Konnektoren: Twelve Data, Gmail, Google Drive
Geplante Aufgabe: Zeit, Name
Sektor-Cap und Filter: nur Abweichungen von den Standardwerten
Offene Punkte
```

Keine Kontonummern, keine Kontostände, keine Stückzahlen.
