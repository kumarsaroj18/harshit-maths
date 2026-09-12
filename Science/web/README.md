# SOF NSO Practice — Web App

A mobile-friendly, interactive quiz version of the 5 worksheets in
`../sof-nso-practise/`. Tap an answer, get instant right/wrong
feedback with the explanation, and progress is remembered on the
phone/browser via `localStorage` (no server, no account).

## Preview it locally

Browsers block `fetch()` of local JSON files opened directly from
disk, so serve the folder over HTTP instead of double-clicking
`index.html`:

```bash
cd Science/web
python3 -m http.server 8000
# then open http://localhost:8000/index.html
```

## If you edit a worksheet .md file

The quiz content is generated from the markdown files in
`../sof-nso-practise/`. After editing one, regenerate the JSON data
and HTML pages:

```bash
python3 Science/web/build/generate.py
```

This re-parses all 5 files and rewrites `web/data/*.json` and every
`web/unit-*.html` + `web/index.html` (all inside `Science/web/`). It
will raise an error if a file doesn't have exactly 30 questions total
or a question's answer key entry is missing, so a malformed edit
fails loudly instead of silently breaking a page.

**Keep the question format intact** when editing — the parser expects:
- `**Qn.** <question text>` (optionally followed by a fenced code block)
- then exactly 4 lines: `(A) ...` / `(B) ...` / `(C) ...` / `(D) ...`
- and a matching `| n | (Letter) ... | why text |` row in the `## ✅ Answer Key` table

## Hosting on GitHub Pages

This folder is served at the `/science/` path as part of the combined
Olympiad site — see the repo root `README` and
`.github/workflows/pages.yml` for how the full multi-subject
deployment works.

No build step, no framework, no server required — it's static HTML/CSS/JS end to end.
