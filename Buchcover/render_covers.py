#!/usr/bin/env python3
"""
Buchcover Renderer
==================
Rendert HTML-basierte Buchcover als hochauflösende PNG-Dateien (300 DPI).

Verwendung:
    python render_covers.py

Voraussetzungen:
    pip install playwright
    playwright install chromium
"""

import os
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Fehler: Playwright ist nicht installiert.")
    print("Bitte installieren Sie es mit: pip install playwright")
    print("Dann: playwright install chromium")
    sys.exit(1)


# Konfiguration
COVER_WIDTH = 1800   # 6 inch @ 300 DPI
COVER_HEIGHT = 2700  # 9 inch @ 300 DPI

# Pfade
SCRIPT_DIR = Path(__file__).parent
HTML_DIR = SCRIPT_DIR / "html"
OUTPUT_DIR = SCRIPT_DIR / "output"


def render_html_to_png(html_path: Path, output_path: Path, width: int = COVER_WIDTH, height: int = COVER_HEIGHT):
    """
    Rendert eine HTML-Datei als PNG mit Playwright.

    Args:
        html_path: Pfad zur HTML-Datei
        output_path: Pfad für die Ausgabe-PNG
        width: Breite in Pixeln (Standard: 1800)
        height: Höhe in Pixeln (Standard: 2700)
    """
    if not html_path.exists():
        print(f"Fehler: HTML-Datei nicht gefunden: {html_path}")
        return False

    # Absoluten Pfad für file:// URL
    html_url = f"file://{html_path.absolute()}"

    print(f"Rendere: {html_path.name}")
    print(f"  Größe: {width}x{height}px")
    print(f"  URL: {html_url}")

    with sync_playwright() as p:
        # Browser starten
        browser = p.chromium.launch()

        # Seite mit exakter Größe erstellen
        page = browser.new_page(
            viewport={'width': width, 'height': height},
            device_scale_factor=1  # Keine Skalierung
        )

        # HTML laden
        page.goto(html_url)

        # Warten bis Fonts geladen sind
        page.wait_for_load_state('networkidle')

        # Kurz warten für Font-Rendering
        page.wait_for_timeout(1000)

        # Screenshot erstellen
        page.screenshot(
            path=str(output_path),
            type='png',
            full_page=False,  # Nur Viewport
            animations='disabled'
        )

        browser.close()

    print(f"  Gespeichert: {output_path}")
    return True


def main():
    """Hauptfunktion - rendert beide Cover."""

    print("=" * 50)
    print("Buchcover Renderer - KI mit Python")
    print("=" * 50)
    print(f"Ausgabeformat: {COVER_WIDTH}x{COVER_HEIGHT}px (300 DPI)")
    print()

    # Output-Verzeichnis erstellen
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Cover-Definitionen
    covers = [
        ("frontcover.html", "frontcover.png"),
        ("backcover.html", "backcover.png"),
    ]

    success_count = 0

    for html_file, output_file in covers:
        html_path = HTML_DIR / html_file
        output_path = OUTPUT_DIR / output_file

        if render_html_to_png(html_path, output_path):
            success_count += 1
        print()

    print("=" * 50)
    print(f"Fertig! {success_count}/{len(covers)} Cover erfolgreich gerendert.")
    print(f"Ausgabe-Verzeichnis: {OUTPUT_DIR}")
    print("=" * 50)

    return success_count == len(covers)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
