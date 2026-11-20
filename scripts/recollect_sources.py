"""Download the cited sources again and check them against the stored hashes.

The full texts of the downloaded sources are not redistributed in this
repository. For every source that was downloaded during the audit, the run
keeps `documents/<id>.meta.json` with the SHA-256 of the Markdown text the
judge's evidence came from. This script downloads each source again with the
same fetcher and converter used by Deep Research Auditor, writes the Markdown
next to its metadata (or to --out), and reports whether the text is identical
to the audited one.

Requires Deep Research Auditor installed in the same environment:
    git clone https://github.com/menezs/deep-research-auditor
    pip install -e ./deep-research-auditor

Usage:
    python scripts/recollect_sources.py [RUN_DIR ...] [--out DIR] [--workers 8] [--report recollect_report.csv]
Without RUN_DIR, every run under Runs/ is processed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from auditframework.ingestion import HttpFetcher
from auditframework.ingestion.service import _ingest_one  # same fetch, conversion, barrier and Wayback logic as the audit
from auditframework.models import Reference

ROOT = Path(__file__).resolve().parents[1]


def sources(run: Path):
    """(run, reference, stored hash) for every source downloaded in the run."""
    refs = {r["id"]: r for r in json.loads((run / "references.json").read_text(encoding="utf-8"))}
    for meta_path in sorted((run / "documents").glob("*.meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta["reference_id"] in refs:
            yield run, Reference.model_validate(refs[meta["reference_id"]]), meta["content_hash"]


def recollect(item, fetcher: HttpFetcher, out: Path | None) -> dict:
    run, ref, stored_hash = item
    row = {"run": run.name, "reference_id": ref.id, "url": ref.raw_url}
    try:
        _, document, markdown = _ingest_one(ref, fetcher)
    except Exception as exc:  # network boundary: record and continue
        return row | {"status": "error", "detail": f"{type(exc).__name__}: {exc}"[:300]}
    if document is None or markdown is None:
        return row | {"status": "unavailable", "detail": "dead, inaccessible, or behind an access barrier now"}
    target = (out / run.name if out else run / "documents")
    target.mkdir(parents=True, exist_ok=True)
    (target / f"{ref.id}.md").write_text(markdown, encoding="utf-8")
    same = hashlib.sha256(markdown.encode("utf-8")).hexdigest() == stored_hash
    return row | {"status": "identical" if same else "changed", "detail": ""}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="*", type=Path)
    ap.add_argument("--out", type=Path, help="write the Markdown here instead of each run's documents/")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--report", type=Path, default=Path("recollect_report.csv"))
    args = ap.parse_args()

    runs = args.runs or sorted(p.parent for p in ROOT.glob("Runs/*/*/run_meta.json"))
    items = [item for run in runs for item in sources(run)]
    print(f"{len(items)} sources in {len(runs)} runs", flush=True)

    fetcher = HttpFetcher()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(lambda it: recollect(it, fetcher, args.out), items))

    with args.report.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["run", "reference_id", "url", "status", "detail"])
        writer.writeheader()
        writer.writerows(rows)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(", ".join(f"{k}: {v}" for k, v in sorted(counts.items())), f"-> {args.report}")


if __name__ == "__main__":
    main()
