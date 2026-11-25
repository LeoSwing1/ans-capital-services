# ANS Capital Services Private Limited — website

Production-ready static website. 25 pages, bilingual (English / हिंदी), no build step,
no server required. Upload the folder and it runs.

**Tagline:** Building Your Financial Future
**Phone:** +91 93196 67592 · **Email:** anscapitalservicespvtltd@gmail.com

---

## What is in here

| Path | What it is |
|---|---|
| `index.html` | Homepage — hero, approach, 4 service cards, process, EMI calculator, FAQs |
| `services.html` | Our Services — 4 core products + additional services |
| `personal-loan.html` `home-loan.html` `car-loan.html` `business-loan.html` | The four core product pages |
| `loan-against-property.html` `other-loans.html` | Additional services, marked subject to availability |
| `how-it-works.html` | The six-step process |
| `emi-calculator.html` | Full EMI calculator — years/months toggle, principal-vs-interest donut |
| `faqs.html` | FAQs grouped into six themes |
| `blog.html` + 6 articles | Knowledge Centre |
| `about.html` `contact.html` | Company and contact |
| `privacy-policy.html` `terms-conditions.html` `disclaimer.html` `cookie-policy.html` `enquiry-consent.html` | Legal |
| `assets/` | CSS, JS, logo, favicon, OG image |
| `sitemap.xml` `robots.txt` `site.webmanifest` | Technical SEO |
| `integrations/chat-endpoint.example.js` | Optional LLM endpoint for the chatbot |
| `build_*.py` `gen_*.py` `data_products.py` | The generators that produced the HTML |

### Regenerating the HTML
The pages are generated from Python so copy stays consistent across 25 files.
Edit the content in `data_products.py` / `build_*.py`, then:

```bash
python3 build_home.py && python3 -c "import data_products,build_products;[build_products.product_page(p) for p in data_products.P]"
python3 build_pages.py && python3 build_pages2.py && python3 build_blog.py
python3 build_rest.py && python3 build_contact.py && python3 build_legal.py && python3 build_meta.py
```

You can also just edit the `.html` files directly — nothing depends on the generators at runtime.

---

## Deploy

Static hosting. Any of these work with zero configuration:

- **Hostinger / cPanel** — upload the folder contents into `public_html`
- **Netlify** — drag the folder onto the dashboard
- **Vercel** — `vercel deploy` from inside the folder
- **GitHub Pages** — push and enable Pages

Then point your domain at it and enable HTTPS.

---

## Before going live — 7 things to replace

See `docs/SETUP.md` for the full checklist. In short:

1. `https://anscapitalservices.com` → your real domain (canonical tags, sitemap, robots)
2. Google Search Console verification token
3. GA4 Measurement ID
4. Google Tag Manager container ID
5. Meta Pixel ID
6. Google Business Profile review link + map embed
7. Office address and confirmed business hours

---

## Documentation

- `docs/SETUP.md` — placeholders, Google setup, GMB, analytics events
- `docs/DEPLOYMENT.md` — hosting, domain, HTTPS, performance
- `docs/INTEGRATIONS.md` — WhatsApp, chatbot, optional LLM endpoint, social
- `docs/CONTENT-POLICY.md` — the claims rules this site follows, and why
