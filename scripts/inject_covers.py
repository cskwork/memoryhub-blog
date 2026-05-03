"""Set cover.image in frontmatter to the first image of each post.

PaperMod uses [cover] image to render thumbnails on list/home pages.
We pick the first ![](...) image found in the markdown body, normalize the
path so it survives the /memoryhub-blog/ subpath (Hugo will resolve it via
relURL when rendered), and write it under the cover block.

Idempotent: replaces an existing [cover] section.
"""
from __future__ import annotations

import re
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO

FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
COVER_BLOCK_RE = re.compile(r'^cover:\n(?:[ \t]+.*\n)+', re.MULTILINE)
IMG_RE = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<url>[^)]+?)(?:\s+"[^"]*")?\)')


def first_image(body: str) -> tuple[str, str] | None:
    m = IMG_RE.search(body)
    if not m:
        return None
    return m.group('url'), m.group('alt') or ''


def yaml_quote(value: str) -> str:
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def update_post(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    m = FRONTMATTER_RE.match(text)
    if not m:
        return False
    fm = m.group(1)
    body = text[m.end():]

    img = first_image(body)
    if not img:
        return False
    url, alt = img

    fm = COVER_BLOCK_RE.sub('', fm).rstrip() + '\n'
    fm += 'cover:\n'
    fm += f'  image: {yaml_quote(url)}\n'
    if alt:
        fm += f'  alt: {yaml_quote(alt)}\n'
    fm += '  relative: false\n'
    fm += '  hidden: false\n'

    new_text = f'---\n{fm}---\n{body}'
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def main() -> None:
    for label, content_dir in (('en', CONTENT_EN), ('ko', CONTENT_KO)):
        updated = skipped = 0
        for path in sorted(content_dir.glob('*.md')):
            if update_post(path):
                updated += 1
            else:
                skipped += 1
        print(f'{label}: updated {updated}, skipped {skipped}')


if __name__ == '__main__':
    main()
