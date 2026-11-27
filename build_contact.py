# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

CFAQ = [
 ("What is the fastest way to reach you?",
  "WhatsApp on " + PHONE_D + ". You can send documents, photos of paperwork and voice notes there, and we reply in business hours — usually within fifteen minutes. If the matter is urgent, call the same number."),
 ("What should I send in the first message?",
  "Four things get us straight to a useful answer: the loan type you need, the amount, whether you are salaried or self-employed, and your approximate monthly income. If you know your CIBIL score, add it. That is enough for us to tell you where you stand before anything formal happens."),
 ("Do I have to visit an office?",
  "Usually not. Most files run end to end on WhatsApp and email — documents, clarifications, status updates. You will meet the lender's representative only where their process requires it, typically for property verification on a home loan or a loan against property, or for signing at disbursal."),
 ("Is my information safe with you?",
  "Your documents are shared only with the lenders you authorise us to approach, and only for the purpose of your application. We do not sell or rent your data to third parties. Our full approach is set out in the Privacy Policy, and you can ask us to delete your file at any time."),
 ("When are you open?",
  "Monday to Saturday, 10:00 AM to 7:00 PM. WhatsApp messages sent outside those hours are answered first thing the next working morning."),
]

BODY = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">Contact</span></nav>
    <div class="split-wide" style="align-items:end">
      <div>
        <span class="eyebrow on-dark">Get in touch</span>
        <h1 data-hi="बात कीजिए।<br><em class='g-gold g-anim'>किसी भी तरह।</em>"><span class="t-md t-thin t-mute">Talk to a person.</span><br><em class="g-gold g-anim t-lg">Any way you like.</em></h1>
      </div>
      <div style="padding-bottom:.4rem">
        <p class="lead">Phone, WhatsApp, email or the form below — all of it reaches the same desk. Tell us what you need and we will tell you honestly where you stand.</p>
        <div class="btn-row" style="margin-top:1.6rem">
          <a class="btn btn-gold" href="tel:+{PHONE}" data-ev="call_contact_hero">{I['phone']}Call {PHONE_D}</a>
          <a class="btn btn-ghost-light" href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_contact_hero">{I['wa']}WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("arc","tr",440,.055),("dots","bl",210,.05))}{orb("tr",560,"gold")}
  <div class="wrap">
    <div class="split-wide" style="align-items:start">
      <div data-rv="l">
        <span class="eyebrow" data-n="01">Direct lines</span>
        <h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)" class="g-navy">Reach us directly</h2>
        <div class="grid" style="gap:.8rem;margin-top:1.8rem">
          <a class="ccard" href="tel:+{PHONE}" data-ev="call_contact">
            <span class="ci2">{I['phone']}</span><span><h3>Phone</h3><p>{PHONE_D}</p></span></a>
          <a class="ccard" href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_contact">
            <span class="ci2">{I['wa']}</span><span><h3>WhatsApp</h3><p>{PHONE_D} · send documents here</p></span></a>
          <a class="ccard" href="mailto:{EMAIL}">
            <span class="ci2">{I['mail']}</span><span><h3>Email</h3><p>{EMAIL}</p></span></a>
          <div class="ccard"><span class="ci2">{I['clock']}</span><span><h3>Office hours</h3><p>Monday – Saturday<br>10:00 AM – 7:00 PM IST<br><span style="font-size:.78rem;color:var(--muted);font-weight:500">Subject to confirmation — please call ahead</span></p></span></div>
          <div class="ccard"><span class="ci2">{I['pin']}</span><span><h3>Service area</h3><p>Delhi NCR and Uttar Pradesh, and elsewhere in India where documents can be shared electronically<br><span style="font-size:.78rem;color:var(--muted);font-weight:500">Full office address will be published here once confirmed</span></p></span></div>
          <button class="ccard" type="button" data-bot style="text-align:left;cursor:pointer;width:100%;font:inherit" data-ev="bot_contact">
            <span class="ci2">{I['bot']}</span><span><h3>Chat assistant</h3><p>हिंदी / English · instant answers on rates, documents and EMI</p></span></button>
        </div>

        <div class="hindi-box" style="margin-top:2rem">
          <h3>हिंदी में बात कीजिए</h3>
          <p>आप हमसे <b>हिंदी</b> में बात कर सकते हैं — फ़ोन पर, WhatsApp पर, और इस वेबसाइट पर भी। मेन्यू में <b>हिं</b> बटन दबाइए, या नीचे दाईं तरफ़ चैट खोलकर हिंदी चुन लीजिए।</p>
          <p>पहली बार मैसेज कर रहे हैं? बस ये चार बातें भेज दीजिए — <b>कौन सा लोन, कितनी रकम, नौकरी या बिज़नेस, और महीने की आमदनी</b>। इतने से हम बता देंगे कि आपको कहाँ से और किस दर पर लोन मिल सकता है।</p>
        </div>
      </div>

      <div data-rv="r" id="enquiry">
        <div class="card glass" style="padding:clamp(1.6rem,3vw,2.4rem)">
          <span class="eyebrow">Enquiry form</span>
          <h3 style="font-size:1.4rem;margin-bottom:.4rem">Tell us what you need</h3>
          <p style="font-size:.92rem;color:var(--muted);margin-bottom:1.6rem">Submitting hands your details to our team over WhatsApp, so nothing is stored on this website. We reply during business hours. No advance fee and no obligation to proceed.</p>
          {enquiry_form("contact")}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-sm wash">
  <div class="wrap">
    <div class="split-wide" style="align-items:start">
      <div data-rv="l">
        <span class="eyebrow" data-n="02">Find us</span>
        <h2 style="font-size:clamp(1.7rem,3.2vw,2.4rem)" class="g-navy">On the map</h2>
        <p class="lead" style="margin-top:1rem">We work across Delhi NCR and the surrounding Uttar Pradesh belt, and handle files from the rest of India remotely. Call before visiting so we can keep the time free for you.</p>
        <div class="card" style="margin-top:1.6rem">
          <h3 style="margin-bottom:.4rem">Google Business Profile</h3>
          <p style="font-size:.9rem;color:var(--muted);margin-bottom:1.2rem">Find our directions, hours and reviews on Google — and if we have helped you, a review genuinely helps other borrowers find an honest desk.</p>
          <div class="btn-row">
            <a class="btn btn-ghost btn-sm" href="{GMB_PROFILE}" target="_blank" rel="noopener" data-ev="gmb_profile">{I['pin']}Open in Google Maps</a>
            <a class="btn btn-gold btn-sm" href="{GMB_REVIEW}" target="_blank" rel="noopener" data-ev="gmb_review_contact">Write a review</a>
          </div>
        </div>
        <div class="card" style="margin-top:1rem">
          <h3 style="margin-bottom:.6rem">Follow us</h3>
          <div class="socials lite">
            <a class="soc ig" href="{SOCIAL['ig']}" target="_blank" rel="noopener me" aria-label="Instagram" data-ev="social_ig">{I['ig']}</a>
            <a class="soc fb" href="{SOCIAL['fb']}" target="_blank" rel="noopener me" aria-label="Facebook" data-ev="social_fb">{I['fb']}</a>
            <a class="soc li" href="{SOCIAL['li']}" target="_blank" rel="noopener me" aria-label="LinkedIn" data-ev="social_li">{I['li']}</a>
            <a class="soc yt" href="{SOCIAL['yt']}" target="_blank" rel="noopener me" aria-label="YouTube" data-ev="social_yt">{I['yt']}</a>
          </div>
        </div>
      </div>
      <div data-rv="r">
        <div class="mapbox" data-map="{MAP_EMBED}" style="min-height:360px">
          <div class="map-pin">
            <b>{BRAND}</b>
            <span>Channel Partner — Ruloans<br>Mon–Sat · 10:00 AM – 7:00 PM<br><span style="font-size:.78rem">Map shows our service region. Exact office address to be confirmed.</span></span>
            <a class="tlink" style="margin-top:.7rem" href="{GMB_PROFILE}" target="_blank" rel="noopener" data-ev="gmb_directions_contact">Get directions {I['arrow']}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{gmb_block()}

{faq_block(CFAQ, "Before you get in touch")}
</main>
"""

html = page("Contact ANS Capital Services Pvt. Ltd. | Call +91 93196 67592",
  "Contact ANS Capital Services Pvt. Ltd. for personal, home, car, business loans and loan against property. Call +91 93196 67592, WhatsApp or email anscapitalservicespvtltd@gmail.com. Mon–Sat, 10 AM – 7 PM.",
  "contact.html", BODY, "contact.html",
  "contact ANS Capital Services, loan agent contact, loan enquiry Delhi NCR, loan DSA phone number, apply for loan India",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("Contact","contact.html")]), faq_schema(CFAQ),
     {"@type":"ContactPage","@id":SITE+"/contact.html#webpage","url":SITE+"/contact.html",
      "name":"Contact ANS Capital Services Pvt. Ltd.","isPartOf":{"@id":SITE+"/#website"},
      "mainEntity":{"@id":SITE+"/#organization"},"inLanguage":"en-IN"}))
open("contact.html","w").write(html)
print("contact.html", f"{len(html):,}", "bytes")
