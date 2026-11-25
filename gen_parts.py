# -*- coding: utf-8 -*-
"""Reusable blocks + JSON-LD builders."""
import json
from gen_core import *

# ------------------------------------------------------------------ schema
ORG = {
  "@type": "FinancialService",
  "@id": SITE + "/#organization",
  "name": BRAND,
  "alternateName": ["ANS Capital Services", "ANS Capital", "ANS Capital Services Private Limited"],
  "url": SITE + "/",
  "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.jpg", "width": 1080, "height": 1080},
  "image": SITE + "/assets/img/og-cover.jpg",
  "description": "ANS Capital Services Private Limited assists customers in understanding and applying for personal, home, car and business loans. It is a loan distribution company and a Channel Partner of Ruloans. It is not a bank or an NBFC and does not sanction or disburse loans.",
  "telephone": "+" + PHONE,
  "email": EMAIL,
  "priceRange": "No advance fee charged to applicants",
  "currenciesAccepted": "INR",
  "paymentAccepted": "Bank transfer, UPI, Cheque",
  # NOTE: no PostalAddress / LocalBusiness markup until the office address is verified (spec §15).
  # Once confirmed, add:  "address": {"@type":"PostalAddress","streetAddress":"...","addressLocality":"...",
  #                                   "postalCode":"...","addressRegion":"Uttar Pradesh","addressCountry":"IN"}
  "areaServed": [{"@type": "Country", "name": "India"},
                 {"@type": "AdministrativeArea", "name": "Delhi NCR"},
                 {"@type": "AdministrativeArea", "name": "Uttar Pradesh"}],
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
      "opens": "10:00", "closes": "19:00"}],
  "sameAs": [SOCIAL["ig"], SOCIAL["fb"], SOCIAL["li"], SOCIAL["yt"]],
  "hasMap": GOOGLE["url"],
  "slogan": "Building Your Financial Future",
  "knowsLanguage": ["en-IN", "hi-IN"],
  "contactPoint": [{"@type": "ContactPoint", "telephone": "+" + PHONE, "contactType": "customer service",
                    "areaServed": "IN", "availableLanguage": ["English", "Hindi"]}],
  "parentOrganization": {"@type": "Organization", "name": "Ruloans Distribution Services Pvt. Ltd.", "url": "https://www.ruloans.com/"}
}

WEBSITE = {
  "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND,
  "inLanguage": "en-IN", "publisher": {"@id": SITE + "/#organization"},
  "potentialAction": {"@type": "SearchAction",
    "target": {"@type": "EntryPoint", "urlTemplate": SITE + "/?s={search_term_string}"},
    "query-input": "required name=search_term_string"}
}

def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n,
         **({"item": SITE + "/" + u} if u else {})} for i, (n, u) in enumerate(items)]}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def loan_schema(name, desc, path, rate_low, rate_high, amt_max, term_min, term_max):
    return {"@type": "LoanOrCredit", "@id": SITE + "/" + path + "#product",
            "name": name, "description": desc, "url": SITE + "/" + path,
            "loanType": name, "currency": "INR",
            "amount": {"@type": "MonetaryAmount", "currency": "INR", "maxValue": amt_max},
            "annualPercentageRate": {"@type": "QuantitativeValue", "minValue": rate_low, "maxValue": rate_high, "unitText": "PERCENT"},
            "loanTerm": {"@type": "QuantitativeValue", "minValue": term_min, "maxValue": term_max, "unitCode": "MON"},
            "provider": {"@id": SITE + "/#organization"},
            "areaServed": {"@type": "Country", "name": "India"},
            "feesAndCommissionsSpecification": "Processing and documentation charges are levied by the lending institution and set out in its sanction letter. ANS Capital Services charges applicants no advance fee.", "disambiguatingDescription": "General market information about this loan category. Not an offer. Rates, fees and eligibility are determined by the lending institution."}

def ld(*blocks):
    data = {"@context": "https://schema.org", "@graph": list(blocks)}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + '</script>'

# ------------------------------------------------------------------ blocks
def faq_block(faqs, title="Frequently Asked Questions", hi_title="अक्सर पूछे जाने वाले सवाल"):
    items = ""
    for q, a in faqs:
        items += f"""<div class="acc-i"><button class="acc-q" type="button"><span>{q}</span><i aria-hidden="true"></i></button>
        <div class="acc-a"><div><p>{a}</p></div></div></div>"""
    return f"""
<section class="sec cream" id="faq">
  {deco(("ring","tl",420,.05),("coin","br",300,.045))}{orb("br",560,"gold")}
  <div class="wrap-n">
    <div class="center" data-rv>
      <div class="orn"><i></i></div>
      <span class="eyebrow c" data-n="07">Questions, answered</span>
      <h2 data-hi="{hi_title}" class="g-navy">{title}</h2>
    </div>
    <div class="acc" style="margin-top:2.8rem" data-rv>{items}</div>
  </div>
</section>"""

