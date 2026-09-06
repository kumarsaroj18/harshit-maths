#!/usr/bin/env python3
"""
Parses the 21 NOF Maths practice markdown files (../../nof-maths-practise/*.md)
into per-unit JSON data files (../data/unit-XX.json) plus a manifest
(../data/manifest.json), and generates the 21 thin HTML shell pages
(../unit-XX-*.html) plus the home page (../index.html) from templates.

Re-run this any time a markdown worksheet file changes:
    python3 web/build/generate.py
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MD_DIR = REPO_ROOT / "nof-maths-practise"
WEB_DIR = REPO_ROOT / "web"
DATA_DIR = WEB_DIR / "data"

Q_MARKER_RE = re.compile(r"(?=\*\*Q\d+\.\*\*)")
Q_NUM_RE = re.compile(r"^\*\*Q(\d+)\.\*\*\s*")
OPTION_LINE_RE = re.compile(r"^\(([ABCD])\)\s*(.*)$")
ANSWER_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*\(([A-D])\)[^|]*\|\s*(.*?)\s*\|$"
)
H1_RE = re.compile(r"^#\s+(\S+)\s+Unit\s+(\d+)\s+—\s+(.+)$")
PARENT_NOTE_RE = re.compile(r"^>\s*\*\*Parent's Note:\*\*\s*(.+)$")


def slice_between(text, start_pat, end_pat):
    start_m = re.search(start_pat, text, re.MULTILINE)
    if not start_m:
        return ""
    body = text[start_m.end():]
    end_m = re.search(end_pat, body, re.MULTILINE)
    if end_m:
        body = body[:end_m.start()]
    return body.strip("\n")


def parse_learn_bullets(text):
    section = slice_between(
        text,
        r"^## 🎯 What You Will Learn\s*$",
        r"^---\s*$",
    )
    bullets = [
        line[2:].strip()
        for line in section.splitlines()
        if line.strip().startswith("- ")
    ]
    return bullets


def parse_learn_it_first(text):
    return slice_between(
        text,
        r"^## 💡 Learn It First\s*$",
        r"^## Section A",
    )


def find_options_block(lines):
    """Options now span 4 consecutive lines: (A).. (B).. (C).. (D)..
    Returns (start_index, end_index_exclusive) or (-1, -1)."""
    expected = ["A", "B", "C", "D"]
    for i in range(len(lines) - 3):
        matches = [OPTION_LINE_RE.match(lines[i + j].strip()) for j in range(4)]
        if all(matches) and [m.group(1) for m in matches] == expected:
            return i, i + 4
    return -1, -1


def parse_questions_in_section(raw_section):
    """Returns (leading_context_markdown, [question dicts])."""
    chunks = Q_MARKER_RE.split(raw_section)
    leading = chunks[0].strip("\n ")
    questions = []
    for chunk in chunks[1:]:
        m = Q_NUM_RE.match(chunk)
        if not m:
            continue
        qnum = int(m.group(1))
        rest = chunk[m.end():]
        lines = rest.split("\n")
        start, end = find_options_block(lines)
        if start == -1:
            raise ValueError(f"No 4-line options block found for Q{qnum}")
        content_md = "\n".join(lines[:start]).strip("\n ")
        options = {}
        for j in range(start, end):
            om = OPTION_LINE_RE.match(lines[j].strip())
            options[om.group(1)] = om.group(2)
        trailing_context = "\n".join(lines[end:]).strip("\n ")
        questions.append({
            "num": qnum,
            "content": content_md,
            "options": options,
            "trailingContext": trailing_context,
        })
    return leading, questions


def parse_answer_key(text):
    section = slice_between(
        text,
        r"^## ✅ Answer Key\s*$",
        r"^---\s*$",
    )
    answers = {}
    for line in section.splitlines():
        m = ANSWER_ROW_RE.match(line.strip())
        if m:
            num = int(m.group(1))
            answers[num] = {"correct": m.group(2), "why": m.group(3)}
    return answers


def parse_unit(md_path):
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    h1_match = None
    for line in lines[:3]:
        h1_match = H1_RE.match(line.strip())
        if h1_match:
            break
    if not h1_match:
        raise ValueError(f"Could not parse H1 title in {md_path}")
    emoji, unit_num, title = h1_match.groups()
    unit_num = int(unit_num)

    parent_note = ""
    for line in lines[:10]:
        pm = PARENT_NOTE_RE.match(line.strip())
        if pm:
            parent_note = pm.group(1)
            break

    learn_bullets = parse_learn_bullets(text)
    learn_it_first = parse_learn_it_first(text)

    section_a_raw = slice_between(
        text, r"^## Section A.*$", r"^## Section B"
    )
    section_b_raw = slice_between(
        text, r"^## Section B.*$", r"^## Section C"
    )
    section_c_raw = slice_between(
        text, r"^## Section C.*$", r"^## ✅ Answer Key"
    )

    answers = parse_answer_key(text)

    sections = []
    for name, raw, total in [
        ("Warm Up", section_a_raw, 10),
        ("Olympiad Practice", section_b_raw, 15),
        ("Achiever's Corner", section_c_raw, 5),
    ]:
        leading, questions = parse_questions_in_section(raw)
        if len(questions) != total:
            raise ValueError(
                f"{md_path.name} section '{name}' expected {total} "
                f"questions, found {len(questions)}"
            )
        for q in questions:
            if q["num"] not in answers:
                raise ValueError(
                    f"{md_path.name} Q{q['num']} missing from answer key"
                )
            q["correct"] = answers[q["num"]]["correct"]
            q["why"] = answers[q["num"]]["why"]
            if q["correct"] not in q["options"]:
                raise ValueError(
                    f"{md_path.name} Q{q['num']} correct letter "
                    f"{q['correct']} not in options"
                )
        sections.append({
            "name": name,
            "leadingContext": leading,
            "questions": questions,
        })

    slug = md_path.stem  # e.g. "unit-01-patterns"

    return {
        "id": f"{unit_num:02d}",
        "slug": slug,
        "num": unit_num,
        "title": title.strip(),
        "emoji": emoji,
        "parentNote": parent_note,
        "learnBullets": learn_bullets,
        "learnItFirst": learn_it_first,
        "sections": sections,
        "totalQuestions": sum(len(s["questions"]) for s in sections),
    }


PALETTE = [
    "#6c5ce7", "#e17055", "#00b894", "#0984e3", "#fdcb6e",
    "#e84393", "#00cec9", "#d63031", "#6c9a3f", "#a29bfe",
]


def accent_for(unit_num):
    return PALETTE[(unit_num - 1) % len(PALETTE)]


HEAD_COMMON = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
"""


