# Content and claims policy

This site is built for a regulated-adjacent business. These rules are applied throughout,
and they should be kept if you edit the copy.

## What the site never says

- **No guaranteed approval.** Nowhere. The FAQ and the chatbot both actively warn against
  anyone who promises it.
- **No RBI registration or licence.** The Terms and the About page state plainly that the
  company holds none and claims none.
- **No invented track record.** No customer counts, no "X years of experience", no awards,
  no fabricated reviews or testimonials.
- **No fake statistics.** The only numbers on the site are either the market rate figures
  (clearly labelled) or figures published by Ruloans about itself (explicitly attributed to
  Ruloans, with a note that they are not ANS's own track record).
- **No invented office address.** It is omitted from the page copy and from the structured
  data, rather than guessed.

## How interest rates are presented

Every rate table carries a **"General market information"** label and a notice stating:

> These are general market figures, not ANS Capital Services' terms. They were compiled from
> publicly available lender information in November 2026 and are published to help you
> understand the product. They are not an offer, a quotation or a commitment.

The figures were sourced from public lender and comparison-site data in November 2026.
**Review them quarterly** — they move with the RBI repo rate. They live in `data_products.py`.

## How the Ruloans relationship is described

The site states that ANS Capital Services is a Channel Partner of Ruloans. This matches what
the company states on its own Instagram and LinkedIn profiles. Network figures published by
Ruloans (partner institutions, years, annual business, towns covered) appear only on the About
page, attributed to Ruloans by name, with an explicit note that they describe that company and
are not a claim about ANS's own experience.

If the relationship changes, update `about.html` and the hero badge on `index.html`.

## Products marked subject to availability

Loan Against Property, education, gold, credit cards and insurance each carry a notice saying
availability depends on the lending institutions ANS is empanelled with at the time of enquiry.
Keep that notice unless and until the empanelment is confirmed and documented.

## Required disclaimer

Every page footer carries the full disclosure: that ANS is a loan distribution company and not
a lender, that all lending decisions rest with the bank or NBFC, that rates shown are indicative,
and that no advance fee is ever charged. Do not remove it.


## Editorial devices

Three patterns are carried over from the agency site (vsmgrowth.com) so the two brands read as
coming from the same studio:

1. **Italic serif accent words** inside otherwise geometric-sans headlines — see Typography below.
2. **Numbered section eyebrows** — `<span class="eyebrow" data-n="01">Our approach</span>` renders
   as `01 | OUR APPROACH` with a gold rule between. The homepage runs 01–08. Keep the sequence
   continuous when adding or removing a section.
3. **↗ affordance** on navigation links and text links, appearing on hover.

What was deliberately *not* carried over: the agency site's "making noise" voice, its hero stat
row and its near-black palette. A loan distributor is selling carefulness, not noise, and the
stat row would require customer numbers this company cannot yet evidence.

## Typography and the shape system

**Typefaces.** Display and headings use **Outfit** (weights 300–700); body copy uses **Inter**;
Hindi uses **Noto Sans Devanagari**. All three are Google Fonts, loaded non-render-blocking.

Outfit replaced Playfair Display as the heading face: a high-contrast classical serif sat
awkwardly against the glass panels, the WebGL hero and the pill buttons.

**Instrument Serif italic** is then used deliberately, for accent words only, inside headlines —
`<em>` inside an `h1`, `h2` or `h3` renders as gold italic serif. This is the house device
carried over from vsmgrowth.com, where key words are italicised in nearly every section title.
Use it for one phrase per headline, never for a whole heading and never in body copy. In Hindi
the accent falls back to bold Devanagari, because an italic Devanagari is not a real style.

**Abstract shapes.** The decorative layer is drawn from the logo's own geometry — the open gold
arc, the coin circle, the roof angle — plus dot grids, line rays and a square grid. They are
emitted by `deco()` and `orb()` in `gen_parts.py` and placed asymmetrically, so the shape mass
counterweights the text block on the opposite side.

To adjust the overall presence, change the multiplier on one line in `style.css`:

```css
.dc{ opacity: calc(var(--o) * 2.1); }   /* lower = subtler, higher = bolder */
```

Shapes sit at `z-index:0`, content at `z-index:2`, and they are non-interactive and hidden from
screen readers. They fade back on mobile and stop animating under `prefers-reduced-motion`.


## Multi-colour type and size contrast

Headlines combine up to three colour treatments and three sizes. The utilities live in
`style.css` and are applied as classes on spans inside an `h1`/`h2`:

| Class | Effect |
|---|---|
| `.g-gold` | gold gradient fill (light → deep → light) |
| `.g-navy` | navy gradient fill (royal → navy → ink) |
| `.g-light` | white → pale blue, for dark backgrounds |
| `.g-dual` | navy running into gold, for a single long phrase |
| `.g-anim` | slow sheen across the gradient — hero and page titles only |
| `.t-sm` `.t-md` `.t-lg` `.t-xl` | relative size steps inside one headline |
| `.t-thin` `.t-blk` | weight contrast |
| `.t-mute` | drops a connecting phrase back in the hierarchy |

Example — the homepage hero carries three fills and two sizes:

```html
<h1>Your Financial <span class="g-light">Goals.</span><br>
    <em class="g-gold g-anim t-lg">Our Commitment.</em></h1>
```

Keep `.g-anim` rare. If every heading shimmers, none of them reads as important.

A `@supports not (background-clip: text)` fallback paints solid gold, so the text can never
disappear on an old browser.

## Heading reveal — why the hidden state is in JavaScript

Headings rise out of their own baseline using `clip-path`. Two things about this are
deliberate and should not be "simplified":

1. **The hidden state (`.mask-ready`) is added by script, never by the stylesheet.** If JS
   fails, is blocked, or `IntersectionObserver` is missing, headings simply render. There is no
   state in which the page can lose its text. This is verified by a test that loads all 25 pages
   with JavaScript disabled.
2. **The observer watches the heading's parent, not the heading.** A heading clipped to zero
   height can never satisfy an intersection threshold on itself — it would hide from the very
   observer meant to reveal it. Watching an unclipped ancestor avoids that deadlock.

There is also a 6.5s backstop that reveals anything still hidden, and a `beforeprint` handler
so printed pages are never blank.