def enquiry_form(ctx="general", amount_label="Approximate amount required"):
    cats = "".join(f'<option value="{n}">{n}</option>' for _, n, _, _ in ALL_PRODUCTS)
    return f"""
<form class="form" data-enquiry="{ctx}" id="enquiry-{ctx}" novalidate>
  <div class="form-msg ok" data-msg-ok role="status" aria-live="polite">
    {I['check']}<span><b>Thank you — your enquiry is ready to send.</b><br><span data-msg-ok-text>We have opened WhatsApp with your details filled in. If it did not open, use the Call or Email buttons and we will pick it up from there.</span></span>
  </div>
  <div class="form-msg err" data-msg-err role="alert">
    {I['shield']}<span data-msg-err-text>Please check the highlighted fields and try again.</span>
  </div>

  <div class="form-row">
    <div class="field"><label for="f{ctx}n">Full name <span aria-hidden="true">*</span></label>
      <input id="f{ctx}n" name="name" data-label="Name" type="text" required placeholder="Your full name" autocomplete="name" data-hi-ph="आपका पूरा नाम">
      <span class="field-err">Please enter your name</span></div>
    <div class="field"><label for="f{ctx}p">Mobile number <span aria-hidden="true">*</span></label>
      <input id="f{ctx}p" name="phone" data-label="Mobile" type="tel" required placeholder="10-digit mobile" autocomplete="tel" inputmode="numeric" maxlength="13" data-hi-ph="10 अंकों का मोबाइल नंबर">
      <span class="field-err">Enter a valid 10-digit Indian mobile number</span></div>
  </div>

  <div class="form-row">
    <div class="field"><label for="f{ctx}e">Email address</label>
      <input id="f{ctx}e" name="email" data-label="Email" type="email" placeholder="you@example.com" autocomplete="email">
      <span class="field-err">Enter a valid email address</span></div>
    <div class="field"><label for="f{ctx}l">Preferred language</label>
      <select id="f{ctx}l" name="language" data-label="Preferred language">
        <option value="Hindi">हिंदी / Hindi</option>
        <option value="English">English</option>
        <option value="Either">Either is fine</option>
      </select></div>
  </div>

  <div class="form-row">
    <div class="field"><label for="f{ctx}t">Loan category <span aria-hidden="true">*</span></label>
      <select id="f{ctx}t" name="loan_type" data-label="Loan category" data-cond-trigger>
        {cats}<option value="Not sure">Not sure — please advise</option>
      </select></div>
    <div class="field"><label for="f{ctx}a">{amount_label}</label>
      <input id="f{ctx}a" name="amount" data-label="Amount" type="text" placeholder="e.g. 10 lakh" data-hi-ph="जैसे 10 लाख"></div>
  </div>

  <!-- conditional fields, shown by loan category -->
  <div class="form-row cond" data-cond="Home Loans">
    <div class="field"><label for="f{ctx}pr">Property status</label>
      <select id="f{ctx}pr" name="property_status" data-label="Property status" disabled>
        <option>Ready to move</option><option>Under construction</option><option>Plot / self-construction</option>
        <option>Renovation</option><option>Balance transfer</option><option>Not finalised yet</option>
      </select></div>
    <div class="field"><label for="f{ctx}pc">Property city / location</label>
      <input id="f{ctx}pc" name="property_city" data-label="Property location" type="text" placeholder="Where is the property?" disabled></div>
  </div>

  <div class="form-row cond" data-cond="Car Loans">
    <div class="field"><label for="f{ctx}vt">Vehicle type</label>
      <select id="f{ctx}vt" name="vehicle_type" data-label="Vehicle type" disabled>
        <option>New car</option><option>Pre-owned car</option><option>Two-wheeler</option>
        <option>Commercial vehicle</option><option>Not decided</option>
      </select></div>
    <div class="field"><label for="f{ctx}vm">Vehicle model, if decided</label>
      <input id="f{ctx}vm" name="vehicle_model" data-label="Vehicle model" type="text" placeholder="e.g. Maruti Brezza" disabled></div>
  </div>

  <div class="form-row cond" data-cond="Business Loans">
    <div class="field"><label for="f{ctx}bv">Years in business</label>
      <select id="f{ctx}bv" name="business_vintage" data-label="Business vintage" disabled>
        <option>Less than 1 year</option><option>1 – 2 years</option><option>2 – 3 years</option><option>More than 3 years</option>
      </select></div>
    <div class="field"><label for="f{ctx}bt">Approximate annual turnover</label>
      <input id="f{ctx}bt" name="turnover" data-label="Annual turnover" type="text" placeholder="e.g. 60 lakh" disabled></div>
  </div>

  <div class="form-row cond" data-cond="Loan Against Property">
    <div class="field"><label for="f{ctx}lt">Type of property owned</label>
      <select id="f{ctx}lt" name="lap_property" data-label="Property type" disabled>
        <option>Residential</option><option>Commercial</option><option>Industrial</option><option>Plot / land</option>
      </select></div>
    <div class="field"><label for="f{ctx}lo">Is the property currently mortgaged?</label>
      <select id="f{ctx}lo" name="lap_mortgaged" data-label="Already mortgaged" disabled>
        <option>No</option><option>Yes — existing loan running</option><option>Not sure</option>
      </select></div>
  </div>

  <div class="form-row">
    <div class="field"><label for="f{ctx}c">City</label>
      <input id="f{ctx}c" name="city" data-label="City" type="text" placeholder="e.g. Meerut, Noida, Delhi" autocomplete="address-level2" data-hi-ph="जैसे मेरठ, नोएडा, दिल्ली"></div>
    <div class="field"><label for="f{ctx}em">Employment type</label>
      <select id="f{ctx}em" name="employment" data-label="Employment type">
        <option>Salaried</option><option>Self-employed / Business</option>
        <option>Professional (Doctor, CA, Architect, etc.)</option><option>Retired</option><option>Other</option>
      </select></div>
  </div>

  <div class="form-row">
    <div class="field"><label for="f{ctx}cb">Preferred callback time</label>
      <select id="f{ctx}cb" name="callback" data-label="Preferred callback time">
        <option>Any time during business hours</option><option>Morning (10 AM – 1 PM)</option>
        <option>Afternoon (1 PM – 4 PM)</option><option>Evening (4 PM – 7 PM)</option>
      </select></div>
    <div class="field"><label for="f{ctx}src">How did you hear about us?</label>
      <select id="f{ctx}src" name="source" data-label="Source">
        <option>Google search</option><option>Instagram</option><option>Facebook</option>
        <option>YouTube</option><option>LinkedIn</option><option>Referred by someone</option><option>Other</option>
      </select></div>
  </div>

  <div class="field"><label for="f{ctx}m">Your message (optional)</label>
    <textarea id="f{ctx}m" name="message" data-label="Message" rows="3" placeholder="Tell us briefly about your requirement, any existing loans, or questions you have"></textarea></div>

  <p class="privacy-note">We use these details only to understand your requirement and, with your permission, to submit an application to lending institutions on your behalf. We never ask for OTPs, passwords, card PINs or account numbers. See our <a href="privacy-policy.html">Privacy Policy</a> and <a href="enquiry-consent.html">Enquiry Consent Policy</a>.</p>

  <label class="consent"><input type="checkbox" name="consent" required>
    <span>I authorise {SHORT} and the lending institutions it approaches on my behalf to contact me by telephone, SMS, WhatsApp or email regarding this enquiry. I understand this consent overrides my DNC/NCPR registration, and that no loan approval is promised. <span class="field-err" style="margin-top:.3rem">Please tick to continue</span></span></label>

  <button class="btn btn-gold btn-lg btn-block" type="submit" data-ev="form_submit_{ctx}">
    <span class="spin" aria-hidden="true"></span><span class="bi">{I['wa']}</span><span data-hi="पूछताछ भेजें">Submit Enquiry</span>
  </button>
  <p class="form-note">No advance fee. No obligation. Final eligibility, sanction and disbursement are decided by the lending institution.</p>
</form>"""

