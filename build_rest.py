# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

out = []

# ============================================================== ABOUT
ABOUT_FAQ = [
 ("Is ANS Capital Services a registered company?",
  "Yes. ANS Capital Services Private Limited is a registered private limited company incorporated under the Companies Act, operating as a loan distribution business and an authorised Channel Partner of Ruloans. We are a distributor and Direct Selling Agent, not a bank or an NBFC, and we do not lend our own money."),
 ("What exactly does a DSA or channel partner do?",
  "A Direct Selling Agent sits between you and the lending market. We take your profile, work out which lender programmes you genuinely qualify for, prepare and pre-check the file, submit it, follow it through underwriting and stay on it until disbursal. The bank or NBFC makes the credit decision and lends the money; we make sure your case reaches the right desk in the right shape."),
 ("How do you earn if I pay you nothing?",
  "The lender pays us a distribution commission after your loan is disbursed. That is the whole of our income, and it is why we charge you nothing upfront. It also means we are only paid when a loan actually completes — which aligns us with getting you a sanction you will accept, rather than collecting application fees."),
 ("Does that commission bias which lender you recommend?",
  "It is a fair question and the honest answer is that commission rates do differ between lenders. Our position is that a borrower who is placed badly does not come back and does not refer anyone, which costs far more than the difference on one file. We will show you the comparison — rate, fee, tenure and conditions — and you make the choice. If you ask us whether a product is worth taking at all, you will get a straight answer, including no."),
 ("Which areas do you cover?",
  "We are based in the Delhi NCR region and work extensively across Delhi, Noida, Ghaziabad, Meerut, Gurugram, Faridabad and the surrounding Uttar Pradesh belt. Because the lender network is national, we also handle files from anywhere in India — documents move over WhatsApp and email, and the lender's own verification happens locally."),
 ("Can I speak to someone in Hindi?",
  "Yes, and most of our conversations are in Hindi or a mix of Hindi and English. The website carries an EN / हिं toggle, the assistant on this page works in both languages, and every explanation we give you — including what you are signing — can be in whichever language you are comfortable in."),
]

VALUES = [
 ("shield","We say no when no is the answer","The easiest money in this business comes from placing a loan someone should not take. We would rather tell you to wait three months and repair your score, or that a balance transfer is not worth the cost on your numbers."),
 ("doc","Every charge, before you sign","The processing fee, the insurance attached to the loan, the foreclosure clause, the rate reset. We go through them with you in advance. Nobody should discover a charge at disbursal."),
 ("handshake","One application, not six","Each application is a hard enquiry on your credit report, and a stack of rejections becomes the reason for the next one. We match first and apply once."),
 ("clock2","We stay on the file","Submitting an application is the easy part. Following it through underwriting, answering the queries and chasing disbursal is where files actually get won or lost."),
]

ABOUT = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">About Us</span></nav>
    <div class="split-wide" style="align-items:end">
      <div>
        <span class="eyebrow on-dark">About the company</span>
        <h1 data-hi="एक छोटा डेस्क।<br><em class='g-gold g-anim'>एक बहुत बड़ा नेटवर्क।</em>"><span class="t-md t-thin t-mute">A small desk.</span><br><em class="g-gold g-anim t-lg">A very large network.</em></h1>
      </div>
      <div style="padding-bottom:.4rem">
        <p class="lead">ANS Capital Services Private Limited is a registered loan distribution company and an authorised Channel Partner of Ruloans. We arrange finance — we do not lend it — and we are paid by the lender, never by you.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("ring","tr",430,.05),("dots","bl",200,.045))}{orb("tr",540,"gold")}
  <div class="wrap">
    <div class="split-wide" style="align-items:start">
      <div data-rv="l">
        <span class="eyebrow" data-n="01">Our role</span>
        <h2><span class="g-navy">What we are,</span><br><em class="g-gold">and what we are not.</em></h2>
      </div>
      <div class="prose" data-rv="r">
        <p class="lead">India does not have a shortage of lenders. It has a shortage of people willing to sit with a borrower and explain, in plain language, which of those lenders will actually say yes — and what the money will truly cost across the full tenure.</p>
        <p>That is the gap ANS Capital Services works in. We are a distribution business: we read your profile honestly, match it against the lender programmes in the Ruloans network, prepare the file so it survives underwriting, and stay with it until the money reaches your account. The sanction is the bank's decision, under the bank's credit policy. Our job is to make sure your case arrives at the right desk, properly built.</p>
        <p>We are not a bank. We are not an NBFC. We hold no Reserve Bank of India licence or registration and do not claim one. We do not lend our own money, we do not approve applications, and we never ask you for cash in advance. Our income is the distribution commission a lender pays after a loan disburses — which means we earn nothing unless a loan you chose to accept actually completes.</p>
        <div class="pullq">Anyone can submit an application. The value is in knowing which application not to submit.</div>
        <h3>The network behind the desk</h3>
        <p>ANS Capital Services is a Channel Partner of Ruloans, a loan distribution company. The figures Ruloans publishes about its own scale are set out below and are attributed to it — they describe that organisation, not ANS Capital Services, which is a young company and does not claim them as its own track record.</p>
        <p>What that is intended to mean for you in practice is access to a wider set of lender programmes than a single local agent would have. Which institutions are actually available for your particular application will be confirmed to you when you apply, rather than promised in advance.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="wrap">
    <div class="stats" data-rv>
      <div class="stat"><b class="g-gold"><span data-count="265">265</span><span class="u">+</span></b><span>Partner banks &amp; NBFCs</span></div>
      <div class="stat"><b class="g-gold"><span data-count="25">25</span><span class="u">+</span></b><span>Years in the market</span></div>
      <div class="stat"><b class="g-gold"><span class="u">₹</span><span data-count="30000">30000</span><span class="u">Cr+</span></b><span>Annual network business</span></div>
      <div class="stat"><b class="g-gold"><span data-count="4000">4000</span><span class="u">+</span></b><span>Towns covered</span></div>
    </div>
    <p style="text-align:center;font-size:.82rem;color:#7D93AE;margin-top:1.2rem;max-width:62ch;margin-inline:auto">These figures are published by Ruloans Distribution Services Pvt. Ltd. and describe that company. They are reproduced here for context and are not a claim about ANS Capital Services Private Limited's own experience, customer numbers or track record.</p>
  </div>
