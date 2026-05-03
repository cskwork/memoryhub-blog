"""Extract categories from Tistory backup and write to data/categories.json.

Tistory category format in HTML: `<sortcode>===<parent>/<child>` (e.g.
`700===Dev Util/자바스크립트 놀기`). We strip the sort prefix, split on `/`,
and keep [parent, child] when present, parent only otherwise.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from config import BACKUP_ROOT, DATA_DIR

CATEGORY_RE = re.compile(r'class="category">([^<]*)</p>')
SORT_PREFIX_RE = re.compile(r'^\d+===')


def parse_category(raw: str) -> list[str]:
    raw = raw.strip()
    if not raw:
        return []
    raw = SORT_PREFIX_RE.sub('', raw)
    parts = [p.strip() for p in raw.split('/') if p.strip()]
    return parts


def main() -> None:
    out: dict[str, list[str]] = {}
    for post_dir in sorted(BACKUP_ROOT.iterdir()):
        if not post_dir.is_dir():
            continue
        htmls = list(post_dir.glob('*.html'))
        if not htmls:
            continue
        html = htmls[0].read_text(encoding='utf-8', errors='ignore')
        m = CATEGORY_RE.search(html)
        if not m:
            continue
        cats = parse_category(m.group(1))
        if cats:
            out[post_dir.name] = cats

    DATA_DIR.mkdir(exist_ok=True)
    target = DATA_DIR / 'categories.json'
    target.write_text(
        json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True),
        encoding='utf-8',
    )
    print(f'wrote {len(out)} category records to {target}')


if __name__ == '__main__':
    main()
