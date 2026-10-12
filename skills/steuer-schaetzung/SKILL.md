---
name: steuer-schaetzung
description: Schätzt die Steuerlast eines Steuerjahrs (Einkommensteuer inkl. Soli und ggf. Kirchensteuer, Umsatzsteuer-Zahllast) und vergleicht Szenarien wie Investition mit oder ohne Investitionsabzugsbetrag, Zuflussjahr von Zuschüssen, Forstpauschale gegen Ist-Kosten. Verwenden bei "Steuerlast schätzen", "Steuer hochrechnen", "Nachzahlung 20xx", "lohnt sich der Traktorkauf steuerlich", "Gewinn ins nächste Jahr verschieben", "IAB" oder "Steuerschätzung".
---

# Steuerlast-Schätzung

Ziel: Steuerlast des Jahres `{JAHR}` hochrechnen, um Investitionen und Gewinnverlagerung zu steuern. Ergebnisse und offene Punkte nur im Chat, keine Dokumente, außer sie sind ausdrücklich gewünscht. Du bist kein Steuerberater. Das Ergebnis ist eine Schätzung, kein Bescheid. Das einmal kurz erwähnen, nicht bei jedem Absatz.

Persönliche Angaben (Steuerklasse, Kinder, Objekte, Einkunftsarten, feste Entscheidungen, Vorjahreswerte) stehen im `Steuerprofil.md`. Zuerst lesen, fehlende Angaben beim Nutzer erfragen.

## Vorgehen

1. **Einkünfte je Anlage ermitteln** aus Kontoauszügen und Belegen: Land- und Forstwirtschaft (Anlage L, Wald mit oder ohne § 34b, Pauschalierung), Vermietung (V), Freiberuf (S), Arbeitnehmer (N), Kapital (KAP), Renten (R). PV-Anlagen sind ertragsteuerfrei nach § 3 Nr. 72 EStG, werden aber bei der Umsatzsteuer berücksichtigt.
2. **Abzüge ansetzen**: Sonderausgaben, Vorsorgeaufwand, Kinderfreibetrag bzw. Kindergeld (Günstigerprüfung), Entlastungsbetrag für Alleinerziehende, § 35a-Aufwendungen, ggf. Sparer-Pauschbetrag.
3. **Tarif des Jahres anwenden**: Grundtarif oder Splitting, Solidaritätszuschlag mit Freigrenze und Milderungszone, Kirchensteuer nur wenn laut Profil pflichtig. Tarifwerte des Jahres per Websuche prüfen, nicht aus dem Gedächtnis nehmen.
4. **Ergebnis als Spanne** angeben: konservativ und wahrscheinlich. Die Annahmen dahinter nennen.
5. **Szenarien rechnen** (siehe `references/szenarien.md`) und gegenüberstellen.
6. **Vergleich mit Vorjahren**: Bescheide und Übersichten laut Profil heranziehen.

## Ausgabeformat im Chat

Tabelle mit den Varianten in den Zeilen und konservativ/wahrscheinlich in den Spalten, Nachzahlung (+) oder Erstattung (−), jeweils ESt plus Soli. Darunter USt-Zahllast mit Spanne und Fälligkeit. Danach höchstens fünf offene Punkte, die das Ergebnis am stärksten verändern. Eine Frage zur Entscheidung nur, wenn sie wirklich offen ist.

## Prinzipien

- Rechenschritte per Skript ausführen und das Ergebnis prüfen, nicht im Kopf rechnen.
- Annahmen und Datenlücken klar benennen, aber knapp.
- Im Zweifel zugunsten des Nutzers kategorisieren, soweit steuerlich vertretbar.
- Entscheidungen des Nutzers (z. B. kein Investitionsabzug, Zuflussjahr eines Zuschusses) als gesetzt behandeln und nicht erneut zur Diskussion stellen, außer neue Zahlen sprechen dagegen.
- Arbeitsdaten und Rechenskripte in `9_Archiv/Arbeitsdateien/` sichern.