def cta_band(title="Ready to find your <em class='g-gold'>best loan offer?</em>", hi="अपना <em class='g-gold'>सबसे अच्छा लोन ऑफ़र</em> पाने के लिए तैयार हैं?",
             sub="One short conversation. We compare the whole network and come back with real numbers — not estimates."):
    return f"""
<section class="sec dark" style="padding-block:clamp(3.5rem,6vw,5.5rem)">
  {deco(("arc","tl",520,.12),("grid","br",360,.05))}{orb("tl",640,"gold")}{orb("br",560,"navy")}
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div data-rv="l">
        <span class="eyebrow on-dark" data-n="08">Next step</span>
        <h2 data-hi="{hi}" class="g-light">{title}</h2>
        <p class="lead" style="color:#A9C0DB;margin-top:1.1rem;max-width:46ch">{sub}</p>
        <div class="btn-row" style="margin-top:2rem">
          <a class="btn btn-gold btn-lg" href="tel:+{PHONE}" data-ev="call_band">{I['phone']}<span data-hi="अभी कॉल करें">Call {PHONE_D}</span></a>
          <a class="btn btn-ghost-light btn-lg" href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_band">{I['wa']}WhatsApp</a>
        </div>
      </div>
      <div data-rv="r">
        <div class="card card-dark" style="padding:clamp(1.6rem,2.6vw,2.2rem)">
          <h3 style="margin-bottom:.4rem">Quick enquiry</h3>
          <p style="font-size:.9rem;margin-bottom:1.4rem">Fill this and we reply within business hours — usually in under 15 minutes.</p>
          {enquiry_form("band")}
        </div>
      </div>
    </div>
  </div>
</section>"""

def trust_row():
    items = [
      ("shield", "Channel Partner of Ruloans", "Backed by India&rsquo;s leading loan distributor — 25+ years in the market."),
      ("handshake", "265+ banks &amp; NBFCs", "One application compared across hundreds of lender programmes."),
      ("coins", "Zero advance fee", "You never pay us cash upfront. Every fee goes to the lender."),
      ("clock2", "Fast, tracked files", "Pre-checked documents mean fewer queries and quicker sanctions."),
    ]
    cards = ""
    for i, (ic, t, d) in enumerate(items):
        cards += f"""<div class="card" data-rv data-delay="{i*90}">
          <div class="ci">{I[ic]}</div><h3>{t}</h3><p style="margin:0">{d}</p></div>"""
    return cards


