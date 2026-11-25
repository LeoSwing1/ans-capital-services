# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

SERVICES = [
 ("personal-loan.html","personal","user","Personal Loans",
  "Finance for medical expenses, education, travel, a family occasion or an unexpected cost — without pledging an asset.",
  ["No collateral required","Used for any legitimate personal need","Fixed monthly instalments","Tenure typically 1 to 7 years"]),
 ("home-loan.html","home","home","Home Loans",
  "Finance to buy a ready or under-construction property, build on your own plot, renovate, or move an existing loan to a different lender.",
  ["Longest tenures in retail lending","Lowest interest rates of any retail loan","Tax relief on interest and principal","Co-applicant income can be combined"]),
 ("car-loan.html","car","car","Car Loans",
  "Finance for a new car, a pre-owned car, a two-wheeler or a commercial vehicle, secured against the vehicle itself.",
  ["Secured by the vehicle, so priced low","New and pre-owned options","Tenure typically up to 7 years","Finance arranged before you negotiate"]),
 ("business-loan.html","business","brief","Business Loans",
  "Working capital, stock, equipment or expansion finance for proprietorships, partnerships and companies — secured and unsecured.",
  ["Term loans and overdraft facilities","Secured and collateral-free options","Assessed on GST and banking history","MSME scheme guidance included"]),
]

TRUST = [
 ("doc","Transparent communication",
  "We tell you what a product actually costs across its full tenure, what the charges are, and where your profile is likely to stand — before any application is submitted."),
 ("user","Understanding your requirement",
  "The first conversation is about what you need the money for and what you can comfortably repay. The product follows from that, not the other way round."),
 ("shield","Assistance with documentation",
  "Most applications are delayed by a missing page or a mismatch, not by the lender. We check the full set with you before anything is submitted."),
 ("handshake","Guidance through the process",
  "We stay with the file through underwriting and the lender's queries, and we keep you updated in plain language — in Hindi or English, whichever you prefer."),
]

STEPS = [
 ("Submit an enquiry","Share your requirement by phone, WhatsApp or the form on this website. It takes two minutes and commits you to nothing.",
  "फ़ोन, WhatsApp या इस वेबसाइट के फ़ॉर्म से अपनी ज़रूरत बताइए। दो मिनट लगेंगे और कोई बाध्यता नहीं।"),
 ("Discuss your requirements","We talk through the purpose, the amount, your income profile and any existing obligations, so the options we discuss are realistic.",
  "हम ज़रूरत, रकम, आपकी आमदनी और मौजूदा EMI पर बात करते हैं, ताकि विकल्प सचमुच आपके मतलब के हों।"),
 ("Understand the available options","We explain which products suit your situation, what each typically costs and what the lender will look at. You decide what to pursue.",
  "कौन सा प्रोडक्ट आपके लिए सही है, उसका ख़र्च कितना होगा और बैंक क्या देखेगा — सब समझाया जाता है। फ़ैसला आपका।"),
 ("Complete the documentation","We give you a precise checklist and review every document with you before submission, so the file goes in complete.",
  "पूरी चेकलिस्ट दी जाती है और हर कागज़ जमा करने से पहले जाँचा जाता है, ताकि फ़ाइल अधूरी न जाए।"),
 ("Application review by the lender","The lending institution carries out its own verification, credit assessment and, where a property or vehicle is involved, valuation.",
  "बैंक या NBFC अपनी जाँच, क्रेडिट मूल्यांकन और ज़रूरत पड़ने पर प्रॉपर्टी या गाड़ी की वैल्यूएशन करता है।"),
 ("The lender communicates its decision","Approval, the amount, the rate and all conditions are decided solely by the lending institution and set out in its sanction letter.",
  "मंज़ूरी, रकम, ब्याज दर और सारी शर्तें सिर्फ़ बैंक तय करता है और सैंक्शन लेटर में लिखता है।"),
]

