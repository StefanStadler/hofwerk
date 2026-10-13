#!/usr/bin/env python3
"""Fixkosten- und Bedarfsauswertung aus Kontoumsätzen.

Eingabe: CSV-Export (Spalten Buchungstag, Buchungstext, Umsatz) oder kopierter Text
         (Zeilen: Datum <TAB> Text <TAB> Betrag). Nur Standardbibliothek.
Aufruf:  python3 kontoauswertung.py umsaetze.csv [weitere.csv|Ordner] --heute 2026-10-13 --inhaber "Vorname Nachname"
         --ablegen <Finanzordner> --konto Girokonto   (Exporte lokal sichern)
"""
import argparse, csv, json, re, statistics, sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

BETRAG = re.compile(r"^-?\d{1,3}(?:\.\d{3})*,\d{2}$|^-?\d+,\d{2}$")


def betrag(s):
    s = s.replace("€", "").replace("EUR", "").strip()
    if not BETRAG.match(s):
        return None
    return float(s.replace(".", "").replace(",", "."))


def datum(s, heute):
    s = s.strip().lower()
    if s == "heute":
        return heute
    if s == "gestern":
        return heute - timedelta(days=1)
    m = re.match(r"(\d{2})\.(\d{2})\.(\d{4})$", s)
    if m:
        return date(int(m[3]), int(m[2]), int(m[1]))
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})$", s)
    return date(int(m[1]), int(m[2]), int(m[3])) if m else None


def lade(pfad, heute):
    roh = Path(pfad).read_text(encoding="utf-8-sig", errors="replace")
    zeilen, kopf = [], None
    for z in roh.splitlines():
        if ";" in z and kopf is None and "Buchungstag" in z:
            kopf = [c.strip().strip('"') for c in z.split(";")]
            break
    if kopf:  # CSV
        i_d = next(i for i, c in enumerate(kopf) if c.startswith("Buchungstag"))
        i_t = next(i for i, c in enumerate(kopf) if "text" in c.lower() or "Vorgang" in c)
        i_b = next(i for i, c in enumerate(kopf) if "Umsatz" in c)
        start = roh.splitlines().index(next(z for z in roh.splitlines() if "Buchungstag" in z)) + 1
        for r in csv.reader(roh.splitlines()[start:], delimiter=";"):
            if len(r) <= max(i_d, i_t, i_b):
                continue
            d, b = datum(r[i_d], heute), betrag(r[i_b])
            if d and b is not None:
                zeilen.append((d, r[i_t].strip(), b))
        return zeilen
    for z in roh.splitlines():  # kopierter Text
        teile = [t.strip() for t in z.split("\t") if t.strip()]
        if len(teile) < 3:
            continue
        d, b = datum(teile[0], heute), betrag(teile[-1])
        if d and b is not None:
            text = re.sub(r"^(neu|offen)\s+", "", " ".join(teile[1:-1]), flags=re.I)
            zeilen.append((d, text, b))
    return zeilen


def regeln_laden(extra):
    pfad = Path(__file__).resolve().parent.parent / "references" / "kategorien.json"
    r = json.loads(pfad.read_text(encoding="utf-8"))["regeln"]
    if extra:
        r = json.loads(Path(extra).read_text(encoding="utf-8"))["regeln"] + r
    return r


def kategorie(text, regeln):
    t = text.lower()
    for r in regeln:
        if any(m in t for m in r["muster"]):
            return r
    return None


def schluessel(text):
    t = re.sub(r"[^a-zäöüß+ ]", " ", text.lower())
    return " ".join(t.split()[:2]) or text.lower()


def dateien_sammeln(pfade):
    """Dateien oder Ordner (rekursiv: .csv, .txt) in eine Dateiliste auflösen."""
    out = []
    for x in pfade:
        pp = Path(x)
        if pp.is_dir():
            out += sorted(f for f in pp.rglob("*") if f.suffix.lower() in (".csv", ".txt"))
        else:
            out.append(pp)
    return out


def zusammenfuehren(listen):
    """Mehrere Exporte ohne Dubletten vereinen. Überlappende Zeiträume zählen einmal:
    je identischer Buchung gilt die höchste Anzahl in einer einzelnen Datei."""
    from collections import Counter
    best = Counter()
    for zeilen in listen:
        for k, v in Counter(zeilen).items():
            best[k] = max(best[k], v)
    return sorted(best.elements())


