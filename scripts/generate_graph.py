"""Generate knowledge graph data for the home page.

Walks both content/en/posts and content/ko/posts, parses YAML frontmatter,
and emits two graph JSON files (one per language) containing nodes for
categories, tags, and posts plus edges connecting them. Also emits a
"wiki" payload with the top categories and their newest posts so the home
template can render category cards without duplicating logic in Hugo.

Output:
- static/data/graph.en.json
- static/data/graph.ko.json
- static/data/wiki.en.json
- static/data/wiki.ko.json
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from config import CONTENT_EN, CONTENT_KO, PROJECT_ROOT

OUT_DIR = PROJECT_ROOT / 'static' / 'data'

FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
FIELD_LINE_RE = re.compile(r'^([a-zA-Z_][a-zA-Z_0-9]*):\s*(.*?)\s*$', re.MULTILINE)
COVER_IMAGE_RE = re.compile(r'^\s*image:\s*"([^"]+)"', re.MULTILINE)


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith('[') and value.endswith(']')):
        return []
    inner = value[1:-1]
    items: list[str] = []
    for part in re.findall(r'"((?:[^"\\]|\\.)*)"', inner):
        items.append(part.replace('\\"', '"').replace('\\\\', '\\'))
    return items


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = m.group(1)
    data: dict = {}
    for fm_match in FIELD_LINE_RE.finditer(fm):
        key, raw = fm_match.group(1), fm_match.group(2)
        if key in {'categories', 'tags'}:
            data[key] = parse_list(raw)
        elif raw.startswith('"') and raw.endswith('"'):
            data[key] = raw[1:-1]
        else:
            data[key] = raw
    cover_match = COVER_IMAGE_RE.search(fm)
    if cover_match:
        data['cover_image'] = cover_match.group(1)
    return data


def post_url(slug: str, *, lang: str) -> str:
    prefix = '/memoryhub-blog' if True else ''
    if lang == 'en':
        return f'{prefix}/posts/{slug}/'
    return f'{prefix}/{lang}/posts/{slug}/'


def cover_url(image: str) -> str:
    if not image:
        return ''
    if image.startswith('http'):
        return image
    cleaned = image.lstrip('/')
    return f'/memoryhub-blog/{cleaned}'


def category_url(name: str, *, lang: str) -> str:
    slug = name.lower().replace(' ', '-')
    prefix = '/memoryhub-blog'
    if lang == 'en':
        return f'{prefix}/categories/{slug}/'
    return f'{prefix}/{lang}/categories/{slug}/'


def tag_url(name: str, *, lang: str) -> str:
    slug = name.lower().replace(' ', '-')
    prefix = '/memoryhub-blog'
    if lang == 'en':
        return f'{prefix}/tags/{slug}/'
    return f'{prefix}/{lang}/tags/{slug}/'


def collect(content_dir: Path, lang: str) -> tuple[dict, dict]:
    posts: list[dict] = []
    for path in content_dir.glob('*.md'):
        text = path.read_text(encoding='utf-8')
        fm = parse_frontmatter(text)
        if not fm or fm.get('draft', '').lower() == 'true':
            continue
        title = fm.get('title') or path.stem
        slug = fm.get('slug') or path.stem
        date_str = fm.get('date', '')
        try:
            date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except ValueError:
            date = datetime.min
        posts.append({
            'title': title,
            'slug': slug,
            'url': post_url(slug, lang=lang),
            'date': date.isoformat() if date != datetime.min else '',
            'date_sort': date.timestamp() if date != datetime.min else 0,
            'categories': fm.get('categories', []) or [],
            'tags': fm.get('tags', []) or [],
            'cover': cover_url(fm.get('cover_image', '')),
        })

    posts.sort(key=lambda p: p['date_sort'], reverse=True)

    cat_to_posts: dict[str, list[dict]] = defaultdict(list)
    tag_counts: dict[str, int] = defaultdict(int)
    for post in posts:
        for cat in post['categories']:
            cat_to_posts[cat].append(post)
        for tag in post['tags']:
            tag_counts[tag] += 1

    cat_sorted = sorted(cat_to_posts.items(), key=lambda kv: -len(kv[1]))

    wiki_categories = []
    for cat, cat_posts in cat_sorted:
        wiki_categories.append({
            'name': cat,
            'url': category_url(cat, lang=lang),
            'count': len(cat_posts),
            'recent': [
                {
                    'title': p['title'],
                    'url': p['url'],
                    'date': p['date'][:10] if p['date'] else '',
                    'cover': p['cover'],
                }
                for p in cat_posts[:6]
            ],
        })
    wiki = {
        'categories': wiki_categories,
        'top_tags': [
            {'name': t, 'url': tag_url(t, lang=lang), 'count': c}
            for t, c in sorted(tag_counts.items(), key=lambda kv: -kv[1])[:30]
        ],
        'total_posts': len(posts),
    }

    nodes: list[dict] = []
    edges: list[dict] = []
    seen: set[str] = set()

    def add_node(node_id: str, label: str, group: str, size: int, url: str = '') -> None:
        if node_id in seen:
            return
        seen.add(node_id)
        nodes.append({
            'id': node_id,
            'label': label,
            'group': group,
            'value': size,
            'url': url,
        })

    for cat, cat_posts in cat_sorted:
        add_node(f'cat:{cat}', cat, 'category', len(cat_posts) + 8, category_url(cat, lang=lang))

    top_post_ids = {p['slug'] for p in posts[:120]}
    for post in posts:
        if post['slug'] not in top_post_ids and not post['categories']:
            continue
        add_node(f'post:{post["slug"]}', post['title'], 'post', 2, post['url'])
        for cat in post['categories']:
            edges.append({'from': f'cat:{cat}', 'to': f'post:{post["slug"]}'})
        for tag in post['tags']:
            tag_id = f'tag:{tag}'
            add_node(tag_id, tag, 'tag', tag_counts[tag] + 1, tag_url(tag, lang=lang))
            edges.append({'from': tag_id, 'to': f'post:{post["slug"]}'})

    graph = {'nodes': nodes, 'edges': edges}
    return graph, wiki


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for lang, content_dir in (('en', CONTENT_EN), ('ko', CONTENT_KO)):
        graph, wiki = collect(content_dir, lang)
        (OUT_DIR / f'graph.{lang}.json').write_text(
            json.dumps(graph, ensure_ascii=False), encoding='utf-8'
        )
        (OUT_DIR / f'wiki.{lang}.json').write_text(
            json.dumps(wiki, ensure_ascii=False), encoding='utf-8'
        )
        print(f'{lang}: {len(graph["nodes"])} nodes, {len(graph["edges"])} edges, '
              f'{len(wiki["categories"])} categories')


if __name__ == '__main__':
    main()
