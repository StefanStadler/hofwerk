# Ordnerstruktur (Steuer {JAHR})

## 1_Eingang/ (Rohmaterial, nicht verändern)
Kontoauszuege (je Konto ein Unterordner laut Steuerprofil) · Scans_Fotos · Mail_Downloads (optional je Bereich ein Unterordner) · Telefon · Online_Bestellungen (z. B. eBay, Amazon)

## 2_Steuererklaerung_Wiso/ (Sortierung wie in WISO)
- 01_Persoenliches
- 02_Anlage_N_Arbeitnehmer
- 03_Anlage_KAP_Kapitalertraege
- 04_Anlage_R_Renten
- 05_Anlage_L_Landwirtschaft (Einnahmen · Ausgaben/{Versicherungen_Beitraege, Gebaeude_Hof, Energie_Wasser_Heizung, Maschinen_Werkzeug, Kfz} · Forst · Nachweise)
- 06_Anlage_V_Vermietung (Einnahmen · Betriebskosten · Erhaltungsaufwand)
- 07_Anlage_S_Freiberuflich (Einnahmen · Ausgaben)
- 08_Anlage_Kind (Unterhalt · Kinderbetreuung)
- 09_Anlage_Vorsorgeaufwand_Versicherungen
- 10_Anlage_Sonderausgaben_Spenden
- 11_Anlage_Aussergewoehnliche_Belastungen
- 12_Anlage_Haushaltsnahe_Aufwendungen
- 13_Umsatzsteuer (Jahreserklaerung · Voranmeldungen · je PV-Anlage ein Unterordner)
- 99_Nicht_abzugsfaehig

## 3_Ausgang_DATEV/ (DATEV-Fächer)
01_Unsortiert · 02_Arbeitnehmer · 03_Aussergewoehnliche_Belastungen · 04_Gewerbebetriebe_und_Selbststaendigkeit/{Landwirtschaft, IT-Beratung, PV-Anlagen} · 05_Handwerker_und_haushaltsnahe_DL · 06_Kapitalanlagen · 07_Kinder · 08_Renten · 09_Sonderausgaben_und_Spenden · 10_Vermietungen · 11_Versicherungen · 12_Weitere_Einnahmen

## 9_Archiv/
Vorjahr_Uebertrag · Folgejahr_{JAHR+1} (Belege, die erst im Folgejahr zählen) · Arbeitsdateien

## Zuordnung WISO → DATEV
| WISO | DATEV |
|---|---|
| 02 Anlage N | 02_Arbeitnehmer |
| 03 Anlage KAP | 06_Kapitalanlagen |
| 04 Anlage R | 08_Renten |
| 05 Anlage L | 04_…/Landwirtschaft |
| 06 Anlage V | 10_Vermietungen |
| 07 Anlage S | 04_…/IT-Beratung |
| 08 Anlage Kind | 07_Kinder |
| 09 Vorsorge/Versicherungen | 11_Versicherungen |
| 10 Sonderausgaben/Spenden | 09_Sonderausgaben_und_Spenden |
| 11 Außergewöhnliche Belastungen | 03_Aussergewoehnliche_Belastungen |
| 12 Haushaltsnahe | 05_Handwerker_und_haushaltsnahe_DL |
| 13 Umsatzsteuer (PV) | 04_…/PV-Anlagen |
| Sonstige Einnahmen | 12_Weitere_Einnahmen |
| nicht zuordenbar | 01_Unsortiert |
