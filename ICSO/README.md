# SOF ICSO Olympiad Practice

Interactive practice app for SOF International Computer Science
Olympiad (ICSO) Class 2 preparation. Note: SOF retired the older "NCO"
(National Cyber Olympiad) name — ICSO is the current exam this content
targets, confirmed against the official syllabus at sofworld.org.

## Contents

7 units covering the ICSO Class 1–2 syllabus:

### Logical Reasoning (Unit 1)
1. **Logical Reasoning** — samples all 9 real Section 1 categories (Patterns, Odd One Out, Measuring Units, Geometrical Shapes, Analogy, Ranking Test, Grouping of Figures, Coding-Decoding, Embedded Figures)

### Computer & IT Skills (Units 2-7)
2. **Introduction to Computers** — computer as a "smart machine", starting/shutting down
3. **Parts of a Computer** — input vs. output device classification, the CPU
4. **Uses of Computers** — school, hospital, bank, home, airport, shop
5. **Keyboard and Mouse** — keys, typing, mouse actions
6. **Introduction to MS-Paint** — tools and their uses
7. **IT Gadgets & Developments** — apps, internet, robots, basic online safety

## Exam Pattern (ICSO Class 1–2, current/official)

| Section | Questions | Marks/Q | Total |
|---------|-----------|---------|-------|
| Section 1: Logical Reasoning | 5 | 1 | 5 |
| Section 2: Computer Science | 20 | 1 | 20 |
| Section 3: Information Technology | 5 | 1 | 5 |
| Section 4: Achievers Section | 5 | 2 | 10 |
| **Total** | **35** | | **40** |

Duration: 1 hour. No negative marking. References Windows 11.

File count (1 reasoning : 6 computer/IT) is weighted toward Computer
Science/IT to roughly mirror the real exam's 5:25 marks split, since
Section 1 reasoning already has deep coverage in `../Maths/`.

## Features

- 210 practice questions (30 per unit)
- 3 difficulty sections per unit: Warm Up, Olympiad Practice, Achiever's Corner
- Progress saving (stored in browser)
- Mobile-friendly design
- Learn-first approach with concepts before questions

## Usage

Open `web/index.html` in a browser to start practicing (or visit the
`/icso/` path on the deployed site).

## Editing content

The 7 worksheets in `sof-icso-practise/*.md` are the source of truth —
edit those, then regenerate the web app:
```bash
python3 ICSO/web/build/generate.py
```
See `web/README.md` for the full workflow and expected markdown format.

## Structure

```
ICSO/
├── sof-icso-practise/
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

No verbatim past-paper questions were available from any source
(official SOF or third-party) at the time this was written — content
is built from the confirmed syllabus topics plus general
computer-literacy knowledge, not transcribed from a real paper.

---

*Made with care for a Class 2 cyber olympian 🌟*
