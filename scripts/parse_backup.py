"""Parse Tistory backup HTML files into a structured JSON index.

Walks BACKUP_ROOT, reads every per-post HTML, and writes data/posts.json with:
    [{ id, slug, title, date, html_path, body_html, img_dir, image_refs }, ...]

Idempotent: rewrites the index every run.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

from bs4 import BeautifulSoup

from config import BACKUP_ROOT, DATA_DIR, POSTS_INDEX


@dataclass
class PostRecord:
    id: str
    slug: str
    title: str
    date: str
    html_path: str
    body_html: str
    img_dir: str | None
    image_refs: list[str]


_invalid_slug_chars = re.compile(r"[^\w\-가-힣]+", flags=re.UNICODE)


def _slugify(text: str) -> str:
    text = text.strip().replace(" ", "-")
    text = _invalid_slug_chars.sub("-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "post"


def _extract_record(post_dir: Path) -> PostRecord | None:
    html_files = sorted(post_dir.glob("*.html"))
    if not html_files:
        return None
    html_path = html_files[0]

    with html_path.open(encoding="utf-8", errors="replace") as fh:
        soup = BeautifulSoup(fh, "lxml")

    title_tag = soup.select_one("h2.title-article") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else post_dir.name

    date_tag = soup.select_one(".date")
    date = date_tag.get_text(strip=True) if date_tag else ""

    body_tag = soup.select_one(".contents_style") or soup.select_one(".article-view")
    body_html = body_tag.decode_contents() if body_tag else ""

    img_dir = post_dir / "img"
    img_dir_str = str(img_dir) if img_dir.exists() else None

    image_refs: list[str] = []
    if body_tag:
        for img in body_tag.find_all("img"):
            src = img.get("src", "").strip()
            if src:
                image_refs.append(src)

    stem = html_path.stem
    if "-" in stem and not stem.split("-")[0].isdigit() is False:
        # filename like "1066-소프트웨어-엔지니어링-핵심-법칙": use it minus the leading id-
        parts = stem.split("-", 1)
        slug_source = parts[1] if len(parts) == 2 and parts[0].isdigit() else stem
    else:
        slug_source = stem
    slug = _slugify(slug_source) if slug_source != post_dir.name else _slugify(title)
    slug = f"{post_dir.name}-{slug}" if slug != post_dir.name else slug

    return PostRecord(
        id=post_dir.name,
        slug=slug,
        title=title,
        date=date,
        html_path=str(html_path),
        body_html=body_html,
        img_dir=img_dir_str,
        image_refs=image_refs,
    )


def main() -> int:
    if not BACKUP_ROOT.exists():
        print(f"FATAL: backup root not found: {BACKUP_ROOT}", file=sys.stderr)
        return 2

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    post_dirs = sorted(
        (p for p in BACKUP_ROOT.iterdir() if p.is_dir() and p.name.isdigit()),
        key=lambda p: int(p.name),
    )

    records: list[PostRecord] = []
    skipped: list[str] = []
    for post_dir in post_dirs:
        record = _extract_record(post_dir)
        if record is None:
            skipped.append(post_dir.name)
            continue
        records.append(record)

    POSTS_INDEX.write_text(
        json.dumps([asdict(r) for r in records], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"parsed: {len(records)} posts")
    print(f"skipped (no html): {len(skipped)}")
    if skipped:
        print(f"  ids: {', '.join(skipped[:20])}{'...' if len(skipped) > 20 else ''}")
    print(f"index written: {POSTS_INDEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