def calc_block(amount=2500000, rate=8.5, years=20, amax=50000000, with_attach=True):
    attach = ('<button class="btn btn-ghost-light btn-block btn-sm" style="margin-top:.55rem" type="button" '
              'data-attach-calc data-ev="emi_attach">Add this to my enquiry</button>') if with_attach else ''
    return f"""
<div class="calc" data-calc data-rv>
  <div class="calc-panel">
    <div class="slide-row">
      <div class="slide-top"><label for="ca-{amount}">Loan amount</label><span class="slide-val" data-o-amt>&#8377;25 L</span></div>
      <input id="ca-{amount}" type="range" data-amt min="50000" max="{amax}" step="50000" value="{amount}" aria-label="Loan amount in rupees">
      <div class="slide-ends"><span>&#8377;50 K</span><span>{'&#8377;5 Cr' if amax >= 50000000 else '&#8377;2 Cr'}</span></div>
    </div>
    <div class="slide-row">
      <div class="slide-top"><label for="cr-{amount}">Annual interest rate</label><span class="slide-val" data-o-rate>8.50%</span></div>
      <input id="cr-{amount}" type="range" data-rate min="7" max="30" step="0.05" value="{rate}" aria-label="Annual interest rate percent">
      <div class="slide-ends"><span>7%</span><span>30%</span></div>
    </div>
    <div class="slide-row">
      <div class="slide-top">
        <label for="ct-{amount}">Loan tenure</label>
        <span style="display:flex;align-items:center;gap:.6rem">
          <span class="unit-toggle" role="group" aria-label="Tenure unit">
            <button type="button" data-unit="years" aria-pressed="true">Years</button>
            <button type="button" data-unit="months" aria-pressed="false">Months</button>
          </span>
          <span class="slide-val" data-o-ten>{years} yrs</span>
        </span>
      </div>
      <input id="ct-{amount}" type="range" data-ten min="1" max="30" step="1" value="{years}" aria-label="Loan tenure">
      <div class="slide-ends" data-ten-ends><span>1 year</span><span>30 years</span></div>
    </div>
    <p style="font-size:.79rem;color:var(--muted);margin:1.6rem 0 0">
      <b>Illustrative estimate only.</b> This calculator applies the standard reducing-balance formula to the figures you enter.
      It does not include processing fees, insurance premiums financed with the loan, or rate resets on floating-rate loans.
      Your actual EMI is the one stated in the lender's sanction letter and Key Facts Statement.
    </p>
  </div>

  <div class="calc-out">
    <span class="emi-label" data-hi="अनुमानित मासिक EMI">Estimated monthly EMI</span>
    <div class="emi-big" data-emi>&#8377;21,696</div>

    <div class="donut-wrap">
      <span class="donut-box">
        <svg class="donut" viewBox="0 0 120 120" role="img" aria-label="Principal versus interest split">
          <circle class="track" cx="60" cy="60" r="52"></circle>
          <circle class="seg" cx="60" cy="60" r="52" stroke-dasharray="0 327"></circle>
        </svg>
        <span class="donut-mid"><span><span>Principal</span><b data-mid-pct>48%</b></span></span>
      </span>
      <div class="donut-key">
        <div><span><i style="background:#DFBA6B"></i>Principal</span><b data-principal>&#8377;25,00,000</b></div>
        <div><span><i style="background:rgba(255,255,255,.3)"></i>Interest</span><b data-interest>&#8377;27,06,939</b></div>
        <div style="border-top:1px solid rgba(255,255,255,.16);padding-top:.55rem"><span>Total payable</span><b data-total>&#8377;52,06,939</b></div>
        <div><span>Instalments</span><b data-months>240 EMIs</b></div>
      </div>
    </div>

    <div class="emi-bar"><i class="p" style="width:48%"></i><i class="n" style="width:52%"></i></div>

    <a class="btn btn-gold btn-block" style="margin-top:1.5rem" data-wa-emi href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_emi">
      {I['wa']}<span data-hi="यह गणना भेजें">Send this calculation to our team</span></a>
    {attach}
  </div>
</div>"""


def availability_notice(product):
    return f"""<div class="notice gold" data-rv>
  {I['shield']}
  <span><b>Please confirm availability.</b> {product} is described here as a general market product.
  Which specific facilities {SHORT} can currently arrange for you depends on the lending institutions it is
  empanelled with at the time of your enquiry. Call {PHONE_D} and we will tell you exactly what is available
  for your profile before you spend time on paperwork.</span>
</div>"""


def market_rate_notice():
    return f"""<div class="notice" data-rv style="margin-top:1.2rem">
  {I['doc']}
  <span><b>These are general market figures, not {SHORT}'s terms.</b> They were compiled from publicly
  available lender information in November 2026 and are published here to help you understand the product.
  They are not an offer, a quotation or a commitment. The interest rate, fees and tenure that apply to you
  are set by the lending institution after it assesses your application, and appear in your sanction letter
  and Key Facts Statement.</span>
</div>"""


