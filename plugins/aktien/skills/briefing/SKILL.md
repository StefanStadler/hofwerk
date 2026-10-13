---
name: briefing
description: Erstellt das tägliche Aktien-Morgen-Briefing auf Deutsch: marktbewegende News der letzten 24 Stunden, danach die Momentum-Übersicht und 5 Value-Picks. Verwenden bei "Aktien-Briefing", "Morgen-Briefing", "was bewegt die Märkte" oder als Prompt für einen geplanten täglichen Lauf.
---

# Tägliches Aktien-Briefing

Ein kompakter Markdown-Text direkt im Chat, keine Dateien. Etwa 1.400 bis 1.800 Wörter gesamt. Bei einem geplanten, unbeaufsichtigten Lauf nicht nachfragen, sondern mit den Vorgaben unten arbeiten.

## Teil 1: Marktbewegende News

Gesucht sind die wichtigsten Meldungen der letzten 24 Stunden, die Aktien oder Märkte bewegen: Unternehmensmeldungen, Zulassungen und Durchbrüche, Übernahmen, Zinsentscheide, Geopolitik, Quartalszahlen.

Zuerst die RSS-Feeds per WebFetch abrufen. Sie sind ohne Anmeldung erreichbar und liefern Titel, Zeitstempel und Link:

| Feed | URL | Schwerpunkt |
|---|---|---|
| Finanznachrichten.de | `https://www.finanznachrichten.de/rss-nachrichten` | Börsenticker auf Deutsch (dpa-AFX, Dow Jones News, ARIVA, XTB), meist nur Überschrift und Link, schnellste Quelle |
| Handelsblatt Finanzen | `https://feeds.cms.handelsblatt.com/finanzen` | Märkte, Dax, Übernahmen auf Deutsch |
| MarketWatch | `https://feeds.content.dowjones.io/public/rss/mw_topstories` | US-Märkte, enthält auch Ratgeberartikel, nur Börsenrelevantes übernehmen |
| Investing.com | `https://www.investing.com/rss/news_25.rss` | Aktienmarkt-News global, Überschrift und Link vor der Übernahme abgleichen |
| TechCrunch | `https://techcrunch.com/feed/` | Tech, Finanzierungen, Übernahmen |

Einträge nach Zeitstempel auf die letzten 24 Stunden filtern, Doppelte zusammenführen und die 4 bis 6 marktbewegendsten wählen. Eine Meldung nur aufnehmen, wenn sie eine Aktie, einen Sektor oder die Gesamtmärkte bewegen kann.

Fehlt in den Feeds etwas Wichtiges (Zinsentscheid, Quartalszahlen großer Firmen, Geopolitik) oder fällt ein Feed aus: ergänzend WebSearch mit Datum und Uhrzeit im Suchstring. Nicht abrufbar und nicht erneut zu versuchen: Bloomberg, Reuters, CNBC, BBC, Tagesschau, SEC und finviz. Der Yahoo-Finance-Feed lieferte veraltete Einträge und wird nicht genutzt.

4 bis 6 Meldungen im Stil der Tagesschau-Wirtschaft, sachlich und kompakt. Je Meldung:

- Kurzüberschrift
- Datum und Uhrzeit
- 2 bis 3 Sätze Zusammenfassung
- betroffene Aktien mit Ticker und, falls bekannt, die Kursreaktion

Quellen nur zitieren, nicht abschreiben: eigene Worte, höchstens ein kurzes Zitat je Quelle.

### CEO-Aussagen aus Google Alerts (optional)

Nur wenn ein Gmail-Konnektor verfügbar ist (Werkzeuge mit dem Präfix `mcp__Gmail__`). Der Nutzer kann Google Alerts für Firmen und Branchen angelegt haben, die als Mails von `googlealerts-noreply@google.com` ankommen. Sonst entfällt dieser Abschnitt.

1. `search_threads` mit `from:googlealerts-noreply@google.com newer_than:1d` (bei Bedarf `newer_than:2d`).
2. Betreff und Auszug der Mails lesen, bei Bedarf `get_message`. Je Alert stehen dort Titel, Quelle und Link der Treffer.
3. Nur konkrete Aussagen von Führungskräften übernehmen (Nachfrage, Engpässe, Prognosen, Investitionen). Reine Berichte über Kursbewegungen oder Meinungsartikel auslassen.
4. In die News aufnehmen, wenn die Aussage marktbewegend ist. Sonst als Signal für `momentum` merken: Firma/Ticker, Aussage in eigenen Worten, Datum, Link.
5. Treffer gelten als Hinweis, nicht als Beleg. Wichtige Aussagen über eine zweite Quelle bestätigen oder weglassen.
6. Mails nur lesen, nichts archivieren, löschen oder beantworten.

## Teil 2: Momentum und Value

1. Skill `momentum` ausführen und sein Ergebnis (Tabelle, Begründungen) übernehmen. Die gemerkten CEO-Signale aus den Google Alerts dabei als Expert Signals mitgeben.
2. Skill `value` ausführen und sein Ergebnis (Tabelle, Begründungen) übernehmen.
3. Disclaimer und Sources der beiden Teile zu je einem gemeinsamen Abschnitt zusammenführen.

Aktien aus Teil 1, die in Teil 2 auftauchen, in der Begründung kurz verknüpfen.

## Persönlicher Kontext

Das Plugin enthält keine persönlichen Daten. Hält der Nutzer bestimmte Werte oder ETFs, kann er sie im Prompt der geplanten Aufgabe nennen. Sie dienen dann als Kontext für die Auswahl der News, nicht als Pflicht für die Auswahl der Aktien. Der Nutzer mag keine unerklärten Finanzabkürzungen, deshalb beim ersten Auftreten ausschreiben.

## Reihenfolge

1. Datum und ein Satz Marktlage
2. News (Teil 1)
3. Momentum-Tabelle und Begründungen
4. Trennlinie, Value-Tabelle und Begründungen
5. Disclaimer
6. Sources