def unit_page_html(unit_info):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}  <title>Unit {unit_info['num']} — {unit_info['title']} | NOF Maths Practice</title>
</head>
<body>
  <div class="topbar">
    <a class="back" href="index.html">← Units</a>
    <span class="title" id="topbar-title">{unit_info['emoji']} {unit_info['title']}</span>
  </div>
  <div class="wrap">
    <div class="callout" id="parent-note"></div>
    <div class="learn-list" id="learn-list"></div>
    <div class="lesson-box" id="learn-it-first"></div>
    <div id="sections"></div>
    <div class="overall-banner" id="overall-banner"></div>
    <div class="unit-footer">
      <button class="submit-btn" id="submit-btn">✅ Submit Answers</button>
      <button class="reset-btn" id="reset-btn">🔄 Reset my answers for this unit</button>
    </div>
  </div>
  <footer class="site-footer">NOF Maths Olympiad Practice &middot; Unit {unit_info['num']} of 21</footer>

  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="assets/app.js"></script>
  <script>initUnit("{unit_info['id']}");</script>
</body>
</html>
"""


def unit_card_html(unit_info):
    color = accent_for(unit_info["num"])
    return f"""      <a class="unit-card" href="{unit_info['slug']}.html" data-unit-id="{unit_info['id']}" style="--card-accent: {color}">
        <span class="num">Unit {unit_info['num']}</span>
        <span class="emoji">{unit_info['emoji']}</span>
        <span class="name">{unit_info['title']}</span>
        <span class="badge none"></span>
      </a>
"""


def index_html(manifest):
    reasoning = [u for u in manifest if u["num"] <= 9]
    maths = [u for u in manifest if u["num"] >= 10]
    reasoning_cards = "".join(unit_card_html(u) for u in reasoning)
    maths_cards = "".join(unit_card_html(u) for u in maths)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}  <title>NOF Maths Olympiad Practice</title>
</head>
<body>
  <div class="topbar">
    <span class="title">🧮 NOF Maths Practice</span>
  </div>
  <div class="wrap">
    <div class="hero">
      <h1>🧮 NOF Maths Olympiad Practice</h1>
      <p>Tap a unit to start practicing — your progress is saved on this phone!</p>
    </div>

    <div class="group-heading">🧠 Reasoning Skills</div>
    <div class="grid">
{reasoning_cards}    </div>

    <div class="group-heading">🔢 Maths Skills</div>
    <div class="grid">
{maths_cards}    </div>
  </div>
  <footer class="site-footer">Made with care for a Class 2 mathematician 🌟</footer>

  <script src="assets/app.js"></script>
  <script>initHome();</script>
</body>
</html>
"""


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    md_files = sorted(MD_DIR.glob("unit-*.md"))
    if not md_files:
        raise SystemExit(f"No unit-*.md files found in {MD_DIR}")

    manifest = []
    for md_path in md_files:
        unit = parse_unit(md_path)
        out_path = DATA_DIR / f"unit-{unit['id']}.json"
        out_path.write_text(
            json.dumps(unit, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        manifest.append({
            "id": unit["id"],
            "slug": unit["slug"],
            "num": unit["num"],
            "title": unit["title"],
            "emoji": unit["emoji"],
            "totalQuestions": unit["totalQuestions"],
        })
        print(f"  parsed {md_path.name} -> {out_path.relative_to(REPO_ROOT)} "
              f"({unit['totalQuestions']} questions)")

    manifest.sort(key=lambda u: u["num"])
    (DATA_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nWrote manifest with {len(manifest)} units to "
          f"{(DATA_DIR / 'manifest.json').relative_to(REPO_ROOT)}")

    for unit_info in manifest:
        page_path = WEB_DIR / f"{unit_info['slug']}.html"
        page_path.write_text(unit_page_html(unit_info), encoding="utf-8")
    print(f"Wrote {len(manifest)} unit pages to {WEB_DIR.relative_to(REPO_ROOT)}/")

    (WEB_DIR / "index.html").write_text(index_html(manifest), encoding="utf-8")
    print(f"Wrote {WEB_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