# ---------------------------------------------------------------- original SVG art
# Illustrative brand artwork, drawn here rather than licensed photography.
# Swap any of these for a licensed photograph by replacing the <svg> with an <img>.
def art(kind, idx=0):
    p = f"a{idx}"
    base = (f'<defs><linearGradient id="{p}g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#2A2015"/><stop offset=".55" stop-color="#17120C"/>'
            f'<stop offset="1" stop-color="#0C0906"/></linearGradient>'
            f'<linearGradient id="{p}d" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#F0D79B"/><stop offset="1" stop-color="#D4A03A"/></linearGradient>'
            f'<radialGradient id="{p}r"><stop offset="0" stop-color="#D4A03A" stop-opacity=".55"/>'
            f'<stop offset="1" stop-color="#D4A03A" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="400" height="200" fill="url(#{p}g)"/>'
            f'<circle cx="330" cy="40" r="110" fill="url(#{p}r)"/>')

    bodies = {
      # a person at a desk — personal finance
      "personal":
        f'<circle cx="300" cy="150" r="78" fill="rgba(255,255,255,.04)"/>'
        f'<rect x="52" y="128" width="190" height="7" rx="3.5" fill="url(#{p}d)" opacity=".85"/>'
        f'<rect x="78" y="86" width="86" height="42" rx="5" fill="rgba(255,255,255,.1)"/>'
        f'<rect x="88" y="96" width="50" height="4" rx="2" fill="rgba(255,255,255,.4)"/>'
        f'<rect x="88" y="106" width="66" height="4" rx="2" fill="rgba(255,255,255,.22)"/>'
        f'<rect x="88" y="116" width="36" height="4" rx="2" fill="rgba(255,255,255,.22)"/>'
        f'<circle cx="208" cy="66" r="19" fill="url(#{p}d)"/>'
        f'<path d="M184 128c0-15 11-27 24-27s24 12 24 27" fill="none" stroke="url(#{p}d)" stroke-width="7" stroke-linecap="round"/>'
        f'<circle cx="300" cy="96" r="30" fill="none" stroke="rgba(223,186,107,.5)" stroke-width="2"/>'
        f'<circle cx="300" cy="96" r="46" fill="none" stroke="rgba(223,186,107,.22)" stroke-width="2"/>',
      # a house with a key line — home finance
      "home":
        f'<circle cx="320" cy="150" r="92" fill="rgba(255,255,255,.04)"/>'
        f'<path d="M60 170V104l62-46 62 46v66z" fill="rgba(255,255,255,.1)"/>'
        f'<path d="M44 108 122 50l78 58" fill="none" stroke="url(#{p}d)" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
        f'<rect x="104" y="128" width="36" height="42" fill="url(#{p}d)" opacity=".9"/>'
        f'<rect x="72" y="118" width="22" height="22" rx="2" fill="rgba(255,255,255,.28)"/>'
        f'<rect x="150" y="118" width="22" height="22" rx="2" fill="rgba(255,255,255,.28)"/>'
        f'<path d="M232 170h130" stroke="rgba(255,255,255,.2)" stroke-width="3" stroke-linecap="round"/>'
        f'<circle cx="290" cy="92" r="26" fill="none" stroke="url(#{p}d)" stroke-width="6"/>'
        f'<path d="M290 118v34m0-12h14" stroke="url(#{p}d)" stroke-width="6" stroke-linecap="round"/>',
      # a car profile — vehicle finance
      "car":
        f'<circle cx="86" cy="54" r="86" fill="rgba(255,255,255,.04)"/>'
        f'<path d="M78 142h244" stroke="rgba(223,186,107,.5)" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M96 136l14-38a16 16 0 0 1 15-11h86a16 16 0 0 1 13 7l22 31 38 6a14 14 0 0 1 12 14v13H96z"'
        f' fill="rgba(255,255,255,.12)" stroke="url(#{p}d)" stroke-width="5" stroke-linejoin="round"/>'
        f'<path d="M126 97h40v24h-56z" fill="rgba(255,255,255,.28)"/>'
        f'<path d="M178 97h30l17 24h-47z" fill="rgba(255,255,255,.28)"/>'
        f'<circle cx="142" cy="152" r="18" fill="#0C0906" stroke="url(#{p}d)" stroke-width="5"/>'
        f'<circle cx="268" cy="152" r="18" fill="#0C0906" stroke="url(#{p}d)" stroke-width="5"/>'
        f'<path d="M300 58h58M312 74h46" stroke="rgba(255,255,255,.22)" stroke-width="4" stroke-linecap="round"/>',
      # bars and a briefcase — business finance
      "business":
        f'<circle cx="70" cy="160" r="90" fill="rgba(255,255,255,.04)"/>'
        f'<rect x="150" y="76" width="104" height="72" rx="8" fill="rgba(255,255,255,.1)" stroke="url(#{p}d)" stroke-width="5"/>'
        f'<path d="M184 76V64a12 12 0 0 1 12-12h12a12 12 0 0 1 12 12v12" fill="none" stroke="url(#{p}d)" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M150 108h104" stroke="url(#{p}d)" stroke-width="5"/>'
        f'<rect x="276" y="120" width="20" height="44" rx="4" fill="rgba(255,255,255,.22)"/>'
        f'<rect x="304" y="96" width="20" height="68" rx="4" fill="rgba(255,255,255,.34)"/>'
        f'<rect x="332" y="64" width="20" height="100" rx="4" fill="url(#{p}d)"/>'
        f'<path d="M58 150h62M58 128h40" stroke="rgba(255,255,255,.2)" stroke-width="5" stroke-linecap="round"/>',
      # a building with a charge line — property
      "property":
        f'<circle cx="320" cy="60" r="90" fill="rgba(255,255,255,.04)"/>'
        f'<rect x="72" y="58" width="92" height="112" rx="5" fill="rgba(255,255,255,.1)" stroke="url(#{p}d)" stroke-width="5"/>'
        f'<rect x="176" y="96" width="70" height="74" rx="5" fill="rgba(255,255,255,.08)" stroke="rgba(223,186,107,.6)" stroke-width="4"/>'
        + "".join(f'<rect x="{88+c*26}" y="{76+r2*26}" width="14" height="14" rx="2" fill="rgba(255,255,255,.3)"/>'
                  for r2 in range(3) for c in range(3))
        + f'<path d="M264 170h86M278 148h72" stroke="rgba(255,255,255,.2)" stroke-width="4" stroke-linecap="round"/>'
          f'<circle cx="306" cy="92" r="24" fill="url(#{p}d)"/>'
          f'<path d="M296 86h20M296 94h20M296 86c12 0 16 4 16 8s-4 8-11 8h-5l14 12" fill="none" stroke="#0C0906" stroke-width="4" stroke-linecap="round"/>',
      # a graduation cap and coin — education and other
      "other":
        f'<circle cx="80" cy="60" r="86" fill="rgba(255,255,255,.04)"/>'
        f'<path d="M190 72 106 102l84 30 84-30z" fill="url(#{p}d)"/>'
        f'<path d="M134 114v30c22 16 90 16 112 0v-30" fill="none" stroke="rgba(255,255,255,.4)" stroke-width="6" stroke-linejoin="round"/>'
        f'<path d="M274 102v38" stroke="url(#{p}d)" stroke-width="5" stroke-linecap="round"/>'
        f'<circle cx="310" cy="140" r="28" fill="url(#{p}d)"/>'
        f'<path d="M300 132h20M300 140h20M300 132c12 0 16 4 16 8s-4 8-11 8h-5l13 11" fill="none" stroke="#0C0906" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="M58 160h70" stroke="rgba(255,255,255,.2)" stroke-width="5" stroke-linecap="round"/>',
      # abstract — blog and generic
      "abstract":
        f'<path d="M0 150c60-40 120 20 180-16s120-54 220-18v84H0z" fill="rgba(255,255,255,.06)"/>'
        f'<path d="M0 168c70-30 130 14 200-14s130-40 200-10" fill="none" stroke="url(#{p}d)" stroke-width="4"/>'
        f'<circle cx="112" cy="70" r="24" fill="none" stroke="rgba(223,186,107,.55)" stroke-width="4"/>'
        f'<circle cx="250" cy="52" r="12" fill="url(#{p}d)"/>',
    }
    return (f'<svg viewBox="0 0 400 200" preserveAspectRatio="xMidYMid slice" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" focusable="false">'
            f'{base}{bodies.get(kind, bodies["abstract"])}</svg>')


