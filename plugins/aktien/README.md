# Plugin: aktien

Identifiziert Aktien nach festen Filtern: trendstarke Momentum-Werte, unterbewertete Value-Picks und ein tägliches Morgen-Briefing, das beides mit den wichtigsten Börsen-News verbindet.

## Skills

| Skill | Zweck |
|---|---|
| `momentum` | 5 bis 10 trendstärkste Aktien weltweit aus Kursmomentum, Fundamentaldaten und Expert Signals (TechCrunch, CEO-Aussagen) |
| `value` | 5 global unterbewertete Aktien mit 5x bis 10x Langfristpotenzial, mit Value-Trap-Filter, Burggraben und Katalysator |
| `briefing` | Tägliches Morgen-Briefing: News der letzten 24 Stunden, dann `momentum` und `value` in einem Text |

## Voraussetzung

Websuche und Abruf von Webseiten (WebFetch) müssen verfügbar sein. Es werden keine Dateien erzeugt, die Ausgabe kommt als Markdown in den Chat.

## Datenquellen

- **News:** Feeds von Finanznachrichten.de, Handelsblatt, MarketWatch, Investing.com und TechCrunch, per WebSearch ergänzt oder ersetzt, wenn ein Feed ausfällt.
- **Expert Signals:** TechCrunch-Feed, Newsroom- und Investor-Relations-Seiten der Shortlist-Aktien, optional Google-Alert-Mails aus Gmail, danach WebSearch nach CEO-Aussagen und Earnings Calls.
- **Kennzahlen:** Websuche, vor allem finviz und Yahoo Finance.
- **Google Finance:** Kurs, 52-Wochen-Spanne und KGV für Aktien außerhalb der US-Börsen sowie die aktuellen Schlagzeilen je Shortlist-Aktie.

## Optional: Twelve Data

Ist der Konnektor Twelve Data verbunden, prüft `momentum` Kurs, RSI, GD50, GD200 und 52-Wochen-Spanne der Shortlist damit statt per Websuche. Der kostenlose Plan genügt (800 Credits pro Tag, 8 pro Minute), deckt aber nur US-Börsen ab und enthält keine Bewertungskennzahlen. Forward-KGV, PEG, Cashflow und Wachstum kommen deshalb weiter aus der Websuche. Ohne den Konnektor läuft alles wie bisher.

## Optional: Google Alerts über Gmail

Legt der Nutzer Google Alerts an (z. B. `"Firma" CEO OR interview OR "said"`, höchstens einmal täglich), liest `briefing` die Alert-Mails von `googlealerts-noreply@google.com` über den Gmail-Konnektor, übernimmt konkrete CEO-Aussagen und gibt sie als Expert Signals an `momentum` weiter. Die Mailbox wird nur gelesen. Ohne Gmail-Konnektor entfällt der Schritt.

## Geplante Aufgabe

Der Skill `briefing` ist als Prompt für einen geplanten Lauf gedacht, zum Beispiel täglich um 6 Uhr: "Erstelle das tägliche Aktien-Briefing mit dem Skill briefing." Persönliche Werte (Depot, ETFs) gehören in den Prompt der Aufgabe, nicht ins Plugin.

## Benutzung

- "Zeig mir die trendstärksten Aktien" (Skill `momentum`)
- "Welche Value-Aktien haben Langfristpotenzial?" (Skill `value`)
- "Aktien-Briefing" (Skill `briefing`)

## Hinweis

Alle Ausgaben sind Recherche, keine Anlageberatung und keine Kaufempfehlung. Kennzahlen stammen aus öffentlichen Quellen und können abweichen oder veraltet sein.
