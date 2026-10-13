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

## Geplante Aufgabe

Der Skill `briefing` ist als Prompt für einen geplanten Lauf gedacht, zum Beispiel täglich um 6 Uhr: "Erstelle das tägliche Aktien-Briefing mit dem Skill briefing." Persönliche Werte (Depot, ETFs) gehören in den Prompt der Aufgabe, nicht ins Plugin.

## Benutzung

- "Zeig mir die trendstärksten Aktien" (Skill `momentum`)
- "Welche Value-Aktien haben Langfristpotenzial?" (Skill `value`)
- "Aktien-Briefing" (Skill `briefing`)

## Hinweis

Alle Ausgaben sind Recherche, keine Anlageberatung und keine Kaufempfehlung. Kennzahlen stammen aus öffentlichen Quellen und können abweichen oder veraltet sein.
