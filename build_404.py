# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

BODY = f"""
<section class="sec" style="padding-top:calc(var(--nav-h) + 6rem)">
  {deco(("ring","tr",420,.05),("dots","bl",200,.045))}
  <div class="wrap" style="text-align:center;max-width:46rem">
    <span class="eyebrow c">404</span>
    <h1 style="margin-top:1rem" data-hi="यह पेज नहीं मिला">This page isn&rsquo;t here</h1>
    <p class="lead" style="margin:1.4rem auto 0;max-width:40ch"
       data-hi="लिंक पुराना हो सकता है या पता बदल गया होगा। नीचे से अपना लोन चुनिए या हमें कॉल कीजिए।">
      The link may be out of date, or the address may have changed. Pick your loan below,
      or call us and we will point you to the right page.
    </p>
    <div class="btn-row" style="margin-top:2.2rem;justify-content:center">
      <a class="btn btn-gold" href="index.html">Back to the homepage</a>
      <a class="tlink" href="tel:+{PHONE}" data-ev="call_404">{PHONE_D}</a>
    </div>
    <div class="strip-grid" style="margin-top:3.4rem;text-align:left">
      <a class="strip-c" href="personal-loan.html"><span class="sc-k">01</span><b>Personal Loans</b><i>No collateral</i></a>
      <a class="strip-c" href="home-loan.html"><span class="sc-k">02</span><b>Home Loans</b><i>Purchase &middot; transfer</i></a>
      <a class="strip-c" href="car-loan.html"><span class="sc-k">03</span><b>Car Loans</b><i>New &middot; pre-owned</i></a>
      <a class="strip-c" href="business-loan.html"><span class="sc-k">04</span><b>Business Loans</b><i>Working capital</i></a>
    </div>
  </div>
</section>
"""

html = page(
    path="404.html",
    title=f"Page not found — {BRAND}",
    desc="The page you were looking for isn't here. Find personal, home, car and business loan help, or call ANS Capital Services.",
    body=BODY,
)
# a 404 must never be indexed, but its links should still be followed
html = html.replace(
    '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">',
    '<meta name="robots" content="noindex, follow">')
open("404.html", "w", encoding="utf-8").write(html)
print("404.html")
