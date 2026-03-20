---
name: quarto
description: "Create and edit Quarto documents (.qmd) for scientific/technical publishing with support for multiple output formats (HTML, PDF, DOCX, presentations). Use when Claude needs to: (1) Create Quarto documents with code execution (Python, R, Julia), (2) Build presentations (Reveal.js, Beamer, PowerPoint), (3) Configure YAML frontmatter for documents/books/websites, (4) Add cross-references, citations, callouts, or figures, (5) Work with computational notebooks or literate programming"
---

# Quarto Document Creation

## Overview

Quarto is an open-source scientific publishing system. A `.qmd` file is Markdown with YAML frontmatter and executable code blocks.

## Quick Reference

| Task | Approach |
|------|----------|
| Create document | Write `.qmd` with YAML + Markdown + code |
| Render document | `quarto render file.qmd` |
| Create presentation | Use `format: revealjs`, `pptx`, or `beamer` |
| Add computation | Use `{python}`, `{r}`, or `{julia}` code blocks |

---

## Document Structure

### Basic Document

```markdown
---
title: "Document Title"
author: "Name"
date: "2025-01-16"
format: html
---

## Introduction

Content here with **bold** and *italic*.
```

### Multiple Output Formats

```yaml
---
title: "Multi-format Doc"
format:
  html:
    toc: true
    code-fold: true
  pdf:
    toc: true
    number-sections: true
  docx: default
---
```

---

## Code Execution

### Executable Code Blocks

````markdown
```{python}
#| label: fig-plot
#| fig-cap: "My Plot"

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()
```
````

### Cell Options (use `#|` prefix)

| Option | Purpose | Example |
|--------|---------|---------|
| `label` | Cross-reference ID | `#| label: fig-myplot` |
| `fig-cap` | Figure caption | `#| fig-cap: "Description"` |
| `tbl-cap` | Table caption | `#| tbl-cap: "Summary"` |
| `echo` | Show code | `#| echo: false` |
| `eval` | Execute code | `#| eval: true` |
| `output` | Show output | `#| output: false` |
| `warning` | Show warnings | `#| warning: false` |

### Inline Code

```markdown
The value is `{python} 2 + 2` (renders as: The value is 4)
```

---

## Cross-References

### Labeling Convention

| Entity | Prefix | Example |
|--------|--------|---------|
| Figure | `fig-` | `#| label: fig-plot` |
| Table | `tbl-` | `#| label: tbl-data` |
| Section | `sec-` | `## Results {#sec-results}` |
| Equation | `eq-` | `$$ E=mc^2 $$ {#eq-energy}` |
| Listing | `lst-` | `#| lst-label: lst-code` |

### Reference Syntax

```markdown
See @fig-plot for the visualization.
As shown in @tbl-data and @sec-results.
From @eq-energy we derive...
```

### Figure with Cross-Reference

```markdown
![Elephant](elephant.png){#fig-elephant}

See @fig-elephant for illustration.
```

### Table with Cross-Reference

```markdown
| A | B |
|---|---|
| 1 | 2 |

: Summary Data {#tbl-summary}

See @tbl-summary.
```

---

## Figures

### Static Image

```markdown
![Caption](image.png){#fig-id width="80%"}
```

### Computational Figure

````markdown
```{python}
#| label: fig-scatter
#| fig-cap: "Scatter Plot"
#| fig-alt: "Description for accessibility"
#| fig-width: 6
#| fig-height: 4

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()
```
````

### Subfigures with Layout

