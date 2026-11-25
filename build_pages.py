# -*- coding: utf-8 -*-
"""Services, How It Works, FAQs, Knowledge Centre, Cookie Policy, Enquiry Consent."""
from gen_core import *
from gen_parts import *
from build_home import SERVICES, STEPS, FAQS as HOME_FAQS

out = []

# ============================================================ OUR SERVICES
EXTRA = [
 ("loan-against-property.html","property","building","Loan Against Property",
  "Finance raised against residential, commercial or industrial property you already own, without selling it.",
  ["Secured against property you own","Larger amounts than unsecured products","Longer tenures than a personal loan","Property remains in your name"]),
 ("other-loans.html","other","grad","Education, Gold, Cards &amp; Insurance",
  "Education finance for study in India or abroad, gold loans, credit cards and insurance products.",
  ["Education loans with deferred repayment","Gold loans against jewellery","Credit card applications","Life, health and general insurance"]),
]

def svc_grid(items, start=0):
    o = ""
    for i,(href,artk,ic,name,desc,feats) in enumerate(items):
        f = "".join(f"<li>{x}</li>" for x in feats)
        o += f"""<article class="svc" data-rv data-delay="{(i%2)*110}">
  <div class="svc-art">{art(artk, start+i)}<span class="tag">{I[ic]}{name}</span></div>
  <div class="svc-b"><h3>{name}</h3><p>{desc}</p><ul class="card-feats">{f}</ul>
    <div class="svc-act">
      <a class="btn btn-gold btn-sm" href="contact.html#enquiry" data-enquire>Enquire Now</a>
      <a class="tlink" href="{href}">Learn more {I['arrow']}</a>
    </div>
  </div></article>"""
    return o

SERV_FAQ = [
 ("Which of these can ANS actually arrange for me?",
  "That depends on the lending institutions we are empanelled with at the time you enquire, and on your own profile. The pages on this website explain each product as it works in the market generally. Before you plan around any particular facility, call us and we will tell you plainly what is available for your situation."),
 ("Do you charge differently for different products?",
  "We charge applicants nothing in advance for any product. Lenders levy their own processing and documentation charges, which vary by product and institution and are always set out in the sanction letter before you sign."),
 ("Can you help if I have been refused elsewhere?",
  "Often, yes — a refusal by one lender is not a refusal by all of them, because each applies its own credit policy. What matters is understanding why the refusal happened. Tell us what you were told, and we will give you an honest view on whether another application now makes sense or whether it is better to wait and address the underlying issue first."),
 ("Can I apply for more than one product at the same time?",
  "You can, but it is rarely a good idea. Each application creates a hard enquiry on your credit report, and several at once can work against you. We would normally recommend identifying the single most suitable product first."),
]

SERVICES_BODY = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">Our Services</span></nav>
    <div class="split-wide" style="align-items:end">
      <div><span class="eyebrow on-dark">What we do</span>
        <h1 data-hi="हमारी <em class='g-gold g-anim'>सेवाएँ</em>"><span class="t-md t-thin t-mute">Our</span><br><em class="g-gold g-anim t-lg">Services</em></h1></div>
      <div style="padding-bottom:.4rem">
        <p class="lead">We help customers understand which financing options suit their requirement, prepare the documentation properly, and take the application through to a decision by the lending institution.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("ring","tr",440,.055),("dots","bl",210,.05))}{orb("tr",560,"gold")}
  <div class="wrap">
    <div class="center" data-rv style="max-width:640px;margin-inline:auto;margin-bottom:3rem">
      <div class="orn"><i></i></div>
      <span class="eyebrow c" data-n="01">Core products</span>
      <h2><span class="t-md t-thin t-mute">The four we are</span><br><em class="g-gold">asked for most</em></h2>
    </div>
    <div class="grid g2">{svc_grid(SERVICES, 10)}</div>
  </div>
</section>

