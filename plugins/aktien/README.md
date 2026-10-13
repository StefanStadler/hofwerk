# Plugin: aktien

Identifiziert Aktien nach festen Filtern: trendstarke Momentum-Werte, unterbewertete Value-Picks und ein tägliches Morgen-Briefing, das beides mit den wichtigsten Börsen-News verbindet.

## Skills

| Skill | Zweck |
|---|---|
| `momentum` | 5 bis 10 trendstärkste Aktien weltweit aus Kursmomentum, Fundamentaldaten und Expert Signals (TechCrunch, CEO-Aussagen), mit BOTSI-Rang und boerse.de-Rating |
| `value` | 5 global unterbewertete Aktien mit 5x bis 10x Langfristpotenzial, mit Value-Trap-Filter, Burggraben und Katalysator |
| `briefing` | Tägliches Morgen-Briefing: News der letzten 24 Stunden, dann `momentum` und `value` in einem Text |

## Voraussetzung

Websuche muss verfügbar sein. Es werden keine Dateien erzeugt, die Ausgabe kommt als Markdown in den Chat.

## Optional: Twelve Data

Ist der Konnektor Twelve Data verbunden, prüft `momentum` Kurs, RSI, GD50, GD200 und 52-Wochen-Spanne der Shortlist damit statt per Websuche. Der kostenlose Plan genügt (800 Credits pro Tag, 8 pro Minute), deckt aber nur US-Börsen ab und enthält keine Bewertungskennzahlen. Forward-KGV, PEG, Cashflow und Wachstum kommen deshalb weiter aus der Websuche. Ohne den Konnektor läuft alles wie bisher.

## Geplante Aufgabe

Der Skill `briefing` ist als Prompt für einen geplanten Lauf gedacht, zum Beispiel täglich um 6 Uhr: "Erstelle das tägliche Aktien-Briefing mit dem Skill briefing." Persönliche Werte (Depot, ETFs) gehören in den Prompt der Aufgabe, nicht ins Plugin.

## Benutzung

- "Zeig mir die trendstärksten Aktien" (Skill `momentum`)
- "Welche Value-Aktien haben Langfristpotenzial?" (Skill `value`)
- "Aktien-Briefing" (Skill `briefing`)

## Hinweis

Alle Ausgaben sind Recherche, keine Anlageberatung und keine Kaufempfehlung. Kennzahlen stammen aus öffentlichen Quellen und können abweichen oder veraltet sein.
