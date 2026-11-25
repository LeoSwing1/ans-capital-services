# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

def legal(slug, h1, eyebrow, lead, prose, title, desc):
    body = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span style="color:#C9DCF2">{h1}</span></nav>
    <span class="eyebrow on-dark">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <p style="color:#7D93AE;font-size:.84rem;margin-top:1.4rem">Last updated: 24 November 2026</p>
  </div>
</section>
<section class="sec">
  {deco(("ring","tr",400,.045),("dots","bl",190,.04))}
  <div class="wrap-n">
    <div class="prose" data-rv>{prose}
      <div class="rule" style="margin:2.6rem 0"></div>
      <h3>Questions about this page?</h3>
      <p>Write to <a href="mailto:{EMAIL}" style="color:var(--gold-400);font-weight:600">{EMAIL}</a> or call <a href="tel:+{PHONE}" style="color:var(--gold-400);font-weight:600">{PHONE_D}</a>. We will respond within three working days.</p>
    </div>
  </div>
</section>
{cta_band()}
</main>"""
    html = page(title, desc, slug, body, active=slug, keywords="",
        schema=ld(ORG, WEBSITE, crumbs([("Home","index.html"),(h1,slug)]),
                  {"@type":"WebPage","@id":SITE+"/"+slug+"#webpage","url":SITE+"/"+slug,
                   "name":h1,"isPartOf":{"@id":SITE+"/#website"},"inLanguage":"en-IN"}))
    open(slug,"w").write(html)
    return slug, len(html)

# ---------------------------------------------------------------- PRIVACY
PRIV = f"""
<p>{BRAND} ("ANS Capital Services", "we", "us") respects the confidentiality of the information you share with us. This policy explains what we collect, why we collect it, who we share it with and what control you have over it.</p>

<h2>1. Information we collect</h2>
<p>We collect only what is needed to assess your loan requirement and submit an application on your behalf:</p>
<ul>
<li><b>Identity and contact details</b> — name, mobile number, email address, residential and office address, date of birth.</li>
<li><b>Financial information</b> — employment or business details, income, existing loan obligations, bank statements, income tax returns and GST returns.</li>
<li><b>Identity documents</b> — PAN, Aadhaar and other KYC documents required by the lender under RBI's Know Your Customer directions.</li>
<li><b>Property and asset information</b> — where you apply for a home loan, loan against property or a secured facility.</li>
<li><b>Credit information</b> — your credit report, where you authorise us or a lender to obtain it.</li>
<li><b>Website usage data</b> — pages viewed, approximate location, device and browser type, collected through analytics cookies.</li>
</ul>

<h2>2. How we collect it</h2>
<p>Through this website's enquiry forms, over WhatsApp, by telephone, by email, and in person. Submitting a form on this website opens WhatsApp with your details pre-filled — the information travels to us through WhatsApp and is not stored in a database on this website.</p>

<h2>3. Why we use it</h2>
<ul>
<li>To assess which lender programmes you are likely to qualify for.</li>
<li>To prepare, check and submit your loan application to the banks and NBFCs you authorise.</li>
<li>To respond to your enquiry and keep you updated on the progress of your file.</li>
<li>To comply with legal, regulatory and contractual obligations, including those of our principal and of the lenders.</li>
<li>To improve this website and the quality of our service.</li>
</ul>

<h2>4. Who we share it with</h2>
<p>We share your information with:</p>
<ul>
<li><b>Banks, NBFCs and insurers</b> you have authorised us to approach for your application.</li>
<li><b>Ruloans Distribution Services Pvt. Ltd.</b>, our principal, through whose platform applications are routed.</li>
<li><b>Credit information companies</b> such as CIBIL, where a credit report is required for assessment.</li>
<li><b>Service providers</b> — valuers, legal counsel and verification agencies engaged by the lender.</li>
<li><b>Authorities</b>, where disclosure is required by law, regulation or an order of a court.</li>
</ul>
<p><b>We do not sell, rent or trade your personal information to third parties for marketing purposes.</b></p>

<h2>5. Consent and DNC</h2>
<p>By submitting an enquiry, you authorise {SHORT} and its partner banks, NBFCs and insurers to contact you by telephone, SMS, WhatsApp or email in connection with your enquiry. This consent operates notwithstanding any registration you may hold under the National Do Not Call or National Customer Preference Register. You may withdraw this consent at any time by writing to {EMAIL}.</p>

