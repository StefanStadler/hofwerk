---
name: value
description: Findet 5 global unterbewertete Aktien mit solider Substanz und 5x bis 10x Langfristpotenzial (Anlagehorizont 5 bis 10 Jahre) und filtert Value-Traps aus. Verwenden bei "Value-Aktien", "günstige Langfrist-Aktien", "unterbewertete Aktien" oder "Aktien mit 5x Potenzial".
---

# Value-Picks mit Langfristpotenzial

Ausgabe direkt im Chat als Markdown, keine Dateien. Abkürzungen beim ersten Auftreten kurz erklären (P/B = Kurs-Buchwert-Verhältnis, P/FCF = Kurs zu freiem Cashflow, IV = innerer Wert).

Preis-zu-Wert schlägt hier Momentum. Ein Kurs auf Jahrestief darf qualifizieren, solange das Geschäft trägt und ein Katalysator für die Neubewertung erkennbar ist.

## Recherche

Datum in den Suchstring aufnehmen. Beispiele:

```
undervalued stocks long-term 5x 10x potential global [Jahr]
deep value stocks low P/E P/B global [Monat Jahr]
stocks trading below intrinsic value DCF [Jahr]
unloved sectors value investing opportunities [Monat Jahr]
[Firma] P/B P/FCF intrinsic value [Jahr]
```

| Stufe | Quellen |
|---|---|
| 1 | gurufocus.com (GF Value, DCF), finviz.com (Value-Filter), morningstar.com (Moat-Rating, Fair Value) |
| 2 | seekingalpha.com, fool.com, valueinvesting.io, macrotrends.net |
| 3 | finanzen.net |

Bei Widersprüchen gewinnt die höhere Stufe.

## Auswahl

Mindestens **3 von 5** Kriterien erfüllen:

| Kriterium | Zielwert |
|---|---|
| Forward-KGV | unter 15 oder deutlich unter Sektor-Median |
| P/B | unter 2,0 |
| P/FCF | unter 15 |
| PEG | unter 1,0 |
| Abschlag zum inneren Wert (DCF, GF Value, Morningstar Fair Value) | mindestens 20 % |

**Value-Trap-Filter, zwingend:**

- Negativer freier Cashflow über 2 Jahre oder länger: ausschließen.
- Nettoverschuldung/EBITDA über 5: ausschließen.
- Schrumpfende Umsätze ohne Trendwende-Katalysator: ausschließen.
- Reine Zykliker ohne strukturellen Vorteil: nicht ausschließen, aber mit `⚠️ Zykliker` kennzeichnen.

**Bonus:** erkennbarer Burggraben, wiederkehrende Umsätze, solide Kapitalallokation (Rückkäufe, stabile oder wachsende Dividende), klarer Katalysator (Spin-off, Management-Wechsel, neue Produktlinie, Sektorwandel, KI-Adoption).

**Diversität:** mindestens 3 Sektoren und mindestens 2 Regionen (USA, Europa, Asien) unter den 5 Picks.

Vorgehen: Longlist mit 8 bis 10 Werten, Trap-Filter anwenden, für die Top 5 P/B, P/FCF, Abschlag, Burggraben und Katalysator nachschlagen, Diversität prüfen.

## Ausgabe

Überschrift `## 💎 Value Picks – Langfrist 5x–10x Potenzial`, dann Tabelle:

```
| # | Ticker | Firma | Region | Branche | Kurs | Fwd-KGV | P/B | P/FCF | Rabatt z. IV | EPS-Wachstum | Burggraben | Katalysator | Status |
```

- **Rabatt z. IV**: Abschlag zum fairen Wert in Prozent, positiv heißt günstiger als Fair Value. Nicht verfügbar: `k.A.`
- **Burggraben**: `Breit`, `Eng`, `Keiner` oder `k.A.` (Morningstar Economic Moat, wenn verfügbar).
- **Katalysator**: 1 bis 3 Wörter, z. B. `Spin-off`, `KI-Adoption`, `Restrukturierung`.
- **Status**: `⚡ Neu`, `📌 Wdh.` oder `⚠️ Zykliker`.

Danach je Aktie 2 bis 3 Sätze Begründung: Warum unterbewertet, welche Kennzahl überzeugt am meisten, was ist der Burggraben, was löst die Neubewertung aus, und ein grober Zeitrahmen (z. B. "in 7 bis 10 Jahren plausibel, wenn ...").

Zum Schluss Disclaimer (keine Anlageberatung, 5x bis 10x ist ein Szenario, keine Prognose) und Sources-Liste mit allen Links. Etwa 400 bis 500 Wörter für diesen Teil.
