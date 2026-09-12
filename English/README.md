# SOF IEO English Olympiad Practice

Interactive practice app for SOF International English Olympiad (IEO)
Class 2 preparation.

## Contents

14 units:

### Grammar Basics (Units 1-7)
1. **Nouns** — common vs. proper nouns
2. **Pronouns**
3. **Verbs**
4. **Adjectives**
5. **Articles**
6. **Prepositions**
7. **Conjunctions**

### Language & Reading Skills (Units 8-14)
8. **Spellings**
9. **Collocations**
10. **Simple Tenses**
11. **Punctuation**
12. **Reading Comprehension**
13. **Spoken & Written Expression**
14. **Achievers Section** — a mixed mock-exam unit (Mixed Grammar / Error Finding and Correction / Complex Comprehension and Logic), intentionally using a 10/10/10 question split instead of the usual 10/15/5

## Features

- 420 practice questions (30 per unit)
- 3 difficulty sections per unit (10/15/5, except Unit 14 — see above)
- Progress saving (stored in browser)
- Mobile-friendly design
- Learn-first approach with concepts before questions

## Usage

Open `web/index.html` in a browser to start practicing (or visit the
`/english/` path on the deployed site).

## Editing content

The 14 worksheets in `sof-ieo-practise/*.md` are the source of truth —
edit those, then regenerate the web app:
```bash
python3 English/web/build/generate.py
```
See `web/README.md` for the full workflow and expected markdown format.

## Structure

```
English/
├── sof-ieo-practise/
│   └── unit-*.md             # Source worksheets (edit these)
├── web/
│   ├── build/generate.py     # Markdown -> JSON/HTML build script
│   ├── index.html            # Home page (generated)
│   ├── unit-*.html           # Unit pages (generated)
│   ├── assets/                # Styling + app logic (shared across subjects)
│   └── data/                  # Question data (generated)
└── README.md
```

## Accuracy note

This content's exam pattern/marks distribution has not been
independently verified against the official SOF IEO syllabus (unlike
`../ICSO/`, where the current syllabus was confirmed via sofworld.org).
Worth a syllabus check before relying on it for real exam calibration.

---

*Made with care for a Class 2 English learner 🌟*