<h2>6. How long we keep it</h2>
<p>We retain your information for as long as your enquiry or loan file is active, and afterwards for the period required by applicable law and by the lenders' own record-keeping obligations. You may ask us to delete information that we are not legally required to retain.</p>

<h2>7. Security</h2>
<p>We apply reasonable technical and organisational safeguards to protect the information you share, including restricted access and secure transmission. No method of transmission over the internet is entirely secure, and we cannot guarantee absolute security. Please do not send complete bank account numbers, card numbers, passwords, OTPs or UPI PINs to anyone, including us. <b>We will never ask you for an OTP, a password or a PIN.</b></p>

<h2>8. Cookies and analytics</h2>
<p>This website uses cookies and similar technologies, including Google Analytics, Google Tag Manager and the Meta Pixel, to understand how visitors use the site and to measure the effectiveness of our advertising. You can block or delete cookies through your browser settings; some features of the site may then not work as intended.</p>

<h2>9. Third-party links</h2>
<p>This website links to external sites, including Instagram, Facebook, LinkedIn, YouTube, WhatsApp, Google Maps and lender websites. Those sites operate under their own privacy policies, and we are not responsible for their content or practices.</p>

<h2>10. Children</h2>
<p>This website and our services are intended for persons aged 18 and above. We do not knowingly collect information from minors.</p>

<h2>11. Your rights</h2>
<p>You may ask us to confirm what information we hold about you, correct anything inaccurate, withdraw your consent to being contacted, or delete information we are not required to keep. Write to {EMAIL} and we will respond within a reasonable period.</p>

<h2>12. Changes to this policy</h2>
<p>We may update this policy from time to time. The revised version takes effect when published on this page, and the date at the top will change accordingly.</p>
"""

# ---------------------------------------------------------------- TERMS
TERMS = f"""
<p>These terms govern your use of this website and the services offered by {BRAND}. By using this website or submitting an enquiry, you accept them.</p>

<h2>1. Who we are</h2>
<p>{BRAND} is a company registered under the Companies Act of India, carrying on the business of loan distribution as a Direct Selling Agent and as an authorised Channel Partner of Ruloans Distribution Services Pvt. Ltd.</p>
<p><b>Our role, stated plainly: we are an intermediary.</b> {BRAND} is a loan distribution company that assists applicants in understanding financing options, preparing documentation and submitting applications to lending institutions. <b>We are not a bank, a non-banking financial company, a housing finance company or a lender of any kind.</b> We do not accept deposits, we do not lend money, and we do not sanction or disburse loans. We hold no licence or registration from the Reserve Bank of India, and we do not claim any. Any empanelment with a particular lending institution that applies to your application will be disclosed to you at the time you apply.</p>

<h2>2. What our service is</h2>
<ul>
<li>Understanding your requirement and assessing your indicative eligibility.</li>
<li>Identifying lender programmes you are likely to qualify for.</li>
<li>Helping you compile and check the documents required.</li>
<li>Submitting your application to the lenders you authorise.</li>
<li>Following up on your application until a decision is reached and, where sanctioned, until disbursal.</li>
</ul>

<h2>3. What our service is not</h2>
<p>We do not guarantee that any loan will be sanctioned, nor the amount, interest rate, tenure or conditions of any sanction. Every credit decision rests solely with the lending institution, applied under its own credit policy, verification process and internal guidelines. A reference to indicative eligibility on this website or in conversation with us is not an offer, a commitment or a sanction.</p>

<h2>4. Fees</h2>
<p>{SHORT} does not charge applicants any advance fee for assessing eligibility, comparing offers or processing an application. Our remuneration is the distribution commission paid to us by the lending institution after a loan is disbursed. The processing fee, documentation charges, valuation and legal fees, stamp duty and any other charge associated with a loan are levied by the lender and are payable directly to the lender.</p>
<p><b>Fraud warning.</b> We will never ask you to pay cash, to transfer money to a personal account, or to share an OTP, password or PIN. If anyone contacts you making such a demand in our name, do not pay. Call us immediately on {PHONE_D}.</p>

<h2>5. Accuracy of information</h2>
<p>You confirm that the information and documents you provide are true, accurate and your own. Providing false information or forged documents is a serious offence and may result in rejection of your application, reporting to credit bureaus, legal action by the lender and termination of our services to you.</p>

