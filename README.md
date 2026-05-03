# Memory Hub Blog

Migration of [memoryhub.tistory.com](https://memoryhub.tistory.com/) to GitHub Pages
via Hugo + PaperMod, with English as the default language and Korean original
preserved at `/ko/`.

## Stack

- **Static site generator:** Hugo (extended)
- **Theme:** PaperMod (git submodule)
- **Languages:** English (default) at `/`, Korean at `/ko/`. Add languages by
  creating `content/<lang>/posts/` plus a `[languages.<lang>]` block in
  `hugo.toml`.
- **Hosting:** GitHub Pages at `cskwork.github.io`
- **CI:** GitHub Actions builds on every push to `main`.

## Local development

```powershell
# Install Hugo (one-time)
winget install Hugo.Hugo.Extended

# Clone PaperMod theme
git submodule update --init --recursive

# Run dev server
hugo server -D
```

Open <http://localhost:1313/> for English, <http://localhost:1313/ko/> for Korean.

## Migration scripts

Run order (from repo root):

```powershell
python scripts/parse_backup.py     # 1. HTML -> data/posts.json
python scripts/migrate_images.py   # 2. img/ -> static/images/<slug>/, download remote URLs
python scripts/html_to_md.py       # 3. HTML body -> Markdown, rewrite image refs
python scripts/build_ko.py         # 4. Markdown -> content/ko/posts/<slug>.md
# 5. Translation: spawned via Claude Code subagents (see scripts/translate_README.md)
```

Each script is idempotent and can be re-run safely.

## Source

Tistory backup is read from `D:\PARA\Resource\memoryhub-1-1-article1-1067\memoryhub-1-1`.
