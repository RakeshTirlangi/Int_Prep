"""Build index.html (for GitHub Pages) from the markdown study guide.

Usage:  python3 build.py
Re-run it whenever you edit QualiZeal_Interview_Study_Guide.md.
"""
from pathlib import Path

here = Path(__file__).resolve().parent
md = (here / "QualiZeal_Interview_Study_Guide.md").read_text(encoding="utf-8")
if "</script" in md.lower():
    raise SystemExit("The guide contains '</script', which would break the page. Remove it and re-run.")

template = (here / "site_template.html").read_text(encoding="utf-8")
html = template.replace("<!--GUIDE_MD-->", md)
(here / "index.html").write_text(html, encoding="utf-8")
print(f"Built index.html ({len(html) // 1024} KB)")