<h2>6. Rates and content on this website</h2>
<p>Interest rates, fees, eligibility criteria, tenures, loan amounts and other figures on this website are indicative, compiled from publicly available lender information at the time of writing, and are subject to change without notice. They are provided for general information and do not constitute financial, legal or tax advice. The terms applicable to you are only those set out in the sanction letter, loan agreement and Key Facts Statement issued by the lender. Please read those documents in full before signing.</p>

<h2>7. Intellectual property</h2>
<p>The content, design, text, graphics, logo and code of this website belong to {BRAND} unless otherwise stated, and may not be copied, reproduced or republished without written permission. Third-party names and marks referred to on this website belong to their respective owners and are used for identification only.</p>

<h2>8. Third-party websites</h2>
<p>This website links to external websites and platforms. We do not control them and are not responsible for their content, availability, terms or privacy practices.</p>

<h2>9. Limitation of liability</h2>
<p>To the extent permitted by law, {BRAND}, its directors and employees shall not be liable for any indirect, incidental or consequential loss arising from the use of this website, from reliance on information published on it, or from the decision of any lender to approve, decline, delay or alter the terms of any application.</p>

<h2>10. Communication consent</h2>
<p>By submitting an enquiry, you authorise {SHORT} and its partner lenders and insurers to contact you by telephone, SMS, WhatsApp or email about your enquiry, notwithstanding any DNC or NCPR registration. You may withdraw this consent in writing at any time.</p>

<h2>11. Governing law</h2>
<p>These terms are governed by the laws of India. Courts at the location of our registered office shall have exclusive jurisdiction over any dispute arising from them.</p>

<h2>12. Changes</h2>
<p>We may revise these terms at any time. The version published on this page is the one that applies.</p>
"""


# ---------------------------------------------------------------- COOKIE
COOKIE = f"""
<p>This policy explains the cookies and similar technologies used on this website, what they do, and how you can control them.</p>

<h2>1. What cookies are</h2>
<p>A cookie is a small text file placed on your device when you visit a website. It allows the site to remember information between pages and visits — for example, that you chose to read this website in Hindi. Similar technologies, such as local storage and tracking pixels, perform comparable functions.</p>

<h2>2. Cookies this website uses</h2>
<h3>Strictly necessary and preference storage</h3>
<ul>
<li><b>Language preference</b> — remembers whether you selected English or हिंदी, so the site opens in your language next time.</li>
<li><b>Introduction animation</b> — records that you have already seen the opening animation in this browsing session, so it is not replayed on every page.</li>
<li><b>Enquiry protection</b> — briefly records that an enquiry was just submitted, so the same enquiry is not sent twice by accident.</li>
</ul>
<p>These are stored in your browser's local and session storage rather than transmitted to us, and the site cannot work as intended without them.</p>

<h3>Analytics</h3>
<ul>
<li><b>Google Analytics 4</b> and <b>Google Tag Manager</b> — tell us which pages are visited, how visitors arrive, and which buttons are used. This helps us improve the website. The data is aggregated and we do not use it to identify you personally.</li>
</ul>

<h3>Advertising and measurement</h3>
<ul>
<li><b>Meta Pixel</b> — measures whether visits resulted from our advertising on Facebook and Instagram, and allows us to show relevant advertising to people who have visited this website.</li>
</ul>

<h3>Embedded third-party content</h3>
<ul>
<li><b>Google Maps</b> — the map on our Contact page is served by Google and may set its own cookies when it loads.</li>
<li><b>Google Fonts</b> — typefaces used across the website are served by Google.</li>
</ul>

<h2>3. Cookies we do not use</h2>
<p>We do not use cookies to read any other website you visit, to access files on your device, or to collect financial account information. Your loan enquiry details are not stored in a cookie.</p>

<h2>4. How to control cookies</h2>
<p>Every major browser lets you block or delete cookies and clear local storage, usually under Settings, Privacy. Browsers also offer private or incognito modes, which discard this data when you close the window. You can opt out of Google Analytics across all websites using Google's browser add-on.</p>
<p>If you block cookies and storage, the website will still work, but it will not remember your language choice and will replay the introduction animation on each visit.</p>

