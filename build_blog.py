# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

POSTS = [
 dict(slug="understanding-emi.html", cat="EMIs", art="abstract", date="2026-11-18", read="6 min",
  title="Understanding your EMI — what the number actually hides",
  excerpt="The instalment is the figure everyone compares. It is also the least informative number in the whole loan.",
  hi="EMI वही किस्त है जिसमें ब्याज और मूलधन दोनों होते हैं। शुरुआती सालों में ज़्यादातर हिस्सा ब्याज का होता है — इसलिए जल्दी किया गया प्री-पेमेंट सबसे ज़्यादा बचाता है। लंबी अवधि EMI घटाती है लेकिन कुल ब्याज बहुत बढ़ा देती है।",
  body="""
<p>Two loans can carry the same monthly instalment and differ by several lakh rupees in what they finally cost you. The instalment hides the tenure, and the tenure is doing most of the work.</p>
<h3>How the instalment is built</h3>
<p>Every lender uses the same formula. The instalment stays constant across the loan, but what sits inside it does not. In the early years most of each payment is interest and only a small part reduces the principal. That ratio reverses slowly over the life of the loan.</p>
<p>This single fact explains why prepaying in year two removes far more future interest than the same amount paid in year twelve. By the later years you have already paid most of the interest the loan was ever going to charge you.</p>
<h3>The tenure trap</h3>
<p>Lengthening the tenure is the easiest way to make an instalment fit a budget, and the most expensive. Take a loan of ten lakh rupees at ten per cent. Over five years the interest comes to roughly ₹2.75 lakh. Over ten years, the same loan at the same rate costs roughly ₹5.86 lakh. Nothing changed except the tenure, and the cost more than doubled.</p>
<p>The practical rule: choose the shortest tenure whose instalment you can carry comfortably, with room for a month when income is short. Not the longest one you qualify for.</p>
<h3>Reducing balance versus flat rate</h3>
<p>A reducing balance rate charges interest only on what you still owe. A flat rate charges interest on the full original amount for the entire tenure. A ten per cent flat rate is roughly equivalent to eighteen or nineteen per cent reducing. Bank loans quote reducing balance; some smaller lenders and dealer schemes quote flat. Always ask which one you are being shown before comparing two offers.</p>
<h3>What a calculator cannot tell you</h3>
<p>An EMI calculator applies the formula to the numbers you type in. It does not know about the processing fee deducted from your disbursal, an insurance premium financed into the loan, or a floating rate that resets next year. Use it to plan, then read the sanction letter and the Key Facts Statement for the figures that actually bind you.</p>
"""),
 dict(slug="credit-score-basics.html", cat="Credit score", art="abstract", date="2026-11-12", read="7 min",
  title="Credit score basics — what actually moves the number",
  excerpt="Most advice about credit scores is folklore. Here is what genuinely affects yours, and what does not.",
  hi="क्रेडिट स्कोर सबसे ज़्यादा इस बात से बनता है कि आपने समय पर भुगतान किया या नहीं, और आप अपनी क्रेडिट लिमिट का कितना हिस्सा इस्तेमाल करते हैं। एक साथ कई बैंकों में अप्लाई करने से स्कोर गिरता है। पुराने कार्ड बंद करने से भी नुक़सान हो सकता है।",
  body="""
<p>A credit score is a summary of how you have handled borrowed money. Lenders use it as a first filter, which means it often decides not just whether you are approved but what you are charged.</p>
<h3>What carries the most weight</h3>
<p><b>Repayment history.</b> Whether you have paid on time, every time, is the single largest factor. One missed instalment is visible for years, and a settled account — where the lender accepted less than the full amount — is worse than a late payment.</p>
<p><b>Credit utilisation.</b> How much of your available credit card limit you actually use. Consistently running close to the limit suggests strain, even if you pay in full each month. Keeping usage below roughly thirty per cent of the limit is a commonly cited threshold.</p>
<p><b>Age of accounts.</b> A long, clean history helps. This is why closing your oldest credit card can reduce your score rather than improve it.</p>
<p><b>Hard enquiries.</b> Every formal application creates one. Several in a short period reads as distress to an underwriter.</p>
<h3>What does not affect it</h3>
<p>Checking your own score does not reduce it. Your salary, savings and investments are not part of the score, though lenders look at income separately. Nor does holding a debit card, or using UPI.</p>
<h3>If yours needs repairing</h3>
<p>Clear outstanding card balances first, bring usage down, and let a cycle or two pass so the improvement is reported. Do not close old accounts. Do not apply anywhere while you are repairing it. Six weeks of patience frequently achieves more than any amount of negotiating at the counter.</p>
<h3>A lower score is not the end of it</h3>
<p>Below the thresholds banks prefer, options narrow but do not disappear — particularly for secured products, where the asset carries much of the risk. The cost is usually a higher rate. Whether that is worth paying now, or whether it is better to wait and apply later, depends entirely on how urgent the requirement is.</p>
"""),
 dict(slug="home-loan-guide.html", cat="Home finance", art="home", date="2026-11-06", read="8 min",
  title="A first-time buyer's guide to home financing",
  excerpt="What to budget for beyond the loan, how lenders assess the property, and the clauses worth reading twice.",
  hi="होम लोन में बैंक प्रॉपर्टी की क़ीमत का 75–90% तक देता है। बाक़ी डाउन पेमेंट और स्टाम्प ड्यूटी-रजिस्ट्री (5–7%) आपको अपनी जेब से देनी होती है — यह कोई बैंक नहीं देता। आपकी फ़ाइल के साथ-साथ प्रॉपर्टी के कागज़ भी जाँचे जाते हैं।",
  body="""
<p>A home loan is assessed in two halves: you, and the property. Applicants prepare carefully for the first and are caught out by the second.</p>
<h3>Budget for what the loan will not cover</h3>
<p>Lenders fund a percentage of the property value, not the whole cost of buying. The balance is your down payment, and it must come from your own resources. Separately there is stamp duty and registration — typically five to seven per cent of the agreement value depending on the state — which lenders generally do not fund. Add legal charges, valuation fees and, if you are buying a flat, society transfer costs.</p>
<p>Plan for all of this as cash before you commit to a property, not after the sanction arrives.</p>
<h3>The property has to qualify too</h3>
<p>A clear and marketable title with the full chain of ownership. An approved building plan. No litigation, encroachment or unapproved construction. Property tax receipts up to date. For an under-construction flat, the project and the builder generally need to be acceptable to the lender.</p>
<p>Most home loan delays come from this half of the file — an old unreleased mortgage, a missing parent document, a name spelled differently across two deeds. Sorting these out before applying is the single biggest thing you can do to speed up the process.</p>
<h3>Clauses worth reading twice</h3>
<p><b>How the rate is built.</b> Most home loans are floating and linked to a benchmark. Your rate is that benchmark plus a spread. The benchmark is the same for everyone; the spread is what differs between borrowers. Ask for it in writing.</p>
<p><b>Reset conditions.</b> When and how the rate changes, and whether the change moves your instalment or your tenure.</p>
<p><b>Prepayment.</b> For floating-rate loans to individuals, the regulatory position is favourable to borrowers. For fixed-rate loans, check the clause.</p>
<h3>One habit worth adopting</h3>
<p>Pay one extra instalment a year. On a twenty-year loan that typically removes four to five years from the tenure. It costs nothing but discipline, and on a floating-rate individual loan there is normally no charge for doing it.</p>
"""),
 dict(slug="business-loan-documents.html", cat="Business finance", art="business", date="2026-10-28", read="6 min",
  title="What an underwriter actually reads in your business file",
  excerpt="Turnover gets the attention. The current account statement decides the outcome.",
  hi="बिज़नेस लोन में बैंक सबसे ध्यान से आपका करंट अकाउंट स्टेटमेंट और GST रिटर्न देखता है। चेक बाउंस, महीने के अंत में निगेटिव बैलेंस और बिना हिसाब के नक़द जमा — ये तीनों सीधे ब्याज दर बढ़ाते हैं या फ़ाइल रुकवाते हैं।",
  body="""
<p>Business owners usually prepare the balance sheet and overlook the bank statement. Underwriters read them in the opposite order.</p>
<h3>The current account tells the real story</h3>
<p>Twelve months of banking shows what financial statements summarise: whether money comes in steadily, whether cheques bounce, whether the balance goes negative at month end, whether large cash deposits appear without a matching invoice trail. Each of those affects pricing, and several together affect whether the file is taken at all.</p>
<p>If you are planning to borrow in the next year, the cheapest thing you can do is keep six clean months of banking before you apply.</p>
<h3>GST filings are now an income document</h3>
<p>Consistent, timely returns that match your declared turnover open programmes that will not look at an irregular filer, whatever the profit figure says. Irregular filing is read as a control problem, not a paperwork problem.</p>
<h3>The trade-off nobody mentions</h3>
<p>Businesses that minimise declared profit to reduce tax also minimise the income a lender can assess. You cannot show a thin return to the tax authority and a strong one to the underwriter. If borrowing is likely within a year or two, that trade-off is worth thinking about before the returns are filed, not after.</p>
<h3>Separate the business and personal accounts</h3>
<p>Mixed accounts make cash flow unreadable. An underwriter who cannot read your cash flow prices for the worst case. A clean, separate current account genuinely moves your rate.</p>
<h3>Match the instrument to the need</h3>
<p>A term loan with a fixed instalment suits an asset you will use for years. For stock or receivables that move with the season, an overdraft — where interest applies only to what you actually draw — is usually far cheaper. Taking a term loan for working capital and parking the surplus in a current account means paying interest on money sitting idle.</p>
"""),
 dict(slug="car-loan-mistakes.html", cat="Vehicle finance", art="car", date="2026-10-20", read="5 min",
  title="Five things buyers get wrong about car finance",
  excerpt="The rate is rarely the problem. The showroom finance desk and the on-road arithmetic usually are.",
  hi="\\\"100% फ़ाइनेंस\\\" का मतलब अक्सर एक्स-शोरूम क़ीमत का 100% होता है, ऑन-रोड का नहीं — और यह अंतर 8–12% तक होता है, जो आपको नक़द देना पड़ता है। शोरूम जाने से पहले लोन मंज़ूर करवा लेना सबसे बड़ा फ़ायदा देता है।",
  body="""
<p>Car finance is among the simpler retail products. Most of the money buyers lose on it is lost before the loan is even arranged.</p>
<h3>1. Confusing ex-showroom with on-road</h3>
<p>Ex-showroom excludes road tax, registration and insurance. On-road includes them and is usually eight to twelve per cent higher. A lender advertising full funding generally means full funding of the ex-showroom price, which still leaves a sizeable amount for you to find in cash. Ask what the actual disbursal figure will be in rupees.</p>
<h3>2. Arranging the loan at the showroom</h3>
<p>The finance desk is convenient and is paid for placing the loan. Walking in with a sanction already in hand changes the conversation — you negotiate on the price of the car rather than on the instalment, and the bundled insurance becomes optional rather than assumed.</p>
<h3>3. Not asking your own bank first</h3>
<p>Many lenders offer a concession to customers who already hold a salary account or another loan with them. It takes one phone call and is frequently the best rate available.</p>
<h3>4. Taking the longest tenure</h3>
<p>A car depreciates. On a very long tenure you will owe more than the vehicle is worth for much of the middle of the loan, which becomes a problem if you want to sell or if it is written off. Five years is a sensible maximum for most buyers. If the instalment only works over seven, the honest conclusion is usually that the car is above budget.</p>
<h3>5. Accepting the bundled insurance</h3>
<p>Dealer-arranged motor insurance is convenient and generally expensive. Two outside quotes for the same insured value and cover will often save more than the entire processing fee.</p>
"""),
 dict(slug="documents-checklist.html", cat="Documentation", art="abstract", date="2026-10-14", read="5 min",
  title="The document checklist that prevents most delays",
  excerpt="Applications are rarely delayed by the lender. They are delayed by a missing page.",
  hi="ज़्यादातर फ़ाइलें बैंक की वजह से नहीं, बल्कि एक छूटे हुए कागज़ या नाम के फ़र्क़ की वजह से रुकती हैं। पैन, आधार, 6 महीने का बैंक स्टेटमेंट और आमदनी का प्रमाण — ये चारों लगभग हर लोन में लगते हैं।",
  body="""
<p>Almost every application needs the same core set. Getting it complete and consistent on day one is the difference between a file that moves and a file that stalls.</p>
<h3>The core set</h3>
<ul>
<li>Identity proof — PAN card</li>
<li>Address proof — Aadhaar, passport, voter ID or a recent utility bill</li>
<li>Bank statements, usually the last six months, of the account where income is credited</li>
<li>Passport-size photographs</li>
</ul>
<h3>If you are salaried</h3>
<ul>
<li>Recent salary slips, usually the last three months</li>
<li>Form 16, or the latest income tax return</li>
<li>Employment proof — appointment letter, confirmation letter or employee ID</li>
</ul>
<h3>If you are self-employed</h3>
<ul>
<li>Income tax returns with computation of income, usually the last two years</li>
<li>Audited profit and loss account and balance sheet, where applicable</li>
<li>Current account statements, usually the last twelve months</li>
<li>GST registration and recent returns</li>
<li>Business proof — Udyam registration, Shop and Establishment licence, partnership deed, or incorporation documents</li>
</ul>
<h3>For a home loan or a loan against property, additionally</h3>
<ul>
<li>The complete title chain, including parent documents</li>
<li>Approved building plan and, where applicable, the completion or occupancy certificate</li>
<li>Latest property tax receipt and an encumbrance certificate</li>
<li>Society share certificate and no-objection certificate, for a flat</li>
</ul>
<h3>The three things that actually cause delays</h3>
<p><b>Name mismatches.</b> A name spelled differently across PAN, Aadhaar and a property deed will be queried. Fix it before applying.</p>
<p><b>Unexplained credits.</b> A large deposit in your bank statement with no obvious source will be asked about. Have the explanation and the supporting document ready.</p>
<p><b>Incomplete statements.</b> Pages missing from the middle of a bank statement, or a statement that does not carry the bank's stamp where one is required, sends the file straight back.</p>
<p>Send soft copies before anything is submitted and have the whole set checked. It costs you nothing and removes most of the delay.</p>
"""),
]

