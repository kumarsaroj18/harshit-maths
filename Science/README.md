# SOF NSO Science Olympiad Practice

Interactive practice app for SOF National Science Olympiad (NSO) Class 2 preparation.

## Contents

5 units covering the core NSO Class 2 Science syllabus:

### Life Science (Units 1-4)
1. **Living and Non-Living Things** - Characteristics of living vs non-living, examples
2. **Plants** - Parts of plants, types, needs, uses
3. **Animals** - Domestic/wild, animal homes, food habits, movement
4. **Human Body and Health** - Body parts, sense organs, food groups, hygiene

### Earth & Environment (Unit 5)
5. **Air, Water and Weather** - Properties of air/water, sources, seasons, water cycle

## Exam Pattern (NSO Class 2)

| Section | Questions | Marks/Q | Total |
|---------|-----------|---------|-------|
| Section 1: Logical Reasoning | 5 | 1 | 5 |
| Section 2: Science | 25 | 1 | 25 |
| Section 3: Achievers Section | 5 | 2 | 10 |
| **Total** | **35** | | **40** |

Duration: 1 hour

## Features

- 150 practice questions (30 per unit)
- 3 difficulty sections per unit: Warm Up, Olympiad Practice, Achiever's Corner
- Progress saving (stored in browser)
- Mobile-friendly design
- Learn-first approach with concepts before questions

## Usage

Open `web/index.html` in a browser to start practicing.

For local testing with fetch support:
```bash
cd Science/web
python3 -m http.server 8000
# then open http://localhost:8000/index.html
```

## Editing content

The 5 worksheets in `sof-nso-practise/*.md` are the source of truth — edit
those, then regenerate the web app:
```bash
python3 Science/web/build/generate.py
```
See `web/README.md` for the full workflow and expected markdown format.

## Structure

```
Science/
├── sof-nso-practise/
│   └── unit-*.md             # Source worksheets (edit these)
├── web/
│   ├── build/generate.py     # Markdown -> JSON/HTML build script
│   ├── index.html            # Home page (generated)
│   ├── unit-*.html           # Unit pages (generated)
│   ├── assets/
│   │   ├── style.css         # Styling (shared with Maths/English/GK)
│   │   └── app.js            # Application logic (shared with Maths/English/GK)
│   └── data/
│       └── unit-*.json       # Question data (generated)
└── README.md
```

## Syllabus Source

Based on the official SOF NSO Class 2 syllabus which includes:
- Living and Non-living things
- Plants (parts, types, uses)
- Animals (domestic, wild, habitats, food)
- Human Body (body parts, sense organs, health, hygiene)
- Air and Water (properties, sources, uses)
- Weather and Seasons

---

*Made with care for a Class 2 scientist 🌟*
