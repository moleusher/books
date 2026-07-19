#!/usr/bin/env python3
"""
Process PDF chunks via PaddleOCR async API.
Reads chunks_manifest.json, submits each chunk, polls, downloads per-page MD + images.

Key difference from paper-ingest: uploads SMALL chunk PDFs (~7MB) instead of full 58MB PDF.

Usage:
  python3 process_chunks.py --chunks-dir chunks/ --output-dir . --model PaddleOCR-VL-1.5
  python3 process_chunks.py --chunks-dir chunks/ --output-dir . --parallel 3
  python3 process_chunks.py --chunks-dir chunks/ --output-dir . --resume
"""
import argparse, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import requests

# ── Constants ──
BASE_URL = "https://paddleocr.aistudio-app.com"
JOB_ENDPOINT = "/api/v2/ocr/jobs"
POLL_INTERVAL = 5
UPLOAD_TIMEOUT = 1200  # 20 min per chunk upload (10MB files on slow connections)
IMAGE_TIMEOUT = 30
CONCURRENT_IMAGE_WORKERS = 10
STATE_FILE = "_process_state.json"


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def load_token() -> str:
    token = os.environ.get("PADDLEOCR_ACCESS_TOKEN")
    if token:
        return token
    for env_file in [Path.cwd() / ".env", Path(__file__).resolve().parent.parent.parent.parent / ".env"]:
        env_file = env_file.resolve()
        if env_file.exists():
            for line in open(env_file):
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                if k.strip() == "PADDLEOCR_ACCESS_TOKEN" and v.strip():
                    return v.strip().strip('"').strip("'")
    raise RuntimeError("PADDLEOCR_ACCESS_TOKEN not found in env or .env")


def _headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


# ── API Operations ──

def submit_job(file_path: str, model: str, token: str) -> str:
    """Upload a chunk PDF and submit OCR job. Returns job_id."""
    fpath = Path(file_path).resolve()
    size_mb = fpath.stat().st_size / 1_048_576
    log(f"  Uploading {fpath.name} ({size_mb:.1f}MB) ...")

    payload = json.dumps({
        "useDocOrientationClassify": True,
        "useDocUnwarping": False,
        "useChartRecognition": True,
    })
    data = {"model": model, "optionalPayload": payload}

    with open(fpath, "rb") as f:
        resp = requests.post(f"{BASE_URL}{JOB_ENDPOINT}",
                             data=data, files={"file": f},
                             headers=_headers(token),
                             timeout=UPLOAD_TIMEOUT)
    if resp.status_code != 200:
        raise RuntimeError(f"Upload failed: HTTP {resp.status_code} {resp.text[:200]}")
    body = resp.json()
    if body.get("code", -1) != 0:
        raise RuntimeError(f"Submit error (code={body.get('code')}): {body.get('msg')}")
    return body["data"]["jobId"]


def poll_job(job_id: str, token: str) -> dict:
    """Poll until job completes. Returns job data dict."""
    url = f"{BASE_URL}{JOB_ENDPOINT}/{job_id}"
    last_msg = ""
    while True:
        body = requests.get(url, headers=_headers(token)).json()
        if body.get("code", -1) != 0:
            raise RuntimeError(f"Poll error: {body.get('msg')}")
        data = body["data"]
        state = data.get("state", "unknown")
        if state in ("pending", "running"):
            prog = data.get("extractProgress", {})
            msg = f"    {state}: {prog.get('extractedPages','?')}/{prog.get('totalPages','?')} pages"
            if msg != last_msg:
                log(msg)
                last_msg = msg
            time.sleep(POLL_INTERVAL)
        elif state == "done":
            ep = data.get("extractProgress", {})
            log(f"    done: {ep.get('extractedPages','?')} pages extracted")
            return data
        elif state == "failed":
            raise RuntimeError(f"Job failed: {data.get('errorMsg')}")
        else:
            raise RuntimeError(f"Unknown state: {state}")


