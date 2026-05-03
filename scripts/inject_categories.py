"""Inject categories/tags into Hugo post frontmatter (en + ko).

Reads data/categories.json (post_id -> [parent, child?]) and updates each
matching post in content/en/posts and content/ko/posts. The Korean parent
becomes `categories: [parent]`; the child becomes `tags: [child]`. For the
English variant we map both via a small bilingual dictionary.

Idempotent: if categories/tags fields already exist, they are replaced.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO, DATA_DIR

CATEGORIES_FILE = DATA_DIR / 'categories.json'

# Parent translations (top-level category)
PARENT_KO_TO_EN: dict[str, str] = {
    'Dev AWS': 'Dev AWS',
    'Dev Concepts and License': 'Dev Concepts',
    'Dev Database': 'Dev Database',
    'Dev Framework': 'Dev Framework',
    'Dev Language': 'Dev Language',
    'Dev Library': 'Dev Library',
    'Dev Ops': 'Dev Ops',
    'Dev Util': 'Dev Util',
    '금용': 'Finance',
    '생활': 'Life',
    '포트폴리오': 'Portfolio',
    '후기': 'Reviews',
}

PARENT_KO_NORMALIZED: dict[str, str] = {
    'Dev AWS': 'Dev AWS',
    'Dev Concepts and License': '데브 컨셉',
    'Dev Database': '데브 데이터베이스',
    'Dev Framework': '데브 프레임워크',
    'Dev Language': '데브 언어',
    'Dev Library': '데브 라이브러리',
    'Dev Ops': '데브 옵스',
    'Dev Util': '데브 유틸',
    '금용': '금융',
    '생활': '생활',
    '포트폴리오': '포트폴리오',
    '후기': '후기',
}

# Child translations (sub-category, used as tags)
CHILD_KO_TO_EN: dict[str, str] = {
    'Flask활용한 todo리스트 구현': 'Flask Todo List',
    'ORACLE 데이터베이스': 'Oracle Database',
    'TA 사업': 'TA Business',
    'THE LAW OF CI': 'CI Laws',
    '개발자 TIL': 'Dev TIL',
    '게임': 'Games',
    '결제 연동': 'Payment Integration',
    '교육': 'Education',
    '구글 연동': 'Google Integration',
    '금용': 'Finance',
    '기본 게시판': 'General Board',
    '기획': 'Planning',
    '네트워크 이론': 'Network Theory',
    '독서': 'Reading',
    '마음 건강': 'Mental Health',
    '맛집': 'Food',
    '미분류': 'Uncategorized',
    '생활': 'Daily Life',
    '설정': 'Settings',
    '소프트웨어 아키텍쳐': 'Software Architecture',
    '심리': 'Psychology',
    '운동': 'Exercise',
    '육체 건강': 'Physical Health',
    '이론 문서': 'Theory Notes',
    '인간관계 TIL': 'Relationships TIL',
    '자기개발': 'Self Development',
    '자바스크립트 놀기': 'JavaScript Play',
    '정보처리기사': 'Info Processing Cert',
    '주택': 'Housing',
    '참고한 사이트 링크': 'Reference Links',
    '창작 소설 (AI)': 'AI Fiction',
    '취업시장 탐구 및 조사': 'Job Market Research',
    '트렌드': 'Trends',
}


def translate_parent(parent: str, *, en: bool) -> str:
    if en:
        return PARENT_KO_TO_EN.get(parent, parent)
    return PARENT_KO_NORMALIZED.get(parent, parent)


def translate_child(child: str, *, en: bool) -> str:
    if en:
        return CHILD_KO_TO_EN.get(child, child)
    return child


FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
CAT_LINE_RE = re.compile(r'^categories:\s*\[.*?\]\s*$\n?', re.MULTILINE)
TAG_LINE_RE = re.compile(r'^tags:\s*\[.*?\]\s*$\n?', re.MULTILINE)


def yaml_list(items: list[str]) -> str:
    quoted = [f'"{item.replace(chr(92), chr(92)*2).replace(chr(34), chr(92)+chr(34))}"' for item in items]
    return '[' + ', '.join(quoted) + ']'


def update_post(path: Path, post_id: str, parts: list[str], *, en: bool) -> bool:
    text = path.read_text(encoding='utf-8')
    m = FRONTMATTER_RE.match(text)
    if not m:
        return False
    fm = m.group(1)
    body = text[m.end():]

    parent = parts[0]
    child = parts[1] if len(parts) > 1 else None

    cats = [translate_parent(parent, en=en)]
    tags = [translate_child(child, en=en)] if child else []

    fm = CAT_LINE_RE.sub('', fm)
    fm = TAG_LINE_RE.sub('', fm)
    fm = fm.rstrip() + '\n'

    fm += f'categories: {yaml_list(cats)}\n'
    if tags:
        fm += f'tags: {yaml_list(tags)}\n'

    new_text = f'---\n{fm}---\n{body}'
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def find_post(content_dir: Path, post_id: str) -> Path | None:
    for p in content_dir.glob(f'{post_id}-*.md'):
        return p
    return None


def main() -> None:
    cats: dict[str, list[str]] = json.loads(CATEGORIES_FILE.read_text(encoding='utf-8'))
    en_updated = ko_updated = en_missing = ko_missing = 0
    for post_id, parts in cats.items():
        if not parts:
            continue
        en_path = find_post(CONTENT_EN, post_id)
        ko_path = find_post(CONTENT_KO, post_id)
        if en_path:
            if update_post(en_path, post_id, parts, en=True):
                en_updated += 1
        else:
            en_missing += 1
        if ko_path:
            if update_post(ko_path, post_id, parts, en=False):
                ko_updated += 1
        else:
            ko_missing += 1

    print(f'en updated: {en_updated} (missing: {en_missing})')
    print(f'ko updated: {ko_updated} (missing: {ko_missing})')


if __name__ == '__main__':
    main()