<h2>5. Changes to this policy</h2>
<p>If we add or remove a tool that uses cookies, we will update this page and change the date shown at the top.</p>
"""

# ---------------------------------------------------------------- ENQUIRY CONSENT
CONSENT = f"""
<p>When you submit an enquiry through this website, by telephone or over WhatsApp, you give {SHORT} permission to act on it. This page sets out exactly what that permission covers, how long it lasts, and how to withdraw it.</p>

<h2>1. What you are consenting to</h2>
<p>By submitting an enquiry and ticking the consent box, you authorise {BRAND} and the lending institutions it approaches on your behalf to contact you by telephone, SMS, WhatsApp or email in connection with that enquiry.</p>
<p>You also authorise us to share the information and documents you provide with those lending institutions for the purpose of assessing and processing your application.</p>

<h2>2. Do Not Call registration</h2>
<p>This consent operates notwithstanding any registration you hold under the National Do Not Call Registry or the National Customer Preference Register. You are giving express permission to be contacted about the enquiry you have raised. It does not permit unrelated marketing, and it does not permit any other company to contact you.</p>

<h2>3. Credit information</h2>
<p>Assessing a loan application normally requires your credit report. Where you ask us to check your indicative eligibility, or where you apply to a lending institution, you authorise that credit information to be obtained from a credit information company such as CIBIL. A formal application creates a record on your credit report, which is why we recommend applying once, to the right lender, rather than to several at the same time.</p>

<h2>4. What this consent does not cover</h2>
<ul>
<li>It is not an application for a loan, and it does not commit you to taking one.</li>
<li>It does not oblige any lending institution to approve, or even consider, an application.</li>
<li>It does not authorise us to sell, rent or share your data for any purpose unconnected with your enquiry.</li>
<li>It does not authorise anyone to ask you for an OTP, password, card PIN or account credentials. <b>We never ask for these.</b></li>
</ul>

<h2>5. How long it lasts</h2>
<p>Your consent remains in effect while your enquiry or application is active, and for the period afterwards during which we and the lending institutions are required to retain records. You may withdraw it at any time.</p>

<h2>6. How to withdraw consent</h2>
<p>Tell us, and we will stop. Write to <a href="mailto:{EMAIL}" style="color:var(--gold-400);font-weight:600">{EMAIL}</a> or call <a href="tel:+{PHONE}" style="color:var(--gold-400);font-weight:600">{PHONE_D}</a> and ask us to close your file and stop contacting you. We will confirm once it is done.</p>
<p>Withdrawing consent does not affect anything already done lawfully while the consent was in force. If an application is already with a lending institution, you should also tell that institution directly.</p>

<h2>7. Minors</h2>
<p>Enquiries may only be submitted by persons aged 18 and above. We do not knowingly process enquiries from minors.</p>

<h2>8. A word on fraud</h2>
<p>Loan fraud in India commonly begins with a request for an advance payment, a processing fee paid in cash, or an OTP shared over the phone. {SHORT} does not do any of these things. Every legitimate lender fee is set out in your sanction letter and paid directly to the lender. If you receive such a request in our name, do not pay — call {PHONE_D} and report it.</p>
"""

# ---------------------------------------------------------------- DISCLAIMER
DISC = f"""
<p>Please read this disclaimer carefully before relying on anything published on this website.</p>

<h2>1. We are a distributor, not a lender</h2>
<p>{BRAND} is a loan distribution company and Direct Selling Agent, and an authorised Channel Partner of Ruloans Distribution Services Pvt. Ltd. <b>We are not a bank, NBFC or housing finance company.</b> We do not lend money, accept deposits, sanction loans or disburse funds. All lending is done by regulated banks and non-banking financial companies under their own credit policies.</p>

<h2>2. No guarantee of sanction</h2>
<p>Nothing on this website is an offer or a commitment to lend. Approval, loan amount, interest rate, tenure and all other conditions are decided exclusively by the lending institution following its own appraisal, verification and documentation process. Indicative eligibility shown here or discussed with us does not bind any lender.</p>

<h2>3. Rates and figures are indicative</h2>
<p>Interest rates, processing fees, charges, loan amounts, loan-to-value ratios, tenures and eligibility criteria published on this website were compiled from publicly available lender information in November 2026. They change frequently — with the RBI repo rate, with lender campaigns and with individual borrower profiles. The rate you are offered depends on your credit score, income, obligations, loan amount, property and the lender's policy on the day. <b>The only binding figures are those in your sanction letter, loan agreement and Key Facts Statement.</b></p>

