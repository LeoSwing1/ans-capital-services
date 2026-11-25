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
