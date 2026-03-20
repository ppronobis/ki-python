# KI mit Python - Quarto Buchprojekt

Dieses Repository enthält das Quarto-Buchprojekt "KI mit Python: Von den Grundlagen bis zur GPT-Integration", basierend auf dem IHK-Zertifikatskurs "KI lernen in 4 Wochen".

## Autoren

- **Paul Pronobis** - Professor, Free University of Bozen-Bolzano
- **Tobias Lämmle** - Software-Architekt & Machine-Learning-Experte

## Voraussetzungen

- [Quarto](https://quarto.org/docs/get-started/) installiert (Version 1.3 oder höher)
- Optional: [RStudio](https://posit.co/download/rstudio-desktop/) oder [VS Code](https://code.visualstudio.com/) mit Quarto-Extension

## Installation von Quarto

### macOS
```bash
brew install quarto
```

### Windows
Laden Sie den Installer von [quarto.org](https://quarto.org/docs/get-started/) herunter.

### Linux
```bash
# Für Ubuntu/Debian
sudo apt-get install quarto
```

## Buch erstellen

### HTML-Version (empfohlen für Online-Ansicht)
```bash
quarto render
```

oder spezifisch:
```bash
quarto render --to html
```

Das fertige Buch wird im Ordner `_book/` erstellt.

### PDF-Version
```bash
quarto render --to pdf
```

**Hinweis:** Für PDF benötigen Sie eine LaTeX-Installation:
- macOS: `brew install --cask mactex`
- Windows: [MiKTeX](https://miktex.org/download)
- Linux: `sudo apt-get install texlive-full`

### EPUB-Version (eBook)
```bash
quarto render --to epub
```

Die EPUB-Datei wird im `_book/` Ordner erstellt und kann auf eReadern, Tablets und mit Apps wie Apple Books, Calibre oder Adobe Digital Editions gelesen werden.

### Alle Formate gleichzeitig
```bash
quarto render --to all
```

### Vorschau während der Entwicklung
```bash
quarto preview
```

Dies startet einen lokalen Server und öffnet das Buch im Browser. Änderungen werden automatisch aktualisiert.

## Projektstruktur

```
KI Python 2025/
├── _quarto.yml          # Hauptkonfigurationsdatei
├── index.qmd            # Startseite
├── _Vorwort.qmd         # Vorwort
├── Kapitel 1.qmd        # Kapitel 1: KI Python lernen
├── Kapitel 2.qmd        # Kapitel 2: Funktionen
├── Kapitel 3.qmd        # Kapitel 3: Bedingungen & Schleifen
├── Kapitel 4.qmd        # Kapitel 4: Datenstrukturen
├── Kapitel 5.qmd        # Kapitel 5: Pandas
├── Kapitel 6.qmd        # Kapitel 6: Arbeiten mit GPT
├── Kapitel 7.qmd        # Kapitel 7: Abschlusstest
├── references.bib       # Literaturverzeichnis
├── custom.scss          # Benutzerdefiniertes Styling
└── _book/              # Generierte Ausgabe (wird erstellt)
```

## Kapitelübersicht

1. **KI Python lernen** - Grundlagen der Programmierung
2. **Funktionen** - Code organisieren und wiederverwenden
3. **Bedingungen & Schleifen** - Programmlogik und Kontrolle
4. **Datenstrukturen** - Listen, Tupel und Dictionaries
5. **Pandas** - Professionelle Datenanalyse
6. **Arbeiten mit GPT** - KI-Integration mit OpenAI
7. **Abschlusstest** - Wissen unter Beweis stellen

## Anpassungen

### Styling ändern
Bearbeiten Sie `custom.scss` für benutzerdefinierte Farben und Stile.

### Buchmetadaten ändern
Bearbeiten Sie den `book:`-Abschnitt in `_quarto.yml`.

### Kapitel hinzufügen/entfernen
Aktualisieren Sie die `chapters:`-Liste in `_quarto.yml`.

## Community

Treten Sie unserer Community bei:
[Business Data Professional Community](https://www.skool.com/business-data-professional)

## Lizenz

© 2025 Paul Pronobis & Tobias Lämmle | IHK Rhein-Neckar

## Support

Bei Fragen oder Problemen:
- Besuchen Sie unsere [Community](https://www.skool.com/business-data-professional)
- Konsultieren Sie die [Quarto-Dokumentation](https://quarto.org/docs/books/)
