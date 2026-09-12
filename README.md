# Olympiad Practice

A mobile-friendly, interactive Olympiad practice site for a Class 2
student — one subject per folder, each self-contained with its own
markdown worksheets and generated web app, all sharing the same quiz
engine and visual design.

**Live site:** deployed via GitHub Pages from `main` — see `hub/`
below for the landing page and each subject's `web/README.md` for its
own local-preview instructions.

## Subjects

| Folder | Exam | Units | Path on deployed site |
|---|---|---|---|
| `Maths/` | SOF NOF | 21 | `/maths/` |
| `ICSO/` | SOF ICSO (computer science; formerly "NCO") | 7 | `/icso/` |
| `English/` | SOF IEO | 14 | `/english/` |
| `Science/` | SOF NSO | 5 | `/science/` |
| `GK/` | SOF IGKO | 11 | `/gk/` |

Each subject folder has its own `README.md` with syllabus/content
details, and `web/README.md` with the technical workflow.

## How each subject is structured

```
<Subject>/
├── <exam-prefix>-practise/    # Source worksheets — one .md file per unit
│   └── unit-*.md
├── web/
│   ├── build/generate.py      # Parses the .md files into JSON + HTML
│   ├── index.html             # Home page (generated — don't hand-edit)
│   ├── unit-*.html            # Unit pages (generated — don't hand-edit)
│   ├── assets/
│   │   ├── style.css          # Shared design system across all 5 subjects
│   │   └── app.js             # Shared quiz engine across all 5 subjects
│   └── data/
│       └── unit-*.json        # Generated question data
└── README.md
```

**The markdown files are the only thing you should hand-edit.** Every
`web/` folder — data, HTML, everything — is generated output. After
editing a worksheet, regenerate that subject's site:
```bash
python3 <Subject>/web/build/generate.py
```

`assets/style.css` is identical byte-for-byte across all 5 subjects.
`assets/app.js` is identical except for one line — `const SUBJECT_ID =
"..."` near the top — which must be unique per subject. All 5 sites
share one origin on GitHub Pages (`.../maths/`, `.../science/`, etc.),
and `localStorage` is scoped by **origin, not path**, so without
`SUBJECT_ID` namespacing the keys, two subjects' "unit 01" collide in
storage and a first-time visitor to one subject can see another
subject's answers pre-filled. If you improve one subject's copy of
either file, copy it to the other four to keep them in sync (re-setting
`SUBJECT_ID` in `app.js` after copying) — there's no central
symlink/package for it.

## The hub

`hub/index.html` is a small static landing page (no build step) that
links to each subject's `index.html`. It's what visitors see at the
site root.

## Hosting on GitHub Pages

`.github/workflows/pages.yml` assembles `hub/` plus all 5 subjects'
`web/` folders into one deployment whenever any of them change on
`main`:
```
site root  → hub/index.html
/maths/    → Maths/web/
/icso/     → ICSO/web/
/english/  → English/web/
/science/  → Science/web/
/gk/       → GK/web/
```
One-time setup once this repo is pushed to GitHub: repo **Settings →
Pages → Source** → **GitHub Actions**.

## Adding a new subject

1. Create `<Subject>/<prefix>-practise/unit-01-....md` following the
   same format as an existing subject (see any `web/README.md` for the
   exact parser expectations: `**Qn.**`, four `(A)`–`(D)` lines, an
   `## ✅ Answer Key` table).
2. Copy an existing `web/build/generate.py`, `assets/app.js`, and
   `assets/style.css` into `<Subject>/web/`, and adjust the
   title/footer text and home-page grouping in `generate.py` for the
   new subject.
3. Run `python3 <Subject>/web/build/generate.py`.
4. Add a card for it in `hub/index.html`.
5. Add `<Subject>/web/**` to the `paths:` trigger in
   `.github/workflows/pages.yml`, and a `cp -r`/`rsync` line for it in
   the assemble step.

---

*Made with care for a Class 2 Olympian 🌟*
