# Postfachregeln

Persönliche Regeln für das Sortieren des Gmail-Posteingangs. Diese Datei liegt im Ordner des Nutzers, nicht im Plugin-Repository.

## Grundsätze

- Löschen heißt Papierkorb, nie endgültig.
- Laufende Vorgänge (offene Anfragen, Fristen, Bewerbungen mit Antwort) bleiben im Posteingang, bis sie erledigt sind.
- Im Zweifel nichts tun und nachfragen.

## Label-Struktur

Gewünschte Hierarchie, `/` trennt die Ebenen. Beim ersten Lauf mit den vorhandenen Gmail-Labels abgleichen.

- `<Oberlabel>/<Unterlabel>`

## Regeln

| Wenn (Absender, Stichwort, Muster) | Dann | Label | Bemerkung |
|---|---|---|---|
| `<Absender oder Stichwort>` | Label + archivieren | `<Oberlabel>/<Unterlabel>` | |
| `<Absender oder Stichwort>` | Im Posteingang lassen | | bis erledigt |
| `<Absender oder Stichwort>` | Papierkorb | | nach Freigabe |

Mögliche Aktionen: **Im Posteingang lassen**, **Label** (nur beschriften), **Label + archivieren**, **Papierkorb**.

## Feste Entscheidungen

- `<Datum>: <Entscheidung des Nutzers in einem Satz>`

## Stand Postfach

- Letzter Lauf: `<Datum>`, `<Anzahl>` Threads geprüft, `<Anzahl>` ohne Regel
- Offene Fragen: `<Liste>`
