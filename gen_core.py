# -*- coding: utf-8 -*-
"""ANS Capital Services — shared shell (head, nav, footer, rail, preloader)."""

SITE = "https://anscapitalservices.com"      # <-- change to the live domain
BRAND = "ANS Capital Services Pvt. Ltd."
SHORT = "ANS Capital Services"
PHONE = "919319667592"
PHONE_D = "+91 93196 67592"
EMAIL = "anscapitalservicespvtltd@gmail.com"
GSC = "REPLACE_WITH_GOOGLE_SEARCH_CONSOLE_TOKEN"
GA4 = "G-XXXXXXXXXX"
GTM = "GTM-XXXXXXX"
PIXEL = "XXXXXXXXXXXXXXX"
GMB_REVIEW = "https://g.page/r/REPLACE_WITH_GMB_REVIEW_LINK/review"
GMB_PROFILE = "https://www.google.com/maps/search/ANS+Capital+Services+Private+Limited"
# ----------------------------------------------------------------------
# TRUST CONFIG — the single place that controls the proof components.
# Everything here must be verifiable before it is switched on. Set
# GOOGLE["reviews"] to a real count and REVIEWS to real quotes, and the
# rating pill, stats band and testimonial wall all light up automatically.
# ----------------------------------------------------------------------
GOOGLE = {
    "rating": "5.0",         # every visible review is 5 stars
    "reviews": 8,            # visible on the profile — update to the live count
    "url": "https://www.google.com/maps/search/ANS+Capital+Services+Private+Limited",
    "review_url": "REPLACE_WITH_GMB_REVIEW_LINK",
}

# Real Google reviews, quoted from the profile. Names as the reviewers left them.
REVIEWS = [
    dict(stars=5, name="Akhilesh Kumar", role="Google review",
         quote="I got the services from the company very quickly and my money was also credited to my account within 12 hours."),
    dict(stars=5, name="Tabrej Aansari", role="Google review",
         quote="The services are very good and the loan is also available very quickly. Within some time my loan money was transferred to my account."),
    dict(stars=5, name="Ajay Sikari", role="Google review &middot; हिंदी",
         quote="Kam interest rate par loan mile tha.", gloss="Got the loan at a low interest rate."),
    dict(stars=5, name="Anoj Jatav", role="Google review", quote="Good finance."),
    dict(stars=5, name="Kailash Kumar", role="Google review", quote="Services. Financial plan."),
]

# Figures the business can evidence. Update as they grow.
STATS = [
    ("100+",        "clients served",         "Individuals and businesses helped to a sanctioned loan"),
    ("&#8377;25 Cr+", "arranged",             "Total loan value disbursed through our partner lending institutions"),
    ("5.0&#9733;",  "Google rating",          "From 8 reviews, every one of them five stars"),
    ("2 yrs",       "arranging loans",        "Working with borrowers across Delhi NCR and Uttar Pradesh since 2024"),
]

MAP_EMBED = "https://www.google.com/maps?q=ANS+Capital+Services+Private+Limited+India&output=embed"

SOCIAL = {
 "ig": "https://www.instagram.com/anscapitalservices",
 "fb": "https://www.facebook.com/profile.php?id=61596099088363",
 "li": "https://www.linkedin.com/in/ans-capital-service-56101a448/",
 "yt": "https://youtube.com/@anscapitalservice",
}

def wa(msg):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (PHONE, quote(msg))

WA_DEFAULT = wa("Hello ANS Capital Services, I would like to enquire about a loan. Please guide me.")

