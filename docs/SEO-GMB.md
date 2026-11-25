# SEO, Google Business Profile and marketing — what is built, what you do

Everything in "Built into the site" already ships. Everything in "Your steps"
needs an account, a token or a decision only ANS can make.

---

## 1. Built into the site

### Indexing and crawling
- `robots.txt` with the sitemap declared
- `sitemap.xml` — all 26 pages, with `lastmod`, `changefreq`, `priority` and
  `hreflang` alternates. The homepage is listed as the bare domain.
- Canonical on every page. The homepage canonical is `https://domain/`, so the
  root and `/index.html` never compete as two addresses for one page.
- `hreflang` en-IN, hi-IN and x-default
- `404.html` — `noindex, follow`, with links back into the four loan products
- Meta robots: `max-snippet:-1, max-image-preview:large, max-video-preview:-1`

### Structured data (validate at search.google.com/test/rich-results)
| Schema | Where |
|---|---|
| `FinancialService` (organization) | every page |
| `WebSite` + `SearchAction` | every page |
| `BreadcrumbList` | every inner page |
| `FAQPage` | FAQs, product pages |
| `LoanOrCredit` | each product page |
| `HowTo` | how-it-works |
| `BlogPosting` | each article |
| `WebApplication` | EMI calculator |

The organization schema carries opening hours, area served, contact point,
languages, `sameAs` for all four social profiles and `hasMap` to the Google
profile.

**Two things deliberately left out:**
1. `PostalAddress` / `LocalBusiness` — waiting on a verified office address.
   Marked with a comment in `gen_parts.py`; drop the address in and the
   markup is one paste.
2. `aggregateRating` on the organization. Google treats self-serving review
   markup on your own site as a guidelines violation and it can cost you
   rich results across the whole domain. The real rating is shown as plain
   text and linked to the Google profile instead, which is the safe pattern.

### Measurement
- **Consent Mode v2** — defaults set before any Google tag fires, so EEA
  traffic is modelled rather than lost. Call `ansConsent(true)` from whichever
  banner you deploy; the choice is remembered.
- **GTM, GA4 and Meta Pixel** containers in `<head>`, one token each
- **First-touch attribution** — `utm_*`, `gclid` and `fbclid` are captured on
  arrival, kept for the session, attached to the GA4 lead event *and written
  into the WhatsApp enquiry message*, so the team sees the source without
  opening analytics.
- **Conversion events**, named so they import into Google Ads and Meta without
  rework:

| Action | GA4 event | Meta event |
|---|---|---|
| Enquiry submitted | `generate_lead` | `Lead` |
| Phone number tapped | `click_to_call` | `Contact` |
| WhatsApp opened | `whatsapp_click` | `Contact` |
| Google review link | `review_click` | `Lead` |
| Directions opened | `directions_click` | `FindLocation` |
| Google profile opened | `gmb_profile_click` | `ViewContent` |

Plus `emi_calculate`, `emi_attach_to_enquiry`, `lang_switch` and `enquire_click`.

### Google Business Profile
- A GMB card on the homepage and the contact page: rating, hours, phone,
  email, service area, languages
- Every outbound GMB link is UTM-tagged
  (`utm_source=website&utm_medium=referral&utm_campaign=gmb`), so map-pack
  traffic separates cleanly from organic in GA4
- NAP (name, address, phone) wording matches the profile exactly — Google
  cross-checks this

### Performance
- Hero shader: render scale and frame rate chosen per device; stops when the
  hero scrolls away or the tab is hidden
- Every decorative canvas capped at 24–30fps and paused off-screen
- `content-visibility:auto` on below-fold sections with intrinsic sizes
- Fonts preconnected and preloaded, `display=swap`
- All JS deferred; no blocking third-party script in the critical path
- Host configs in `deploy/` — one year immutable cache on `/assets/*`,
  HTML always revalidated, Brotli/gzip, HSTS and the standard security headers

---

## 2. Your steps

### Before launch
1. Point the domain, upload the site, copy the right file out of `deploy/`
   (`_headers` for Netlify/Cloudflare, `vercel.json` for Vercel,
   `.htaccess` for cPanel) into the site root.
2. Replace the tokens listed in `SETUP.md` — domain, GSC, GA4, GTM, Pixel,
   Bing, Meta domain verification, GMB review link, map embed.
3. Verify in **Google Search Console** → submit `sitemap.xml` → request
   indexing on the homepage and the four product pages.
4. Verify in **Bing Webmaster Tools** (import from GSC, it takes a minute).
5. Run the **Rich Results Test** on the homepage, one product page and the
   FAQ page.
6. Run **PageSpeed Insights** on mobile and desktop and keep the report.

### Google Business Profile — the work that actually moves the map pack
1. **Categories.** Primary: *Loan agency*. Secondary: *Mortgage broker*,
   *Financial institution*. The primary category carries most of the ranking
   weight, so do not experiment with it.
2. **Service area.** List the specific cities you serve, not "India".
3. **Services.** Add each product as a service with its own description:
   personal loan, home loan, car loan, business loan, loan against property.
4. **Photos.** Minimum 10 to start — office exterior, interior, team at work,
   logo, cover. Add 2–3 every month; profiles with recent photos get more
   views than static ones.
5. **Posts.** One a week. Rate updates, document checklists, a sanctioned
   case with no personal details. Every post links back with the UTM tags.
6. **Q&A.** Seed the ten questions customers actually ask and answer them
   from the business account.
7. **Reviews.** Send the review link after every sanction, while the customer
   is still pleased. Reply to every review within 48 hours — replies are a
   ranking factor and visible to everyone deciding whether to call you.
8. **Messaging.** Turn it on only if someone will answer within the hour.
   A slow reply time is shown on the profile.

### Citations and NAP
Build listings with exactly the same name, phone and address as the Google
profile: Justdial, IndiaMART, Sulekha, Yellow Pages India, 99acres (property
loans), BankBazaar partner listings, Facebook, LinkedIn, Apple Business
Connect, Bing Places. Inconsistent NAP is the most common reason a local
business does not rank.

### Content plan
The blog already carries five articles. Keep the cadence at two a month and
write for the question, not the keyword:
- "Home loan balance transfer — when it is worth it and when it is not"
- "Documents a salaried applicant needs for a business loan"
- "What a lender sees when they pull your CIBIL report"
- "Loan against property vs top-up loan"
- City pages once you have a verified address — "Personal loan in Meerut" and
  similar only work when the address and the Google profile back them up.

### Paid
- **Google Ads**: start on brand plus high-intent exact match
  ("home loan dsa near me", "personal loan agent Meerut"). Import
  `generate_lead` and `click_to_call` as conversions from GA4.
- **Meta**: the Pixel is already firing `Lead` and `Contact`. Build a
  lookalike off the lead event once there are ~100 leads.
- Keep UTM tags consistent — they already flow into the enquiry message.

### Monthly review
Search Console: impressions, clicks, average position, top queries.
GA4: leads by source, call clicks, WhatsApp clicks.
GMB Insights: searches, direction requests, calls.
If GMB calls are rising but form leads are not, the phone number is doing the
work and the form needs attention — not the other way round.
