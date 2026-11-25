# -*- coding: utf-8 -*-
"""FAQs, Knowledge Centre, Cookie Policy, Enquiry Consent."""
from gen_core import *
from gen_parts import *

out = []

# ============================================================ FAQs
GROUPS = [
 ("About ANS Capital Services", [
  ("Is ANS Capital Services a bank or an NBFC?",
   "No. ANS Capital Services Private Limited is a loan distribution company. We assist customers in understanding financing options, preparing documentation and submitting applications to lending institutions. We do not accept deposits, we do not lend our own money, and we do not sanction or disburse loans."),
  ("What does ANS Capital Services actually do for me?",
   "We help you work out which products suit your requirement, give you a precise document checklist, check the documents before submission, submit the application to the lending institutions you authorise, follow it through underwriting and explain the sanction terms before you sign."),
  ("Are you connected to any larger organisation?",
   "Yes. ANS Capital Services is a Channel Partner of Ruloans, a loan distribution company, as stated on our own social media profiles. Any specific lender empanelment that applies to your application will be disclosed to you at the time you apply."),
  ("Do you have a physical office I can visit?",
   "We work across Delhi NCR and Uttar Pradesh. Please call " + PHONE_D + " before visiting so that we can confirm a time and keep it free for you. Our full office address will be published on this website once it is confirmed for publication."),
 ]),
 ("Fees and charges", [
  ("What do you charge me?",
   "We do not ask applicants for any advance payment, and we never ask for cash. If a lender sanctions a loan, that institution levies its own processing and documentation charges, set out in your sanction letter and paid directly to it."),
  ("Someone asked me to pay in advance in your name. What should I do?",
   "Do not pay. We never request advance payments, OTPs, passwords, card PINs or account credentials. Call us immediately on " + PHONE_D + " so we can confirm whether the person is connected with us, and report the matter."),
  ("Will I be told about all the charges before I commit?",
   "Yes. Before you sign anything, we will go through the sanction letter and the Key Facts Statement with you, including the processing fee, any insurance bundled with the loan, prepayment terms and the conditions under which the rate can change."),
 ]),
 ("Eligibility and documents", [
  ("What documents are usually required?",
   "Identity and address proof, recent bank statements, and proof of income — salary slips and Form 16 if you are salaried, or income tax returns and GST filings if you are self-employed. Home loans and loans against property additionally require the property documents. The exact list depends on the lender and the product, and we will give you a precise checklist."),
  ("Does my credit score matter?",
   "For most products it is one of the most important factors a lender considers, alongside your income and existing obligations. A lower score does not automatically mean refusal, but it usually narrows which institutions will consider the application and on what terms."),
  ("Can I apply if I am self-employed?",
   "Yes. Self-employed applicants are assessed primarily on filed income tax returns, business vintage and banking turnover rather than on salary slips. The documentation is heavier, which is exactly why it helps to have the file checked before it goes in."),
  ("Can I apply with a co-applicant?",
   "For several products, yes, and it can materially improve eligibility — a spouse's or parent's income may be combined with yours. The co-applicant's credit record is assessed alongside your own, so it cuts both ways."),
 ]),
 ("The application process", [
  ("Can you guarantee approval?",
   "No, and nobody honestly can. Approval, the amount, the interest rate and every condition are decided by the lending institution after its own assessment. Treat any promise of guaranteed approval, from anyone, as a warning sign."),
  ("How long does it take?",
   "It depends on the product and the lender. Unsecured products are generally quicker than secured ones, because secured lending requires valuation and legal verification of the asset. We will give you a realistic timeline for your case at the outset."),
  ("What if my application is declined?",
   "We will tell you the reason given, where one is given, and advise honestly on whether a different lender, a different product, or simply waiting and fixing the underlying issue is the better next step."),
  ("Can I track my application?",
   "We update you at each stage — submission, lender queries, and the decision. Tell us if you would prefer updates on WhatsApp rather than by phone."),
 ]),
 ("Language and support", [
  ("Can I deal with you in Hindi?",
   "Yes. We work in Hindi and English on the phone, on WhatsApp and on this website. Use the EN / हिं control in the menu to read the site in Hindi, and the assistant at the bottom of the page replies in whichever language you write in."),
  ("What are your working hours?",
   "Monday to Saturday, 10:00 AM to 7:00 PM. These hours are subject to confirmation and will be updated here if they change. Messages sent outside these hours are answered the next working morning."),
 ]),
 ("Privacy and data", [
  ("What do you do with my information?",
   "We use it to assess your requirement and, with your consent, to submit an application to the lending institutions you authorise. We do not sell or rent your personal data. Our Privacy Policy sets out the detail."),
  ("Can I ask you to delete my information?",
   "Yes. Write to " + EMAIL + " and we will delete whatever we are not legally or contractually required to retain, and confirm to you once it is done."),
 ]),
]

