# Translation pipeline (Korean → English)

Strategy: Korean posts in `content/ko/posts/` are translated to English in
`content/en/posts/` using Claude Code subagents in parallel.

## Approach

1. `scripts/plan_translation_batches.py` lists every ko post that does not yet
   have an en counterpart and splits them into N batches.
2. The orchestrator (this Claude Code session) spawns one general-purpose
   subagent per batch, each given the file list and the translation
   instructions below.
3. Each subagent reads ko Markdown, translates body + frontmatter title,
   and writes the en Markdown atomically.

Subagents are stateless; re-running is safe because already-translated files
are skipped.

## Translation instructions (passed verbatim to each subagent)

```
You are translating Korean technical-blog Markdown to natural English. For each
file in the list:

1. Read content/ko/posts/<slug>.md
2. Translate the post into English. Rules:
   - Preserve Markdown structure exactly: headings, lists, tables, blockquotes,
     code fences, image references, links.
   - Do NOT translate code inside fenced code blocks or inline code spans.
   - Translate the frontmatter `title:` field; keep all other frontmatter keys
     (date, slug, original_url, tistory_id, draft) UNCHANGED.
   - Keep the slug identical. Do not invent new slugs.
   - Use natural, idiomatic English that an engineering audience would expect.
     Avoid literal word-for-word translation. Korean honorific/polite endings
     should become neutral English prose.
   - Preserve technical terms (Spring Boot, JPA, RAG, etc.) as-is.
   - Preserve emoji.
3. Write the result to content/en/posts/<slug>.md (same basename).
4. If content/en/posts/<slug>.md already exists, SKIP — do not overwrite.

Report counts at the end: translated / skipped / errors.
```

## Running

```powershell
python scripts/plan_translation_batches.py     # writes data/translation_batches.json
# Then this orchestrator session spawns subagents per batch.
```
