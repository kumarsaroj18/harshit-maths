# SOF IGKO GK Olympiad Practice

Interactive practice app for SOF International General Knowledge Olympiad (IGKO) Class 2 preparation.

## Contents

11 units covering the complete IGKO Class 2 syllabus:

### General Awareness (Units 1-9)
1. **Me and My Family** - Family relationships, home, personal info
2. **Plants and Animals** - Types of animals, plants, animal homes
3. **Our Body and Health** - Body parts, sense organs, healthy habits
4. **India - Our Country** - National symbols, festivals, monuments
5. **The World Around Us** - Community helpers, places, directions
6. **Science and Technology** - Machines, inventions, scientists
7. **Earth and Environment** - Seasons, weather, environmental awareness
8. **Sports and Games** - Indoor/outdoor games, famous players
9. **Transport and Communication** - Vehicles, traffic rules, communication

### Current Affairs & Life Skills (Units 10-11)
10. **Current Affairs** - Recent events, important days, achievements
11. **Life Skills (Do's and Don'ts)** - Good manners, safety rules

## Features

- 330 practice questions (30 per unit)
- 3 difficulty sections per unit: Warm Up, Olympiad Practice, Achiever's Corner
- Progress saving (stored in browser)
- Mobile-friendly design
- Learn-first approach with concepts before questions

## Usage

Open `web/index.html` in a browser to start practicing.

## Editing content

The 11 worksheets in `sof-igko-practise/*.md` are the source of truth — edit
those, then regenerate the web app:
```bash
python3 GK/web/build/generate.py
```
See `web/README.md` for the full workflow and expected markdown format.

## Structure

```
GK/
├── sof-igko-practise/
│   └── unit-*.md             # Source worksheets (edit these)
├── web/
│   ├── build/generate.py     # Markdown -> JSON/HTML build script
│   ├── index.html            # Home page (generated)
│   ├── unit-*.html           # Unit pages (generated)
│   ├── assets/
│   │   ├── style.css        # Styling (shared with Maths/English/Science)
│   │   └── app.js           # Application logic (shared with Maths/English/Science)
│   └── data/
│       ├── manifest.json    # Unit listing (generated)
│       └── unit-*.json      # Question data (generated)
└── README.md
```

---

*Made with care for a Class 2 GK champion 🌟*