# ---------------------------------------------------------------- abstract shape system
# The vocabulary is taken from the logo itself: the open gold arc, the coin circle and the
# roof angle. Placement is deliberately asymmetric so each shape counterweights the text.
def deco(*layers):
    """deco(("arc","tr",380,.1), ("dots","bl",190,.5)) -> positioned decorative layer"""
    out = ""
    for i, spec in enumerate(layers):
        kind, pos, size, op = spec
        uid = f"d{abs(hash((kind,pos,size,i)))%100000}"
        inner = {
            "arc":  f'<path d="M6 60a54 54 0 1 1 108 0" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>'
                    f'<path d="M20 60a40 40 0 0 1 80 0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" opacity=".55"/>',
            "ring": f'<circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="2.4"/>'
                    f'<circle cx="60" cy="60" r="36" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".5"/>',
            "coin": f'<circle cx="60" cy="60" r="52" fill="currentColor" opacity=".1"/>'
                    f'<circle cx="60" cy="60" r="52" fill="none" stroke="currentColor" stroke-width="1.6" opacity=".55"/>'
                    f'<circle cx="60" cy="60" r="26" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".4"/>',
            "roof": f'<path d="M10 86 60 30l50 56" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>'
                    f'<path d="M30 86 60 52l30 34" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" opacity=".5"/>',
            "dots": f'<defs><pattern id="{uid}" width="14" height="14" patternUnits="userSpaceOnUse">'
                    f'<circle cx="2" cy="2" r="1.7" fill="currentColor"/></pattern></defs>'
                    f'<rect width="120" height="120" fill="url(#{uid})"/>',
            "rays": "".join(f'<path d="M{8+j*17} 112 L{30+j*17} 8" stroke="currentColor" stroke-width="1.6" '
                            f'stroke-linecap="round" opacity="{0.9-j*0.12:.2f}"/>' for j in range(6)),
            "grid": f'<defs><pattern id="{uid}" width="24" height="24" patternUnits="userSpaceOnUse">'
                    f'<path d="M24 0H0v24" fill="none" stroke="currentColor" stroke-width="1"/></pattern></defs>'
                    f'<rect width="120" height="120" fill="url(#{uid})"/>',
        }.get(kind, "")
        out += (f'<svg class="dc dc-{pos}" style="--s:{size}px;--o:{op}" viewBox="0 0 120 120" '
                f'aria-hidden="true" focusable="false">{inner}</svg>')
    return f'<div class="deco" aria-hidden="true">{out}</div>'


def orb(pos="tr", size=520, tone="gold"):
    return f'<span class="orb orb-{pos} orb-{tone}" style="--s:{size}px" aria-hidden="true"></span>'


# ======================================================================
# TRUST COMPONENTS (5) — every one reads from the TRUST CONFIG in
# gen_core.py, so nothing claims anything the business cannot evidence.
# ======================================================================

def rating_pill(center=True):
    """1 — Google rating pill. Shows the rating once it exists, otherwise invites one."""
    has = GOOGLE["rating"] is not None and GOOGLE["reviews"] > 0
    if has:
        inner = (f'<b>{GOOGLE["rating"]}</b><span class="rp-star">&#9733;</span>'
                 f'<span class="rp-txt">Google rating &middot; {GOOGLE["reviews"]} reviews</span>')
        href = GOOGLE["url"]; ev = "gmb_rating"
    else:
        inner = ('<span class="rp-star">&#9733;</span>'
                 '<span class="rp-txt">New on Google &mdash; be the first to review us</span>')
        href = GOOGLE["review_url"]; ev = "gmb_review_invite"
    return f"""
<div class="ratingwrap{' center' if center else ''}">
  <canvas class="starfield" data-stars aria-hidden="true"></canvas>
  <a class="ratingpill" href="{href}" target="_blank" rel="noopener" data-ev="{ev}">{inner}</a>
</div>"""


def stats_band(label="Built on delivered files",
               intro="Two years of real borrowers, real sanctions and reviews left on Google."):
    """2 — light stats band. Process facts, not invented totals."""
    cells = "".join(
        f'<div class="sb-cell" data-rv data-delay="{i*80}"><b>{v}</b><span>{k}</span><i>{note}</i></div>'
        for i, (v, k, note) in enumerate(STATS))
    return f"""
<section class="band sec-sm" id="stats">
  <div class="wrap">
    <div class="sb-grid">
      <div class="sb-intro" data-rv="l">
        <span class="sb-label">{label}</span>
        <p>{intro}</p>
      </div>
      {cells}
    </div>
  </div>
</section>"""


