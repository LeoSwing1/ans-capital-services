# -*- coding: utf-8 -*-
import datetime, re, os
from gen_core import SITE, BRAND, SHORT, PHONE_D

PAGES = [
 ("index.html","1.0","weekly"),
 ("services.html","0.9","monthly"),
 ("personal-loan.html","0.9","monthly"),("home-loan.html","0.9","monthly"),
 ("car-loan.html","0.9","monthly"),("business-loan.html","0.9","monthly"),
 ("loan-against-property.html","0.8","monthly"),("other-loans.html","0.8","monthly"),
 ("how-it-works.html","0.8","monthly"),("emi-calculator.html","0.8","monthly"),
 ("faqs.html","0.8","monthly"),("about.html","0.7","yearly"),("contact.html","0.8","yearly"),
 ("blog.html","0.7","weekly"),
 ("understanding-emi.html","0.6","monthly"),("credit-score-basics.html","0.6","monthly"),
 ("home-loan-guide.html","0.6","monthly"),("business-loan-documents.html","0.6","monthly"),
 ("car-loan-mistakes.html","0.6","monthly"),("documents-checklist.html","0.6","monthly"),
 ("privacy-policy.html","0.3","yearly"),("terms-conditions.html","0.3","yearly"),
 ("disclaimer.html","0.3","yearly"),("cookie-policy.html","0.3","yearly"),
 ("enquiry-consent.html","0.3","yearly"),
]
today = datetime.date.today().isoformat()

def loc(p):
    return SITE + '/' if p == 'index.html' else SITE + '/' + p

urls = "".join(f"""
  <url>
    <loc>{loc(p)}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{cf}</changefreq>
    <priority>{pr}</priority>
    <xhtml:link rel="alternate" hreflang="en-in" href="{loc(p)}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{loc(p)}"/>
  </url>""" for p, pr, cf in PAGES)

open("sitemap.xml","w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}
</urlset>
""")

open("robots.txt","w").write(f"""# robots.txt — {BRAND}
User-agent: *
Allow: /
Disallow: /assets/js/
Crawl-delay: 1

# AI / LLM crawlers — allowed, so the business is discoverable in AI answers
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
""")

open("site.webmanifest","w").write(f"""{{
  "name": "{BRAND}",
  "short_name": "ANS Capital",
  "description": "Personal, Home, Car and Business loans arranged from 265+ banks and NBFCs. Channel Partner of Ruloans.",
  "start_url": "/index.html",
  "scope": "/",
  "display": "standalone",
  "background_color": "#061527",
  "theme_color": "#012C59",
  "lang": "en-IN",
  "categories": ["finance", "business"],
  "icons": [
    {{ "src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any" }},
    {{ "src": "assets/img/logo.jpg", "sizes": "1080x1080", "type": "image/jpeg", "purpose": "any maskable" }}
  ],
  "shortcuts": [
    {{ "name": "EMI Calculator", "url": "/emi-calculator.html" }},
    {{ "name": "Contact", "url": "/contact.html" }}
  ]
}}
""")

# favicon.svg — the mark, extracted from logo.js
js = open("assets/js/logo.js").read()
body = re.findall(r"'(<(?:path|g|circle|rect)[^']*?)'", js)