def card(p, i):
    return f"""<article class="post" data-rv data-delay="{(i%3)*80}">
  <a href="{p['slug']}" class="post-art" aria-label="{p['title']}">{art(p['art'], 40+i)}</a>
  <div class="post-b">
    <div class="post-meta"><span class="pill">{p['cat']}</span><span>{p['read']} read</span></div>
    <h3><a href="{p['slug']}">{p['title']}</a></h3>
    <p>{p['excerpt']}</p>
    <a class="tlink" href="{p['slug']}">Read article {I['arrow']}</a>
  </div>
</article>"""

# ---------------- index ----------------
INDEX = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">Knowledge Centre</span></nav>
    <div class="split-wide" style="align-items:end">
      <div><span class="eyebrow on-dark">Financial education</span>
        <h1 data-hi="जानकारी <em class='g-gold g-anim'>केंद्र</em>"><span class="t-md t-thin t-mute">Knowledge</span><br><em class="g-gold g-anim t-lg">Centre</em></h1></div>
      <div style="padding-bottom:.4rem">
        <p class="lead">Plain-language guides to borrowing in India — how instalments work, what moves a credit score, what lenders read in your file, and the documents that prevent most delays.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("coin","tr",400,.05),("grid","bl",340,.04))}{orb("tr",560,"gold")}
  <div class="wrap">
    <div class="grid g3">{''.join(card(p,i) for i,p in enumerate(POSTS))}</div>
    <div class="notice" data-rv style="margin-top:2.4rem">
      {I['doc']}
      <span><b>This section is general educational information.</b> It is not financial, legal or tax advice, and it is
      not specific to your circumstances. Figures and regulations mentioned were accurate when written and change over
      time. For advice on your own situation, speak to a qualified professional — or call us and we will tell you what
      we can and cannot help with.</span>
    </div>
  </div>
