"""Convert each post's body_html into a Hugo-ready Korean Markdown file.

Reads:
    data/posts.json
    data/image_map.json
Writes:
    content/ko/posts/<slug>.md

Idempotent: overwrites existing files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from config import CONTENT_KO, DATA_DIR, ORIGINAL_BASE_URL, POSTS_INDEX


KST_OFFSET = "+09:00"


class _Converter(MarkdownConverter):
    """markdownify with sensible defaults for Tistory HTML."""

    def convert_figure(self, el, text, parent_tags=None):
        # Tistory wraps images in <figure class="imageblock">; markdownify
        # already handles the inner <img>, so just unwrap caption (if any).
        return text

    def convert_span(self, el, text, parent_tags=None):
        return text

    def convert_div(self, el, text, parent_tags=None):
        return text


def _to_md(html: str) -> str:
    converter = _Converter(
        heading_style="ATX",
        bullets="-",
        code_language="",
        strip=["style", "script"],
    )
    md = converter.convert(html)
    md = re.sub(r" ", " ", md)  # non-breaking spaces
    md = re.sub(r"\n{3,}", "\n\n", md)  # collapse blank lines
    md = re.sub(r"^[ \t]+\n", "\n", md, flags=re.MULTILINE)
    return md.strip() + "\n"


def _rewrite_images(html: str, image_map: dict[str, str]) -> str:
    if not image_map:
        return html
    soup = BeautifulSoup(html, "lxml")
    for img in soup.find_all("img"):
        src = img.get("src", "")
        new = image_map.get(src)
        if new:
            img["src"] = new
        for attr in ("width", "height", "data-lightbox", "data-ke-mobilestyle"):
            if attr in img.attrs:
                del img.attrs[attr]
    return str(soup)


_yaml_escape = re.compile(r'(["\\])')


def _escape_yaml(text: str) -> str:
    return _yaml_escape.sub(r"\\\1", text)


def _format_date(raw: str) -> str:
    try:
        dt = datetime.strptime(raw, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return raw
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + KST_OFFSET


def _frontmatter(rec: dict) -> str:
    title = _escape_yaml(rec["title"])
    date = _format_date(rec["date"])
    return (
        "---\n"
        f'title: "{title}"\n'
        f"date: {date}\n"
        f'slug: "{rec["slug"]}"\n'
        f'original_url: "{ORIGINAL_BASE_URL}/{rec["id"]}"\n'
        f'tistory_id: {rec["id"]}\n'
        "draft: false\n"
        "---\n\n"
    )


def main() -> int:
    if not POSTS_INDEX.exists():
        print(f"FATAL: run parse_backup.py first ({POSTS_INDEX} missing)", file=sys.stderr)
        return 2

    image_map_path = DATA_DIR / "image_map.json"
    image_map_all = (
        json.loads(image_map_path.read_text(encoding="utf-8"))
        if image_map_path.exists()
        else {}
    )

    records = json.loads(POSTS_INDEX.read_text(encoding="utf-8"))
    CONTENT_KO.mkdir(parents=True, exist_ok=True)

    written = 0
    empty_body = 0
    for rec in records:
        body_html = rec.get("body_html", "")
        if not body_html.strip():
            empty_body += 1
            body_html = ""

        per_post_map = image_map_all.get(rec["id"], {})
        body_html = _rewrite_images(body_html, per_post_map)
        md_body = _to_md(body_html) if body_html else "\n"

        out = _frontmatter(rec) + md_body
        out_path = CONTENT_KO / f"{rec['slug']}.md"
        out_path.write_text(out, encoding="utf-8")
        written += 1

    print(f"written: {written} files -> {CONTENT_KO}")
    print(f"empty body: {empty_body}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
