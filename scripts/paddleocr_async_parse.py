#!/usr/bin/env python3
"""
PaddleOCR Async Document Parsing Script
========================================
Generic, reusable script for submitting PDFs/images to the Baidu AI Studio
PaddleOCR async API, polling for completion, and downloading structured
Markdown + extracted images.

API Reference:
  - https://ai.baidu.com/ai-doc/AISTUDIO/Cmkz2m0ma  (sync API / layout-parsing)
  - https://ai.baidu.com/ai-doc/AISTUDIO/fml7mozw5   (async API / jobs)

Authentication:
  Token from https://aistudio.baidu.com/account/accessToken
  Set via PADDLEOCR_ACCESS_TOKEN env var or .env file.

Usage:
  python paddleocr_async_parse.py --pdf <path> [--output-dir <dir>] [--model <name>]
  python paddleocr_async_parse.py --pdf doc.pdf --output-dir ./output --model PaddleOCR-VL-1.5
  python paddleocr_async_parse.py --pdf doc.pdf --pages "1-5,10" --chart-recognition

Environment:
  PADDLEOCR_ACCESS_TOKEN  - API access token (required)
  PADDLEOCR_BASE_URL      - API base URL (default: https://paddleocr.aistudio-app.com)
"""

import argparse
import base64
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests


# ── Constants ────────────────────────────────────────────────────────────────

DEFAULT_BASE_URL = "https://paddleocr.aistudio-app.com"
JOB_ENDPOINT = "/api/v2/ocr/jobs"
POLL_INTERVAL = 5  # seconds
MAX_RETRIES = 3
RETRY_BACKOFF = 2  # multiplicative backoff

VALID_MODELS = [
    "PaddleOCR-VL-1.5",
    "PaddleOCR-VL",
    "PP-StructureV3",
    "PP-OCRv5",
]

MODELS_WITH_LAYOUT = {
    "PaddleOCR-VL-1.5",
    "PaddleOCR-VL",
    "PP-StructureV3",
}


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_token() -> str:
    """Load the access token from environment or .env file."""
    token = os.environ.get("PADDLEOCR_ACCESS_TOKEN")
    if token:
        return token

    # Try .env file in the script's parent directory and cwd
    env_paths = [
        Path(__file__).resolve().parent.parent / ".env",
        Path.cwd() / ".env",
    ]
    for env_file in env_paths:
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k == "PADDLEOCR_ACCESS_TOKEN" and v:
                        return v

    raise RuntimeError(
        "PADDLEOCR_ACCESS_TOKEN not set. Either:\n"
        "  export PADDLEOCR_ACCESS_TOKEN=<your_token>\n"
        "  or create a .env file with PADDLEOCR_ACCESS_TOKEN=<your_token>"
    )


def log(msg: str, level: str = "INFO") -> None:
    """Timestamped log message."""
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] [{level}] {msg}", flush=True)


# ── API Client ───────────────────────────────────────────────────────────────