<section class="sec cream">
  {deco(("roof","tl",400,.05),("coin","br",320,.05))}{orb("bl",580,"navy")}
  <div class="wrap">
    <div class="center" data-rv style="max-width:640px;margin-inline:auto;margin-bottom:3rem">
      <span class="eyebrow c" data-n="02">Also arranged</span>
      <h2><em class="g-gold t-lg">Additional</em><br><span class="g-navy">services</span></h2>
      <p class="lead" style="margin-top:1rem">Subject to availability through the lending institutions we work with at the time of your enquiry.</p>
    </div>
    <div class="grid g2">{svc_grid(EXTRA, 20)}</div>
    {availability_notice("Each of the products on this page")}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div data-rv="l">
        <span class="eyebrow" data-n="03">What assistance includes</span>
        <h2><span class="t-md t-thin t-mute">What you</span> <em class="g-gold">actually get</em><br><span class="g-navy">from us.</span></h2>
        <p class="lead" style="margin-top:1.1rem">Our role is practical rather than promotional. In plain terms, here is what we do on a file.</p>
        <ul class="card-feats" style="margin-top:1.6rem">
          <li>An honest read of where your profile is likely to stand</li>
          <li>An explanation of which products suit the requirement, and which do not</li>
          <li>A precise document checklist, and a review of every document before submission</li>
          <li>Submission of the application to the lending institutions you authorise</li>
          <li>Follow-up through underwriting, and help answering the lender's queries</li>
          <li>A clear explanation of the sanction terms before you sign anything</li>
        </ul>
      </div>
      <div data-rv="r">
        <div class="card" style="background:linear-gradient(160deg,var(--navy),var(--navy-900));border:0;color:#fff">
          <h3 style="color:#fff;margin-bottom:.6rem">What we do not do</h3>
          <p style="color:#A9C0DB;font-size:.95rem">Being clear about this saves everybody time.</p>
          <ul class="card-feats" style="margin-top:1.2rem">
            <li style="color:#C3D2E4">We do not lend money — we are not a bank or an NBFC</li>
            <li style="color:#C3D2E4">We do not approve loans or decide your interest rate</li>
            <li style="color:#C3D2E4">We do not promise approval, and we will not pretend to</li>
            <li style="color:#C3D2E4">We do not ask for advance cash, OTPs, passwords or card PINs</li>
          </ul>
          <div class="btn-row" style="margin-top:1.6rem">
            <a class="btn btn-gold btn-sm" href="contact.html#enquiry" data-enquire>Enquire Now</a>
            <a class="btn btn-ghost-light btn-sm" href="tel:+{PHONE}" data-ev="call_services">{I['phone']}{PHONE_D}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{faq_block(SERV_FAQ, "About our services")}
{cta_band()}
</main>
"""
out.append(("services.html", page(
  "Our Services | Loan Assistance — ANS Capital Services Pvt. Ltd.",
  "Personal, home, car and business loan assistance from ANS Capital Services Private Limited, plus loan against property, education, gold, credit card and insurance products subject to availability.",
  "services.html", SERVICES_BODY, "services.html",
  "loan services India, loan assistance, personal home car business loan help, loan against property assistance, education loan assistance",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("Our Services","services.html")]), faq_schema(SERV_FAQ),
     {"@type":"CollectionPage","@id":SITE+"/services.html#webpage","url":SITE+"/services.html",
      "name":"Our Services","isPartOf":{"@id":SITE+"/#website"},"inLanguage":"en-IN"}))))

# ============================================================ HOW IT WORKS
HIW_FAQ = [
 ("Who decides whether my loan is approved?",
  "The lending institution, and only the lending institution. It applies its own credit policy, verifies your documents and income, and where a property or vehicle is involved, has it valued. ANS Capital Services prepares and submits the application and follows it up — it has no role in the credit decision and cannot influence or guarantee the outcome."),
 ("What happens if the lender declines my application?",
  "We will tell you what reason was given, where one is given. Depending on that reason, the sensible next step may be a different lender whose policy fits your profile better, a different product, or waiting a few months to address the underlying issue. We will say honestly which of those applies rather than simply submitting the file somewhere else."),
 ("Do I need to visit an office?",
  "For most of the process, no. Documents and clarifications can be handled over WhatsApp and email. You may need to meet the lender's representative where its own process requires it — for example, property verification on a home loan or a loan against property, or signing at disbursal."),
 ("How will I know what is happening with my application?",
  "We update you at each stage — when the file is submitted, when the lender raises a query, and when a decision is communicated. If you would rather be updated on WhatsApp than by phone, tell us and we will do that."),
]

HIW_BODY = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">How It Works</span></nav>
    <div class="split-wide" style="align-items:end">
      <div><span class="eyebrow on-dark">The process</span>
        <h1 data-hi="यह <em class='g-gold g-anim'>कैसे</em> काम करता है"><span class="t-md t-thin t-mute">How It</span><br><em class="g-gold g-anim t-lg">Works</em></h1></div>
      <div style="padding-bottom:.4rem">
        <p class="lead">Six steps from your first message to the lender's decision. You are told what happens next at every stage, and nothing is submitted anywhere without your say-so.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("rays","r",420,.06),("arc","bl",380,.05))}{orb("tr",540,"gold")}
  <div class="wrap-n">
    <div class="flow">
      {''.join(f'''<div class="flow-i" data-rv data-delay="{i*70}"><div class="flow-n" aria-hidden="true"></div>
        <div class="flow-b"><h3>{t}</h3><p data-hi="{hi}">{d}</p></div></div>''' for i,(t,d,hi) in enumerate(STEPS))}
    </div>

    <div class="notice gold" data-rv style="margin-top:1.8rem">
      {I['shield']}
      <span><b>Final eligibility, sanction and disbursement are determined by the relevant lending institution.</b>
      {SHORT} is a loan distribution company. It assists with understanding options, preparing documentation and
      submitting applications. It does not lend, does not approve applications, does not set interest rates, and
      cannot guarantee any outcome.</span>
    </div>

    <div class="hindi-box" data-rv style="margin-top:2rem">
      <h4>प्रक्रिया — हिंदी में</h4>
      <p><b>1. पूछताछ:</b> फ़ोन, WhatsApp या फ़ॉर्म से अपनी ज़रूरत बताइए।<br>
         <b>2. बातचीत:</b> रकम, ज़रूरत, आमदनी और मौजूदा EMI पर बात।<br>
         <b>3. विकल्प:</b> कौन सा प्रोडक्ट सही है और ख़र्च कितना — सब समझाया जाता है।<br>
         <b>4. कागज़ात:</b> पूरी चेकलिस्ट, और जमा करने से पहले हर कागज़ की जाँच।<br>
         <b>5. बैंक की जाँच:</b> बैंक या NBFC अपनी जाँच और मूल्यांकन करता है।<br>
         <b>6. फ़ैसला:</b> मंज़ूरी, रकम और ब्याज दर बैंक तय करता है और सैंक्शन लेटर में देता है।</p>
      <p style="margin-top:.8rem"><b>ज़रूरी बात:</b> लोन मंज़ूर होगा या नहीं, यह पूरी तरह बैंक या NBFC तय करता है। हम आवेदन में मदद करते हैं — मंज़ूरी की गारंटी कोई नहीं दे सकता, और जो दे, उससे सावधान रहिए।</p>
    </div>

    <div class="split" style="margin-top:clamp(3rem,5vw,4.5rem);align-items:start">
      <div data-rv="l">
        <span class="eyebrow" data-n="02">Before you start</span>
        <h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)"><span class="t-md t-thin t-mute">Four things</span><br><em class="g-gold">worth knowing</em></h2>
      </div>
      <div class="prose" data-rv="r">
        <h3>Apply once, not everywhere</h3>
        <p>Every application creates a hard enquiry on your credit report. Several at the same time can count against you, and a string of refusals becomes a reason for the next refusal. Identifying the right lender first is worth more than speed.</p>
        <h3>Your credit record matters more than anything else</h3>
        <p>For most unsecured products it is the single biggest influence on whether you are approved and at what price. If yours has a problem, it is usually better to know that before applying than after.</p>
        <h3>A complete file moves faster than a quick one</h3>
        <p>Applications are most often delayed by a missing page, a name mismatch across documents or an unexplained credit in a bank statement — not by the lender being slow.</p>
        <h3>Read the sanction letter and the Key Facts Statement</h3>
        <p>These are the documents that actually bind you. The rate, the fees, the prepayment terms and the reset conditions are all there. We will go through them with you line by line before you sign.</p>
      </div>
    </div>
  </div>
</section>

{faq_block(HIW_FAQ, "Questions about the process")}
{cta_band()}
</main>
"""
out.append(("how-it-works.html", page(
  "How It Works | Loan Application Process — ANS Capital Services Pvt. Ltd.",
  "The six-step loan assistance process at ANS Capital Services Private Limited — from enquiry and document preparation to the lending institution's decision. Final sanction rests with the lender.",
  "how-it-works.html", HIW_BODY, "how-it-works.html",
  "loan application process India, how to apply for a loan, loan documentation process, loan approval process, loan assistance steps",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("How It Works","how-it-works.html")]), faq_schema(HIW_FAQ),
     {"@type":"HowTo","@id":SITE+"/how-it-works.html#howto",
      "name":"How to apply for a loan with assistance from ANS Capital Services",
      "description":"The steps involved in enquiring about, preparing and submitting a loan application, and how the lending institution reaches its decision.",
      "step":[{"@type":"HowToStep","position":i+1,"name":t,"text":d} for i,(t,d,_) in enumerate(STEPS)]}))))

for name, html in out:
    open(name,"w").write(html)
    print(f"{name:26s} {len(html):>8,} bytes")
