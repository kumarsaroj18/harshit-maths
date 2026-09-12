# SOF IEO Practice — Web App

A mobile-friendly, interactive quiz version of the 14 worksheets in
`../sof-ieo-practise/`. Tap an answer, get instant right/wrong
feedback with the explanation, and progress is remembered on the
phone/browser via `localStorage` (no server, no account).

## Preview it locally

Browsers block `fetch()` of local JSON files opened directly from
disk, so serve the folder over HTTP instead of double-clicking
`index.html`:

```bash
cd English/web
python3 -m http.server 8000
# then open http://localhost:8000/index.html
```

## If you edit a worksheet .md file

The quiz content is generated from the markdown files in
`../sof-ieo-practise/`. After editing one, regenerate the JSON data
and HTML pages:

```bash
python3 English/web/build/generate.py
```

This re-parses all 14 files and rewrites `web/data/*.json` and every
`web/unit-*.html` + `web/index.html` (all inside `English/web/`). It
will raise an error if a file's three sections don't total 30
questions, or a question's answer key entry is missing, so a
malformed edit fails loudly instead of silently breaking a page.
(Unlike the other subjects, section sizes here aren't fixed at
10/15/5 — Unit 14 "Achievers Section" intentionally uses 10/10/10 with
its own section names; the parser reads whatever three `## Section A/B/C
— Name (Qx–Qy)` headings are present.)

**Keep the question format intact** when editing — the parser expects:
- `**Qn.** <question text>` (optionally followed by a fenced code block or a reading passage as leading/trailing context)
- then exactly 4 lines: `(A) ...` / `(B) ...` / `(C) ...` / `(D) ...`
- and a matching `| n | (Letter) ... | why text |` row in the `## ✅ Answer Key` table

## Hosting on GitHub Pages

This folder is served at the `/english/` path as part of the combined
Olympiad site — see the repo root `README` and
`.github/workflows/pages.yml` for how the full multi-subject
deployment works.

No build step, no framework, no server required — it's static HTML/CSS/JS end to end.
