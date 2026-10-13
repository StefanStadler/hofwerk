---
name: bedarf
description: Berechnet Fixkosten und den monatlichen Lebensbedarf aus Kontoauszügen (CSV oder kopierter Text), trennt fixe, variable und einmalige Posten und schätzt Lebensmittel und Bargeld. Verwenden bei "Fixkosten berechnen", "was brauche ich im Monat", "Lebenshaltungskosten", "Bedarf ohne Gehalt", "wie viel gebe ich für Lebensmittel aus" oder "Kontoauszug auswerten".
---

# Fixkosten und Lebensbedarf

Ziel: Aus Kontoauszügen den monatlichen Bedarf ableiten, getrennt nach fix, variabel und einmalig. Ergebnis im Chat, keine Dokumente, außer sie sind ausdrücklich gewünscht.

Persönliche Angaben (Konten, Kredite, Annahmen, Vorauswertungen, feste Entscheidungen) stehen im `Finanzprofil.md`. Zuerst lesen und an der letzten Vorauswertung ansetzen, statt neu zu beginnen. Fehlt das Profil, den Skill `start` ausführen. Vorlage: `references/profil-vorlage.md`.

## Vorgehen

1. **Daten einlesen** und den Zeitraum nennen. Erste Auswertung mit `scripts/kontoauswertung.py` (siehe unten), danach die Ergebnisse mit dem Nutzer prüfen und von Hand korrigieren. Nicht im Kopf rechnen.
2. **Nur Ausgaben zählen.** Ausschließen: Überträge zwischen eigenen Konten (Inhaber als Gegenpartei, Hin- und Rückbuchung), Depot- und Bausparbewegungen, alle Zuflüsse (Gehalt, ALG, Kindergeld, Unterhaltsvorschuss, Miete, Pacht, Einspeisevergütung, Erstattungen).
3. **Fixe Posten erkennen:** gleicher Empfänger in mindestens drei verschiedenen Monaten bei ähnlichem Betrag (±10 %). Jahresbeiträge durch 12 teilen. Fehlt im laufenden Monat eine erwartete Abbuchung, das melden, damit die Summe nicht stillschweigend zu niedrig ist.
4. **Quasi-fixe Posten mit schwankender Höhe** (Kita, Abschläge): Mittelwert der letzten 3 bis 6 Monate. Nennt der Nutzer einen neuen Betrag, gilt dieser ab sofort.
5. **Variable Posten** über volle Monate mitteln, den laufenden Monat getrennt zeigen: Lebensmittel (Supermarkt, Bäcker, Metzger), Gastronomie getrennt, Tanken, Drogerie, Onlinehandel.
6. **Bargeld an Supermarktkassen:** Abhebungen an der Kasse stecken im Einkaufsbetrag. Auffällig sind Einkäufe ab ca. 200 € in sonst kleinen Märkten. Vor dem Hochrechnen der Lebensmittel den Nutzer fragen und abgehobene Beträge als Bargeld getrennt führen. Einmalige Bargeldverluste und Urlaubsmonate nicht hochrechnen.
7. **Einmalige Posten** ausschließen, aber nennen: Inkasso, Reparaturen, Zahnarzt, Reisen, Anschaffungen.
8. **Konten abgrenzen:** Was nicht auf dem ausgewerteten Konto liegt (Kreditrate, Strom, Wasser, Gebäude- und Kfz-Versicherung, Steuern), ausdrücklich nennen und aus dem Profil oder der Vorauswertung ergänzen.
9. **Gesamtbedarf** bilden: Lebenshaltung plus Kredittilgung, Krankenversicherung für die Zeit ohne Gehalt und Einkommensteuer, jeweils als Annahme gekennzeichnet. Mit der Vorauswertung im Profil vergleichen und die größten Abweichungen benennen.

## Dokumenteingang

Jede Datei, die der Nutzer im Chat schickt (Kontoexport, Kontoauszug, Bescheid), kommt zuerst unverändert in den Eingang: `<Finanzordner>/1_Eingang/`, Kontoauszüge nach `Kontoauszuege/<Konto>/`, Bescheide und Verträge nach `Bescheide_Vertraege/`, alles andere nach `Sonstiges/`. Originalname und Inhalt bleiben, nichts wird umbenannt, gedreht oder geändert. Erst danach wird gerechnet, immer aus einer Kopie. Dem Nutzer in einem Satz sagen, wo das Original liegt. Ist kein Finanzordner verbunden, trotzdem auswerten und darauf hinweisen, dass das Original noch nicht abgelegt ist.

Für Kontoauszüge übernimmt das `--ablegen`: Es kopiert das Original byte-identisch, überspringt gleiche Inhalte und setzt bei eingefügtem Text mit „Heute“ und „Gestern“ das Einfügedatum als Namenspräfix, damit die Daten später stimmen. Text aus dem Chat zuerst unverändert als Datei speichern (z. B. `einfuegung.txt`) und dann ablegen. Beim nächsten Lauf genügt der Ordner `1_Eingang/Kontoauszuege` als Eingabe. Überlappende Exporte zählen einmal.

## Skript

```
python3 scripts/kontoauswertung.py <datei|ordner> [weitere ...] --heute JJJJ-MM-TT --inhaber "Vorname Nachname" \
  --ablegen <Finanzordner> --konto <Kontoname>
```

Eingabe sind eine oder mehrere Dateien oder ein Ordner (rekursiv). Erkannt werden ein CSV-Export (Spalten Buchungstag, Buchungstext, Umsatz) oder aus der Bank kopierter Text. Das Skript trennt Überträge an den Inhaber, erkennt wiederkehrende Posten (mindestens drei Monate, Betrag ±10 %), mittelt variable Kategorien über volle Monate, markiert Lebensmittel-Einkäufe ab 150 € als möglichen Bargeldbezug (`--kasse` ändert die Schwelle) und meldet fehlende Abbuchungen im laufenden Monat. Die Händlerregeln stehen in `references/kategorien.json`, eigene Regeln kommen per `--regeln` dazu. `--json` liefert maschinenlesbare Ausgabe. Das Skript ist eine Vorauswertung: Kita, Abschläge und Sonderfälle bleiben Sache der Prüfung mit dem Nutzer.

## Ausgabeformat im Chat

Tabelle mit Position und € pro Monat, darunter Zwischensumme Lebenshaltung und Gesamtbedarf pro Monat und Jahr. Danach höchstens drei Hinweise zu Lücken oder unsicheren Annahmen, die das Ergebnis am stärksten verändern. Eine Frage nur, wenn sie wirklich offen ist.

## Stand sichern

Nach der Bestätigung durch den Nutzer im `Finanzprofil.md` den Abschnitt „Vorauswertung“ ersetzen (Datum, Zeitraum, Fixkosten und Gesamtbedarf pro Monat, Annahmen) und im Abschnitt „Verlauf“ eine Zeile anhängen. Vom Nutzer genannte Korrekturen und Entscheidungen (z. B. neuer Kita-Betrag, Bargeld-Annahme) unter „Feste Entscheidungen“ eintragen. Vorher zeigen, was sich ändert.

## Prinzipien

- Korrekturen des Nutzers sofort übernehmen und die Summe neu nennen.
- Entscheidungen des Nutzers aus dem Profil (z. B. Kredittilgung im Bedarf lassen) als gesetzt behandeln.
- Optionale Ausgaben (Lifestyle, Onlinehandel, Seminare) getrennt vom Bedarf ausweisen.
- Annahmen und Datenlücken knapp benennen.