# ---------------------------------------------------------------- icons
I = {
"check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
"arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
"phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.23a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>',
"wa":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-1.77-.88-2.93-1.58-4.1-3.58-.31-.53.31-.5.89-1.64.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47s1.06 2.87 1.21 3.07c.15.2 2.1 3.2 5.08 4.49 3 1.29 3 .86 3.54.81.54-.05 1.75-.71 2-1.4.25-.69.25-1.28.17-1.4-.07-.13-.27-.2-.57-.35ZM12 2a10 10 0 0 0-8.5 15.26L2 22l4.86-1.47A10 10 0 1 0 12 2Zm0 18.18a8.17 8.17 0 0 1-4.27-1.2l-.3-.18-2.9.84.85-2.82-.2-.3A8.18 8.18 0 1 1 12 20.18Z"/></svg>',
"mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
"pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
"clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
"user":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
"home":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M9 21v-7h6v7"/></svg>',
"brief":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/></svg>',
"car":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17h14M3 13l2-5.5A2 2 0 0 1 6.9 6h10.2a2 2 0 0 1 1.9 1.5L21 13v4a1 1 0 0 1-1 1h-1a1 1 0 0 1-1-1v-1H6v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1Z"/><circle cx="7.5" cy="14.5" r="1"/><circle cx="16.5" cy="14.5" r="1"/></svg>',
"building":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V5a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v16M15 21V11h3a2 2 0 0 1 2 2v8M2 21h20M8 7h3M8 11h3M8 15h3"/></svg>',
"grad":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c3 2.5 9 2.5 12 0v-5"/></svg>',
"shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
"spark":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/><circle cx="12" cy="12" r="3"/></svg>',
"doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>',
"chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="m7 15 4-4 3 3 5-6"/></svg>',
"coins":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="6"/><path d="M18.1 10.4a6 6 0 0 1-9 7.5M7 6h2.5a1.5 1.5 0 0 1 0 3H7h3"/></svg>',
"card":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h3"/></svg>',
"handshake":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a2 2 0 0 1 0-2.8l.8-.8a2 2 0 0 1 2.8 0L22 9"/><path d="m2 9 3.5-3.5a2 2 0 0 1 2.8 0l4 4a2 2 0 0 1 0 2.8l-.8.8a2 2 0 0 1-2.8 0L6 11"/></svg>',
"clock2":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/><circle cx="12" cy="12" r="6"/><path d="M12 9v3l2 1"/></svg>',
"bot":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7V4M9 2h6"/><rect x="3" y="7" width="18" height="13" rx="3"/><circle cx="8.5" cy="13" r="1.3" fill="currentColor" stroke="none"/><circle cx="15.5" cy="13" r="1.3" fill="currentColor" stroke="none"/><path d="M9.5 17h5"/></svg>',
"chev":'<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
"ig":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.86s0 3.6-.07 4.86c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.86.07s-3.6 0-4.86-.07c-1.17-.05-1.8-.25-2.23-.41a3.8 3.8 0 0 1-1.38-.9 3.8 3.8 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.21 15.6 2.2 15.2 2.2 12s0-3.6.07-4.86c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.4 2.21 8.8 2.2 12 2.2Zm0 1.98c-3.14 0-3.5.01-4.74.07-1.14.05-1.76.24-2.17.4-.55.21-.94.47-1.35.88-.41.41-.67.8-.88 1.35-.16.41-.35 1.03-.4 2.17-.06 1.24-.07 1.6-.07 4.74s.01 3.5.07 4.74c.05 1.14.24 1.76.4 2.17.21.55.47.94.88 1.35.41.41.8.67 1.35.88.41.16 1.03.35 2.17.4 1.24.06 1.6.07 4.74.07s3.5-.01 4.74-.07c1.14-.05 1.76-.24 2.17-.4.55-.21.94-.47 1.35-.88.41-.41.67-.8.88-1.35.16-.41.35-1.03.4-2.17.06-1.24.07-1.6.07-4.74s-.01-3.5-.07-4.74c-.05-1.14-.24-1.76-.4-2.17a3.6 3.6 0 0 0-.88-1.35 3.6 3.6 0 0 0-1.35-.88c-.41-.16-1.03-.35-2.17-.4-1.24-.06-1.6-.07-4.74-.07Zm0 3.37a5.45 5.45 0 1 1 0 10.9 5.45 5.45 0 0 1 0-10.9Zm0 8.99a3.54 3.54 0 1 0 0-7.08 3.54 3.54 0 0 0 0 7.08Zm6.94-9.2a1.27 1.27 0 1 1-2.55 0 1.27 1.27 0 0 1 2.55 0Z"/></svg>',
"fb":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.77-3.89 1.1 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.45 2.89h-2.33v6.99A10 10 0 0 0 22 12Z"/></svg>',
"li":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3V9Zm7 0h3.8v1.65h.05A4.17 4.17 0 0 1 17.6 8.7c4 0 4.73 2.63 4.73 6.05V21h-4v-5.44c0-1.3-.02-2.97-1.81-2.97-1.82 0-2.1 1.42-2.1 2.88V21h-3.99V9Z"/></svg>',
"yt":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.5-.44-5.17a2.98 2.98 0 0 0-2.1-2.11C18.8 4.27 12 4.27 12 4.27s-6.8 0-8.46.45a2.98 2.98 0 0 0-2.1 2.11C1 8.5 1 12 1 12s0 3.5.44 5.17c.24.9.95 1.61 1.85 1.85 1.67.45 8.71.45 8.71.45s6.8 0 8.46-.45a2.98 2.98 0 0 0 2.1-2.11C23 15.5 23 12 23 12ZM9.75 15.27V8.73L15.5 12l-5.75 3.27Z"/></svg>',
}