</section>

<section class="sec cream">
  {deco(("roof","tl",400,.05),("coin","br",300,.05))}{orb("bl",560,"navy")}
  <div class="wrap">
    <div class="center" data-rv style="max-width:620px;margin-inline:auto;margin-bottom:3rem">
      <div class="orn"><i></i></div>
      <span class="eyebrow c" data-n="02">How we work</span>
      <h2 data-hi="चार बातें जिन पर<br><em class='g-gold'>हम समझौता नहीं करते।</em>"><span class="t-md t-thin t-mute">Four things we</span><br><em class="g-gold">do not compromise on.</em></h2>
    </div>
    <div class="grid g2">
      {''.join(f'''<div class="card" data-rv data-delay="{i*90}"><div class="ci">{I[ic]}</div>
      <h3>{t}</h3><p style="margin:0">{d}</p></div>''' for i,(ic,t,d) in enumerate(VALUES))}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div data-rv="l">
        <div class="hindi-box">
          <h4>हमारे बारे में — हिंदी में</h4>
          <p><b>ANS Capital Services Pvt. Ltd.</b> एक रजिस्टर्ड प्राइवेट लिमिटेड कंपनी है और <b>Ruloans की Channel Partner</b> है। हम ख़ुद बैंक या NBFC नहीं हैं — हम लोन दिलवाते हैं, देते नहीं।</p>
          <p>आपकी एक एप्लिकेशन हम <b>265+ बैंक और NBFC</b> के प्रोग्राम से मिलाते हैं, और जो ऑफ़र वाक़ई आपकी प्रोफ़ाइल पर मिलेगा, वही आपके सामने रखते हैं। फ़ाइल तैयार करने से लेकर पैसा आने तक हम साथ रहते हैं।</p>
          <p><b>आपसे कोई एडवांस पैसा नहीं लिया जाता।</b> हमारी कमाई बैंक से मिलने वाले कमीशन से होती है, और वह भी तभी जब आपका लोन असल में पास होकर डिस्बर्स हो जाए।</p>
          <p>और अगर कोई लोन आपके लिए सही नहीं है, तो हम साफ़ मना भी कर देते हैं — यही हमारा तरीक़ा है।</p>
        </div>
      </div>
      <div data-rv="r">
        <span class="eyebrow" data-n="03">Reach the desk</span>
        <h2>Talk to us before you apply anywhere.</h2>
        <p class="lead" style="margin-top:1.1rem">One conversation costs you nothing and often saves a hard enquiry you did not need to take. Call, WhatsApp, or send your documents and we will come back with where you actually stand.</p>
        <div class="grid" style="gap:.8rem;margin-top:1.8rem">
          <a class="ccard" href="tel:+{PHONE}" data-ev="call_about"><span class="ci2">{I['phone']}</span><span><h4>Call</h4><p>{PHONE_D}</p></span></a>
          <a class="ccard" href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_about"><span class="ci2">{I['wa']}</span><span><h4>WhatsApp</h4><p>Send documents, get a reply</p></span></a>
          <a class="ccard" href="mailto:{EMAIL}"><span class="ci2">{I['mail']}</span><span><h4>Email</h4><p>{EMAIL}</p></span></a>
        </div>
      </div>
    </div>
  </div>