def ablegen(datei, zeilen, ziel, konto):
    """Export nach <ziel>/Kontoauszuege/<konto>/ sichern. Kopierter Text wird als CSV mit
    festen Datumsangaben gespeichert. Schon vorhandene Inhalte (Hash) werden übersprungen."""
    import hashlib
    ordner = Path(ziel) / "Kontoauszuege" / konto
    ordner.mkdir(parents=True, exist_ok=True)
    roh = datei.read_text(encoding="utf-8-sig", errors="replace")
    ist_csv = ";" in roh and "Buchungstag" in roh
    if ist_csv:
        inhalt, endung = roh, ".csv"
    else:
        zeilen_csv = ["Buchungstag;Buchungstext;Umsatz in EUR"] + [
            f"{d:%d.%m.%Y};{t.replace(';', ',')};" + f"{b:.2f}".replace(".", ",")
            for d, t, b in zeilen]
        inhalt, endung = "\n".join(zeilen_csv) + "\n", ".csv"
    h = hashlib.sha256(inhalt.encode("utf-8")).hexdigest()[:8]
    if any(f.name.endswith(f"_{h}{endung}") for f in ordner.iterdir()):
        return None
    von, bis = zeilen[0][0], zeilen[-1][0]
    ziel_datei = ordner / f"{von:%Y-%m-%d}_bis_{bis:%Y-%m-%d}_{h}{endung}"
    ziel_datei.write_text(inhalt, encoding="utf-8")
    return ziel_datei