<h2>4. The EMI calculator is an estimate</h2>
<p>The EMI calculator on this website applies the standard reducing-balance formula to the figures you enter. It does not account for processing fees deducted from disbursal, insurance premiums financed with the loan, rate resets on floating-rate facilities, part-disbursements or changes in tenure. Treat its output as an estimate for planning, not as a quotation.</p>

<h2>5. Not financial, legal or tax advice</h2>
<p>The content on this website is general information about loan products in India. It does not take account of your personal financial situation and is not a substitute for advice from a qualified financial adviser, chartered accountant or lawyer. Tax benefits referred to, such as those under Sections 24(b), 80C and 80E of the Income Tax Act, are subject to the provisions of the Act as amended and to your chosen tax regime. Please confirm your position with a tax professional.</p>

<h2>6. Borrow responsibly</h2>
<p>A loan is a long-term obligation. Default affects your credit record and, for a secured loan, can result in the lender enforcing its security — including proceeding against mortgaged property under the SARFAESI Act. Borrow only what you can repay comfortably, and read every document before you sign it.</p>

<h2>7. Fraud warning</h2>
<p>{SHORT} <b>never</b> asks applicants for an advance cash payment, for money transferred to a personal account, or for an OTP, password, PIN or card number. All lender fees are paid directly to the lender, and are reflected in your sanction letter. If you receive any such demand in our name, do not pay — call {PHONE_D} immediately and report it.</p>

<h2>8. Third-party content and marks</h2>
<p>References to banks, NBFCs, Ruloans, credit bureaus, regulators and other organisations are for identification and information only. All trademarks and logos belong to their respective owners. We are not responsible for the content, policies or practices of any external website linked from here.</p>

<h2>9. Accuracy and availability</h2>
<p>We take reasonable care to keep this website accurate and current but make no warranty that it is free from error or omission, or that it will be available without interruption. We may change or remove content at any time without notice.</p>

<h2>10. Limitation of liability</h2>
<p>To the extent permitted by law, {BRAND} accepts no liability for loss or damage arising from reliance on the content of this website, or from any act or omission of a lending institution.</p>
"""

for s in [
  legal("cookie-policy.html","Cookie Policy","Your browser",
        "The cookies and storage this website uses, what each one does, and how to switch them off.", COOKIE,
        "Cookie Policy | ANS Capital Services Pvt. Ltd.",
        "Cookie policy of ANS Capital Services Private Limited — the preference storage, analytics and advertising cookies used on this website and how to control them."),
  legal("enquiry-consent.html","Enquiry Consent Policy","Your permission",
        "What you authorise when you submit an enquiry, what it does not cover, and how to withdraw it.", CONSENT,
        "Enquiry Consent Policy | ANS Capital Services Pvt. Ltd.",
        "What you consent to when submitting a loan enquiry to ANS Capital Services Private Limited, how credit information is used, and how to withdraw consent at any time."),
  legal("privacy-policy.html","Privacy Policy","Your data",
        "What we collect, why we collect it, who we share it with — and what you can ask us to delete.", PRIV,
        "Privacy Policy | ANS Capital Services Pvt. Ltd.",
        "Privacy policy of ANS Capital Services Pvt. Ltd. — what personal and financial information we collect for loan applications, how it is used, who it is shared with and your rights over it."),
  legal("terms-conditions.html","Terms & Conditions","The agreement",
        "The terms on which we provide loan distribution services and on which you use this website.", TERMS,
        "Terms & Conditions | ANS Capital Services Pvt. Ltd.",
        "Terms and conditions for using the ANS Capital Services Pvt. Ltd. website and loan distribution services. We are a DSA and Ruloans channel partner, not a lender."),
  legal("disclaimer.html","Disclaimer","Please read",
        "We are a loan distributor, not a lender. Rates shown here are indicative. Here is exactly what that means.", DISC,
        "Disclaimer | ANS Capital Services Pvt. Ltd.",
        "Disclaimer — ANS Capital Services Pvt. Ltd. is a loan distribution company and Ruloans channel partner, not a bank or NBFC. Interest rates and figures on this site are indicative only."),
]:
    print(f"{s[0]:26s} {s[1]:>8,} bytes")
