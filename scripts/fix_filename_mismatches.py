"""Rename en posts to match ko filenames so Hugo i18n links them as translations.

Some translation subagents wrote files with English-translated slugs in the
filename instead of preserving the Korean filename. Hugo i18n matches translations
by filename (or translationKey), so this mismatch breaks language switching.

Strategy: for every en file whose tistory id (numeric prefix) matches a ko file's
tistory id, rename the en file to the ko file's name. Slug field inside the
frontmatter is left untouched (already correct).
"""
from __future__ import annotations

import re
import shutil
from collections import defaultdict
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO


_id_prefix = re.compile(r"^(\d+)-")


def _post_id(name: str) -> str | None:
    m = _id_prefix.match(name)
    return m.group(1) if m else None


def main() -> int:
    ko_by_id: dict[str, str] = {}
    for p in CONTENT_KO.glob("*.md"):
        if p.name == "_index.md":
            continue
        pid = _post_id(p.name)
        if pid:
            ko_by_id[pid] = p.name

    en_by_id: dict[str, list[str]] = defaultdict(list)
    for p in CONTENT_EN.glob("*.md"):
        if p.name == "_index.md":
            continue
        pid = _post_id(p.name)
        if pid:
            en_by_id[pid].append(p.name)

    renamed = 0
    skipped_match = 0
    duplicates: list[str] = []
    no_ko: list[str] = []

    for pid, en_names in en_by_id.items():
        ko_name = ko_by_id.get(pid)
        if not ko_name:
            for en in en_names:
                no_ko.append(f"{pid}: {en}")
            continue

        if len(en_names) == 1 and en_names[0] == ko_name:
            skipped_match += 1
            continue

        # If the canonical ko name already exists in en/, prefer it; remove
        # the duplicate.
        if ko_name in en_names:
            for en in en_names:
                if en == ko_name:
                    continue
                duplicates.append(f"{pid}: removed duplicate {en} (kept {ko_name})")
                (CONTENT_EN / en).unlink()
            continue

        # Otherwise pick the first en file and rename to ko_name. If multiple
        # candidates exist, keep the largest (most-translated) and discard others.
        candidates = sorted(en_names, key=lambda n: (CONTENT_EN / n).stat().st_size, reverse=True)
        winner = candidates[0]
        target = CONTENT_EN / ko_name
        if target.exists():
            (CONTENT_EN / winner).unlink()
        else:
            shutil.move(str(CONTENT_EN / winner), str(target))
            renamed += 1
        for losing in candidates[1:]:
            duplicates.append(f"{pid}: removed extra {losing}")
            (CONTENT_EN / losing).unlink()

    print(f"renamed:    {renamed}")
    print(f"already matched: {skipped_match}")
    print(f"removed duplicates: {len(duplicates)}")
    print(f"en without matching ko id: {len(no_ko)}")
    if duplicates[:10]:
        print("\nfirst duplicates removed:")
        for d in duplicates[:10]:
            print(f"  {d}")
    if no_ko[:10]:
        print("\nfirst en without ko match:")
        for n in no_ko[:10]:
            print(f"  {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