def fetch_and_save(job_data: dict, output_dir: Path, page_offset: int, token: str) -> tuple[int, list]:
    """Download JSONL, write per-page MD, return (num_pages, image_manifest)."""
    jsonl_url = job_data["resultUrl"]["jsonUrl"]
    resp = requests.get(jsonl_url, headers=_headers(token))
    if resp.status_code != 200:
        resp = requests.get(jsonl_url)  # retry without auth
    if resp.status_code != 200:
        raise RuntimeError(f"Download results failed: HTTP {resp.status_code}")

    md_dir = output_dir / "md"
    images_dir = output_dir / "images"
    md_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    image_manifest = []
    page_count = 0

    for line in resp.text.strip().split("\n"):
        if not line.strip():
            continue
        page = json.loads(line)
        result = page.get("result", {})
        for res in result.get("layoutParsingResults", []):
            original_page = page_offset + page_count  # page_offset is 1-indexed start
            prefix = f"page_{original_page:04d}"

            # Write per-page MD
            md_text = res.get("markdown", {}).get("text", "")
            if md_text:
                (md_dir / f"{prefix}.md").write_text(md_text, encoding="utf-8")

            # Collect images with renamed paths
            for rel_path, img_url in res.get("markdown", {}).get("images", {}).items():
                # Rewrite image references in MD to use original page numbering
                img_path = images_dir / f"{prefix}_{Path(rel_path).name}"
                image_manifest.append((img_path, img_url))

            for name, img_url in res.get("outputImages", {}).items():
                img_path = images_dir / f"{prefix}_{name}.jpg"
                image_manifest.append((img_path, img_url))

            page_count += 1

    return page_count, image_manifest


def download_images(manifest: list, max_workers: int = 10) -> dict:
    """Download images concurrently."""
    def _dl(args):
        path, url = args
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists():
                return ("skip", str(path))
            r = requests.get(url, timeout=IMAGE_TIMEOUT)
            if r.status_code == 200:
                path.write_bytes(r.content)
                return ("ok", str(path))
            return ("err", f"HTTP {r.status_code}")
        except Exception as e:
            return ("err", str(e)[:80])

    if not manifest:
        return {"ok": 0, "skip": 0, "err": 0}

    ok = skip = err = 0
    total = len(manifest)
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(_dl, t): t for t in manifest}
        for i, fut in enumerate(as_completed(futures)):
            status, _ = fut.result()
            if status == "ok": ok += 1
            elif status == "skip": skip += 1
            else: err += 1
            if (i + 1) % 50 == 0 or (i + 1) == total:
                log(f"    Images: {i+1}/{total} ok={ok} skip={skip} err={err}")

    return {"ok": ok, "skip": skip, "err": err}


# ── State Management ──

def load_state(output_dir: Path) -> dict:
    sf = output_dir / STATE_FILE
    if sf.exists():
        return json.loads(sf.read_text())
    return {"completed_chunks": [], "total_pages_out": 0}


def save_state(output_dir: Path, state: dict) -> None:
    (output_dir / STATE_FILE).write_text(json.dumps(state, indent=2))


# ── Main ──

