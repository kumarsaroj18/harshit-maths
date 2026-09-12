# NOF Maths Practice — Web App

A mobile-friendly, interactive quiz version of the 21 worksheets in
`../nof-maths-practise/`. Tap an answer, get instant right/wrong
feedback with the explanation, and progress is remembered on the
phone/browser via `localStorage` (no server, no account).

## Preview it locally

Browsers block `fetch()` of local JSON files opened directly from
disk, so serve the folder over HTTP instead of double-clicking
`index.html`:

```bash
cd Maths/web
python3 -m http.server 8000
# then open http://localhost:8000/index.html
```

## If you edit a worksheet .md file

The quiz content is generated from the markdown files in
`../nof-maths-practise/`. After editing one, regenerate the JSON data
and HTML pages:

```bash
python3 Maths/web/build/generate.py
```

This re-parses all 21 files and rewrites `web/data/*.json` and every
`web/unit-*.html` + `web/index.html` (all inside `Maths/web/`). It will raise an error if a file
doesn't have exactly 30 questions or a question's answer key entry is
missing, so a malformed edit fails loudly instead of silently breaking
a page.

**Keep the question format intact** when editing — the parser expects:
- `**Qn.** <question text>` (optionally followed by a fenced code block for ASCII-art questions)
- then exactly 4 lines: `(A) ...` / `(B) ...` / `(C) ...` / `(D) ...`
- and a matching `| n | (Letter) ... | why text |` row in the `## ✅ Answer Key` table

## Hosting on GitHub Pages

A workflow at `.github/workflows/pages.yml` (repo root) deploys this
`Maths/web/` folder straight to GitHub Pages whenever it changes on
`main`. One-time setup
once you've pushed this repo to GitHub:

1. Repo **Settings → Pages → Source** → select **GitHub Actions**.
2. Push to `main` (or run the workflow manually from the Actions tab).
3. Your son can open the resulting `https://<you>.github.io/<repo>/` URL on his phone — bookmark it or add it to the home screen for app-like access.

No build step, no framework, no server required — it's static HTML/CSS/JS end to end.
