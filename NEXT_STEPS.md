# Next steps

Run these once translation finishes. Each step is idempotent.

## 1. Install Hugo (one-time, local)

```powershell
winget install Hugo.Hugo.Extended
```

Verify:

```powershell
hugo version
```

## 2. Verify translation completeness

```powershell
cd D:\PARA\Project\memoryhub-blog
python scripts\verify_translation.py
```

Re-run translation for any `missing_en` files by re-running:

```powershell
python scripts\plan_translation_batches.py
```

Then ask Claude Code to spawn subagents for the new (smaller) batches.

## 3. Local preview

```powershell
cd D:\PARA\Project\memoryhub-blog
hugo server -D
```

- English (default): http://localhost:1313/
- Korean: http://localhost:1313/ko/

Verify:
- [ ] Language switcher in top-right works
- [ ] Same post URL switches between en/ko (e.g., /posts/<slug>/ ↔ /ko/posts/<slug>/)
- [ ] Images render
- [ ] Tables render
- [ ] Code blocks have copy buttons
- [ ] Search works (`/search/`)
- [ ] Archives works (`/archives/`)

## 4. Push to GitHub

```powershell
cd D:\PARA\Project\memoryhub-blog
git add -A
git commit -m "feat: initial migration from tistory (628 posts, en+ko)"
gh repo create cskwork.github.io --public --source=. --remote=origin --push
```

If you don't use `gh`, create the repo manually on GitHub first
(name MUST be `cskwork.github.io`), then:

```powershell
git remote add origin https://github.com/cskwork/cskwork.github.io.git
git branch -M main
git push -u origin main
```

## 5. Enable GitHub Pages

GitHub repo → Settings → Pages → Build and deployment → Source: **GitHub Actions**.

The workflow at `.github/workflows/deploy.yml` will run on every push to `main`.

Live URL: https://cskwork.github.io/

## 6. Add a new language later

1. Create `content/<lang>/posts/` and put translated `.md` files there
2. Add a `[languages.<lang>]` block in `hugo.toml` mirroring `[languages.ko]`
3. Add `_index.md`, `archives.md`, `search.md` under `content/<lang>/`
4. Commit and push — language switcher picks it up automatically.

## Troubleshooting

- **Image filenames with spaces** (e.g. `ChatGPT Image ...png`): Hugo handles
  via URL encoding. If a specific image fails, rename the source file under
  `static/images/<slug>/` and update the markdown reference.
- **Hugo build fails on a malformed table**: search the offending markdown
  file and fix the `|` alignment.
- **Translation re-run**: `verify_translation.py` finds gaps. Delete a bad
  `content/en/posts/<slug>.md` to force re-translation.