</section>

{faq_block(ABOUT_FAQ, "About ANS Capital Services")}
{cta_band()}
</main>
"""
out.append(("about.html", page(
  "About ANS Capital Services Pvt. Ltd. | Loan DSA & Ruloans Channel Partner",
  "ANS Capital Services Private Limited is a registered loan distribution company and authorised Channel Partner of Ruloans, with access to 265+ partner banks and NBFCs. We arrange loans; we do not lend. Zero advance fee.",
  "about.html", ABOUT, "about.html",
  "about ANS Capital Services, loan DSA company, Ruloans channel partner, loan distributor India, loan agent Delhi NCR, is ANS Capital Services genuine",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("About Us","about.html")]), faq_schema(ABOUT_FAQ),
     {"@type":"AboutPage","@id":SITE+"/about.html#webpage","url":SITE+"/about.html",
      "name":"About ANS Capital Services Pvt. Ltd.","isPartOf":{"@id":SITE+"/#website"},
      "mainEntity":{"@id":SITE+"/#organization"},"inLanguage":"en-IN"}))))

# ============================================================== EMI CALCULATOR
EMI_FAQ = [
 ("How is EMI actually calculated?",
  "Every lender uses the same formula: EMI = P × r × (1+r)^n ÷ ((1+r)^n − 1), where P is the principal, r is the monthly interest rate (the annual rate divided by twelve, then by a hundred) and n is the number of monthly instalments. The EMI stays constant, but its composition changes — early instalments are mostly interest, later ones mostly principal. That is why prepaying in the first third of a loan saves far more than prepaying near the end."),
 ("Why is the bank's EMI different from this calculator?",
  "Three usual reasons. First, the sanctioned rate differs from the rate you assumed here. Second, the lender may deduct the processing fee from the disbursal, so you receive less than the principal you are paying EMI on. Third, some loans bundle an insurance premium into the amount financed. Ask for the amortisation schedule and the Key Facts Statement — both show the real numbers, and the lender is required to provide them."),
 ("Should I pick a longer tenure for a lower EMI?",
  "Only as far as your cash flow genuinely requires. A longer tenure reduces the monthly outgo and increases the total interest substantially. A ₹10 lakh loan at 10% costs about ₹2.75 lakh in interest over five years and about ₹5.86 lakh over ten. Same loan, same rate — the tenure more than doubles the cost. Pick the shortest tenure whose EMI you can carry comfortably, with room for a bad month."),
 ("What is a reducing balance rate, and how is it different from flat rate?",
  "A reducing balance rate charges interest only on the outstanding principal, which falls with every EMI. A flat rate charges interest on the full original amount for the whole tenure. A 10% flat rate is roughly equivalent to an 18% to 19% reducing rate — nearly double. All bank loans quote reducing balance; some smaller lenders and dealer schemes quote flat. Always ask which one is being quoted before you compare two offers."),
 ("Does prepaying actually help, and when?",
  "Substantially, and earlier is better. Because the front of the schedule is interest-heavy, a prepayment in year two removes far more future interest than the same amount in year twelve. On a floating-rate loan taken by an individual there is no prepayment charge, so an annual lump sum — a bonus, a maturity — is pure saving. One extra EMI every year on a twenty-year home loan typically takes four to five years off the tenure."),
 ("How much EMI can I afford?",
  "Lenders cap total EMIs at roughly 50% to 60% of net monthly income, but that is their risk limit, not your comfort limit. A more practical personal rule is to keep all EMIs under 40% of take-home pay, leaving room for a month of illness, a slow quarter or a job change. If the EMI only fits at the lender's maximum, the loan is probably larger than it should be."),
]

EMI_BODY = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">EMI Calculator</span></nav>
    <div class="split-wide" style="align-items:end">
      <div>
        <span class="eyebrow on-dark">Free tool</span>
        <h1 data-hi="EMI <em class='g-gold g-anim'>कैलकुलेटर</em>"><span class="t-md t-thin t-mute">EMI</span><br><em class="g-gold g-anim t-lg">Calculator</em></h1>
      </div>
      <div style="padding-bottom:.4rem">
        <p class="lead">Move the sliders and see the monthly instalment, the total interest and what the loan really costs across its full life. No sign-up, no form, nothing recorded.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="calculator">
  {deco(("coin","tl",420,.05),("grid","br",340,.04))}{orb("br",600,"gold")}
  <div class="wrap">
    {calc_block(amount=2500000, rate=8.5, years=20, amax=50000000, with_attach=True)}

    <div class="split" style="margin-top:clamp(3.5rem,6vw,5.5rem);align-items:start">
      <div class="prose" data-rv="l">
        <h2 style="margin-top:0"><span class="t-md t-thin t-mute">Reading the number</span><br><em class="g-gold">properly</em></h2>
        <p>The EMI is the figure everyone looks at, and it is the least informative one on the page. Two loans with the same EMI can differ by lakhs in total cost, because the tenure quietly does the work.</p>
        <p>Watch the <b>total interest</b> figure instead, and the gold-to-grey bar beneath it. When the grey portion approaches or exceeds the gold, you are paying as much for the money as the thing you bought with it. That is normal on a thirty-year home loan and a warning sign on a five-year personal loan.</p>
        <h3>The three levers</h3>
        <ul>
          <li><b>Amount</b> — the only one fully in your control before you borrow. Borrowing 10% less is the cleanest saving available.</li>
          <li><b>Rate</b> — set by your credit profile and the lender you reach. This is where we add value: the same profile is priced differently across the network.</li>
          <li><b>Tenure</b> — the lever people pull to make an EMI fit, and the most expensive one. Shorten it the moment your cash flow allows.</li>
        </ul>
        <div class="pullq">If the EMI only works at the longest tenure available, the loan is bigger than it should be.</div>
      </div>
      <div data-rv="r">
        <div class="hindi-box">
          <h4>EMI को समझिए — हिंदी में</h4>
          <p><b>EMI क्या है:</b> हर महीने की वह किस्त जिसमें ब्याज और मूलधन दोनों शामिल होते हैं। शुरू के सालों में ज़्यादातर हिस्सा ब्याज का होता है — इसलिए <b>शुरुआत में किया गया प्री-पेमेंट</b> सबसे ज़्यादा बचत कराता है।</p>
          <p><b>लंबी अवधि का जाल:</b> ₹10 लाख का लोन 10% पर — 5 साल में ब्याज लगभग ₹2.75 लाख, और 10 साल में लगभग ₹5.86 लाख। लोन वही, ब्याज दर वही — सिर्फ़ अवधि ने ख़र्च दोगुना कर दिया।</p>
          <p><b>फ़्लैट रेट से सावधान:</b> "10% फ़्लैट" असल में लगभग <b>18–19% रिड्यूसिंग</b> के बराबर होता है। हमेशा पूछिए कि दर <b>रिड्यूसिंग बैलेंस</b> पर है या फ़्लैट पर।</p>
          <div class="btn-row" style="margin-top:1.2rem">
            <a class="btn btn-gold btn-sm" href="tel:+{PHONE}" data-ev="call_emi_hi">{I['phone']}हिंदी में समझिए</a>
          </div>
        </div>
        <div class="card" style="margin-top:1.2rem">
          <h3 style="font-size:1.1rem">Want the real number?</h3>
          <p>A calculator uses the rate you type in. We will tell you the rate you will actually be offered, across the lenders you qualify for.</p>
          <a class="btn btn-gold btn-block" href="contact.html" data-ev="cta_emi">Get a real quote {I['arrow']}</a>
        </div>
      </div>
    </div>
  </div>
</section>

{faq_block(EMI_FAQ, "EMI questions, answered")}
{cta_band()}
</main>
"""
out.append(("emi-calculator.html", page(
  "EMI Calculator — Home, Personal, Car & Business Loan EMI | ANS Capital Services",
  "Free EMI calculator for home, personal, car, business and property loans. See monthly EMI, total interest and total payable instantly. Current India rates included. ANS Capital Services Pvt. Ltd.",
  "emi-calculator.html", EMI_BODY, "emi-calculator.html",
  "EMI calculator, home loan EMI calculator, personal loan EMI calculator, car loan EMI, business loan EMI, loan EMI calculator India, reducing balance EMI",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("EMI Calculator","emi-calculator.html")]), faq_schema(EMI_FAQ),
     {"@type":"WebApplication","@id":SITE+"/emi-calculator.html#app","name":"ANS EMI Calculator",
      "applicationCategory":"FinanceApplication","operatingSystem":"Any","url":SITE+"/emi-calculator.html",
      "offers":{"@type":"Offer","price":"0","priceCurrency":"INR"},
      "description":"Free loan EMI calculator for home, personal, car, business and property loans in India.",
      "publisher":{"@id":SITE+"/#organization"}}))))

print("\n".join(f"{n} queued" for n,_ in out))
for name, html in out:
    open(name,"w").write(html)
    print(f"{name:26s} {len(html):>8,} bytes")