def group_block(title, items, i):
    acc = "".join(f"""<div class="acc-i"><button class="acc-q" type="button"><span>{q}</span><i aria-hidden="true"></i></button>
      <div class="acc-a"><div><p>{a}</p></div></div></div>""" for q,a in items)
    return f"""<div data-rv style="margin-bottom:2.8rem">
      <h2 style="font-size:clamp(1.4rem,2.6vw,1.95rem);margin-bottom:1rem" class="g-navy">{title}</h2>
      <div class="acc">{acc}</div></div>"""

ALL_FAQ = [qa for _, items in GROUPS for qa in items]

FAQ_BODY = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">FAQs</span></nav>
    <div class="split-wide" style="align-items:end">
      <div><span class="eyebrow on-dark">Answers</span>
        <h1 data-hi="सामान्य <em class='g-gold g-anim'>प्रश्न</em>"><span class="t-md t-thin t-mute">Frequently Asked</span><br><em class="g-gold g-anim t-lg">Questions</em></h1></div>
      <div style="padding-bottom:.4rem">
        <p class="lead">Straight answers about what we do, what it costs, what a lender looks at and what we cannot promise. If your question is not here, call {PHONE_D} and ask.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("ring","tr",440,.05),("dots","bl",220,.05))}{orb("br",560,"gold")}
  <div class="wrap-n">
    {''.join(group_block(t, items, i) for i,(t,items) in enumerate(GROUPS))}
    <div class="notice gold" data-rv>
      {I['shield']}
      <span><b>One answer worth repeating.</b> No loan is approved by {SHORT}. Final eligibility, the sanctioned
      amount, the interest rate and every condition are decided by the lending institution after its own assessment.
      Anyone promising guaranteed approval — in our name or any other — should not be trusted.</span>
    </div>
  </div>
</section>

{cta_band("Still have a question?", "कोई और सवाल है?",
  "Call us and ask. A short conversation usually settles in five minutes what a page of text cannot.")}
</main>
"""
out.append(("faqs.html", page(
  "FAQs | Loan Questions Answered — ANS Capital Services Pvt. Ltd.",
  "Answers about loan assistance, fees, eligibility, documents, the application process, language support and data privacy from ANS Capital Services Private Limited.",
  "faqs.html", FAQ_BODY, "faqs.html",
  "loan FAQ India, loan questions, loan eligibility questions, loan documents required, is loan approval guaranteed, loan agent fees",
  ld(ORG, WEBSITE, crumbs([("Home","index.html"),("FAQs","faqs.html")]), faq_schema(ALL_FAQ),
     {"@type":"FAQPage","@id":SITE+"/faqs.html#webpage","url":SITE+"/faqs.html",
      "name":"Frequently Asked Questions","isPartOf":{"@id":SITE+"/#website"},"inLanguage":"en-IN"}))))

for name, html in out:
    open(name,"w").write(html)
    print(f"{name:26s} {len(html):>8,} bytes")