def monat(d):
    return d.year * 12 + d.month


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dateien", nargs="+", help="Dateien oder Ordner (Ordner werden rekursiv gelesen)")
    p.add_argument("--ablegen", metavar="FINANZORDNER", help="Exporte nach <Ordner>/Kontoauszuege/<Konto>/ sichern")
    p.add_argument("--konto", default="Girokonto", help="Kontoname für die Ablage")
    p.add_argument("--heute", default=date.today().isoformat())
    p.add_argument("--inhaber", default="", help="Name des Kontoinhabers, erkennt Überträge")
    p.add_argument("--regeln", help="zusätzliche Regeln (JSON im Format von kategorien.json)")
    p.add_argument("--kasse", type=float, default=150.0, help="Schwelle für Verdacht auf Bargeld an der Kasse")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    heute = datum(a.heute, date.today())
    dateien = dateien_sammeln(a.dateien)
    listen = [sorted(lade(f, heute)) for f in dateien]
    if a.ablegen:
        for f, z in zip(dateien, listen):
            if z:
                ziel = ablegen(f, z, a.ablegen, a.konto)
                print(f"Abgelegt: {ziel}" if ziel else f"Schon vorhanden, übersprungen: {f.name}", file=sys.stderr)
    umsaetze = zusammenfuehren(listen)
    if not umsaetze:
        sys.exit("Keine Umsätze erkannt. Format prüfen (CSV mit Buchungstag oder Text mit Tabs).")
    regeln = regeln_laden(a.regeln)
    inh = a.inhaber.lower().strip()

    erste, letzte = umsaetze[0][0], umsaetze[-1][0]
    voll = sorted({monat(d) for d, _, _ in umsaetze})
    if erste.day > 3 and voll:
        voll = voll[1:]
    if voll and voll[-1] == monat(letzte) and letzte.month == heute.month and letzte.year == heute.year:
        voll = voll[:-1]
    laufend = monat(heute)
    n_voll = max(len(voll), 1)

    ausgaben, uebertraege, zufluss = [], 0.0, 0.0
    for d, t, b in umsaetze:
        if inh and inh in t.lower():
            uebertraege += abs(b)
            continue
        if b > 0:
            zufluss += b
            continue
        ausgaben.append((d, t, -b, kategorie(t, regeln)))

    # wiederkehrende Posten
    gruppen = defaultdict(list)
    for d, t, b, k in ausgaben:
        gruppen[(k["name"] if k and k["typ"] == "fix" else schluessel(t))].append((d, t, b, k))
    fix, pruefen = {}, []
    for key, eintraege in gruppen.items():
        k = eintraege[0][3]
        monate = {monat(d) for d, _, _, _ in eintraege}
        betraege = [b for _, _, b, _ in eintraege]
        med = statistics.median(betraege)
        regelmaessig = len(monate) >= 3 and all(abs(b - med) <= 0.1 * med + 0.5 for b in betraege)
        if k and k["typ"] == "fix" and k.get("jaehrlich"):
            fix[key] = ("Jahresbeitrag", sum(betraege) / max(len(monate), 1) / 12 if len(monate) else 0, eintraege)
        elif regelmaessig and not (k and k["typ"] == "variabel"):
            fix[key] = ("fix", sum(betraege[-3:]) / len(betraege[-3:]), eintraege)
        elif k and k["typ"] == "fix" and len(monate) >= 2:
            letzte3 = sorted(eintraege)[-3:]
            fix[key] = ("schwankend", sum(b for _, _, b, _ in letzte3) / len(letzte3), eintraege)
        elif len(monate) >= 3 and not k:
            pruefen.append((key, med, len(monate)))

    # fehlende Abbuchung im laufenden Monat
    fehlt = [key for key, (art, _, e) in fix.items()
             if art == "fix" and laufend not in {monat(d) for d, _, _, _ in e}
             and heute.day > max(d.day for d, _, _, _ in e) + 3]

    # variable Kategorien über volle Monate
    var = defaultdict(float)
    for d, t, b, k in ausgaben:
        if k and k["typ"] == "variabel" and monat(d) in voll:
            var[k["name"]] += b
    var_monat = {k: v / n_voll for k, v in var.items()}

    # Verdacht: Bargeld an der Kasse
    kasse = [(d, t, b) for d, t, b, k in ausgaben
             if k and k["name"] == "Lebensmittel" and b >= a.kasse]

    einmalig = [(d, t, b) for d, t, b, k in ausgaben if k and k["typ"] == "einmalig"]

    erg = {
        "zeitraum": [erste.isoformat(), letzte.isoformat()],
        "volle_monate": len(voll),
        "fix": {k: round(v[1], 2) for k, v in sorted(fix.items(), key=lambda x: -x[1][1])},
        "fix_summe_monat": round(sum(v[1] for v in fix.values()), 2),
        "variabel_monat": {k: round(v, 2) for k, v in sorted(var_monat.items(), key=lambda x: -x[1])},
        "ueberweisungen_an_sich_selbst": round(uebertraege, 2),
        "zufluesse": round(zufluss, 2),
        "kassenverdacht": [(d.isoformat(), t[:40], b) for d, t, b in kasse],
        "einmalig": [(d.isoformat(), t[:40], b) for d, t, b in einmalig],
        "fehlende_abbuchung_laufender_monat": fehlt,
        "regelmaessig_ohne_regel": [(k, round(m, 2), n) for k, m, n in pruefen],
    }
    if a.json:
        print(json.dumps(erg, ensure_ascii=False, indent=2))
        return
    print(f"Zeitraum {erste:%d.%m.%Y} bis {letzte:%d.%m.%Y}, {len(voll)} volle Monate")
    print("\nFixkosten (€/Monat)")
    for k, v in erg["fix"].items():
        print(f"  {k:<32}{v:>9.2f}  [{fix[k][0]}]")
    print(f"  {'Summe':<32}{erg['fix_summe_monat']:>9.2f}")
    print("\nVariabel (Mittel der vollen Monate, €/Monat)")
    for k, v in erg["variabel_monat"].items():
        print(f"  {k:<32}{v:>9.2f}")
    if kasse:
        print(f"\nLebensmittel-Einkäufe ab {a.kasse:.0f} € (Bargeld an der Kasse?):")
        for d, t, b in kasse:
            print(f"  {d:%d.%m.%Y}  {t[:34]:<34}{b:>9.2f}")
    if fehlt:
        print("\nErwartete Abbuchung im laufenden Monat fehlt:", ", ".join(fehlt))
    if pruefen:
        print("\nRegelmäßig, aber ohne Regel (bitte einordnen):")
        for k, m, n in pruefen:
            print(f"  {k:<32}{m:>9.2f}  in {n} Monaten")
    if einmalig:
        print("\nAls einmalig ausgeschlossen:")
        for d, t, b in einmalig:
            print(f"  {d:%d.%m.%Y}  {t[:34]:<34}{b:>9.2f}")
    print(f"\nÜberträge an sich selbst (nicht gezählt): {uebertraege:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))


if __name__ == "__main__":
    main()
