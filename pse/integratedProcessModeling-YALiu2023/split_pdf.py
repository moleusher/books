#!/usr/bin/env python3
"""
Split a large PDF into physical chunks of ≤N pages each.
Outputs: chunk PDFs + chunks_manifest.json

Usage:
  python3 split_pdf.py --pdf input.pdf --output-dir chunks/ --max-pages 100
"""
import argparse, json, sys
from pathlib import Path


def split_pdf(pdf_path: str, output_dir: Path, max_pages: int = 100) -> list[dict]:
    """Split PDF into chunks. Returns manifest list."""
    try:
        import fitz
    except ImportError:
        sys.exit("Please install PyMuPDF: pip install PyMuPDF")

    pdf = fitz.open(pdf_path)
    total = pdf.page_count
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    chunk_idx = 0

    for start in range(0, total, max_pages):
        end = min(start + max_pages, total) - 1  # inclusive
        chunk_pdf = fitz.open()  # new empty PDF

        # Copy pages [start, end] inclusive
        chunk_pdf.insert_pdf(pdf, from_page=start, to_page=end)

        p_start = start + 1  # 1-indexed
        p_end = end + 1
        fname = f"chunk_{p_start:04d}-{p_end:04d}.pdf"
        out_path = output_dir / fname
        chunk_pdf.save(str(out_path), garbage=4, deflate=True)
        chunk_pdf.close()

        size_mb = out_path.stat().st_size / 1_048_576
        entry = {
            "file": fname,
            "path": str(out_path),
            "pdf_page_start": p_start,
            "pdf_page_end": p_end,
            "num_pages": p_end - p_start + 1,
            "size_mb": round(size_mb, 2),
        }
        manifest.append(entry)
        print(f"  [{chunk_idx+1}] {fname}: pages {p_start}-{p_end} ({entry['num_pages']}p, {size_mb:.1f}MB)")
        chunk_idx += 1

    pdf.close()

    # Write manifest
    manifest_path = output_dir / "chunks_manifest.json"
    manifest_path.write_text(json.dumps({"total_pages": total, "chunks": manifest}, indent=2))
    print(f"\n  Manifest → {manifest_path}")
    print(f"  Total: {total} pages → {len(manifest)} chunk(s)")
    return manifest


def main():
    p = argparse.ArgumentParser(description="Split PDF into ≤N-page physical chunks")
    p.add_argument("--pdf", required=True, help="Path to input PDF")
    p.add_argument("--output-dir", required=True, help="Output directory for chunk PDFs")
    p.add_argument("--max-pages", type=int, default=100, help="Max pages per chunk (default: 100)")
    args = p.parse_args()

    if not Path(args.pdf).exists():
        sys.exit(f"PDF not found: {args.pdf}")

    split_pdf(args.pdf, Path(args.output_dir), args.max_pages)


if __name__ == "__main__":
    main()