# The four primary products (spec §5). The last two are additional services and are
# marked "subject to availability" on their own pages, per spec §6B.
NAV_PRODUCTS = [
 ("personal-loan.html", "Personal Loans", "Medical, education, travel, emergencies", "user"),
 ("home-loan.html", "Home Loans", "Purchase, construction, renovation", "home"),
 ("car-loan.html", "Car Loans", "New and pre-owned vehicle finance", "car"),
 ("business-loan.html", "Business Loans", "Working capital, expansion, equipment", "brief"),
]
EXTRA_PRODUCTS = [
 ("loan-against-property.html", "Loan Against Property", "Finance secured against property you own", "building"),
 ("other-loans.html", "Education, Gold & Other", "Education, gold, cards and insurance", "grad"),
]
ALL_PRODUCTS = NAV_PRODUCTS + EXTRA_PRODUCTS

def head(title, desc, path, keywords="", schema="", og_type="website"):
    url = SITE + "/" + path
    # the homepage's canonical is the bare domain, so the root and /index.html
    # do not compete as two addresses for the same page
    canon = SITE + "/" if path in ("index.html", "") else url
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="author" content="{BRAND}">
<meta name="publisher" content="{BRAND}">
<meta name="theme-color" content="#0A0806">
<meta name="format-detection" content="telephone=yes">
<meta name="geo.region" content="IN-UP">
<meta name="geo.placename" content="Delhi NCR and Uttar Pradesh">
<meta name="coverage" content="Delhi NCR, Uttar Pradesh, India">
<meta name="distribution" content="global">
<meta name="rating" content="general">
<link rel="alternate" hreflang="en-in" href="{canon}">
<link rel="alternate" hreflang="hi-in" href="{canon}">
<link rel="alternate" hreflang="x-default" href="{canon}">

<!-- Google Search Console verification -->
<meta name="google-site-verification" content="{GSC}">
<!-- Bing Webmaster -->
<meta name="msvalidate.01" content="REPLACE_WITH_BING_TOKEN">
<!-- Facebook domain verification -->
<meta name="facebook-domain-verification" content="REPLACE_WITH_META_BUSINESS_TOKEN">

<!-- Open Graph -->
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta property="og:locale:alternate" content="hi_IN">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/og-cover.jpg">

<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/logo.jpg">
<link rel="manifest" href="site.webmanifest">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap"></noscript>
<link rel="stylesheet" href="assets/css/style.css">

