"""Copy local images and download remote ones into static/images/<slug>/.

Reads data/posts.json, for each post:
  - copies post_dir/img/* (if any) into static/images/<slug>/
  - for image_refs starting with http(s) or //, downloads to the same dir
    using a deterministic filename derived from the URL
  - writes data/image_map.json: { post_id: { original_src: new_path } }

The new path uses Hugo's site-absolute form: /images/<slug>/<filename>
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests

from config import DATA_DIR, POSTS_INDEX, STATIC_IMAGES


HTTP_TIMEOUT = 30
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
COMMON_IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}


def _safe_filename_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path)
    name = Path(path).name
    if not name or "." not in name:
        digest = hashlib.sha1(url.encode()).hexdigest()[:12]
        name = f"remote-{digest}.png"
    if Path(name).suffix.lower() not in COMMON_IMG_EXTS:
        digest = hashlib.sha1(url.encode()).hexdigest()[:8]
        name = f"{Path(name).stem or 'remote'}-{digest}.png"
    return name


def _download(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        resp = requests.get(
            url,
            headers={"User-Agent": USER_AGENT, "Referer": "https://www.tistory.com/"},
            timeout=HTTP_TIMEOUT,
            stream=True,
        )
        resp.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("wb") as fh:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    fh.write(chunk)
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"  download failed: {url} ({exc})", file=sys.stderr)
        return False


def main() -> int:
    if not POSTS_INDEX.exists():
        print(f"FATAL: run parse_backup.py first ({POSTS_INDEX} missing)", file=sys.stderr)
        return 2

    records = json.loads(POSTS_INDEX.read_text(encoding="utf-8"))

    image_map: dict[str, dict[str, str]] = {}
    copied = 0
    downloaded = 0
    failed: list[tuple[str, str]] = []

    for rec in records:
        post_id = rec["id"]
        slug = rec["slug"]
        target_dir = STATIC_IMAGES / slug
        per_post_map: dict[str, str] = {}

        if rec.get("img_dir"):
            src_dir = Path(rec["img_dir"])
            if src_dir.exists():
                target_dir.mkdir(parents=True, exist_ok=True)
                for src_file in src_dir.iterdir():
                    if not src_file.is_file():
                        continue
                    dst = target_dir / src_file.name
                    if not dst.exists() or dst.stat().st_size != src_file.stat().st_size:
                        shutil.copy2(src_file, dst)
                        copied += 1

        for src in rec.get("image_refs", []):
            src_clean = src.strip()
            if not src_clean:
                continue
            if src_clean.startswith("./img/") or src_clean.startswith("img/"):
                fname = Path(unquote(src_clean.split("img/", 1)[1])).name
                per_post_map[src] = f"/images/{slug}/{fname}"
                continue
            if src_clean.startswith(("http://", "https://", "//")):
                url = src_clean if not src_clean.startswith("//") else f"https:{src_clean}"
                fname = _safe_filename_from_url(url)
                dst = target_dir / fname
                ok = _download(url, dst)
                if ok:
                    downloaded += 1
                    per_post_map[src] = f"/images/{slug}/{fname}"
                else:
                    failed.append((post_id, url))
                    per_post_map[src] = src
                time.sleep(0.2)
                continue
            per_post_map[src] = src

        if per_post_map:
            image_map[post_id] = per_post_map

    map_path = DATA_DIR / "image_map.json"
    map_path.write_text(json.dumps(image_map, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"copied local files: {copied}")
    print(f"downloaded remote: {downloaded}")
    print(f"failed downloads: {len(failed)}")
    for pid, url in failed[:10]:
        print(f"  - post {pid}: {url}")
    print(f"image_map written: {map_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
