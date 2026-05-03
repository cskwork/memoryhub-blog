"""Remove orphan `  hidden: false` lines that landed before the `cover:` block.

This was caused by an off-by-one bug in COVER_BLOCK_RE: the previous regex
required a trailing newline after the last indented line, but the frontmatter
capture didn't include one, leaving the last `hidden: false` orphaned when the
cover block was rebuilt on a subsequent run.

This script scans en/ko posts and strips a single orphan indented line that
appears between top-level keys and the cover block.
"""
from __future__ import annotations

import re
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO

ORPHAN_RE = re.compile(
    r'(^[a-zA-Z_][^\n]*: [^\n]*\n)([ \t]+hidden:\s*false\n)(cover:\n)',
    re.MULTILINE,
)


def fix(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    new_text, n = ORPHAN_RE.subn(r'\1\3', text)
    if n:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def main() -> None:
    for label, content_dir in (('en', CONTENT_EN), ('ko', CONTENT_KO)):
        fixed = 0
        for path in sorted(content_dir.glob('*.md')):
            if fix(path):
                fixed += 1
        print(f'{label}: fixed {fixed}')


if __name__ == '__main__':
    main()