<!-- ===== Consent Mode v2 — defaults set before any Google tag loads =====
     Denied by default; assets/js/app.js updates it once the visitor chooses.
     Without this, EEA traffic is neither measured nor modelled. -->
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{
  ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',
  analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',
  wait_for_update:600
}});
gtag('set','ads_data_redaction',true);
gtag('set','url_passthrough',true);
</script>
<!-- ===== Google Tag Manager ===== -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM}');</script>
<!-- ===== GA4 ===== -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
<script>gtag('js',new Date());gtag('config','{GA4}',{{send_page_view:true}});</script>
<!-- ===== Meta Pixel ===== -->
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{PIXEL}');fbq('track','PageView');</script>

<script>window.ANS={{phone:'{PHONE}',phoneDisplay:'{PHONE_D}'}};</script>
<!-- scroll reveals only arm themselves once scripts are confirmed to run, so a script failure leaves every section visible -->
<script>document.documentElement.className+=' rv';</script>
{schema}
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
"""

PRE = """
<div id="pre" aria-hidden="true">
  <div class="pre-flash"></div>
  <div class="pre-stage">
    <div data-mark></div>
    <div class="pre-word">
      <div class="pw1" aria-hidden="true"></div>
      <div class="pw2">Capital Services</div>
      <div class="pw3">Private Limited</div>
      <div class="pw4">Building Your Financial Future</div>
    </div>
  </div>
  <button class="pre-skip" type="button">Skip intro</button>
</div>
"""

def nav(active=""):
    def cls(p): return ' aria-current="page"' if p == active else ''
    core = NAV_PRODUCTS
    extra = EXTRA_PRODUCTS
    col_a = "".join(f'<a href="{h}"{cls(h)}>{n}</a>' for h, n, _, _ in core)
    col_b = "".join(f'<a href="{h}"{cls(h)}>{n}</a>' for h, n, _, _ in extra)

    return f"""
<a class="skip-link" href="#main">Skip to content</a>

<header class="nav">
  <div class="nav-in">
    <div class="nav-side nav-left">
      <a class="ratepill" href="emi-calculator.html" data-ev="ratepill">
        <span class="rp-k">Indicative market rates</span>
        <span class="rp-row">
          <span class="rp-lbl">Home / Personal</span>
          <span class="rp-num" data-rate-a>7.35%</span>
          <span class="rp-sep">/</span>
          <span class="rp-num" data-rate-b>10.25%</span>
          <span class="rp-live"><i></i>p.a.</span>
        </span>
      </a>
    </div>

    <a class="nav-logo" href="index.html" aria-label="{BRAND} — home">
      <span data-logo></span>
      <span class="nm"><b>ANS</b><span>Capital Services</span></span>
    </a>

    <div class="nav-side nav-right">
      <a class="btn btn-gold btn-sm nav-join" href="contact.html#enquiry" data-enquire data-ev="cta_nav">
        <span data-hi="पूछताछ करें">Enquire Now</span>{I['user']}</a>
      <button class="navtoggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="sheet">
        <span class="nt-bars"><i></i><i></i></span>
        <span class="nt-x">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        </span>
      </button>
    </div>
  </div>
</header>

