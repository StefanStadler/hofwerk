---
name: deckung
description: Stellt das passive Einkommen dem Bedarf ohne Gehalt gegenüber (Deckungsgrad), rechnet die Entnahme aus dem Depot und vergleicht Szenarien wie Krankenversicherung, Pachtänderung, Kreditende und Entnahmerate. Verwenden bei "Deckungsgrad", "finanzielle Freiheit", "reicht mein passives Einkommen", "Entnahmerate", "wann kann ich aufhören zu arbeiten" oder "Lücke passives Einkommen".
---

# Deckungsgrad passives Einkommen

Ziel: Zeigen, wie viel des Bedarfs ohne Gehalt das passive Einkommen deckt und was die Lücke oder den Überschuss am stärksten verändert. Ergebnis im Chat.

Quellen, Annahmen und feste Entscheidungen stehen im `Finanzprofil.md`. Den Bedarf liefert der Skill `bedarf`, oder die letzte Vorauswertung im Profil. Nicht neu erfragen, was dort steht. Fehlt das Profil, den Skill `start` ausführen.

## Vorgehen

1. **Passives Einkommen netto je Quelle** ansetzen: Vermietung nach laufenden Kosten und Zinsen, Pacht nach Betriebsbeiträgen, PV-Einspeisung, Zinsen, Depotentnahme netto nach Steuer. Nicht ansetzen, was der Nutzer ausgeschlossen hat (z. B. Holzerlöse als Rücklage).
2. **Bedarf ohne Gehalt** aus dem Skill `bedarf`, inklusive Kredittilgung, Krankenversicherung und Steuer.
3. **Deckungsgrad** = passives Einkommen geteilt durch Bedarf, dazu Lücke oder Überschuss pro Monat und Jahr.
4. **Zeitliche Änderungen** abbilden: Pachtanpassungen, Kreditende, Wegfall von Kita oder Kindergeld.
5. **Szenarien** gegenüberstellen:
   - Krankenversicherung von Mindest- bis Höchstbeitrag
   - Entnahmerate 3 %, 3,5 % und 4 %. Bei langem Horizont eher 3 %, weil die 4-%-Regel auf rund 30 Jahre ausgelegt ist.
   - Renditeannahmen als Annahme kennzeichnen, Realwerte nach Inflation zusätzlich nennen.
   - Steuer auf Entnahmen mit Teilfreistellung und Sparerpauschbetrag.
6. **Größte Hebel** nennen: welche zwei Annahmen die Deckung am stärksten verschieben.

## Ausgabeformat im Chat

Tabelle mit Quelle und € pro Jahr, darunter Bedarf, Deckungsgrad und Lücke bzw. Überschuss pro Monat. Eine zweite Tabelle für die Szenarien. Danach höchstens drei offene Punkte.

## Stand sichern

Nach der Bestätigung im `Finanzprofil.md` die Angaben zum passiven Einkommen aktualisieren und im Abschnitt „Verlauf“ eine Zeile mit Datum, Bedarf, passivem Einkommen und Deckungsgrad anhängen. Neue Entscheidungen unter „Feste Entscheidungen“ eintragen. Vorher zeigen, was sich ändert.

## Prinzipien

- Rechnen per Skript und das Ergebnis prüfen.
- Entscheidungen des Nutzers als gesetzt behandeln, außer neue Zahlen sprechen dagegen.
- Marktannahmen (Rendite, Inflation) per Websuche prüfen und als Annahme kennzeichnen.
- Faktenbasis für die Entscheidung liefern, keine Anlageberatung.
