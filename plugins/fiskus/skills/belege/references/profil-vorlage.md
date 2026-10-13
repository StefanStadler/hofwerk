# Steuerprofil (Vorlage)

Diese Datei ausfüllen und als `Steuerprofil.md` im Steuer-Ordner oder Projekt ablegen. Sie ist die einzige Stelle mit persönlichen Daten. Das Plugin selbst enthält keine.

## Person
- Name:
- Anschrift:
- Finanzamt:
- Familienstand / Steuerklasse / Kinder (Sorgerecht, Kindergeld):
- Kirchensteuer: ja / nein (seit wann)

## Steuernummern
- Einkommensteuer:
- Umsatzsteuer (gesamtes Unternehmen) und PV:
- EÜR Freiberuf:
- EÜR Landwirtschaft:
- Hinweis auf typische Verwechslungen in WISO/ELSTER:

## Einkunftsarten und Objekte
- Land-/Forstwirtschaft (Betrieb, Waldfläche, § 34b ja/nein, Pauschalierung):
- Vermietung (Objekt, Kaltmiete):
- Freiberuf (Tätigkeit):
- Anlage N (Arbeitgeber, Wohnsitz, Elternzeit):
- Kapitalerträge / Renten (Banken, Riester o. Ä.):
- PV-Anlagen (Standort, kWp, Inbetriebnahme, Einspeiseart), ertragsteuerfrei nach § 3 Nr. 72 EStG:

## USt
- Besteuerungsform je Bereich (Regelbesteuerung, § 24 UStG, Kleinunternehmer):
- Optionsbindung je Objekt (bis wann, frühester Wechsel):

## Bereiche, Präfixe und Gmail-Labels
Eine Zeile je Bereich. Das Präfix steht im Dateinamen. Das Gmail-Unterlabel bestimmt den Namen unter `Rechnungen/Rechnungen_{JAHR}/` und wird nur für Bereiche vergeben, die hier stehen. Bleibt die Spalte leer, gilt der Bereichsname.

| Bereich | Präfix | Gmail-Unterlabel |
|---|---|---|
| Land-/Forstwirtschaft | LuF | Landwirtschaft |
| IT-Beratung | IT | IT-Beratung |
| PV-<Standort> | PV-<Standort> | PV-<Standort> |
| Vermietung | V | Vermietung |
| Anlage N | AN | Arbeitnehmer |

Weitere Präfixe, z. B.: KIND, VERS, AgB

## Händlerregeln (Absender zu Bereich)
Eindeutige Absender oder Händler und ihr Bereich. Die Skills schlagen neue Zeilen nach Bestätigung des Nutzers vor. Was nicht eindeutig ist, steht hier nicht und bekommt kein Bereichs-Unterlabel.

| Absender / Händler (Muster) | Bereich | Anmerkung |
|---|---|---|
| | | |

## Konten (Unterordner in 1_Eingang/Kontoauszuege)
-

## Feste Entscheidungen des Jahres
Beispiel: Investitionsabzugsbetrag ja/nein, Zuflussjahr bestimmter Zuschüsse, Zuordnung einzelner Einnahmen.

## Vorjahreswerte (Vergleich)
Ergebnisse je Bereich, Kapitalerträge, Bescheide, USt-Zahllast.

## Stand Steuerjahr {JAHR}
Wird von den Skills nach Bestätigung aktualisiert. Je Zeile Datum und Ergebnis.
- Belege:
- Online-Rechnungen:
- Schätzung:
- USt:
- Offene Punkte:

## Zu klären für das Jahr
-
