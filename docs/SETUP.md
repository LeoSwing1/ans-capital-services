# Setup checklist

## 1. Placeholders to replace

Find-and-replace across all `.html` files (or edit `gen_core.py` and regenerate).

| Placeholder | Where it appears | What to put |
|---|---|---|
| `https://anscapitalservices.com` | canonical, Open Graph, `sitemap.xml`, `robots.txt` | your live domain, no trailing slash |
| `REPLACE_WITH_GOOGLE_SEARCH_CONSOLE_TOKEN` | `<meta name="google-site-verification">` | Search Console → add property → HTML tag method |
| `G-XXXXXXXXXX` | GA4 snippet | your GA4 Measurement ID |
| `GTM-XXXXXXX` | Tag Manager snippet | your GTM container ID |
| `XXXXXXXXXXXXXXX` | Meta Pixel snippet | your Pixel ID |
| `REPLACE_WITH_BING_TOKEN` | `<meta name="msvalidate.01">` | Bing Webmaster Tools |
| `REPLACE_WITH_META_BUSINESS_TOKEN` | `<meta name="facebook-domain-verification">` | Meta Business Suite → Brand Safety → Domains |
| `REPLACE_WITH_GMB_REVIEW_LINK` | review buttons | Google Business Profile → Ask for reviews → copy link |
| `MAP_EMBED` in `gen_core.py` | Contact + Home maps | GMB → Share → Embed a map → copy the `src` URL |

**If you are not using one of these tools**, delete its `<script>` block from the `<head>`
rather than leaving the placeholder in — an invalid ID produces console errors.

## 2. Business details still to confirm

These are deliberately marked "subject to confirmation" on the site. Replace the wording
once you have confirmed them:

- **Office address.** Not published anywhere, and deliberately left out of the structured data.
  Once confirmed, add a `PostalAddress` block to the JSON-LD in `gen_parts.py` (the exact shape
  is in a comment there) and switch the schema type to `LocalBusiness`. This is what unlocks
  local map rankings, so it is worth doing early.
- **Business hours.** Currently shown as Mon–Sat, 10:00–19:00 with a "subject to confirmation" note.
- **Lender empanelment.** The site says ANS is a Channel Partner of Ruloans, which is what the
  company states on its own Instagram and LinkedIn profiles. If any specific bank or NBFC
  empanelment is to be named on the site, keep the paperwork on file first.

## 3. Google Search Console

1. Add the property, verify with the HTML tag already in the `<head>`
2. Submit `https://yourdomain.com/sitemap.xml`
3. Request indexing for the homepage and the four product pages
4. Check Coverage after a week for anything excluded

## 4. Google Business Profile

This matters more than anything else on this list for a local loan business.

1. Claim the profile, category **Loan agency**
2. Enter the name, address and phone **exactly** as they appear on the website — Google cross-checks this
3. Add the website URL, hours, service areas, and at least 10 photos
4. Copy the review short link into `GMB_REVIEW` in `gen_core.py` and regenerate
5. Post weekly — Google weights recency

## 5. Analytics events already firing

No extra tagging needed. These fire on GA4, GTM dataLayer and Meta Pixel:

| Event | Fires when |
|---|---|
| `generate_lead` | any enquiry form submitted (carries `loan_type`, `city`, `source`) |
| `enquire_click` | an Enquire Now button is used |
| `call_*` | any phone link tapped (`call_nav`, `call_hero`, `call_bar`, …) |
| `wa_*` | any WhatsApp link used |
| `chatbot_open` | chat opened |
| `emi_calculate` / `emi_unit` / `emi_attach_to_enquiry` | calculator interactions |
| `lang_switch` / `lang_auto` | language changed manually or automatically |
| `gmb_review` / `gmb_profile` | Google Business Profile links used |
| `social_*` | social icons used |

In GA4, mark `generate_lead` as a **Key Event** so it shows as a conversion.

## 6. Accessibility and performance notes

- Skip-to-content link, focus rings, ARIA labels and `prefers-reduced-motion` are all implemented
- The hero shader falls back to a CSS gradient when WebGL is unavailable
- The map iframe is lazy-loaded only when scrolled into view
- Fonts load non-render-blocking with a `print`-media swap
