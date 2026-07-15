# CLAUDE.md

## Purpose
Books repository — literature, professional books, open-source code.
Operations: chart digitization, PDF OCR → structured MD, literature ingestion.

## Directory Structure
sources/               Original PDFs, papers, figures (read-only)
  figures/             Chart images: fig3-conversion-time-140C.png, etc.
data/                  Extracted datasets by figure/temperature
  fig3-conversion-time/{140,160,180}C/  → extracted_data.csv, verification.png
scripts/               Extraction scripts: extract_<temp>C_<color>.py
*.md                   Method docs (extract_scatter.md)

## Virtual Environment
Path:    /home/admin/books/env chartocr/bin/python3
Install: /home/admin/books/env chartocr/bin/pip install <pkg>
Libraries: opencv-python-headless (NOT opencv-python/contrib — conflicts on headless servers), numpy, pandas, matplotlib, scipy, Pillow, paddleocr
Token: 在/home/admin/books/.claude/settings.local.json

## Key Skills
Trigger via Skill tool or /<name> when conditions match:
- paper-ingest  — extract structured MD + images from PDF via PaddleOCR async API (>100p auto-chunk)
- chartdigitizer — extract colored scatter points from chart images (HSV+axis mapping)
- wiki-ingest    — convert PDFs/papers to structured MD in vault

## Common Commands
# Chart extraction (see scripts/extract_scatter.py --help for all options)
"/home/admin/books/env chartocr/bin/python3" \
  /home/admin/.claude/skills/chartdigitizer/scripts/extract_scatter.py \
  sources/figures/<file>.png --color <name> \
  --manual-bounds "xmin,xmax,ymin,ymax" --x-range "<min>,<max>" --y-range "<min>,<max>" \
  --output-dir data/<dataset>/

# PDF OCR → structured MD (paper-ingest skill)
"/home/admin/books/env chartocr/bin/python3" \
  /home/admin/.claude/skills/paper-ingest/scripts/parse_pdf.py \
  --pdf <file>.pdf --output-dir <output_dir>/

## Naming Conventions
- Files: kebab-case, descriptive, no spaces or special chars beyond `-` and `_`
- Data CSV: always `extracted_data.csv` in its dataset subdirectory
- Scripts: `extract_<variant>.py` — variant describes what differs (color, source, method)
- Outputs: `data/<dataset>/` — one subdirectory per extracted dataset, flat inside
- Figures: `sources/figures/<figure-id>-<variant>.png` — group related figures by id

## Chart Extraction Gotchas
- Axis bounds: scan dark-pixel peaks per column/row (threshold <80); use float centers (axis lines ~2px wide)
- Color: sample actual pixel HSV before picking preset; red needs two hue ranges (0-10 ∪ 160-180)
- Margin: first data point often sits on axis → ±4px tolerance in boundary checks
- Verify: always check verification_result.png for green-ring alignment before trusting CSV
