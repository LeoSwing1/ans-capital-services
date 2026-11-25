# Integrations

## WhatsApp — the enquiry channel

Every enquiry form, the chatbot's lead capture and the bottom bar hand off to
`https://wa.me/919319667592` with the message pre-filled.

- Nothing is stored on the website. There is no database and no server.
- If the browser blocks the popup, the code falls back to a real anchor click so the lead is not lost.
- Duplicate submissions of the same payload within 10 minutes are caught and shown a "we already have this" message.

To change the number, edit `PHONE` in `gen_core.py` and regenerate, or find-and-replace
`919319667592` across the HTML and `assets/js/`.

### If you later want enquiries in a database or inbox
Point the form at a form backend instead — Formspree, Basin, Web3Forms and Google Forms all
work with a static site. The submit handler lives in `assets/js/app.js`, in the
`form[data-enquiry]` block. Replace the `window.open(...)` call with a `fetch()` POST.

## Chatbot

**Default: rule-based, bilingual, no server.** It handles the four loan categories, documents,
eligibility, fees, credit score, the enquiry process, EMI calculation from a typed sentence,
human escalation and click-to-call. It detects whether you are writing English, Hindi or
romanised Hinglish and switches the whole site to match.

**Guardrails built in** — it will not guarantee approval, will not present rates as ANS's own
terms, asks for consent before collecting any personal detail, shows a summary for confirmation
before sending, and refuses to handle OTPs, passwords, PINs or account numbers.

**Optional LLM upgrade.** `integrations/chat-endpoint.example.js` is a ready-to-deploy
serverless function:

1. Deploy it as `/api/chat` on Vercel (or an equivalent on Netlify/Cloudflare)
2. Set `ANTHROPIC_API_KEY` in the hosting dashboard — **never in a file the browser downloads**
3. Add after `app.js`: `<script>window.ANS.chatEndpoint = '/api/chat';</script>`

The system prompt in that file already carries the compliance rules. If the endpoint is absent,
times out or errors, the site silently falls back to the rule-based engine — the chatbot never breaks.

## Social

Live links, already wired into the footer, contact page and homepage:

- Instagram — https://www.instagram.com/anscapitalservices
- Facebook — https://www.facebook.com/profile.php?id=61596099088363
- LinkedIn — https://www.linkedin.com/in/ans-capital-service-56101a448/
- YouTube — https://youtube.com/@anscapitalservice

Open Graph and Twitter Card metadata are set on every page, using `assets/img/og-cover.jpg`.

**Facebook post embedding** is not included: it requires a Page ID and the Facebook SDK, which
adds a third-party script and a cookie to every page. If you want it, add the Page Plugin to
`contact.html` only, and add it to the Cookie Policy.

## Maps

The Contact and Home maps use the keyless Google Maps embed and are lazy-loaded.
Once the office address is confirmed, replace `MAP_EMBED` in `gen_core.py` with the embed
URL from the Google Business Profile so the pin lands on the actual office.