<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-label="Menu">
  <canvas class="rupee-field" data-rupees aria-hidden="true"></canvas>
  <span class="sheet-orb" aria-hidden="true"></span>

  <div class="sheet-in">
    <div class="panels">

      <section class="panel panel-wide">
        <h5>Loan products</h5>
        <div class="panel-2col">
          <nav class="panel-links" aria-label="Core loan products">{col_a}</nav>
          <nav class="panel-links" aria-label="Other loan products">{col_b}</nav>
        </div>
      </section>

      <section class="panel">
        <h5>Tools &amp; guides</h5>
        <nav class="panel-links" aria-label="Tools">
          <a href="emi-calculator.html"{cls('emi-calculator.html')}>EMI Calculator</a>
          <a href="how-it-works.html"{cls('how-it-works.html')}>How It Works</a>
          <a href="blog.html"{cls('blog.html')}>Knowledge Centre</a>
          <a href="faqs.html"{cls('faqs.html')}>FAQs</a>
        </nav>
      </section>

      <section class="panel">
        <h5>Company</h5>
        <nav class="panel-links" aria-label="Company">
          <a href="index.html"{cls('index.html')}>Home</a>
          <a href="about.html"{cls('about.html')}>About Us</a>
          <a href="services.html"{cls('services.html')}>Our Services</a>
          <a href="contact.html"{cls('contact.html')}>Contact Us</a>
        </nav>
      </section>

      <section class="panel panel-meter">
        <h5>Rate meter</h5>
        <div class="meter" data-meter>
          <div class="meter-top">
            <span class="meter-prod" data-meter-name>Home Loan</span>
            <span class="meter-val"><b data-meter-val>7.35</b>%<i>p.a.</i></span>
          </div>
          <div class="meter-track">
            <span class="meter-fill" data-meter-fill></span>
            <span class="meter-knob" data-meter-knob></span>
          </div>
          <div class="meter-scale"><span>7%</span><span>15%</span><span>24%</span></div>
          <p class="meter-note">Indicative market starting rates, Nov 2026. Not {SHORT}&rsquo;s terms.</p>
        </div>
        <div class="panel-ct">
          <a class="sheet-call" href="tel:+{PHONE}" data-ev="call_sheet">{I['phone']}<span>{PHONE_D}</span></a>
          <a class="sheet-call" href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_sheet">{I['wa']}<span>WhatsApp</span></a>
          <p class="sheet-hrs">Mon–Sat &middot; 10:00 AM – 7:00 PM</p>
          <div class="lang" style="margin-top:1rem;width:max-content">
            <button type="button" data-l="en" aria-pressed="true">English</button>
            <button type="button" data-l="hi" aria-pressed="false">हिंदी</button>
          </div>
        </div>
      </section>

    </div>
  </div>
</div>
"""

def footer():
    socs = (f'<a class="soc ig" href="{SOCIAL["ig"]}" target="_blank" rel="noopener me" aria-label="Instagram" data-ev="social_ig">{I["ig"]}</a>'
            f'<a class="soc fb" href="{SOCIAL["fb"]}" target="_blank" rel="noopener me" aria-label="Facebook" data-ev="social_fb">{I["fb"]}</a>'
            f'<a class="soc li" href="{SOCIAL["li"]}" target="_blank" rel="noopener me" aria-label="LinkedIn" data-ev="social_li">{I["li"]}</a>'
            f'<a class="soc yt" href="{SOCIAL["yt"]}" target="_blank" rel="noopener me" aria-label="YouTube" data-ev="social_yt">{I["yt"]}</a>'
            f'<a class="soc wa" href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="WhatsApp" data-ev="social_wa">{I["wa"]}</a>')
    prod = ''.join(f'<li><a href="{h}">{n}</a></li>' for h, n, _, _ in ALL_PRODUCTS)
    return f"""
