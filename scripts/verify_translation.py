"""Audit translation completeness.

Reports which ko posts have no en counterpart, and inspects basic
frontmatter/structure consistency.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO, DATA_DIR


_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def _read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm


def main() -> int:
    ko_files = sorted(p.name for p in CONTENT_KO.glob("*.md") if p.name != "_index.md")
    en_files = {p.name for p in CONTENT_EN.glob("*.md")}

    missing = [n for n in ko_files if n not in en_files]
    extra = [n for n in en_files if n not in set(ko_files) and n != "_index.md"]

    inconsistencies: list[str] = []
    untranslated_titles: list[str] = []
    for name in ko_files:
        if name in missing:
            continue
        ko_fm = _read_frontmatter(CONTENT_KO / name)
        en_fm = _read_frontmatter(CONTENT_EN / name)
        for key in ("date", "slug", "tistory_id", "original_url"):
            if ko_fm.get(key) != en_fm.get(key):
                inconsistencies.append(
                    f"{name}: {key} ko={ko_fm.get(key)!r} en={en_fm.get(key)!r}"
                )
                break
        # crude check: english title shouldn't contain hangul
        if en_fm.get("title") and re.search(r"[가-힣]", en_fm["title"]):
            untranslated_titles.append(f"{name}: {en_fm['title']}")

    report = {
        "ko_total": len(ko_files),
        "en_total": len(en_files - {"_index.md"}),
        "missing_en": len(missing),
        "extra_en": len(extra),
        "frontmatter_inconsistent": len(inconsistencies),
        "title_still_korean": len(untranslated_titles),
        "missing_files": missing[:50],
        "inconsistencies": inconsistencies[:20],
        "untranslated_titles": untranslated_titles[:20],
    }

    out_path = DATA_DIR / "translation_audit.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"ko total: {report['ko_total']}")
    print(f"en total: {report['en_total']}")
    print(f"missing en: {report['missing_en']}")
    print(f"frontmatter mismatches: {report['frontmatter_inconsistent']}")
    print(f"english titles still in korean: {report['title_still_korean']}")
    if missing:
        print("\nfirst 10 missing en files:")
        for f in missing[:10]:
            print(f"  - {f}")
    print(f"\naudit written: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