FAQS = [
 ("What exactly does ANS Capital Services do?",
  "We are a loan distribution business. We help you understand which financing options suit your requirement, prepare and check your documentation, submit your application to lending institutions, and follow it through to a decision. We are not a bank or an NBFC, we do not lend money ourselves, and we do not decide whether your loan is approved — that rests entirely with the lending institution."),
 ("Do you charge me anything?",
  "We do not ask applicants for any advance payment, and we never ask for cash. If a lender sanctions a loan, that lender levies its own processing and documentation charges, which are set out in your sanction letter and paid directly to the lender. If anyone ever asks you for an advance payment in our name, please stop and call us on " + PHONE_D + " before paying anything."),
 ("Can you guarantee that my loan will be approved?",
  "No, and you should be cautious of anyone who says they can. Approval, the sanctioned amount, the interest rate and every condition are determined by the lending institution after its own assessment of your income, credit history, documentation and, where applicable, the property or vehicle. What we can do is help you understand where you are likely to stand and make sure your application is presented properly and completely."),
 ("How long does the process take?",
  "It depends entirely on the product and the lender. Unsecured products are generally quicker than secured ones, because secured lending involves valuation and legal verification of the asset. We will give you a realistic timeline for your specific case at the start rather than a number we cannot stand behind."),
 ("What documents will I need?",
  "For most applications: identity and address proof, recent bank statements, and proof of income — salary slips and Form 16 if you are salaried, or income tax returns and GST filings if you are self-employed. Home loans and loans against property additionally require the property documents. We will give you a precise checklist once we know which product fits."),
 ("Can I speak with someone in Hindi?",
  "Yes. We work in Hindi and English, on the phone, on WhatsApp and on this website. Use the EN / हिं switch in the menu to read the site in Hindi, and the assistant at the bottom of the page replies in whichever language you write in."),
 ("Is my personal information safe?",
  "Your information is used to assess your requirement and, with your consent, to submit an application to the lending institutions you authorise. We do not sell or rent your data. Our Privacy Policy sets out exactly what we collect and why, and you can ask us to delete anything we are not legally required to keep."),
 ("Which areas do you serve?",
  "We work with customers across Delhi NCR and Uttar Pradesh, and can assist applicants elsewhere in India as well, since documents are shared electronically and the lender's own verification happens locally. Please confirm your location when you enquire so we can tell you what is practical."),
]

def service_cards():
    out = ""
    for i,(href,artk,ic,name,desc,feats) in enumerate(SERVICES):
        f = "".join(f"<li>{x}</li>" for x in feats)
        out += f"""<article class="svc" data-rv data-delay="{(i%2)*110}">
  <div class="svc-art">{art(artk, i)}<span class="tag">{I[ic]}{name}</span></div>
  <div class="svc-b">
    <h3>{name}</h3>
    <p>{desc}</p>
    <ul class="card-feats">{f}</ul>
    <div class="svc-act">
      <a class="btn btn-gold btn-sm" href="contact.html#enquiry" data-enquire data-ev="enquire_{artk}">Enquire Now</a>
      <a class="tlink" href="{href}">Learn more {I['arrow']}</a>
    </div>
  </div>
</article>"""
    return out

SCHEMA = ld(ORG, WEBSITE, crumbs([("Home","")]), faq_schema(FAQS[:6]),
  {"@type":"Service","@id":SITE+"/#service","name":"Loan assistance and application support",
   "serviceType":"Loan distribution and application assistance",
   "provider":{"@id":SITE+"/#organization"},
   "areaServed":{"@type":"Country","name":"India"},
   "availableChannel":{"@type":"ServiceChannel","servicePhone":"+"+PHONE,
     "serviceUrl":SITE+"/contact.html","availableLanguage":["en-IN","hi-IN"]},
   "hasOfferCatalog":{"@type":"OfferCatalog","name":"Loan products we assist with",
     "itemListElement":[{"@type":"Offer","itemOffered":{"@type":"LoanOrCredit","name":n,"url":SITE+"/"+h,"currency":"INR"}}
                        for h,n,_,_ in ALL_PRODUCTS]}})

