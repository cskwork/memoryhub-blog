"""Plan translation work: find untranslated ko posts and split into batches.

Writes data/translation_batches.json with shape:
    { "batches": [ { "id": int, "files": ["1-환영합니다.md", ...] }, ... ] }

Defaults to ~50 files per batch; tune via --batch-size.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO, DATA_DIR


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=50)
    args = ap.parse_args()

    ko_files = sorted(p.name for p in CONTENT_KO.glob("*.md"))
    en_existing = {p.name for p in CONTENT_EN.glob("*.md")}

    todo = [name for name in ko_files if name not in en_existing]

    batches = []
    for i in range(0, len(todo), args.batch_size):
        batches.append({"id": len(batches), "files": todo[i : i + args.batch_size]})

    out = {
        "total_ko": len(ko_files),
        "already_translated": len(en_existing),
        "remaining": len(todo),
        "batch_size": args.batch_size,
        "batches": batches,
    }
    out_path = DATA_DIR / "translation_batches.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"ko total:           {out['total_ko']}")
    print(f"already translated: {out['already_translated']}")
    print(f"remaining:          {out['remaining']}")
    print(f"batches:            {len(batches)} of size <= {args.batch_size}")
    print(f"plan written:       {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
