#!/bin/bash
cd /home/admin/books/pse/integratedProcessModeling-YALiu2023
"/home/admin/books/env chartocr/bin/python3" process_chunks.py \
  --chunks-dir chunks \
  --output-dir . \
  --only chunk_0001-0100.pdf