<footer class="foot">
  <div class="wrap">
    <div class="foot-glass">
      <div class="foot-top">
        <div>
          <div class="foot-logo"><span data-logo></span><span><b>ANS</b><span>Capital Services Pvt. Ltd.</span></span></div>
          <p class="foot-tag">Building Your Financial Future</p>
          <p>A registered private limited loan distribution company and an authorised <b style="color:#C9DCF2">Channel Partner of Ruloans</b>. One application, compared across 265+ partner banks and NBFCs — you choose the best offer, we handle the paperwork.</p>
          <div class="socials" style="margin-top:1.6rem">{socs}</div>
        </div>
        <div>
          <h5>Loan Products</h5>
          <ul class="foot-links">{prod}</ul>
        </div>
        <div>
          <h5>Company</h5>
          <ul class="foot-links">
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Our Services</a></li>
            <li><a href="how-it-works.html">How It Works</a></li>
            <li><a href="emi-calculator.html">EMI Calculator</a></li>
            <li><a href="faqs.html">FAQs</a></li>
            <li><a href="blog.html">Knowledge Centre</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>
        <div>
          <h5>Get In Touch</h5>
          <ul class="foot-ct">
            <li>{I['phone']}<a href="tel:+{PHONE}" data-ev="call_footer">{PHONE_D}</a></li>
            <li>{I['wa']}<a href="{WA_DEFAULT}" target="_blank" rel="noopener" data-ev="wa_footer">WhatsApp us</a></li>
            <li>{I['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{I['clock']}<span>Mon – Sat · 10:00 AM – 7:00 PM</span></li>
            <li>{I['pin']}<span>Serving Delhi NCR &amp; across India</span></li>
          </ul>
          <a class="btn btn-gold btn-sm" style="margin-top:.4rem" href="contact.html" data-ev="cta_footer">Enquire Now {I['arrow']}</a>
        </div>
      </div>

      <div class="disclaimer">
        <b>Important disclosure:</b> {BRAND} is a loan distribution company / Direct Selling Agent (DSA) and an authorised Channel Partner of Ruloans. We are <b>not a bank, NBFC or lender</b> and we do not lend money ourselves. All loans are sanctioned and disbursed at the sole discretion of the partner bank or NBFC, subject to their credit policy, documentation and verification. Interest rates, fees, eligibility and tenures shown on this website are indicative, sourced from publicly available lender information, and change from time to time — the final terms are those stated in your sanction letter and Key Facts Statement. We never ask for any advance cash payment; every fee is paid directly to the lender. Please read all loan documents carefully before signing.
      </div>
    </div>
    <div class="foot-bot">
      <span>© <span data-year>2026</span> {BRAND}. All rights reserved.</span>
      <nav aria-label="Legal">
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms-conditions.html">Terms</a>
        <a href="disclaimer.html">Disclaimer</a>
        <a href="cookie-policy.html">Cookie Policy</a>
        <a href="enquiry-consent.html">Enquiry Consent</a>
        <a href="sitemap.xml">Sitemap</a>
        <button type="button" data-replay-intro class="replay-btn">Replay intro</button>
      </nav>
    </div>
  </div>
</footer>
"""

def rail():
    return f"""
<div class="rail">
  <button class="fab fab-bot" type="button" data-bot aria-label="Chat with ANS Assist" data-ev="bot_fab">{I['bot']}<span class="fab-lbl">Chat — हिंदी / English</span></button>
  <a class="fab fab-wa" href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="WhatsApp" data-ev="wa_fab">{I['wa']}<span class="fab-lbl">WhatsApp us</span></a>
  <a class="fab fab-call" href="tel:+{PHONE}" aria-label="Call" data-ev="call_fab">{I['phone']}<span class="fab-lbl">{PHONE_D}</span></a>
</div>
<div class="callbar" id="callbar">
  <span class="cb-txt"><b data-hi="लोन की बात करें?">Talk to a loan expert</b><span data-hi="सोम–शनि · सुबह 10 – शाम 7">Mon–Sat · 10 AM – 7 PM</span></span>
  <span class="cb-sep"></span>
  <a class="btn btn-ghost" href="tel:+{PHONE}" data-ev="call_bar">{I['phone']}<span data-hi="अभी कॉल करें">Call Now</span></a>
  <a class="btn btn-gold" href="contact.html#enquiry" data-enquire data-ev="cta_bar">{I['doc']}<span data-hi="पूछताछ करें">Enquire Now</span></a>
</div>

<div class="langnudge" id="langnudge" role="status" hidden>
  <span>हिंदी में देखना चाहेंगे?</span>
  <button type="button" data-lnudge-yes>हाँ, हिंदी</button>
  <button type="button" class="lx" data-lnudge-no aria-label="Dismiss">&times;</button>
</div>
"""

SCRIPTS = """
<script src="assets/js/logo.js"></script>
<script src="assets/js/preloader.js"></script>
<script src="assets/js/shader.js" defer></script>
<script src="assets/js/chatbot.js" defer></script>
<script src="assets/js/app.js" defer></script>
<script src="assets/js/ux.js" defer></script>
<script src="assets/js/nav.js" defer></script>
</body>
</html>
"""

def page(title, desc, path, body, active="", keywords="", schema="", pre=True):
    return head(title, desc, path, keywords, schema) + (PRE if pre else "") + nav(active) + body + footer() + rail() + SCRIPTS
