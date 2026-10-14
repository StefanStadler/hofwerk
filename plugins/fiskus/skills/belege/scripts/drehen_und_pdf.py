#!/usr/bin/env python3
"""Dreht einen Beleg-Scan oder ein Foto und schreibt ihn als PDF.

Das Original bleibt unverändert. Das Ergebnis liegt als Kopie im Ausgabeordner,
Name = Originalname ohne Endung + .pdf.

Aufruf:
  drehen_und_pdf.py --ausgabe ORDNER [--grad N] DATEI [DATEI ...]

--grad N   Zusätzliche Drehung in Grad, gleiche Richtung wie PIL rotate(N, expand=True)
           (positiv = gegen den Uhrzeigersinn, -90 = 90° im Uhrzeigersinn).
           Gilt für alle Dateien des Aufrufs. Für unterschiedliche Drehungen
           das Skript je Drehung einmal aufrufen.

Ablauf je Bild: EXIF-Orientierung anwenden (exif_transpose), dann --grad,
dann als PDF speichern. Bereits vorhandene PDFs werden nur gedreht,
wenn pypdf installiert ist, sonst wird die Datei übersprungen und gemeldet.

Ausgabe: eine Zeile je Datei "OK <eingang> -> <ausgang>" oder "FEHLER <eingang>: <grund>".
Exitcode 0, wenn alle Dateien verarbeitet wurden, sonst 1.
"""
import argparse
import sys
from pathlib import Path

BILDENDUNGEN = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp", ".heic"}


def bild_zu_pdf(quelle: Path, ziel: Path, grad: float) -> None:
    from PIL import Image, ImageOps

    if quelle.suffix.lower() == ".heic":
        try:
            import pillow_heif
            pillow_heif.register_heif_opener()
        except ImportError:
            raise RuntimeError("HEIC braucht pillow-heif")
    with Image.open(quelle) as img:
        img = ImageOps.exif_transpose(img)
        if grad:
            img = img.rotate(grad, expand=True)
        img = img.convert("RGB")
        img.save(ziel, "PDF", resolution=200.0)


def pdf_drehen(quelle: Path, ziel: Path, grad: float) -> None:
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        raise RuntimeError("PDF drehen braucht pypdf")
    # pypdf dreht im Uhrzeigersinn, PIL gegen den Uhrzeigersinn
    im_uhrzeigersinn = int(round(-grad)) % 360
    if im_uhrzeigersinn % 90:
        raise RuntimeError("PDF nur in 90°-Schritten drehbar")
    leser = PdfReader(str(quelle))
    schreiber = PdfWriter()
    for seite in leser.pages:
        if im_uhrzeigersinn:
            seite.rotate(im_uhrzeigersinn)
        schreiber.add_page(seite)
    with open(ziel, "wb") as f:
        schreiber.write(f)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ausgabe", required=True, help="Zielordner für die Kopien")
    p.add_argument("--grad", type=float, default=0.0, help="zusätzliche Drehung in Grad")
    p.add_argument("dateien", nargs="+")
    a = p.parse_args()

    ausgabe = Path(a.ausgabe)
    ausgabe.mkdir(parents=True, exist_ok=True)
    fehler = 0
    for name in a.dateien:
        quelle = Path(name)
        ziel = ausgabe / (quelle.stem + ".pdf")
        try:
            if not quelle.is_file():
                raise RuntimeError("Datei nicht gefunden")
            if ziel.resolve() == quelle.resolve():
                raise RuntimeError("Ziel wäre das Original")
            endung = quelle.suffix.lower()
            if endung in BILDENDUNGEN:
                bild_zu_pdf(quelle, ziel, a.grad)
            elif endung == ".pdf":
                if a.grad:
                    pdf_drehen(quelle, ziel, a.grad)
                else:
                    ziel.write_bytes(quelle.read_bytes())
            else:
                raise RuntimeError(f"Dateityp {endung} nicht unterstützt")
            print(f"OK {quelle} -> {ziel}")
        except Exception as e:  # noqa: BLE001
            fehler += 1
            print(f"FEHLER {quelle}: {e}")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
