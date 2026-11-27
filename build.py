# -*- coding: utf-8 -*-
"""Single entry point. Run `python3 build.py` after any change.

Order matters: the minified assets must exist before the pages that link to
them are written, and the sitemap is generated from the finished page list.
"""
import subprocess, sys, glob

STEPS = [
    ("assets   ", "build_assets.py"),
    ("home     ", "build_home.py"),
    ("products ", "build_products.py"),
    ("pages    ", "build_pages.py"),
    ("pages 2  ", "build_pages2.py"),
    ("rest     ", "build_rest.py"),
    ("blog     ", "build_blog.py"),
    ("legal    ", "build_legal.py"),
    ("contact  ", "build_contact.py"),
    ("404      ", "build_404.py"),
    ("sitemap  ", "build_meta.py"),
]

for label, script in STEPS:
    r = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if r.returncode:
        print(f"✗ {label} {script}\n{r.stdout[-800:]}{r.stderr[-800:]}")
        sys.exit(1)
    print(f"✓ {label} {script}")

print(f"\n{len(glob.glob('*.html'))} pages built")

# ── remind whoever runs this what is still a placeholder ──────────────────
import re as _re
_src = open("gen_core.py", encoding="utf-8").read()
_tokens = {
    "GTM container":        _re.search(r'GTM\s*=\s*"([^"]*)"', _src),
    "GA4 measurement ID":   _re.search(r'GA4\s*=\s*"([^"]*)"', _src),
    "Meta Pixel ID":        _re.search(r'PIXEL\s*=\s*"([^"]*)"', _src),
    "Search Console":       _re.search(r'GSC\s*=\s*"([^"]*)"', _src),
    "live domain":          _re.search(r'SITE\s*=\s*"([^"]*)"', _src),
}
_todo = [k for k, m in _tokens.items()
         if m and (not m.group(1) or _re.search(r"X{4,}|REPLACE|example\.", m.group(1)))]
_rev = _re.search(r'"review_url":\s*"([^"]*)"', open("gen_core.py", encoding="utf-8").read())
if _rev and _rev.group(1).startswith("REPLACE"):
    _todo.append("Google review link")
if _todo:
    print("\n⚠  still placeholders — analytics and verification stay switched off until these are set:")
    for t in _todo:
        print(f"     · {t}")
    print("   (see docs/SETUP.md; the tag loader skips placeholder IDs on purpose,")
    print("    so no failed requests reach the visitor's browser)")
