# -*- coding: utf-8 -*-
"""Minify CSS and JS into the .min.* files the pages actually load.
Run this after any edit to assets/css/style.css or assets/js/*.js."""
import os, subprocess, sys

NPX = os.path.expanduser("/home/claude/node_modules/.bin")
JS = ["logo", "preloader", "shader", "chatbot", "app", "ux", "nav"]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(cmd[0] + ": " + r.stderr[:400])
    return r

total_before = total_after = 0
# build_purge.py writes style.purged.css; use it when it is there
SRC = "assets/css/style.purged.css" if os.path.exists("assets/css/style.purged.css") \
      else "assets/css/style.css"
run([NPX + "/cleancss", "-O2", "--format", "keep-breaks:false",
     "-o", "assets/css/style.min.css", SRC])
b = os.path.getsize("assets/css/style.css"); a = os.path.getsize("assets/css/style.min.css")
total_before += b; total_after += a
print(f"  style.css      {b//1024:>4} KB -> {a//1024:>4} KB")

for name in JS:
    src, dst = f"assets/js/{name}.js", f"assets/js/{name}.min.js"
    # ecma 2018 keeps modern syntax instead of down-levelling it, which is
    # what Lighthouse flags as "legacy JavaScript"
    run([NPX + "/terser", src, "-c", "passes=2,ecma=2018", "-m",
         "--ecma", "2018", "--comments", "false", "-o", dst])
    b = os.path.getsize(src); a = os.path.getsize(dst)
    total_before += b; total_after += a
    print(f"  {name+'.js':<14} {b//1024:>4} KB -> {a//1024:>4} KB")

print(f"  {'TOTAL':<14} {total_before//1024:>4} KB -> {total_after//1024:>4} KB "
      f"({100 - total_after*100//total_before}% smaller)")
