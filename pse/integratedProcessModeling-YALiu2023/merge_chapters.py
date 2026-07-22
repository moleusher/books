#!/usr/bin/env python3
"""
Merge per-page MD files into per-chapter files, organized by volume.
Reads chapter_map.json to determine chapter boundaries.

Handles:
- Chapters that span across API chunks (invisible to this script — just merges by page range)
- Chapters >100 pages (split across multiple API jobs, merged here)
- Volume 1 & Volume 2 organization

Usage:
  python3 merge_chapters.py --md-dir md/ --chapter-map chapter_map.json --output-dir .
"""
import argparse, json, sys
from pathlib import Path


def merge_chapters(md_dir: Path, chapter_map: dict, output_dir: Path) -> dict:
    """Merge per-page MDs into per-chapter files. Returns stats."""
    stats = {"volumes": {}, "total_pages_merged": 0, "total_pages_missing": 0, "missing_pages": []}

    for vol_key, vol_data in chapter_map["volumes"].items():
        vol_dir = output_dir / vol_data["dir"]
        vol_dir.mkdir(parents=True, exist_ok=True)

        vol_pages_merged = 0
        all_entries = []

        # Include front matter if present
        if "front_matter" in vol_data:
            all_entries.append(vol_data["front_matter"])

        all_entries.extend(vol_data["chapters"])

        for entry in all_entries:
            start, end = entry["pages"]
            out_file = vol_dir / entry["file"]
            chapter_pages = []
            missing = []

            for pg in range(start, end + 1):
                md_file = md_dir / f"page_{pg:04d}.md"
                if md_file.exists():
                    text = md_file.read_text(encoding="utf-8")
                    chapter_pages.append(f"<!-- PDF page {pg} -->\n\n{text}")
                else:
                    missing.append(pg)
                    chapter_pages.append(f"<!-- PDF page {pg} — MISSING, not yet parsed -->\n")

            if missing:
                print(f"  ⚠ {entry['file']}: {len(missing)}/{end-start+1} pages missing: {missing[:10]}{'...' if len(missing)>10 else ''}")
                stats["total_pages_missing"] += len(missing)
                stats["missing_pages"].extend([(entry["file"], pg) for pg in missing])

            # Write chapter file
            entry_title = entry.get('title') or entry.get('label', 'Untitled')
            header = f"# {entry_title}\n\n"
            out_file.write_text(header + "\n\n---\n\n".join(chapter_pages), encoding="utf-8")

            size_kb = out_file.stat().st_size / 1024
            merged_count = len([p for p in chapter_pages if "MISSING" not in p])
            print(f"  ✓ {vol_data['dir']}/{entry['file']}: {merged_count} pages → {size_kb:.0f} KB")
            vol_pages_merged += merged_count
            stats["total_pages_merged"] += merged_count

        stats["volumes"][vol_key] = {"dir": vol_data["dir"], "pages_merged": vol_pages_merged}

    return stats


def main():
    p = argparse.ArgumentParser(description="Merge per-page MD files into per-chapter files by volume")
    p.add_argument("--md-dir", required=True, help="Directory containing page_XXXX.md files")
    p.add_argument("--chapter-map", required=True, help="Path to chapter_map.json")
    p.add_argument("--output-dir", default=".", help="Output directory for volume1/ and volume2/")
    p.add_argument("--dry-run", action="store_true", help="Check which pages exist without writing files")
    args = p.parse_args()

    md_dir = Path(args.md_dir).resolve()
    cmap_path = Path(args.chapter_map).resolve()
    output_dir = Path(args.output_dir).resolve()

    if not md_dir.exists():
        sys.exit(f"MD directory not found: {md_dir}")
    if not cmap_path.exists():
        sys.exit(f"Chapter map not found: {cmap_path}")

    chapter_map = json.loads(cmap_path.read_text())

    # Dry run: count available pages
    existing_pages = sorted([
        int(f.stem.split("_")[1]) for f in md_dir.glob("page_*.md")
    ])
    total_expected = sum(
        entry["pages"][1] - entry["pages"][0] + 1
        for vol in chapter_map["volumes"].values()
        for entries in [list(vol.get("chapters", [])) + ([vol["front_matter"]] if "front_matter" in vol else [])]
        for entry in entries
    )
    print(f"  MD files found: {len(existing_pages)} / {total_expected} expected")
    if existing_pages:
        print(f"  Page range: {existing_pages[0]} – {existing_pages[-1]}")

    if args.dry_run:
        # Show per-chapter coverage
        for vol_key, vol_data in chapter_map["volumes"].items():
            print(f"\n  {vol_key}/")
            all_entries = list(vol_data.get("chapters", []))
            if "front_matter" in vol_data:
                all_entries.insert(0, vol_data["front_matter"])
            for entry in all_entries:
                start, end = entry["pages"]
                present = sum(1 for pg in range(start, end+1) if (md_dir / f"page_{pg:04d}.md").exists())
                pct = present / (end-start+1) * 100
                bar = "█" * int(pct/10) + "░" * (10 - int(pct/10))
                print(f"    [{bar}] {entry['file']}: {present}/{end-start+1} ({pct:.0f}%)")
        return

    print(f"\n  Merging chapters...")
    stats = merge_chapters(md_dir, chapter_map, output_dir)

    print(f"\n{'='*56}")
    print(f"  MERGE COMPLETE")
    print(f"  Total pages merged: {stats['total_pages_merged']}")
    print(f"  Total pages missing: {stats['total_pages_missing']}")
    for vol_key, vs in stats["volumes"].items():
        print(f"    {vs['dir']}: {vs['pages_merged']} pages")
    print(f"{'='*56}")


if __name__ == "__main__":
    main()
