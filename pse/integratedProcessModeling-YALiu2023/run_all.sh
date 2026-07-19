#!/bin/bash
# Process all 9 PDF chunks via PaddleOCR API
# Resume-safe: re-run to pick up where left off

cd /home/admin/books/pse/integratedProcessModeling-YALiu2023

"/home/admin/books/env chartocr/bin/python3" process_chunks.py \
  --chunks-dir chunks \
  --output-dir . \
  --resume
