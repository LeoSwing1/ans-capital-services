# -*- coding: utf-8 -*-
from gen_core import *
from gen_parts import *

def product_page(p):
    key_rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in p["key"])
    variants = "".join(f"""<article class="card" data-rv data-delay="{i*80}">
        <div class="ci">{I[v[2]]}</div><h3>{v[0]}</h3><p style="margin:0">{v[1]}</p></article>"""
        for i, v in enumerate(p["variants"]))
    rate_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in p["rates"])
    elig = "".join(f"""<div class="doc-col"><h4>{I['user']}{t}</h4><ul>{''.join(f'<li>{x}</li>' for x in rows)}</ul></div>"""
                   for t, rows in p["elig"])
    docs = "".join(f"""<div class="doc-col"><h4>{I['doc']}{t}</h4><ul>{''.join(f'<li>{x}</li>' for x in rows)}</ul></div>"""
                   for t, rows in p["docs"])
    fees = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in p["fees"])
    uses = "".join(f"<li>{u}</li>" for u in p["uses"])
    tips = "".join(f"""<div class="card" data-rv data-delay="{i*80}"><div class="ci">{I['spark']}</div>
        <h3 style="font-size:1.08rem">{t}</h3><p style="margin:0">{d}</p></div>""" for i, (t, d) in enumerate(p["tips"]))

    side_nav = "".join(f'<li><a href="#{s}">{n}</a></li>' for s, n in [
        ("overview","Overview"),("variants","Types available"),("rates","Interest rates"),
        ("eligibility","Eligibility"),("documents","Documents"),("fees","Fees & charges"),
        ("tips","How to get a better deal"),("faq","FAQs")])

    schema = ld(ORG, WEBSITE,
        crumbs([("Home","index.html"),("Loans",""),(p["name"], p["slug"])]),
        loan_schema(p["name"], p["meta_desc"], p["slug"], p["apr"][0], p["apr"][1], p["max_amt"], p["term"][0], p["term"][1]),
        faq_schema(p["faqs"]),
        {"@type":"WebPage","@id":SITE+"/"+p["slug"]+"#webpage","url":SITE+"/"+p["slug"],
         "name":p["title"],"description":p["meta_desc"],"isPartOf":{"@id":SITE+"/#website"},
         "about":{"@id":SITE+"/"+p["slug"]+"#product"},"inLanguage":"en-IN",
         "primaryImageOfPage":{"@type":"ImageObject","url":SITE+"/assets/img/og-cover.jpg"}})

    body = f"""
<main id="main">
<section class="phead">
  {deco(("arc","tr",460,.14),("dots","bl",210,.05),("rays","l",300,.07))}{orb("tr",620,"gold")}{orb("bl",520,"navy")}
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span>/</span><span>Loans</span><span>/</span><span style="color:#C9DCF2">{p['name']}</span>
    </nav>
    <div class="split-wide" style="align-items:end">
      <div>
        <span class="eyebrow on-dark">{p['eyebrow']}</span>
        <h1 data-hi="{p['h1_hi']}">{p['h1']}</h1>
      </div>
      <div style="padding-bottom:.4rem">
        <p class="lead">{p['intro']}</p>
        <div class="phead-meta">
          <span class="hbadge">{I['chart']}From {p['from_rate']} p.a.</span>
          <span class="hbadge">{I['coins']}Up to {p['max_label']}</span>
          <span class="hbadge">{I['clock2']}{p['tenure_label']}</span>
        </div>
        <div class="btn-row" style="margin-top:1.6rem">
          <a class="btn btn-gold" href="tel:+{PHONE}" data-ev="call_{p['ev']}">{I['phone']}Call {PHONE_D}</a>
          <a class="btn btn-ghost-light" href="{wa('Hello ANS Capital Services, I am interested in a ' + p['name'] + '. Please share the best offer.')}" target="_blank" rel="noopener" data-ev="wa_{p['ev']}">{I['wa']}WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  {deco(("ring","tr",430,.05),("dots","bl",200,.045))}{orb("tr",540,"gold")}
  <div class="wrap">
    <div class="split-wide" style="align-items:start">
      <!-- sidebar -->
      <aside class="side">
        <div class="side-card">
          <h4>On this page</h4>
          <ul class="side-nav">{side_nav}</ul>
        </div>
        <div class="side-card" style="background:linear-gradient(160deg,var(--navy),var(--navy-900));border:0;color:#fff">
          <h4 style="color:#fff">Check your eligibility free</h4>
          <p style="font-size:.88rem;color:#A9C0DB;margin-bottom:1.2rem">Send us three details. We'll tell you where you stand before any lender runs a hard enquiry.</p>
          <a class="btn btn-gold btn-block btn-sm" href="{wa('Hello ANS Capital Services, please check my eligibility for a ' + p['name'] + '.')}" target="_blank" rel="noopener" data-ev="wa_side_{p['ev']}">{I['wa']}Check on WhatsApp</a>
          <a class="btn btn-ghost-light btn-block btn-sm" style="margin-top:.55rem" href="tel:+{PHONE}" data-ev="call_side_{p['ev']}">{I['phone']}{PHONE_D}</a>
        </div>
      </aside>

      <!-- content -->
      <div class="prose">
        {availability_notice(p['name']) if p.get('extra') else ''}
        <div id="overview" data-rv>
          <h2 style="margin-top:0">{p['ov_title']}</h2>
          {p['overview']}
          <div class="pullq">{p['quote']}</div>
          <h3>What people use it for</h3>
          <ul>{uses}</ul>
          <div class="tbl-wrap" style="margin:2rem 0">
            <table><caption class="sr-only">{p['name']} at a glance</caption>
              <thead><tr><th>Feature</th><th>What you get</th></tr></thead>
              <tbody>{key_rows}</tbody></table>
          </div>
        </div>

        <div class="hindi-box" data-rv style="margin:2.6rem 0">
          <h4>{p['hi_title']}</h4>
          {p['hi_body']}
          <div class="btn-row" style="margin-top:1.2rem">
            <a class="btn btn-gold btn-sm" href="tel:+{PHONE}" data-ev="call_hi_{p['ev']}">{I['phone']}हिंदी में बात करें</a>
            <button class="btn btn-ghost btn-sm" type="button" data-bot>{I['bot']}चैट में पूछें</button>
          </div>
        </div>

        <div id="variants" data-rv>
          <h2>Types of {p['name']} we arrange</h2>
          <p>{p['variants_intro']}</p>
          <div class="grid g2" style="margin:1.6rem 0 0">{variants}</div>
        </div>

        <div id="rates" data-rv style="margin-top:3rem">
          <span class="market-label">{I['doc']}General market information</span>
          <h2>{p['name']} interest rates in the market</h2>
          <p>{p['rates_intro']}</p>
          <div class="tbl-wrap" style="margin:1.6rem 0">
            <table><thead><tr><th>Lender category</th><th>Indicative rate (p.a.)</th><th>What to expect</th></tr></thead>
              <tbody>{rate_rows}</tbody></table>
          </div>
          {market_rate_notice()}
        </div>

        <div id="eligibility" data-rv style="margin-top:3rem">
          <h2>Who qualifies</h2>
          <p>{p['elig_intro']}</p>
          <div class="docs-grid" style="margin-top:1.6rem">{elig}</div>
        </div>

        <div id="documents" data-rv style="margin-top:3rem">
          <h2>Documents you'll need</h2>
          <p>Send clear soft copies on WhatsApp and we will pre-check the whole set before anything goes to a lender. A file that is complete on day one is the single biggest reason a sanction comes back fast.</p>
          <div class="docs-grid" style="margin-top:1.6rem">{docs}</div>
        </div>

        <div id="fees" data-rv style="margin-top:3rem">
          <h2>Fees and charges, stated upfront</h2>
          <p>{p['fees_intro']}</p>
          <div class="tbl-wrap" style="margin:1.6rem 0">
            <table><thead><tr><th>Charge</th><th>Typical range</th></tr></thead><tbody>{fees}</tbody></table>
          </div>
          <p><b>What ANS charges you: nothing in advance.</b> Our eligibility check, comparison and file handling cost you no money upfront. Every fee above is the lender's and is paid directly to the bank or NBFC. If anyone asks you for cash in our name, stop and call {PHONE_D}.</p>
        </div>

        <div id="tips" data-rv style="margin-top:3rem">
          <h2>How to get a better deal</h2>
          <div class="grid g2" style="margin-top:1.6rem">{tips}</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec wash" id="enquiry">
  {deco(("coin","tl",400,.05),("arc","br",360,.05))}{orb("br",600,"gold")}
  <div class="wrap-n">
    <div class="center" data-rv style="margin-bottom:2.6rem">
      <div class="orn"><i></i></div>
      <span class="eyebrow c">Apply</span>
      <h2>Start your {p['name']} enquiry</h2>
      <p class="lead" style="max-width:54ch;margin:1rem auto 0">Tell us what you need and we will come back with what is realistically available for your profile. No advance fee, and no obligation to proceed.</p>
    </div>
    <div class="card glass" data-rv style="padding:clamp(1.6rem,3vw,2.6rem)">{enquiry_form(p['ev'])}</div>
  </div>
</section>

{faq_block(p['faqs'], p['name'] + " — your questions answered")}
{cta_band()}
</main>
"""
    html = page(p["title"], p["meta_desc"], p["slug"], body, active=p["slug"], keywords=p["kw"], schema=schema)
    open(p["slug"], "w").write(html)
    return p["slug"], len(html)


if __name__ == "__main__":
    from data_products import P
    for p in P:
        slug, n = product_page(p)
        print(f"  {slug:<30} {n//1024} KB")