</section>
{cta_band()}
</main>
"""
pages = [("blog.html", page(
  "Knowledge Centre | Loan & Personal Finance Guides — ANS Capital Services",
  "Plain-language guides to borrowing in India: understanding EMIs, credit score basics, home loan guidance, business loan documentation and vehicle finance, from ANS Capital Services Private Limited.",
  "blog.html", INDEX, "blog.html",
  "EMI explained, credit score India, home loan guide, business loan documents, car loan tips, personal finance India, loan documentation checklist",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("Knowledge Centre","blog.html")]),
     {"@type":"Blog","@id":SITE+"/blog.html#blog","name":"ANS Capital Services Knowledge Centre",
      "url":SITE+"/blog.html","inLanguage":"en-IN","publisher":{"@id":SITE+"/#organization"},
      "blogPost":[{"@type":"BlogPosting","headline":p["title"],"url":SITE+"/"+p["slug"],
                   "datePublished":p["date"],"description":p["excerpt"],
                   "author":{"@id":SITE+"/#organization"},"publisher":{"@id":SITE+"/#organization"}} for p in POSTS]})))]

# ---------------- articles ----------------
for i, p in enumerate(POSTS):
    others = "".join(card(q, j) for j, q in enumerate(POSTS) if q["slug"] != p["slug"])[:0]
    rel = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    body = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap-n">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="blog.html">Knowledge Centre</a><span>/</span><span style="color:#C9DCF2">{p['cat']}</span></nav>
    <span class="eyebrow on-dark">{p['cat']} · {p['read']} read</span>
    <h1 style="max-width:20ch">{p['title']}</h1>
    <p class="lead">{p['excerpt']}</p>
  </div>
</section>

<section class="sec">
  {deco(("rays","r",360,.05),("dots","bl",200,.045))}
  <div class="wrap-n">
    <div class="prose" data-rv>{p['body']}</div>

    <div class="hindi-box" data-rv style="margin:2.4rem 0">
      <h4>संक्षेप में — हिंदी</h4>
      <p>{p['hi']}</p>
      <div class="btn-row" style="margin-top:1rem">
        <a class="btn btn-gold btn-sm" href="tel:+{PHONE}" data-ev="call_blog">{I['phone']}हिंदी में बात करें</a>
      </div>
    </div>

    <div class="notice" data-rv>
      {I['doc']}
      <span><b>General information, not advice.</b> This article explains how these products work in the Indian market
      generally. It is not specific to your circumstances and is not financial, legal or tax advice. Interest rates,
      charges and regulations change. Any loan you take is sanctioned by a lending institution on its own terms.</span>
    </div>

    <div style="margin-top:3rem" data-rv>
      <h2 style="font-size:clamp(1.6rem,2.8vw,2.1rem);margin-bottom:1.4rem"><span class="t-md t-thin t-mute">Related</span> <em class="g-gold">reading</em></h2>
      <div class="grid g3">{''.join(card(q, 70+j) for j,q in enumerate(rel))}</div>
    </div>
  </div>
</section>
{cta_band()}
</main>
"""
    pages.append((p["slug"], page(
      p["title"] + " | ANS Capital Services Pvt. Ltd.",
      p["excerpt"] + " A plain-language guide from ANS Capital Services Private Limited.",
      p["slug"], body, "blog.html", p["cat"] + ", " + p["title"].lower(),
      ld(ORG, WEBSITE,
         crumbs([("Home","index.html"),("Knowledge Centre","blog.html"),(p["title"], p["slug"])]),
         {"@type":"BlogPosting","@id":SITE+"/"+p["slug"]+"#post","headline":p["title"],
          "description":p["excerpt"],"url":SITE+"/"+p["slug"],"datePublished":p["date"],
          "dateModified":p["date"],"inLanguage":"en-IN","articleSection":p["cat"],
          "author":{"@id":SITE+"/#organization"},"publisher":{"@id":SITE+"/#organization"},
          "isPartOf":{"@id":SITE+"/blog.html#blog"},
          "mainEntityOfPage":{"@type":"WebPage","@id":SITE+"/"+p["slug"]}}),
      )))

for name, html in pages:
    open(name,"w").write(html)
    print(f"{name:30s} {len(html):>8,} bytes")
