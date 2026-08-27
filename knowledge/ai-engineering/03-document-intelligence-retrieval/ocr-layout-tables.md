---
id: ocr-layout-tables
title: OCR, Layout, Tables, and Reading Order
level: L1-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [pdf-to-evidence]
---

# OCR, Layout, Tables, and Reading Order

## Intuition

OCR answers “which characters might these pixels represent?” Document understanding additionally asks “which region is a heading, cell, caption, paragraph, or footnote, and how are they related?”

## OCR pipeline

1. Render or acquire image.
2. Correct orientation, skew, noise, contrast, and resolution where appropriate.
3. Detect text regions or lines.
4. Recognize characters/tokens.
5. reconstruct words and reading order.
6. attach coordinates, language, and confidence.
7. preserve original image for verification.

## Why accuracy numbers deceive

A character error rate can hide catastrophic semantic errors:

- `0.01` becomes `0.1`;
- “shall” becomes “shall not” after a missed word;
- a table value attaches to the wrong row;
- two columns interleave;
- a footnote exception disappears;
- page headers pollute every chunk.

Evaluate task-relevant structures and high-risk fields, not only average characters.

## Layout and reading order

Layout models detect regions such as title, paragraph, list, figure, table, formula, header, and footer. Reading order is a graph problem when pages contain columns, sidebars, captions, or floating objects.

A robust representation preserves hierarchy rather than immediately concatenating strings.

## Tables

A table encodes meaning through rows, columns, headers, spans, units, and notes. Flattening it can destroy which value belongs to which entity.

Represent:

- cell text;
- row/column indices;
- row/column spans;
- header relationships;
- units and captions;
- page coordinates;
- merged-cell interpretation;
- continuation across pages.

Choose retrieval units based on question type: entire small table, selected rows with headers, or structured database records.

## Equations, diagrams, and handwriting

Plain OCR is insufficient when meaning is spatial or symbolic. Preserve image regions and consider specialised recognizers or multimodal models. Always retain coordinates for inspection.

## Tool evolution

Classical OCR remains valuable for speed, local execution, mature language coverage, and coordinates. Layout models add structure. Vision-language document models can jointly interpret page appearance and text, reducing dependence on brittle staged pipelines, but they add model cost, nondeterminism, and new evaluation requirements.

## Cross-domain transfer

- **AI:** structured parsing improves chunking, citations, and multimodal retrieval.
- **Full stack:** OCR is a job pipeline with queues, storage, retries, progress, and human correction.
- **Games:** UI/screenshot understanding and accessibility agents face similar spatial-semantic problems.
- **Game AI research:** vision-based agents must distinguish pixels, objects, state, and affordances; OCR is only one perceptual channel.

## Research questions

- How should parsing uncertainty propagate into retrieval and answer confidence?
- Which document representations preserve layout without making retrieval prohibitively expensive?
- How should multilingual and visually diverse documents be evaluated fairly?