PROMISE = [
    ("An honest read of where you stand", "Before any application, we tell you plainly what a lender is likely to see in your profile — including when the answer is to wait."),
    ("A precise document checklist", "Not a generic list. The exact set for your product, your employment type and the lender we are approaching."),
    ("Every document pre-checked", "We review the full file before submission. Missing pages and name mismatches are what actually delay sanctions."),
    ("One application, not six", "Each application marks your credit report. We identify the right lender first and apply once."),
    ("Options explained side by side", "Rate, processing fee, tenure and conditions, compared in plain language. You choose; we do not choose for you."),
    ("No advance fee, ever", "You pay us nothing before disbursal. Lender charges appear in the sanction letter and go straight to the lender."),
    ("Hindi or English, your choice", "On the phone, on WhatsApp, and across this website — including the paperwork walkthrough."),
    ("We stay on the file", "Through underwriting, lender queries and verification, until the money reaches your account."),
    ("The sanction letter, read together", "Before you sign: the rate, the reset terms, the prepayment clause and every charge."),
    ("Reachable afterwards", "For a top-up, a balance transfer, or the next requirement — the same desk, not a call centre."),
]

def promise_ring(title='Ten things you get <em>with every file.</em>',
                 hi='हर फ़ाइल पर <em>दस बातें, हमेशा।</em>',
                 label="The ANS commitment"):
    """3 — orbital ring of numbered nodes; the centre reads out the current item."""
    nodes = "".join(
        f'<button class="ring-node" type="button" data-node="{i}" '
        f'style="--a:{(i / len(PROMISE)) * 360 - 90}deg" aria-label="{t}"><span>{i+1:02d}</span></button>'
        for i, (t, _) in enumerate(PROMISE))
    items = "".join(
        f'<div class="ring-item" data-item="{i}"><b>{t}</b><p>{d}</p></div>'
        for i, (t, d) in enumerate(PROMISE))
    return f"""
<section class="sec" id="promise">
  {deco(("ring","tr",420,.05),("dots","bl",200,.045))}
  <div class="wrap">
    <div class="ring-grid">
      <div data-rv="l">
        <span class="eyebrow" data-n="05">{label}</span>
        <h2 data-hi="{hi}">{title}</h2>
        <p class="lead" style="margin-top:1.4rem;max-width:44ch">
          No add-on menus and no surprise invoices. This is how every application is handled,
          whatever the size of the loan.
        </p>
        <div class="btn-row" style="margin-top:2rem">
          <a class="btn btn-gold" href="contact.html#enquiry" data-enquire data-ev="cta_promise">Start your enquiry</a>
          <a class="tlink" href="how-it-works.html">See the full process</a>
        </div>
      </div>

      <div class="ring-wrap" data-ring data-rv="r">
        <div class="ring-orbit" aria-hidden="true">
          <canvas class="ring-field" data-ringfield></canvas>
          <span class="ring-circle"></span>
          <span class="ring-sweep"></span>
          {nodes}
        </div>
        <div class="ring-read" aria-live="polite">
          <span class="ring-count"><b data-ring-n>01</b> / {len(PROMISE)}</span>
          <div class="ring-items">{items}</div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def gradient_band(a="Registered.", b="Transparent.", c="Accountable.",
                  label="Where we stand",
                  note="A registered private limited company and a Channel Partner of Ruloans. "
                       "Not a bank, not an NBFC, and holding no RBI licence &mdash; we say so on every page."):
    """4 — light iridescent band carrying a three-word statement."""
    return f"""
<section class="gband">
  <div class="wrap">
    <span class="gb-label" data-rv>{label}</span>
    <h2 class="gb-h" data-rv>{a}<br>{b} <em>{c}</em></h2>
    <p class="gb-note" data-rv>{note}</p>
    <div class="gb-marks" data-rv>
      <span class="gb-mark">{I['shield']}Registered Pvt. Ltd.</span>
      <span class="gb-mark">{I['handshake']}Channel Partner &mdash; Ruloans</span>
      <span class="gb-mark">{I['coins']}No advance fee</span>
      <span class="gb-mark">{I['doc']}Charges disclosed upfront</span>
    </div>
  </div>
</section>"""


def testimonials(title='See what clients <em>say about us.</em>', label="Customer feedback"):
    """5 — review wall. Real reviews only; an honest invitation until then."""
    has = bool(REVIEWS)
    if has:
        cards = "".join(f"""<article class="tcard" data-rv data-delay="{i*80}">
          <div class="tstars">{'&#9733;' * int(r.get('stars',5))}</div>
          <p>&ldquo;{r['quote']}&rdquo;</p>
          {f'<p class="tgloss">{r["gloss"]}</p>' if r.get('gloss') else ''}
          <div class="twho"><span class="tav">{r['name'][:2].upper()}</span>
            <span><b>{r['name']}</b><i>{r['role']}</i></span></div>
        </article>""" for i, r in enumerate(REVIEWS))
        rating_block = f"""<div class="tbig"><b>{GOOGLE['rating']}</b>
            <span class="tstars big">{'&#9733;' * 5}</span></div>
          <p class="tsub">Google rating from {GOOGLE['reviews']} reviews</p>
          <a class="btn btn-ghost" href="{GOOGLE['url']}" target="_blank" rel="noopener" data-ev="gmb_read">Read Google reviews</a>"""
    else:
        cards = f"""<article class="tcard tcard-empty" data-rv>
          <div class="tstars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p>This is where our clients&rsquo; own words will go &mdash; once there are real ones to publish.
             We would rather show you an empty space than someone else&rsquo;s review.</p>
          <div class="twho"><span class="tav">&#43;</span><span><b>Your review</b><i>After we have helped you</i></span></div>
        </article>
        <article class="tcard tcard-note" data-rv data-delay="80">
          <b>Why there is nothing here yet</b>
          <p>{BRAND} is a young company. Rather than borrow testimonials or buy ratings, we are
             letting them accumulate honestly. If we have helped you, a Google review genuinely
             helps the next borrower find an honest desk.</p>
          <a class="tlink" href="{GOOGLE['review_url']}" target="_blank" rel="noopener" data-ev="gmb_review_wall">Write a Google review</a>
        </article>"""
        rating_block = f"""<div class="tbig tbig-empty"><b>&mdash;</b></div>
          <p class="tsub">No Google rating yet. The profile is new, and every review on it will be a real one.</p>
          <a class="btn btn-ghost" href="{GOOGLE['review_url']}" target="_blank" rel="noopener" data-ev="gmb_review_cta">Be the first to review</a>"""

    return f"""
