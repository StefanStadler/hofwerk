---
name: regeln
description: Pflegt die Regeln in der Postfachregeln.md: leitet aus Entscheidungen des Nutzers neue Regeln ab, ändert oder entfernt bestehende und testet sie vorher gegen das Postfach. Verwenden bei "mach daraus eine Regel", "neue Regel", "Regel ändern", "Regel löschen", "merk dir das fürs Sortieren", "Regeln anzeigen" oder wenn beim Sortieren eine Entscheidung wiederholt auftaucht.
---

# Regeln pflegen

Zuerst die `Postfachregeln.md` lesen. Fehlt sie, den Skill `start` ausführen. Regeln entstehen nur aus dem, was der Nutzer ausdrücklich entschieden hat. Nichts aus einem einzelnen Fall verallgemeinern, ohne zu fragen.

## Vorgehen

1. **Regel formulieren.** Aus der Entscheidung eine Zeile bauen: Wenn (Absender, Stichwort, Muster), Dann (Im Posteingang lassen, Label, Label + archivieren, Papierkorb), Label, Bemerkung. So eng wie möglich fassen, lieber ein Absender als eine ganze Domain.
2. **Gegen das Postfach testen.** Nur lesend: mit `search_threads` zählen, wie viele Threads die Regel treffen würde, und wenige Beispiele nennen. Trifft sie viel mehr als gedacht, die Regel enger fassen und das sagen.
3. **Konflikte prüfen.** Überschneidet sich die Regel mit einer bestehenden (gleicher Absender, anderes Ziel, Oberbegriff)? Beide nebeneinanderlegen und fragen, welche gilt oder in welcher Reihenfolge.
4. **Änderung zeigen.** Die neue, geänderte oder gelöschte Zeile als Vorher/Nachher vorlegen und um ein klares Ja bitten.
5. **Speichern.** Nur die betroffene Zeile in der `Postfachregeln.md` ändern. Entscheidungen, die keine Regel sind (z. B. „Kanzleipost bleibt immer im Posteingang“), unter „Feste Entscheidungen“ mit Datum eintragen.
6. **Bestehende Mails.** Fragen, ob die neue Regel auch auf schon vorhandene Mails angewendet werden soll. Wenn ja, den Skill `sortieren` mit dieser Regel ausführen. Nicht stillschweigend rückwirkend sortieren.

## Regeln für Regeln

- Papierkorb-Regeln nur auf ausdrücklichen Wunsch anlegen und eng fassen.
- Kein Wildcard-Löschen. Regeln für Behörden, Gerichte, Anwälte, Steuerberater und Fristen lauten immer „Im Posteingang lassen“, solange der Nutzer nichts anderes sagt.
- Eine Regel, die nie trifft, beim nächsten Überblick vorschlagen zu entfernen, aber nicht von sich aus löschen.
- Löschen einer Regel heißt, die Zeile zu entfernen, nicht sie umzuformulieren.
