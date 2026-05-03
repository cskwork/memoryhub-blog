"""Fix image URLs in markdown bodies and cover.image frontmatter.

Two issues to address:

1. Inline `![alt](<url>)` whose URL contains spaces or other characters
   that CommonMark rejects as bare destinations is not parsed as an image
   at all. We URL-encode unsafe characters (spaces -> %20, etc.) so the
   URL becomes a valid bare destination.

2. PaperMod's cover.html applies `absURL` to `cover.image`. With a leading
   slash, Hugo's absURL strips the subpath and resolves against the host
   root, not the project pages baseURL. Stripping the leading slash makes
   absURL join the path under the configured baseURL correctly.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote

from config import CONTENT_EN, CONTENT_KO

FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
COVER_IMAGE_LINE_RE = re.compile(r'^(\s*image:\s*)"(?P<url>/[^"]+)"\s*$', re.MULTILINE)
IMG_REF_RE = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<url>[^)]+?)(?P<title>\s+"[^"]*")?\)')

SAFE_URL_CHARS = "/-_.~!*'(),;:@&=+$#?%"


def encode_url(raw: str) -> str:
    return quote(raw, safe=SAFE_URL_CHARS)


def fix_body_images(body: str) -> tuple[str, int]:
    changes = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changes
        url = match.group('url').strip()
        alt = match.group('alt')
        title = match.group('title') or ''
        encoded = encode_url(url)
        if encoded == url:
            return match.group(0)
        changes += 1
        return f'![{alt}]({encoded}{title})'

    new_body = IMG_REF_RE.sub(replace, body)
    return new_body, changes


def fix_cover_image(fm: str) -> tuple[str, bool]:
    def replace(match: re.Match[str]) -> str:
        prefix = match.group(1)
        url = match.group('url')
        encoded = encode_url(url.lstrip('/'))
        return f'{prefix}"{encoded}"'

    new_fm, n = COVER_IMAGE_LINE_RE.subn(replace, fm)
    return new_fm, bool(n)


def update_post(path: Path) -> tuple[bool, int, bool]:
    text = path.read_text(encoding='utf-8')
    m = FRONTMATTER_RE.match(text)
    if not m:
        body_only, body_changes = fix_body_images(text)
        if body_changes:
            path.write_text(body_only, encoding='utf-8')
            return True, body_changes, False
        return False, 0, False

    fm = m.group(1)
    body = text[m.end():]
    new_fm, cover_changed = fix_cover_image(fm)
    new_body, body_changes = fix_body_images(body)
    if not cover_changed and not body_changes:
        return False, 0, False
    new_text = f'---\n{new_fm}\n---\n{new_body}'
    path.write_text(new_text, encoding='utf-8')
    return True, body_changes, cover_changed


def main() -> None:
    for label, content_dir in (('en', CONTENT_EN), ('ko', CONTENT_KO)):
        files_changed = total_imgs = covers_fixed = 0
        for path in sorted(content_dir.glob('*.md')):
            changed, imgs, cover = update_post(path)
            if changed:
                files_changed += 1
            total_imgs += imgs
            covers_fixed += 1 if cover else 0
        print(f'{label}: {files_changed} files changed, {total_imgs} body imgs encoded, {covers_fixed} covers fixed')


if __name__ == '__main__':
    main()