<section class="sec" id="reviews">
  {deco(("coin","tl",380,.045),("rays","r",340,.05))}
  <div class="wrap">
    <div class="tgrid">
      <div data-rv="l">
        <span class="eyebrow" data-n="06">{label}</span>
        <h2>{title}</h2>
      </div>
      <div class="trate" data-rv="r">{rating_block}</div>
    </div>
    <div class="twall">{cards}</div>
  </div>
</section>"""


# ── live rate meter ───────────────────────────────────────────────────────
# Indicative market starting rates with the EMI arithmetic done live in the
# browser. Every figure is published market information, never ANS's terms.
def rate_meter(hero=True):
    """Live rate + EMI meter. hero=True renders the glass card for the hero."""
    cls  = "hmeter" if hero else "meter"
    flag = " data-meter-live" if hero else ""
    live = ('<div class="hm-top"><span class="hm-live"><i></i>'
            '<span data-hi="लाइव बाज़ार दरें">Live market rates</span></span>'
            '<span class="hm-date">Nov 2026</span></div>') if hero else ""
    emi  = ('<div class="hm-emi"><span data-meter-on>on &#8377;30,00,000 &middot; 20 yrs</span>'
            '<b data-meter-emi>&#8377;23,893</b></div>') if hero else ""
    return (
        f'<aside class="{cls}" data-meter{flag} aria-label="Indicative market starting rates">'
        f'{live}'
        '<div class="meter-top">'
        '<span class="meter-prod" data-meter-name>Home Loan</span>'
        '<span class="meter-val"><b data-meter-val>7.35</b>%<i>p.a.</i></span>'
        '</div>'
        '<div class="meter-track">'
        '<span class="meter-fill" data-meter-fill></span>'
        '<span class="meter-knob" data-meter-knob></span>'
        '</div>'
        '<div class="meter-scale"><span>7%</span><span>15%</span><span>24%</span></div>'
        f'{emi}'
        '<p class="meter-note" data-hi="सांकेतिक बाज़ार दरें, नवंबर 2026। ये ANS की शर्तें या ऑफ़र नहीं हैं।">'
        'Indicative market starting rates, Nov 2026 &mdash; not ANS&rsquo;s terms or an offer.</p>'
        '</aside>')


# ── Google Business Profile ───────────────────────────────────────────────
# Every outbound link carries UTM tags, so GA4 can separate map-pack traffic
# from organic search. No rating is claimed anywhere the profile doesn't show it.
def gmb_block(label="Find us on Google"):
    def utm(url, content):
        joiner = "&" if "?" in url else "?"
        return (url + joiner +
                "utm_source=website&utm_medium=referral&utm_campaign=gmb&utm_content=" + content)
    rating = ""
    if GOOGLE["reviews"]:
        rating = (f'<div class="gmb-rate"><b>{GOOGLE["rating"]}</b>'
                  f'<span class="gmb-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
                  f'<i>{GOOGLE["reviews"]} Google reviews</i></div>')
    review_url = GOOGLE["review_url"]
    review_cta = ("" if review_url.startswith("REPLACE") else
        f'<a class="btn btn-ghost" href="{utm(review_url, "review")}" target="_blank" '
        f'rel="noopener" data-ev="gmb_review">Write a review</a>')
    return f"""
<section class="sec-sm gmb" id="google">
  <div class="wrap">
    <div class="gmb-card">
      <div>
        <span class="eyebrow" data-n="06">{label}</span>
        <h2 style="margin-top:.8rem" data-hi="गूगल पर ANS Capital Services">{BRAND} on Google</h2>
        {rating}
        <p class="lead" style="margin-top:1rem;max-width:46ch" data-hi="हमारी गूगल प्रोफ़ाइल पर समय, फ़ोन नंबर और रिव्यू देखें। रास्ता देखने के लिए डायरेक्शंस खोलें।">
          Opening hours, phone number and every review sit on our Google Business Profile.
          Open directions when you want to visit, or leave a review if we have helped you.
        </p>
        <div class="btn-row" style="margin-top:1.8rem">
          <a class="btn btn-gold" href="{utm(GOOGLE["url"], "profile")}" target="_blank"
             rel="noopener" data-ev="gmb_profile">Open our Google profile</a>
          <a class="tlink" href="{utm(GOOGLE["url"], "directions")}" target="_blank"
             rel="noopener" data-ev="gmb_directions">Get directions</a>
          {review_cta}
        </div>
      </div>
      <ul class="gmb-nap">
        <li><span>Call</span><a href="tel:+{PHONE}" data-ev="call_gmb">{PHONE_D}</a></li>
        <li><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span>Hours</span><b>Mon&ndash;Sat &middot; 10:00&nbsp;AM &ndash; 7:00&nbsp;PM</b></li>
        <li><span>Serving</span><b>Delhi NCR &amp; Uttar Pradesh</b></li>
        <li><span>Languages</span><b>Hindi &amp; English</b></li>
      </ul>
    </div>
  </div>
</section>"""