````markdown
::: {#fig-combined layout-ncol=2}

![First](a.png){#fig-a}

![Second](b.png){#fig-b}

Combined caption
:::
````

---

## Tables

### Markdown Table

```markdown
| Fruit | Price |
|-------|-------|
| Apple | $1.00 |
| Pear  | $0.75 |

: Fruit Prices {#tbl-prices .striped .hover}
```

### Computational Table (Python)

````markdown
```{python}
#| label: tbl-summary
#| tbl-cap: "Summary Statistics"

from IPython.display import Markdown
from tabulate import tabulate

data = [["A", 1], ["B", 2]]
Markdown(tabulate(data, headers=["Name", "Value"]))
```
````

### Computational Table (R)

````markdown
```{r}
#| label: tbl-cars
#| tbl-cap: "Car Data"

knitr::kable(head(mtcars))
```
````

---

## Callouts

```markdown
::: {.callout-note}
This is a note callout.
:::

::: {.callout-tip}
## Custom Title
This is a tip with a title.
:::

::: {.callout-warning collapse="true"}
## Click to expand
Collapsible warning content.
:::
```

**Callout types:** `note`, `tip`, `warning`, `caution`, `important`

---

## Citations

### Setup

```yaml
---
bibliography: references.bib
csl: apa.csl  # optional style
---
```

### Citation Syntax

```markdown
Studies show [@smith2020].
Smith says [-@smith2020] (suppress author).
@smith2020 argues that... (in-text).
Multiple sources [@smith2020; @jones2021].
With page [@smith2020, pp. 23-25].
```

---

## Presentations

### Reveal.js (HTML slides)

```yaml
---
title: "My Talk"
format:
  revealjs:
    theme: dark
    slide-number: true
    transition: slide
    chalkboard: true
---

## Slide 1

Content

---

## Slide 2 {.smaller}

More content

::: {.notes}
Speaker notes here
:::
```

### PowerPoint

```yaml
---
title: "Presentation"
format:
  pptx:
    reference-doc: template.pptx
    incremental: true
---
```

### Beamer (LaTeX PDF)

```yaml
---
title: "Academic Talk"
format:
  beamer:
    theme: Madrid
    colortheme: beaver
---
```

### Slide Structure

```markdown
# Section Title (creates title slide)

## Slide Title

- Point 1
- Point 2

---

Slide without title (use `---` separator)
```

### Incremental Lists

```markdown
::: {.incremental}
- First item
- Second item
:::
```

---

## Common YAML Options

### Document Options

```yaml
---
title: "Title"
subtitle: "Subtitle"
author:
  - name: "First Author"
    affiliation: "University"
  - name: "Second Author"
date: last-modified
date-format: "MMMM D, YYYY"
abstract: |
  Multi-line abstract here.
toc: true
toc-depth: 3
number-sections: true
---
```

### HTML Options

```yaml
format:
  html:
    theme: cosmo
    toc: true
    toc-location: left
    code-fold: true
    code-tools: true
    highlight-style: github
    embed-resources: true
```

### PDF Options

```yaml
format:
  pdf:
    documentclass: article
    papersize: letter
    geometry:
      - top=1in
      - left=1in
    fontsize: 11pt
    colorlinks: true
    keep-tex: true
```

---

## Layouts

### Column Layout

```markdown
:::: {.columns}
::: {.column width="50%"}
Left content
:::
::: {.column width="50%"}
Right content
:::
::::
```

### Panel Layout

```markdown
::: {layout-ncol=2}
![](a.png)

![](b.png)
:::
```

### Custom Grid

```markdown
::: {layout="[[1,1], [1]]"}
Top-left

Top-right

Bottom (full width)
:::
```

---

## Conditional Content

```markdown
::: {.content-visible when-format="html"}
HTML-only content
:::

::: {.content-visible when-format="pdf"}
PDF-only content
:::

::: {.content-hidden when-format="html"}
Hidden in HTML
:::
```

---

## Projects

### _quarto.yml for Website

```yaml
project:
  type: website

website:
  title: "My Site"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - about.qmd

format:
  html:
    theme: cosmo
```

### _quarto.yml for Book

```yaml
project:
  type: book

book:
  title: "My Book"
  author: "Name"
  chapters:
    - index.qmd
    - intro.qmd
    - methods.qmd
    - references.qmd

bibliography: references.bib

format:
  html:
    theme: cosmo
  pdf:
    documentclass: scrreprt
```

---

## Tips and Gotchas

- **Use `#|` for cell options** - not chunk headers like `{python label=...}`
- **Cross-ref labels need prefixes** - `fig-`, `tbl-`, `sec-`, `eq-`, `lst-`
- **Reference with `@`** - e.g., `@fig-plot`, not `\ref{fig-plot}`
- **PDF requires LaTeX** - install TinyTeX: `quarto install tinytex`
- **Blank line before lists** - required for proper rendering
- **Code folding** - only works in HTML format
- **`default` for format** - use when no options needed: `docx: default`

---

## Rendering

```bash
# Single file
quarto render document.qmd

# Specific format
quarto render document.qmd --to pdf

# Project
quarto render

# Preview with live reload
quarto preview document.qmd
```

---

## References

For advanced topics see `references/` directory:
- **presentations.md** - Detailed presentation options
- **advanced-yaml.md** - Complex YAML configurations