def process_chunk(chunk: dict, output_dir: Path, model: str, token: str, state: dict) -> dict:
    """Process a single chunk: submit → poll → download MD + images."""
    chunk_file = chunk["path"]
    offset = chunk["pdf_page_start"]  # 1-indexed start page of this chunk

    # Skip if already done
    cid = chunk["file"]
    if cid in state["completed_chunks"]:
        log(f"  SKIP {cid}: already completed")
        return {"chunk": cid, "pages": 0, "images": 0, "status": "skipped"}

    log(f"\n{'='*50}")
    log(f"  Processing: {cid} ({chunk['num_pages']} pages, offset={offset})")
    log(f"{'='*50}")

    # Submit
    job_id = submit_job(chunk_file, model, token)
    log(f"  job_id: {job_id}")

    # Poll
    log(f"  Polling...")
    job_data = poll_job(job_id, token)

    # Fetch + save per-page MD
    log(f"  Downloading MD...")
    num_pages, img_manifest = fetch_and_save(job_data, output_dir, offset, token)
    log(f"  Saved {num_pages} per-page MD files")

    # Download images
    img_stats = {"ok": 0, "skip": 0, "err": 0}
    if img_manifest:
        log(f"  Downloading {len(img_manifest)} images...")
        img_stats = download_images(img_manifest)
        log(f"  Images: ok={img_stats['ok']} skip={img_stats['skip']} err={img_stats['err']}")

    # Save state
    state["completed_chunks"].append(cid)
    state["total_pages_out"] += num_pages
    save_state(output_dir, state)

    return {"chunk": cid, "pages": num_pages, "images": img_stats["ok"], "status": "done"}


def main():
    p = argparse.ArgumentParser(description="Process PDF chunks via PaddleOCR API")
    p.add_argument("--chunks-dir", required=True, help="Directory with chunk PDFs + chunks_manifest.json")
    p.add_argument("--output-dir", required=True, help="Output directory for md/ and images/")
    p.add_argument("--model", default="PaddleOCR-VL-1.5", help="OCR model (default: PaddleOCR-VL-1.5)")
    p.add_argument("--parallel", type=int, default=1, help="Parallel chunk submissions (default: 1)")
    p.add_argument("--resume", action="store_true", help="Resume from last checkpoint")
    p.add_argument("--only", type=str, default=None, help="Process only this chunk file (e.g. chunk_0001-0100.pdf)")
    args = p.parse_args()

    chunks_dir = Path(args.chunks_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load manifest
    manifest_path = chunks_dir / "chunks_manifest.json"
    if not manifest_path.exists():
        sys.exit(f"Manifest not found: {manifest_path}. Run split_pdf.py first.")
    manifest = json.loads(manifest_path.read_text())

    # Filter chunks if --only specified
    chunks = manifest["chunks"]
    if args.only:
        chunks = [c for c in chunks if c["file"] == args.only]
        if not chunks:
            sys.exit(f"Chunk '{args.only}' not found in manifest")

    # Load state
    state = load_state(output_dir) if args.resume else {"completed_chunks": [], "total_pages_out": 0}

    token = load_token()

    # Optional: verify total pages in chunk files versus expected
    for chunk in chunks:
        cpath = Path(chunk["path"])
        if not cpath.exists():
            sys.exit(f"Chunk file missing: {cpath}")

    log(f"{'='*56}")
    log(f"  Process Chunks — PaddleOCR Async API")
    log(f"{'='*56}")
    log(f"  Chunks dir: {chunks_dir}")
    log(f"  Output dir: {output_dir}")
    log(f"  Total chunks: {len(chunks)}")
    log(f"  Model: {args.model}")
    log(f"  Parallel: {args.parallel}")
    if args.resume:
        log(f"  Resume: yes ({len(state['completed_chunks'])} already done)")
    log(f"{'='*56}")

    if args.parallel > 1:
        # Parallel mode: submit all, then poll all
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            futures = [ex.submit(process_chunk, c, output_dir, args.model, token, state)
                       for c in chunks]
            results = [fut.result() for fut in as_completed(futures)]
    else:
        # Sequential mode
        results = []
        for chunk in chunks:
            result = process_chunk(chunk, output_dir, args.model, token, state)
            results.append(result)

    # Summary
    total_pages = sum(r["pages"] for r in results)
    total_images = sum(r["images"] for r in results)
    log(f"\n{'='*56}")
    log(f"  ALL CHUNKS COMPLETE")
    log(f"  Total MD pages: {total_pages}")
    log(f"  Total images:   {total_images}")
    log(f"  MD dir:         {output_dir / 'md'}")
    log(f"  Images dir:     {output_dir / 'images'}")
    log(f"{'='*56}")


if __name__ == "__main__":
    main()
