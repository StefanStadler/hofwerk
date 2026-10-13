---
name: momentum
description: Erstellt eine kompakte Übersicht der 5 bis 10 weltweit trendstärksten Aktien (USA, Europa, Asien) aus Kursmomentum, Fundamentaldaten und Expert Signals, ergänzt um BOTSI-Rang und boerse.de-Rating. Verwenden bei "Momentum-Aktien", "trendstarke Aktien", "Top-Momentum-Werte", "BOTSI-Übersicht" oder wenn ein geplanter Lauf trendstarke Aktien liefern soll.
---

# Momentum-Aktien

Ausgabe direkt im Chat als Markdown, keine Dateien. Kennzahlen vor Prosa, Abkürzungen beim ersten Auftreten kurz erklären (KGV = Kurs-Gewinn-Verhältnis, PEG = KGV geteilt durch Gewinnwachstum, RSI = Relative-Stärke-Index).

## Drei gleichwertige Säulen

1. **Kursmomentum**: Kurs nahe 52-Wochen-Hoch, positive Performance über 1, 3 und 6 Monate, Kurs über GD50 und GD200 (gleitende Durchschnitte über 50 und 200 Tage), hohe relative Stärke.
2. **Fundamentaldaten**: Umsatz- und Gewinnwachstum, vertretbare Bewertung (Forward-KGV, PEG).
3. **Expert Signals**: konkrete Aussagen von CEOs, aus Earnings Calls und Konferenzen zu Nachfrage, Engpässen, Wachstumsfeldern.

## Recherche

Datum immer in den Suchstring aufnehmen.

**Expert Signals zuerst, TechCrunch ist Pflicht.** WebFetch funktioniert nur für URLs, die vorher in einem Suchergebnis aufgetaucht sind. Direktes Abrufen von techcrunch.com schlägt fehl. Deshalb:

1. WebSearch zuerst, z. B. `site:techcrunch.com [Monat Jahr]` oder `techcrunch AI funding CEO [Monat Jahr]`.
2. 1 bis 2 relevante Artikel-URLs aus den Treffern per WebFetch holen. Die Snippets genügen als Signalbasis, wenn der Abruf scheitert.
3. Je Signal intern notieren: Firma/Ticker, Signal, Datum, URL. Nur Signale vom heutigen Tag oder den letzten 3 Tagen.
4. Danach weitere CEO-Aussagen suchen (Earnings-Call-Transkripte, Konferenzen, Branchenausblicke).

Qualitätsfilter für Signale: Earnings Calls nicht älter als 8 Wochen, Interviews und Konferenzen nicht älter als 4 Wochen. Die Aussage muss konkret sein (Engpass, Wachstum, Nachfrage, Investitionsabsicht), die Quelle seriös und verifizierbar, der Bezug zu einer Aktie oder einem Sektor herstellbar. Kein Social Media, keine Gerüchte. Ein TechCrunch-Signal mit CEO-Zitat und konkreter Marktgröße darf einen Kandidaten direkt auf die Longlist heben.

**Momentum-Listen**, je Region: globale Momentum-Listen, S&P 500/Nasdaq, DAX/STOXX 600, Nikkei/Hang Seng/KOSPI, 52-Wochen-Hochs mit starkem Gewinnwachstum. Je finaler Aktie gezielt Forward-KGV und PEG nachschlagen.

**Quellenrangfolge bei Widersprüchen:**

| Stufe | Quellen |
|---|---|
| 1 | investors.com (IBD 50), finviz.com, barchart.com |
| 2 | marketwatch.com, seekingalpha.com, zacks.com |
| 3 | boerse.de, handelsblatt.com, finanzen.net |

Stufe 1 gewinnt. Weichen zwei Quellen der Stufe 1 ab, die konservativere Einschätzung nehmen und mit `⚡ Quellen-Diskrepanz` kennzeichnen. Forward-KGV und PEG primär über finviz.com, Fallback macrotrends.net und Yahoo Finance.

## Auswahlkriterien

Momentum **und** Fundamentals müssen stimmen.

- **RSI(14)** idealerweise 50 bis 74. Ab 75 überkauft, mit `⚠️ RSI` kennzeichnen. Unter 50 kein Momentum-Kandidat.
- **PEG** idealerweise unter 2. Fehlt er, selbst berechnen (Forward-KGV geteilt durch erwartetes EPS-Wachstum in Prozent) und als `PEG*` kennzeichnen.
- Large und Mid Caps bevorzugen. Keine reinen Hype- oder Mikrocap-Werte ohne Fundamentalbasis.
- **Sektor-Cap**: höchstens 3 Titel je Sektor. Überschuss als `📌 Alternativkandidat` führen.

## Verifikation über boerse.de

Für jede ausgewählte Aktie per WebSearch (`boerse.de BOTSI [Ticker oder Firma]`):

- **BOTSI-Rang**, technischer Trendindikator. Niedrigere Zahl bedeutet stärkerer Trend: bis 50 Top-Tier, 50 bis 150 solide, 150 bis 300 mittel, über 300 schwach.
- **boerse.de-Rating** von AAA (höchste) bis C. Nicht abrufbar: `k.A.`

## Ausgabe

1. Einleitungssatz mit heutigem Datum und 1 bis 2 Sätzen Marktkontext.
2. Tabelle:

```
| # | Ticker | Firma | Region | Branche | Kurs | RSI | 1M % | 3M % | YTD % | Abst. 52W-Hoch | Fwd-KGV | PEG | EPS/Umsatz-Wachstum | BOTSI-Rang | Rating | Status |
```

   Status: `⚡ Neu`, `📌 Wdh.` oder `📌 Alternativkandidat`. Fehlende Daten als `k.A.`, nicht tagesaktuelle Werte mit `Stand: [Datum]` oder `*Schätzung`.
3. Nummerierte Begründungen, 1 bis 2 Sätze je Aktie: Momentum-Trigger, Fundamental-Qualität, Bestätigung durch BOTSI und Rating.
4. Disclaimer: keine Anlageberatung, keine Kaufempfehlung.
5. Sources-Liste mit allen verwendeten Links.

Etwa 500 bis 700 Wörter für diesen Teil.
