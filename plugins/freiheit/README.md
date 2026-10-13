# Plugin: freiheit

Werkzeuge für den Weg zur finanziellen Freiheit: Was brauche ich im Monat, und wie viel davon deckt mein passives Einkommen?

## Skills

| Skill | Zweck |
|---|---|
| `start` | Erste Einrichtung des Finanzprofils, danach Einstieg am gespeicherten Stand |
| `bedarf` | Fixkosten und monatlichen Lebensbedarf aus Kontoauszügen berechnen, fix, variabel und einmalig trennen |
| `deckung` | Passives Einkommen gegen den Bedarf stellen: Deckungsgrad, Depotentnahme, Szenarien |

## Skript

`skills/bedarf/scripts/kontoauswertung.py` wertet CSV-Exporte oder kopierten Text aus (nur Python-Standardbibliothek). Mit `--ablegen` sichert es die Exporte lokal unter `<Finanzordner>/Kontoauszuege/<Konto>/` und führt mehrere Exporte ohne Dubletten zusammen. Händlerregeln: `skills/bedarf/references/kategorien.json`.

## Persönliche Daten

Das Plugin enthält keine persönlichen Daten. Quellen des passiven Einkommens, Kredite, Annahmen und Vorauswertungen stehen in einer separaten Datei `Finanzprofil.md`. Eine Vorlage liegt unter `skills/bedarf/references/profil-vorlage.md`.

## Benutzung

1. Beim ersten Mal: "Richte mein Finanzprofil ein" (Skill `start`). Die Datei `Finanzprofil.md` liegt danach im Finanzordner und ist der gespeicherte Stand.
2. Kontoauszüge als CSV oder kopierten Text bereitstellen.
3. Anfrage stellen, z. B. "Berechne meine Fixkosten" oder "Reicht mein passives Einkommen?"

## Hinweis

Die Skills liefern Berechnungen und Annahmen, keine Anlage- oder Steuerberatung.