BODY = f"""
<main id="main">

<!-- ================= HERO ================= -->
<section class="hero">
  <canvas id="shader" aria-hidden="true"></canvas>
  <canvas class="hero-rupees" data-herorupees aria-hidden="true"></canvas>
  <div class="hero-in">
    <div class="wrap">
      <h1 class="hero-h" data-hi="एक बातचीत।<br>छह रिजेक्शन नहीं।<br><em>होम लोन 7.35%* सालाना से।</em>">
        One conversation.<br>
        Not six rejections.<br>
        <em>Home loans from 7.35%* p.a.</em>
      </h1>

      <p class="hero-sub" data-hi="हर आवेदन आपकी क्रेडिट रिपोर्ट पर दर्ज होता है। हम पहले यह तय करते हैं कि कौन सा बैंक आपकी प्रोफ़ाइल पर हाँ कहेगा — फिर एक ही जगह आवेदन करते हैं।">
        Every application leaves a mark on your credit report. We work out which lender fits your
        profile first, then apply once — in Hindi or English, with no advance fee.
      </p>

      <div class="hero-cta">
        <a class="btn btn-gold btn-lg" href="contact.html#enquiry" data-enquire data-ev="hero_enquire">
          <span data-hi="पूछताछ शुरू कीजिए">Start your enquiry</span>{I['user']}</a>
        <a class="hero-call" href="tel:+{PHONE}" data-ev="call_hero">
          {I['phone']}<span>{PHONE_D}</span></a>
      </div>

      {rate_meter()}

      <p class="hero-foot">
        *General market rate for home loans, November 2026 — not {SHORT}&rsquo;s terms and not an offer.
        Approval, the rate and every condition are decided by the lending institution.
        <a href="disclaimer.html">Read the full disclaimer</a>
      </p>
    </div>
  </div>

  <div class="hero-strip" aria-hidden="true">
    <div class="wrap">
      <div class="strip-grid">
        <a class="strip-c" href="personal-loan.html"><span class="sc-k">01</span><b>Personal Loans</b><i>No collateral &middot; 1–7 years</i></a>
        <a class="strip-c" href="home-loan.html"><span class="sc-k">02</span><b>Home Loans</b><i>Purchase &middot; build &middot; transfer</i></a>
        <a class="strip-c" href="car-loan.html"><span class="sc-k">03</span><b>Car Loans</b><i>New &middot; pre-owned</i></a>
        <a class="strip-c" href="business-loan.html"><span class="sc-k">04</span><b>Business Loans</b><i>Working capital &middot; equipment</i></a>
      </div>
    </div>
  </div>
</section>

{stats_band()}

<!-- ================= TRUST INTRODUCTION (spec §5) ================= -->
<section class="sec" id="approach">
  {deco(("ring","tr",430,.055),("dots","bl",200,.05))}{orb("tr",560,"gold")}
  <div class="wrap">
    <div class="split-wide" style="margin-bottom:3.2rem;align-items:end">
      <div data-rv="l">
        <span class="eyebrow" data-n="01">Our approach</span>
        <h2 data-hi="<span class='t-xs t-mute'>हमारा तरीक़ा</span>आपके हिसाब से बनी<br><em class='g-gold'>वित्तीय सलाह।</em>"><span class="g-navy">Financial Guidance</span><br><span class="t-md t-thin t-mute">Built</span> <em class="g-gold">Around You.</em></h2>
      </div>
      <div data-rv="r" style="padding-bottom:.6rem">
        <p class="lead" style="margin:0" data-hi="हर आवेदक की स्थिति अलग होती है। हम पहले आपकी ज़रूरत और चुकाने की क्षमता समझते हैं, फिर बताते हैं कि कौन से विकल्प मौजूद हैं और बैंक किन बातों को देखता है।">
          Every applicant's situation is different. We start by understanding what you need and what you can comfortably repay, then explain which options exist and what a lending institution will look at. No pressure, and no promises we are not in a position to keep.
        </p>
      </div>
    </div>
    <div class="grid g4">
      {''.join(f'''<div class="card" data-rv data-delay="{i*90}"><div class="ci">{I[ic]}</div>
      <h3>{t}</h3><p style="margin:0">{d}</p></div>''' for i,(ic,t,d) in enumerate(TRUST))}
    </div>
  </div>
</section>

<!-- ================= SERVICES (spec §5) ================= -->
<section class="sec cream" id="services">
  {deco(("roof","tl",380,.05),("coin","br",320,.045))}{orb("bl",600,"navy")}
  <div class="wrap">
    <div class="center" data-rv style="max-width:640px;margin-inline:auto;margin-bottom:3.2rem">
      <div class="orn"><i></i></div>
      <span class="eyebrow c" data-n="02">What we assist with</span>
      <h2 data-hi="चार <em class='g-gold'>मुख्य</em> लोन सेवाएँ"><span class="t-md t-thin t-mute">Four</span> <em class="g-gold t-lg">core</em> <span class="g-navy">loan services</span></h2>
      <p class="lead" style="margin-top:1rem" data-hi="हर प्रोडक्ट का अपना पेज है, जहाँ पात्रता, दस्तावेज़ और प्रक्रिया विस्तार से दी गई है।">
        Each product has its own page explaining eligibility, documentation and the application process in detail.
      </p>
    </div>
    <div class="grid g2">{service_cards()}</div>

    <div class="notice" data-rv style="margin-top:2.2rem">
      {I['doc']}
      <span>We also assist with <a href="loan-against-property.html" style="color:var(--gold-400);font-weight:600">Loan Against Property</a>,
      and with <a href="other-loans.html" style="color:var(--gold-400);font-weight:600">education, gold, credit card and insurance</a> products.
      Availability of any specific facility depends on the lending institutions we are empanelled with at the time of your enquiry —
      please confirm with us before planning around it.</span>
    </div>
  </div>
</section>

<!-- ================= HOW IT WORKS (spec §8) ================= -->
<section class="sec">
  {deco(("rays","r",400,.06),("arc","bl",360,.05))}{orb("tr",520,"gold")}
  <div class="wrap">
    <div class="split-wide" style="margin-bottom:2.4rem;align-items:end">
      <div data-rv="l">
        <span class="eyebrow" data-n="03">How it works</span>
        <h2 data-hi="पूछताछ से<br><em class='g-gold'>फ़ैसले तक।</em>"><span class="t-md t-thin t-mute">From</span> <span class="g-navy">enquiry</span><br><span class="t-md t-thin t-mute">to</span> <em class="g-gold t-lg">decision.</em></h2>
      </div>
      <div data-rv="r" style="padding-bottom:.6rem">
        <p class="lead" style="margin:0">Six steps. Most of it happens over the phone and WhatsApp, and you are told at each stage exactly what happens next.</p>
      </div>
    </div>
    <div class="flow">
      {''.join(f'''<div class="flow-i" data-rv data-delay="{i*70}"><div class="flow-n" aria-hidden="true"></div>
        <div class="flow-b"><h3>{t}</h3><p data-hi="{hi}">{d}</p></div></div>''' for i,(t,d,hi) in enumerate(STEPS))}
    </div>
    <div class="notice gold" data-rv style="margin-top:1.6rem">
      {I['shield']}
      <span><b>Please note.</b> Final eligibility, sanction and disbursement are determined solely by the relevant
      lending institution, under its own credit policy and verification process. {SHORT} assists with the
      application; it does not approve loans and cannot guarantee any outcome.</span>
    </div>
    <div class="center" style="margin-top:2.2rem" data-rv>
      <a class="btn btn-ghost" href="how-it-works.html">See the full process {I['arrow']}</a>
    </div>
  </div>
</section>

<!-- ================= EMI CALCULATOR (spec §7) ================= -->
<section class="sec wash" id="emi">
  {deco(("coin","tl",420,.05),("grid","br",340,.04))}{orb("br",620,"gold")}
  <div class="wrap">
    <div class="center" data-rv style="max-width:620px;margin-inline:auto;margin-bottom:3rem">
      <span class="eyebrow c" data-n="04">Plan before you borrow</span>
      <h2 data-hi="पहले <em class='g-gold'>EMI</em> देखिए,<br>फिर फ़ैसला कीजिए।"><span class="t-md t-thin t-mute">Estimate the</span><br><em class="g-gold t-lg">EMI</em> <span class="g-navy">first.</span></h2>
      <p class="lead" style="margin-top:1rem" data-hi="यह सिर्फ़ अनुमान है। असली EMI वही होगी जो बैंक के सैंक्शन लेटर में लिखी होगी।">
        An illustrative estimate, not a quotation. Your actual instalment is the one stated in the lender's sanction letter.
      </p>
    </div>
    {calc_block(amount=1000000, rate=9.5, years=15, amax=20000000, with_attach=False)}
    <div class="center" style="margin-top:2rem" data-rv>
      <a class="btn btn-ghost" href="emi-calculator.html">Open the full calculator {I['arrow']}</a>
    </div>
  </div>
</section>

<!-- ================= LANGUAGE ================= -->
<section class="sec">
  {deco(("arc","tr",400,.055),("dots","bl",220,.05))}
  <div class="wrap">
    <div class="split-flip">
      <div data-rv="l">
        <div class="hindi-box">
          <h4>लोन लेना मुश्किल नहीं — समझ न आना मुश्किल है।</h4>
          <p>ज़्यादातर लोगों की दिक़्क़त यह नहीं होती कि लोन मिलता नहीं। दिक़्क़त यह होती है कि यह साफ़ समझ ही नहीं आता कि कौन सा विकल्प उनके लिए सही है, कौन से कागज़ लगेंगे, और पूरी अवधि में असल ख़र्च कितना आएगा।</p>
          <p>हम यही हिस्सा आसान करते हैं — <b>पूरी बात हिंदी में</b>। कॉल पर, WhatsApp पर, और इस वेबसाइट पर भी। ऊपर मेन्यू में <b>हिं</b> दबाइए, या नीचे दाईं तरफ़ चैट खोलिए।</p>
          <p><b>कोई एडवांस पैसा नहीं। कोई छिपा हुआ चार्ज नहीं।</b> बैंक की जो भी फ़ीस होगी, वह सैंक्शन लेटर में लिखी होगी और सीधे बैंक को जाएगी।</p>
          <div class="btn-row" style="margin-top:1.4rem">
            <a class="btn btn-gold btn-sm" href="tel:+{PHONE}" data-ev="call_hindi">{I['phone']}हिंदी में बात करें</a>
            <button class="btn btn-ghost btn-sm" type="button" data-bot data-ev="bot_hindi">{I['bot']}चैट खोलें</button>
          </div>
        </div>
      </div>
      <div data-rv="r">
        <span class="eyebrow" data-n="05">Spoken plainly</span>
        <h2><span class="t-md t-thin t-mute">We explain it in</span><br><em class="g-gold">the language you think in.</em></h2>
        <p class="lead" style="margin-top:1.1rem">A sanction letter is not light reading, and neither is a Key Facts Statement. We will go through what you are signing, what it costs across the full tenure, and what happens if you want to prepay — in Hindi or English, whichever is easier for you.</p>
        <ul class="card-feats" style="margin-top:1.6rem">
          <li>The whole website switches with the <b>EN / हिं</b> control in the menu</li>
          <li>The assistant replies in whichever language you write in</li>
          <li>Every charge explained before you sign, not after</li>
        </ul>
        <a class="tlink" href="about.html" style="margin-top:1.4rem">More about how we work {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<!-- ================= SOCIAL ================= -->
{rating_pill()}

<section class="sec-sm dark" style="padding-block:clamp(3rem,5vw,4.5rem)">
  {deco(("ring","tr",420,.1),("rays","bl",300,.08))}{orb("tr",580,"gold")}
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div data-rv="l">
        <span class="eyebrow on-dark" data-n="06">Follow us</span>
        <h2 style="font-size:clamp(1.7rem,3.2vw,2.5rem)"><span class="g-light">Plain-language finance,</span><br><em class="g-gold">posted regularly.</em></h2>
        <p style="color:#A9C0DB;margin-top:1rem;max-width:48ch">Short explainers on credit scores, documentation, EMIs and the questions borrowers most often get wrong.</p>
        <a class="tlink" href="blog.html" style="margin-top:1.2rem;color:#fff;border-color:rgba(223,186,107,.5)">Visit the Knowledge Centre {I['arrow']}</a>
      </div>
      <div data-rv="r">
        <div class="socials" style="gap:.8rem">
          <a class="soc ig" style="width:64px;height:64px;border-radius:18px" href="{SOCIAL['ig']}" target="_blank" rel="noopener me" aria-label="Instagram" data-ev="social_ig">{I['ig']}</a>
          <a class="soc fb" style="width:64px;height:64px;border-radius:18px" href="{SOCIAL['fb']}" target="_blank" rel="noopener me" aria-label="Facebook" data-ev="social_fb">{I['fb']}</a>
          <a class="soc li" style="width:64px;height:64px;border-radius:18px" href="{SOCIAL['li']}" target="_blank" rel="noopener me" aria-label="LinkedIn" data-ev="social_li">{I['li']}</a>
          <a class="soc yt" style="width:64px;height:64px;border-radius:18px" href="{SOCIAL['yt']}" target="_blank" rel="noopener me" aria-label="YouTube" data-ev="social_yt">{I['yt']}</a>
          <a class="soc wa" style="width:64px;height:64px;border-radius:18px" href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="WhatsApp" data-ev="social_wa">{I['wa']}</a>
        </div>
        <p style="font-size:.84rem;color:#7D93AE;margin-top:1.2rem">@anscapitalservices</p>
      </div>
    </div>
  </div>
</section>

{promise_ring()}
{testimonials()}

{gmb_block()}
{gradient_band()}
{faq_block(FAQS, "Frequently asked questions")}
{cta_band()}
</main>
"""

html = page(
  title="ANS Capital Services Pvt. Ltd. | Personal, Home, Car & Business Loan Assistance",
  desc="ANS Capital Services Private Limited helps you understand and apply for personal, home, car and business loans. Assistance with eligibility, documentation and the application process, in Hindi and English. Call +91 93196 67592.",
  path="index.html", body=BODY, active="index.html",
  keywords="personal loan assistance, home loan assistance, car loan assistance, business loan assistance, loan agent India, loan application help, ANS Capital Services, loan assistance Delhi NCR, loan assistance Uttar Pradesh",
  schema=SCHEMA)
open("index.html","w").write(html)
print("index.html", f"{len(html):,}", "bytes")