class PaddleOCRAsyncClient:
    """Client for the PaddleOCR async document parsing API."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL, token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.token = token or load_token()
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def submit_job(
        self,
        file_path: str,
        model: str = "PaddleOCR-VL-1.5",
        page_ranges: Optional[str] = None,
        use_doc_orientation: bool = True,
        use_doc_unwarping: bool = False,
        use_chart_recognition: bool = True,
    ) -> str:
        """Submit a file for async parsing. Returns the job ID."""
        log(f"Submitting file: {file_path}")
        log(f"  Model: {model}")

        abs_path = Path(file_path).resolve()
        if not abs_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        file_size_mb = abs_path.stat().st_size / (1024 * 1024)
        log(f"  File size: {file_size_mb:.1f} MB")

        if file_size_mb > 50:
            raise ValueError(
                f"File too large ({file_size_mb:.1f} MB). "
                "Local upload limit is 50 MB. Use a file URL instead."
            )

        optional_payload = {
            "useDocOrientationClassify": use_doc_orientation,
            "useDocUnwarping": use_doc_unwarping,
            "useChartRecognition": use_chart_recognition,
        }

        data = {
            "model": model,
            "optionalPayload": json.dumps(optional_payload),
        }
        if page_ranges:
            data["pageRanges"] = page_ranges
            log(f"  Page ranges: {page_ranges}")

        with open(abs_path, "rb") as f:
            resp = self.session.post(
                f"{self.base_url}{JOB_ENDPOINT}",
                data=data,
                files={"file": f},
            )

        if resp.status_code != 200:
            self._handle_http_error(resp)

        result = resp.json()
        code = result.get("code", -1)
        if code != 0:
            raise RuntimeError(
                f"Job submission failed (code={code}): {result.get('msg', 'Unknown error')}"
            )

        job_id = result["data"]["jobId"]
        log(f"  Job ID: {job_id}")
        log(f"  Trace ID: {result.get('traceId', 'N/A')}")
        return job_id

    def poll_job(self, job_id: str, poll_interval: int = POLL_INTERVAL) -> dict:
        """Poll job status until done or failed. Returns the final job data."""
        url = f"{self.base_url}{JOB_ENDPOINT}/{job_id}"
        last_progress = ""

        while True:
            resp = self.session.get(url)
            if resp.status_code != 200:
                self._handle_http_error(resp)

            result = resp.json()
            code = result.get("code", -1)
            if code != 0:
                raise RuntimeError(
                    f"Status query failed (code={code}): {result.get('msg', '')}"
                )

            data = result["data"]
            state = data.get("state", "unknown")

            if state in ("pending", "running"):
                progress = data.get("extractProgress", {})
                if progress:
                    current = progress.get("extractedPages", "?")
                    total = progress.get("totalPages", "?")
                    msg = f"Parsing: {current}/{total} pages"
                else:
                    msg = f"State: {state}"

                if state == "pending":
                    msg = "Queued (pending)..."
                if msg != last_progress:
                    log(msg)
                    last_progress = msg

                time.sleep(poll_interval)

            elif state == "done":
                progress = data.get("extractProgress", {})
                pages = progress.get("extractedPages", "?")
                log(f"Parsing complete. {pages} pages extracted.")
                return data

            elif state == "failed":
                error_msg = data.get("errorMsg", "Unknown failure")
                raise RuntimeError(f"Job failed: {error_msg}")

            else:
                raise RuntimeError(f"Unknown job state: {state}")

    def download_results(self, job_data: dict, output_dir: Path) -> dict:
        """Download JSONL results and return parsed data."""
        jsonl_url = job_data["resultUrl"]["jsonUrl"]
        log(f"Downloading results: {jsonl_url}")

        resp = self.session.get(jsonl_url)
        if resp.status_code != 200:
            # Retry without session auth (signed URLs already have auth)
            resp = requests.get(jsonl_url, timeout=120)
        if resp.status_code != 200:
            raise RuntimeError(
                f"Failed to download results: HTTP {resp.status_code}\n"
                f"  URL: {jsonl_url[:100]}..."
            )

        lines = resp.text.strip().split("\n")
        log(f"  Downloaded {len(lines)} lines (pages)")

        pages = []
        for line in lines:
            if not line.strip():
                continue
            page = json.loads(line)
            pages.append(page)

        return self._process_pages(pages, output_dir)

    def _process_pages(
        self, pages: list, output_dir: Path
    ) -> dict:
        """Extract and save MD + images from parsed pages."""
        md_dir = output_dir / "md"
        images_dir = output_dir / "images"
        md_dir.mkdir(parents=True, exist_ok=True)
        images_dir.mkdir(parents=True, exist_ok=True)

        # Detect result format from actual data, not job metadata
        first_page = pages[0] if pages else {}
        first_result = first_page.get("result", {})
        uses_layout = "layoutParsingResults" in first_result
        total_pages = len(pages)
        saved_images = 0

        all_md_texts = []

        for i, page in enumerate(pages):
            if not page or "result" not in page:
                log(f"  Skipping page {i}: no result data")
                continue

            result = page["result"]

            if uses_layout:
                layout_results = result.get("layoutParsingResults", [])
                for j, res in enumerate(layout_results):
                    suffix = f"_page{i}_{j}" if len(layout_results) > 1 else f"_page{i}"
                    markdown = res.get("markdown", {})

                    # Extract markdown text
                    md_text = markdown.get("text", "")
                    if md_text:
                        page_md_file = md_dir / f"{suffix}.md"
                        with open(page_md_file, "w", encoding="utf-8") as f:
                            f.write(md_text)
                        all_md_texts.append((i, suffix, md_text))

                    # Download embedded images
                    md_images = markdown.get("images", {})
                    for rel_path, img_url in md_images.items():
                        img_path = images_dir / rel_path
                        img_path = Path(str(img_path))  # normalize
                        self._save_image(img_url, img_path)
                        saved_images += 1

                    # Download output/render images
                    output_images = res.get("outputImages", {})
                    for name, img_url in output_images.items():
                        img_path = images_dir / f"{suffix}_{name}.jpg"
                        if self._save_image(img_url, img_path):
                            saved_images += 1
            else:
                # PP-OCRv5: plain text results
                ocr_results = result.get("ocrResults", [])
                for j, res in enumerate(ocr_results):
                    suffix = f"_page{i}_{j}" if len(ocr_results) > 1 else f"_page{i}"
                    ocr_image = res.get("ocrImage")
                    if ocr_image:
                        img_path = images_dir / f"{suffix}_ocr.jpg"
                        self._save_image(ocr_image, img_path)
                        saved_images += 1

        # Merge all MD into full_document.md
        if all_md_texts:
            full_md_path = md_dir / "full_document.md"
            parts = []
            for _, _, text in all_md_texts:
                parts.append(text)
            with open(full_md_path, "w", encoding="utf-8") as f:
                f.write("\n\n".join(parts))
            log(f"  Merged document: {full_md_path}")

        return {
            "pages_processed": total_pages,
            "images_saved": saved_images,
            "md_files": len(all_md_texts),
            "output_dir": str(output_dir),
        }

    @staticmethod
    def _save_image(url: str, path: Path) -> bool:
        """Download and save an image from URL. Returns True on success."""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            # Handle both absolute URLs and bare strings
            if url.startswith("http"):
                resp = requests.get(url, timeout=60)
                if resp.status_code == 200:
                    with open(path, "wb") as f:
                        f.write(resp.content)
                    return True
            else:
                # Might be base64 encoded
                try:
                    data = base64.b64decode(url)
                    with open(path, "wb") as f:
                        f.write(data)
                    return True
                except Exception:
                    pass
        except Exception as e:
            log(f"  Warning: Failed to save image {path.name}: {e}", "WARN")
        return False

    @staticmethod
    def _handle_http_error(resp: requests.Response) -> None:
        """Parse and raise a descriptive error from an HTTP response."""
        try:
            body = resp.json()
            code = body.get("code", resp.status_code)
            msg = body.get("msg", resp.text)
        except Exception:
            code = resp.status_code
            msg = resp.text

        error_map = {
            401: "Invalid or expired access token. Get a new one from https://aistudio.baidu.com/account/accessToken.",
            10001: "Empty file - check the file content.",
            10002: "File URL unrecognized - provide a valid, accessible URL.",
            10003: "File exceeds size limit (200 MB URL, 50 MB upload).",
            10004: "Unsupported file format.",
            10005: "File content unparseable - verify the document is not corrupted.",
            10006: "Page count exceeds limit (max 1000 pages).",
            10007: f"Invalid model name. Choose from: {', '.join(VALID_MODELS)}",
            10008: "Parameter error - check optionalPayload.",
            10009: "Batch job limit reached (max 100 per batchId).",
            10010: "Submission queue full - retry later.",
            11001: "Unknown jobId - verify the job ID.",
            11002: "Expired job - results stored temporarily; resubmit.",
            11003: "Parsing failure - check data.errorMsg for details.",
            12001: "Daily page quota exceeded - upgrade quota.",
            12002: "Rate limited - reduce request frequency.",
        }

        explanation = error_map.get(code, f"Unexpected error (code={code})")
        raise RuntimeError(f"API error: {explanation}\n  Details: {msg}")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="PaddleOCR Async Document Parsing — submit PDFs/images to the "
                    "Baidu AI Studio async API and download structured Markdown + images.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --pdf document.pdf
  %(prog)s --pdf document.pdf --output-dir ./parsed --model PaddleOCR-VL-1.5
  %(prog)s --pdf scan.pdf --pages "1-5,10-15" --chart-recognition
  %(prog)s --pdf large.pdf --pages "1-100" --no-chart --no-orientation

Environment:
  PADDLEOCR_ACCESS_TOKEN   API token (required)
  PADDLEOCR_BASE_URL       API base URL (default: https://paddleocr.aistudio-app.com)
        """,
    )

    parser.add_argument(
        "--pdf", required=True, metavar="PATH",
        help="Path to the PDF or image file to parse.",
    )
    parser.add_argument(
        "--output-dir", default=None, metavar="DIR",
        help="Directory to save results (md/ and images/ subdirectories). "
             "Defaults to '<input_dir>/<basename>_parsed/'.",
    )
    parser.add_argument(
        "--model", default="PaddleOCR-VL-1.5",
        choices=VALID_MODELS,
        help="Model to use for parsing (default: PaddleOCR-VL-1.5).",
    )
    parser.add_argument(
        "--pages", default=None, metavar="RANGE",
        help='Page range spec, e.g. "1-5,10,15-20" or "2--2" (page 2 to second-to-last).',
    )
    parser.add_argument(
        "--orientation", action="store_true", default=True, dest="orientation",
        help="Auto-detect and correct page orientation (default: on).",
    )
    parser.add_argument(
        "--no-orientation", action="store_false", dest="orientation",
        help="Disable orientation detection.",
    )
    parser.add_argument(
        "--unwarp", action="store_true", default=False, dest="unwarp",
        help="Auto-correct distorted/curved pages (default: off).",
    )
    parser.add_argument(
        "--no-unwarp", action="store_false", dest="unwarp",
        help="Disable unwarping.",
    )
    parser.add_argument(
        "--chart-recognition", action="store_true", default=True, dest="chart_recognition",
        help="Recognize and parse charts into table format (default: on).",
    )
    parser.add_argument(
        "--no-chart", action="store_false", dest="chart_recognition",
        help="Disable chart recognition.",
    )
    parser.add_argument(
        "--poll-interval", type=int, default=POLL_INTERVAL, metavar="SEC",
        help=f"Seconds between status polls (default: {POLL_INTERVAL}).",
    )

    args = parser.parse_args()

    # Determine output directory
    input_path = Path(args.pdf).resolve()
    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = input_path.parent / f"{input_path.stem}_parsed"

    log(f"╔══════════════════════════════════════════════╗")
    log(f"║  PaddleOCR Async Document Parsing           ║")
    log(f"╚══════════════════════════════════════════════╝")
    log(f"Input:      {input_path}")
    log(f"Output:     {output_dir}")
    log(f"Model:      {args.model}")

    # Initialize client
    base_url = os.environ.get("PADDLEOCR_BASE_URL", DEFAULT_BASE_URL)
    client = PaddleOCRAsyncClient(base_url=base_url)

    # Submit job
    job_id = client.submit_job(
        file_path=str(input_path),
        model=args.model,
        page_ranges=args.pages,
        use_doc_orientation=args.orientation,
        use_doc_unwarping=args.unwarp,
        use_chart_recognition=args.chart_recognition,
    )

    # Poll until done
    log(f"Polling job status every {args.poll_interval}s...")
    job_data = client.poll_job(job_id, poll_interval=args.poll_interval)

    # Download & save results
    log(f"Saving results to {output_dir} ...")
    summary = client.download_results(job_data, output_dir)

    # Summary
    log("━" * 50)
    log("Parsing complete!", "DONE")
    log(f"  Pages processed:  {summary['pages_processed']}")
    log(f"  MD files saved:   {summary['md_files']}")
    log(f"  Images saved:     {summary['images_saved']}")
    log(f"  Output directory: {summary['output_dir']}")
    log(f"  Merged document:  {output_dir / 'md' / 'full_document.md'}")
    log("━" * 50)

    return 0


if __name__ == "__main__":
    sys.exit(main())
