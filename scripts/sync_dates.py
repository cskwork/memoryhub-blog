"""Copy ko date into en frontmatter for any post where they diverged."""
from __future__ import annotations

import re
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO


_FM = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_DATE = re.compile(r"^date:\s*(.+)$", re.MULTILINE)


def _read_date(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    fm_match = _FM.match(text)
    if not fm_match:
        return None
    date_match = _DATE.search(fm_match.group(1))
    return date_match.group(1).strip() if date_match else None


def main() -> int:
    fixed = 0
    for ko_path in CONTENT_KO.glob("*.md"):
        if ko_path.name == "_index.md":
            continue
        en_path = CONTENT_EN / ko_path.name
        if not en_path.exists():
            continue
        ko_date = _read_date(ko_path)
        en_date = _read_date(en_path)
        if not ko_date or not en_date or ko_date == en_date:
            continue
        en_text = en_path.read_text(encoding="utf-8")
        # Replace only the first `date:` line (inside frontmatter)
        new_text = _DATE.sub(f"date: {ko_date}", en_text, count=1)
        en_path.write_text(new_text, encoding="utf-8")
        fixed += 1

    print(f"dates synced: {fixed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
