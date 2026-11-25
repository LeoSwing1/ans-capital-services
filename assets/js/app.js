/* ANS Capital Services — site behaviour */
(function () {
  'use strict';
  var W = window.ANS || (window.ANS = {});
  var PHONE = W.phone || '919319667592';

  /* ---------------- analytics helper (GA4 / GTM / Meta Pixel safe) --------------- */
  window.ansTrack = function (name, params) {
    params = params || {};
    try { if (typeof gtag === 'function') gtag('event', name, params); } catch (e) {}
    try { if (window.dataLayer) window.dataLayer.push(Object.assign({ event: name }, params)); } catch (e) {}
    try { if (typeof fbq === 'function') fbq('trackCustom', name, params); } catch (e) {}
  };
  /* Standard GA4 / Meta names for the three actions that are worth money,
     so conversions can be imported into Google Ads and Meta without rework. */
  var CONVERSIONS = {
    call_hero: ['click_to_call', 'Contact'], call_sheet: ['click_to_call', 'Contact'],
    call_fab: ['click_to_call', 'Contact'], call_rail: ['click_to_call', 'Contact'],
    call_footer: ['click_to_call', 'Contact'], call_now: ['click_to_call', 'Contact'],
    wa_fab: ['whatsapp_click', 'Contact'], wa_sheet: ['whatsapp_click', 'Contact'],
    wa_rail: ['whatsapp_click', 'Contact'], wa_footer: ['whatsapp_click', 'Contact'],
    gmb_review: ['review_click', 'Lead'], gmb_directions: ['directions_click', 'FindLocation'],
    gmb_profile: ['gmb_profile_click', 'ViewContent']
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-ev]');
    if (!a) return;
    var ev = a.getAttribute('data-ev');
    var base = { href: a.getAttribute('href') || '', page: location.pathname, link_text: (a.textContent || '').trim().slice(0, 60) };
    window.ansTrack(ev, base);
    var map = CONVERSIONS[ev];
    if (map) {
      try { if (typeof gtag === 'function') gtag('event', map[0], base); } catch (x) {}
      try { if (typeof fbq === 'function') fbq('track', map[1], { content_name: ev }); } catch (x) {}
      try { if (window.dataLayer) window.dataLayer.push({ event: map[0], ans_source: ev }); } catch (x) {}
    }
  });

  /* Consent Mode v2 — the banner, or the visitor's stored choice, flips this.
     Call window.ansConsent(true|false) from whichever banner you deploy. */
  window.ansConsent = function (granted) {
    var v = granted ? 'granted' : 'denied';
    try {
      if (typeof gtag === 'function') gtag('consent', 'update', {
        ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v
      });
      localStorage.setItem('ans_consent', v);
    } catch (x) {}
  };
  try {
    var stored = localStorage.getItem('ans_consent');
    if (stored) window.ansConsent(stored === 'granted');
  } catch (x) {}

  /* First-touch attribution: the campaign that actually brought the visitor in
     is stamped on the enquiry, instead of the last click before the form. */
  try {
    if (!sessionStorage.getItem('ans_src')) {
      var q = new URLSearchParams(location.search), src = {};
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid'].forEach(function (k) {
        if (q.get(k)) src[k] = q.get(k);
      });
      if (!src.utm_source && document.referrer && document.referrer.indexOf(location.host) === -1) {
        src.referrer = document.referrer.slice(0, 180);
      }
      sessionStorage.setItem('ans_src', JSON.stringify(src));
    }
    window.ANS.source = JSON.parse(sessionStorage.getItem('ans_src') || '{}');
  } catch (x) { window.ANS.source = {}; }

  /* ---------------- logo injection --------------- */
  function paintLogos() {
    document.querySelectorAll('[data-logo]').forEach(function (n, i) {
      if (n.dataset.done) return;
      n.dataset.done = '1';
      n.innerHTML = window.ANSLogo('lg' + i, {});
    });
  }
  paintLogos();

  /* ---------------- nav --------------- */
  var nav = document.querySelector('.nav');
  var lastY = window.scrollY;
  function onScroll() {
    var y = window.scrollY;
    if (nav) {
      nav.classList.toggle('scrolled', y > 24);
      if (y > 420 && y > lastY + 6 && !document.body.classList.contains('menu-open')) nav.classList.add('hide');
      else if (y < lastY - 6 || y < 200) nav.classList.remove('hide');
    }
    lastY = y;
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* dropdowns */
  document.querySelectorAll('.nav-menu li.has-drop').forEach(function (li) {
    var btn = li.querySelector('button');
    if (!btn) return;
    btn.setAttribute('aria-expanded', 'false');
    function shut() { li.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var was = li.classList.contains('open');
      document.querySelectorAll('.nav-menu li.open').forEach(function (o) {
        o.classList.remove('open');
        var b = o.querySelector('button'); if (b) b.setAttribute('aria-expanded', 'false');
      });
      if (!was) { li.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    });
    li.addEventListener('mouseleave', shut);
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-menu')) {
      document.querySelectorAll('.nav-menu li.open').forEach(function (o) { o.classList.remove('open'); });
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.nav-menu li.open').forEach(function (o) { o.classList.remove('open'); });
      document.body.classList.remove('menu-open');
    }
  });

  /* mobile sheet */
  var burger = document.querySelector('.navtoggle');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', String(open));
      document.documentElement.style.overflow = open ? 'hidden' : '';
    });
  }
  document.querySelectorAll('.sheet a, .sheet').forEach(function (n) {
    n.addEventListener('click', function (e) {
      if (n.tagName === 'A' || e.target === n) {
        document.body.classList.remove('menu-open');
        document.documentElement.style.overflow = '';
        if (burger) burger.setAttribute('aria-expanded', 'false');
      }
    });
  });

  /* ---------------- scroll reveal --------------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) {
          var d = parseInt(en.target.dataset.delay || 0, 10);
          setTimeout(function () { en.target.classList.add('in'); }, d);
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px' });
    document.querySelectorAll('[data-rv]').forEach(function (n) { io.observe(n); });

    var so = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); so.unobserve(en.target); } });
    }, { threshold: 0.4 });
    document.querySelectorAll('.step').forEach(function (n) { so.observe(n); });
  } else {
    document.querySelectorAll('[data-rv]').forEach(function (n) { n.classList.add('in'); });
  }

  /* ---------------- counters --------------- */
  function animateCount(el) {
    var target = parseFloat(el.dataset.count), dec = (el.dataset.dec | 0), dur = 1500, t0 = null;
    function tick(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var e = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * e).toFixed(dec).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { animateCount(en.target); co.unobserve(en.target); } });
    }, { threshold: 0.6 });
    document.querySelectorAll('[data-count]').forEach(function (n) { co.observe(n); });
  }

  /* ---------------- accordion --------------- */
  document.querySelectorAll('.acc-q').forEach(function (q) {
    q.setAttribute('aria-expanded', 'false');
    q.addEventListener('click', function () {
      var item = q.closest('.acc-i'), panel = item.querySelector('.acc-a');
      var open = item.classList.toggle('open');
      q.setAttribute('aria-expanded', String(open));
      panel.style.maxHeight = open ? panel.scrollHeight + 'px' : 0;
      if (open) {
        var sibs = item.parentElement.querySelectorAll('.acc-i.open');
        sibs.forEach(function (s) {
          if (s !== item) {
            s.classList.remove('open');
            s.querySelector('.acc-a').style.maxHeight = 0;
            s.querySelector('.acc-q').setAttribute('aria-expanded', 'false');
          }
        });
      }
    });
  });
  window.addEventListener('resize', function () {
    document.querySelectorAll('.acc-i.open .acc-a').forEach(function (p) { p.style.maxHeight = p.scrollHeight + 'px'; });
  });

  /* ---------------- number helpers --------------- */
  function inr(n) { return '₹' + Math.round(n).toLocaleString('en-IN'); }
  function shortINR(n) {
    if (n >= 1e7) return '₹' + (n / 1e7).toFixed(n % 1e7 === 0 ? 0 : 2).replace(/\.00$/, '') + ' Cr';
    if (n >= 1e5) return '₹' + (n / 1e5).toFixed(n % 1e5 === 0 ? 0 : 1).replace(/\.0$/, '') + ' L';
    if (n >= 1e3) return '₹' + (n / 1e3).toFixed(0) + 'K';
    return '₹' + n;
  }
  W.inr = inr; W.shortINR = shortINR;

  /* ---------------- EMI calculator (spec §7) --------------- */
  document.querySelectorAll('[data-calc]').forEach(function (root) {
    var A = root.querySelector('[data-amt]'), R = root.querySelector('[data-rate]'), T = root.querySelector('[data-ten]');
    if (!A || !R || !T) return;
    var oA = root.querySelector('[data-o-amt]'), oR = root.querySelector('[data-o-rate]'), oT = root.querySelector('[data-o-ten]');
    var emiEl = root.querySelector('[data-emi]'), pEl = root.querySelector('[data-principal]'),
        iEl = root.querySelector('[data-interest]'), tEl = root.querySelector('[data-total]'),
        nEl = root.querySelector('[data-months]');
    var seg = root.querySelector('.donut .seg'), midP = root.querySelector('[data-mid-pct]');
    var barP = root.querySelector('.emi-bar .p'), barN = root.querySelector('.emi-bar .n');
    var unit = 'years';
    var CIRC = 2 * Math.PI * 52;   /* r = 52 */

    function paint(el) {
      var pct = (el.value - el.min) / (el.max - el.min) * 100;
      el.style.background = 'linear-gradient(90deg,#C99A35 0%,#DFBA6B ' + pct + '%,#E3E8EF ' + pct + '%)';
    }

    function setUnit(u) {
      if (u === unit) return;
      var yrs = unit === 'years' ? +T.value : +T.value / 12;
      unit = u;
      if (u === 'months') { T.min = 6; T.max = 360; T.step = 6; T.value = Math.round(yrs * 12); }
      else { T.min = 1; T.max = 30; T.step = 1; T.value = Math.max(1, Math.round(yrs)); }
      root.querySelectorAll('[data-unit]').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.unit === u));
      });
      var ends = root.querySelector('[data-ten-ends]');
      if (ends) ends.innerHTML = u === 'months'
        ? '<span>6 months</span><span>360 months</span>'
        : '<span>1 year</span><span>30 years</span>';
      calc();
    }
    root.querySelectorAll('[data-unit]').forEach(function (b) {
      b.addEventListener('click', function () { setUnit(b.dataset.unit); window.ansTrack('emi_unit', { unit: b.dataset.unit }); });
    });

    function calc() {
      var P = +A.value, r = +R.value;
      var n = unit === 'months' ? Math.round(+T.value) : Math.round(+T.value * 12);
      var i = r / 1200;
      var emi = i > 0 ? P * i * Math.pow(1 + i, n) / (Math.pow(1 + i, n) - 1) : P / n;
      var tot = emi * n, intr = tot - P;

      if (oA) oA.textContent = shortINR(P);
      if (oR) oR.textContent = r.toFixed(2) + '%';
      if (oT) oT.textContent = unit === 'months'
        ? (+T.value + (+T.value === 1 ? ' month' : ' months'))
        : (+T.value + (+T.value === 1 ? ' year' : ' years'));
      if (emiEl) emiEl.textContent = inr(emi);
      if (pEl) pEl.textContent = inr(P);
      if (iEl) iEl.textContent = inr(intr);
      if (tEl) tEl.textContent = inr(tot);
      if (nEl) nEl.textContent = n + ' EMIs';

      var pPct = tot > 0 ? (P / tot * 100) : 100;
      if (barP && barN) { barP.style.width = pPct + '%'; barN.style.width = (100 - pPct) + '%'; }
      if (seg) {
        var dash = CIRC * (pPct / 100);
        seg.style.strokeDasharray = dash + ' ' + (CIRC - dash);
      }
      if (midP) midP.textContent = Math.round(pPct) + '%';

      [A, R, T].forEach(paint);

      var wa = root.querySelector('[data-wa-emi]');
      if (wa) {
        wa.href = 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent(
          'Hello ANS Capital Services,\n\nI used the EMI calculator on your website:\n' +
          'Loan amount: ' + inr(P) + '\nInterest rate assumed: ' + r + '% p.a.\n' +
          'Tenure: ' + (unit === 'months' ? n + ' months' : (+T.value) + ' years') + ' (' + n + ' EMIs)\n' +
          'Estimated EMI: ' + inr(emi) + '\nEstimated total interest: ' + inr(intr) +
          '\n\nPlease help me understand the options available for this requirement.');
      }
      /* let an enquiry form on the same page pick the calculation up */
      window.ANSLastCalc = {
        amount: inr(P), rate: r + '% p.a.',
        tenure: unit === 'months' ? n + ' months' : (+T.value) + ' years',
        emi: inr(emi), interest: inr(intr), total: inr(tot)
      };
    }

    [A, R, T].forEach(function (sl) {
      sl.addEventListener('input', calc);
      sl.addEventListener('change', function () { window.ansTrack('emi_calculate', { page: location.pathname }); });
    });
    calc();
  });

  /* attach the last EMI calculation to an enquiry, if the visitor asks (spec §7) */
  document.querySelectorAll('[data-attach-calc]').forEach(function (b) {
    b.addEventListener('click', function () {
      var c = window.ANSLastCalc;
      var box = document.querySelector('form[data-enquiry] [name="message"]');
      if (!c || !box) return;
      box.value = ('My EMI calculation — amount ' + c.amount + ', rate ' + c.rate + ', tenure ' + c.tenure +
                   ', estimated EMI ' + c.emi + '. ' + (box.value || '')).trim();
      var form = box.closest('form');
      window.scrollTo({ top: form.getBoundingClientRect().top + window.scrollY - 110, behavior: 'smooth' });
      setTimeout(function () { box.focus({ preventScroll: true }); }, 600);
      window.ansTrack('emi_attach_to_enquiry', {});
    });
  });

  /* ---------------- enquiry forms --------------- */
  function hiNow() { return document.documentElement.lang === 'hi-IN'; }

  document.querySelectorAll('form[data-enquiry]').forEach(function (f) {
    var ctx = f.dataset.enquiry || 'enquiry';
    var btn = f.querySelector('button[type="submit"]');
    var okBox = f.querySelector('[data-msg-ok]');
    var errBox = f.querySelector('[data-msg-err]');
    var trigger = f.querySelector('[data-cond-trigger]');

    /* conditional fields — shown AND enabled only when they apply */
    function syncCond() {
      if (!trigger) return;
      var v = trigger.value;
      f.querySelectorAll('[data-cond]').forEach(function (row) {
        var on = row.dataset.cond === v;
        row.classList.toggle('on', on);
        row.querySelectorAll('input,select,textarea').forEach(function (i) { i.disabled = !on; });
      });
    }
    if (trigger) { trigger.addEventListener('change', syncCond); syncCond(); }

    function mark(el, bad) {
      var fieldEl = el.closest('.field') || el.closest('.consent');
      if (fieldEl) fieldEl.classList.toggle('invalid', bad);
      return !bad;
    }
    function clearState() {
      okBox && okBox.classList.remove('show');
      errBox && errBox.classList.remove('show');
      f.querySelectorAll('.invalid').forEach(function (n) { n.classList.remove('invalid'); });
    }
    f.addEventListener('input', function (e) {
      var fieldEl = e.target.closest('.field, .consent');
      if (fieldEl) fieldEl.classList.remove('invalid');
    });

    function validate() {
      var ok = true, firstBad = null;
      var nameEl = f.querySelector('[name="name"]');
      var phoneEl = f.querySelector('[name="phone"]');
      var mailEl = f.querySelector('[name="email"]');
      var consentEl = f.querySelector('[name="consent"]');

      if (nameEl && !nameEl.value.trim()) { ok = mark(nameEl, true) && ok; ok = false; firstBad = firstBad || nameEl; }
      else if (nameEl) mark(nameEl, false);

      if (phoneEl) {
        var d = phoneEl.value.replace(/\D/g, '').replace(/^91/, '');
        if (!/^[6-9]\d{9}$/.test(d)) { mark(phoneEl, true); ok = false; firstBad = firstBad || phoneEl; }
        else mark(phoneEl, false);
      }
      if (mailEl && mailEl.value.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mailEl.value.trim())) {
        mark(mailEl, true); ok = false; firstBad = firstBad || mailEl;
      } else if (mailEl) mark(mailEl, false);

      if (consentEl && !consentEl.checked) { mark(consentEl, true); ok = false; firstBad = firstBad || consentEl; }
      else if (consentEl) mark(consentEl, false);

      if (firstBad) { try { firstBad.focus({ preventScroll: false }); } catch (e) { firstBad.focus(); } }
      return ok;
    }

    f.addEventListener('submit', function (e) {
      e.preventDefault();
      clearState();

      if (!validate()) {
        errBox.querySelector('[data-msg-err-text]').textContent = hiNow()
          ? 'कृपया लाल रंग में दिखाए गए खाने ठीक करें और दोबारा भेजें।'
          : 'Please correct the highlighted fields and submit again.';
        errBox.classList.add('show');
        return;
      }

      /* build the enquiry summary from enabled fields only */
      var fd = new FormData(f), lines = [], name = '', phone = '';
      fd.forEach(function (v, k) {
        if (k === 'consent' || !String(v).trim()) return;
        var input = f.querySelector('[name="' + k + '"]');
        if (input && input.disabled) return;
        var label = (input && input.dataset.label) || k.replace(/_/g, ' ');
        lines.push(label.charAt(0).toUpperCase() + label.slice(1) + ': ' + v);
        if (k === 'name') name = v;
        if (k === 'phone') phone = v;
      });

      /* duplicate submission prevention — same payload within 10 minutes */
      var sig = ctx + '|' + lines.join('|');
      try {
        var prev = JSON.parse(sessionStorage.getItem('ans_sent') || '{}');
        if (prev.sig === sig && (Date.now() - prev.at) < 600000) {
          okBox.querySelector('[data-msg-ok-text]').textContent = hiNow()
            ? 'यह पूछताछ अभी-अभी भेजी जा चुकी है। हम जल्द ही संपर्क करेंगे — दोबारा भेजने की ज़रूरत नहीं।'
            : 'This enquiry was just sent. We have it and will be in touch — no need to submit again.';
          okBox.classList.add('show');
          okBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
          return;
        }
      } catch (err) {}

      btn.setAttribute('aria-busy', 'true');

      /* the first-touch campaign travels with the enquiry, so the team can
         see which channel produced the lead without opening analytics */
      var src = window.ANS.source || {};
      var srcLine = Object.keys(src).length
        ? '\nCame from: ' + Object.keys(src).map(function (k) { return k + '=' + src[k]; }).join(', ')
        : '';

      var msg = 'New enquiry — ANS Capital Services website\n\n' + lines.join('\n') +
                '\n\nSource page: ' + location.pathname.replace(/^\//, '') +
                '\nForm: ' + ctx + srcLine;

      window.ansTrack('generate_lead', Object.assign({
        source: ctx, page: location.pathname,
        loan_type: fd.get('loan_type') || '', city: fd.get('city') || ''
      }, src));
      try { if (typeof gtag === 'function') gtag('event', 'generate_lead', { currency: 'INR', value: 0, lead_source: ctx }); } catch (x) {}
      try { if (typeof fbq === 'function') fbq('track', 'Lead', { content_name: ctx }); } catch (x) {}

      var url = 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent(msg);

      setTimeout(function () {
        var opened = false;
        try {
          var w = window.open(url, '_blank', 'noopener');
          opened = !!(w && !w.closed);
        } catch (err) { opened = false; }

        if (!opened) {
          var a = document.createElement('a');
          a.href = url; a.target = '_blank'; a.rel = 'noopener';
          document.body.appendChild(a); a.click(); a.remove();
        }

        try { sessionStorage.setItem('ans_sent', JSON.stringify({ sig: sig, at: Date.now() })); } catch (err) {}

        btn.removeAttribute('aria-busy');
        var first = String(name).trim().split(' ')[0];
        okBox.querySelector('[data-msg-ok-text]').textContent = hiNow()
          ? ('धन्यवाद ' + first + '! आपकी पूछताछ WhatsApp पर भेजने के लिए तैयार है। अगर WhatsApp नहीं खुला, तो नीचे दिए नंबर पर कॉल कर लीजिए — हम वहीं से आगे बढ़ा देंगे।')
          : ('Thank you ' + first + '. We have opened WhatsApp with your details filled in. If it did not open, call us on ' + '+91 93196 67592' + ' and we will take it from there.');
        okBox.classList.add('show');
        okBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
        f.reset();
        syncCond();
      }, 520);
    });
  });

  /* "Enquire Now" — scroll to the form on this page, else go to Contact (spec §11) */
  document.querySelectorAll('[data-enquire]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var form = document.querySelector('form[data-enquiry]');
      if (!form) return;                                   // no form here: follow the href
      e.preventDefault();
      var target = form.closest('section') || form;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 96, behavior: 'smooth' });
      setTimeout(function () {
        var first = form.querySelector('input:not([disabled])');
        if (first && window.innerWidth > 720) first.focus({ preventScroll: true });
      }, 650);
      window.ansTrack('enquire_click', { page: location.pathname });
      document.body.classList.remove('menu-open');
      document.documentElement.style.overflow = '';
    });
  });

  /* ---------------- site language: auto-detect + manual toggle --------------- */
  var LKEY = 'ans_lang', LSET = 'ans_lang_set';

  function applyLang(l, fromUser) {
    document.documentElement.lang = l === 'hi' ? 'hi-IN' : 'en-IN';
    document.documentElement.setAttribute('data-lang', l);
    document.querySelectorAll('[data-hi]').forEach(function (n) {
      if (n.dataset.en === undefined) n.dataset.en = n.innerHTML;
      var next = (l === 'hi') ? n.dataset.hi : n.dataset.en;
      if (n.innerHTML !== next) n.innerHTML = next;
    });
    document.querySelectorAll('[data-hi-ph]').forEach(function (n) {
      if (n.dataset.enPh === undefined) n.dataset.enPh = n.placeholder;
      n.placeholder = (l === 'hi') ? n.dataset.hiPh : n.dataset.enPh;
    });
    document.querySelectorAll('.lang button').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.l === l));
    });
    try {
      localStorage.setItem(LKEY, l);
      if (fromUser) localStorage.setItem(LSET, '1');
    } catch (e) {}
    // keep the assistant in the same language
    if (window.ANSBot && window.ANSBot.setLang) window.ANSBot.setLang(l);
    // a heading swapped by the language toggle must not stay clipped
    document.querySelectorAll('h1.mask-ready,h2.mask-ready').forEach(function (h) { h.classList.add('in'); });
    window.ANSLang = l;
  }
  window.ansApplyLang = applyLang;

  document.querySelectorAll('.lang button').forEach(function (b) {
    b.addEventListener('click', function () {
      applyLang(b.dataset.l, true);
      window.ansTrack('lang_switch', { lang: b.dataset.l, source: 'toggle' });
    });
  });

  /* Automatic choice:
     1. a language the visitor picked before always wins
     2. otherwise follow the browser / device language
     3. if the browser is English but an Indian locale, offer Hindi once, non-intrusively */
  (function autoLang() {
    var stored = null, userSet = false;
    try { stored = localStorage.getItem(LKEY); userSet = localStorage.getItem(LSET) === '1'; } catch (e) {}

    if (userSet && stored) { applyLang(stored); return; }

    var langs = (navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || 'en'])
                .join(',').toLowerCase();
    var wantsHindi = /\bhi\b|hi-|hi_/.test(langs);

    if (wantsHindi) {
      applyLang('hi');
      window.ansTrack('lang_auto', { lang: 'hi' });
      return;
    }

    applyLang(stored === 'hi' ? 'hi' : 'en');

    // Indian visitor on an English browser — ask once, politely
    var indian = /-in\b|_in\b/.test(langs);
    try { if (!indian) indian = (Intl.DateTimeFormat().resolvedOptions().timeZone || '').indexOf('Calcutta') > -1 || (Intl.DateTimeFormat().resolvedOptions().timeZone || '').indexOf('Kolkata') > -1; } catch (e) {}
    var asked = false;
    try { asked = sessionStorage.getItem('ans_lang_ask') === '1'; } catch (e) {}
    if (!indian || asked || stored) return;

    var nudge = document.getElementById('langnudge');
    if (!nudge) return;
    setTimeout(function () {
      try { sessionStorage.setItem('ans_lang_ask', '1'); } catch (e) {}
      nudge.hidden = false;
      requestAnimationFrame(function () { nudge.classList.add('show'); });
      var hide = function () { nudge.classList.remove('show'); setTimeout(function () { nudge.hidden = true; }, 500); };
      nudge.querySelector('[data-lnudge-yes]').onclick = function () {
        applyLang('hi', true); hide();
        window.ansTrack('lang_switch', { lang: 'hi', source: 'nudge' });
      };
      nudge.querySelector('[data-lnudge-no]').onclick = function () {
        try { localStorage.setItem(LSET, '1'); } catch (e) {} hide();
      };
      setTimeout(function () { if (!nudge.hidden) hide(); }, 12000);
    }, 6500);
  })();

  /* ---------------- bottom action bar --------------- */
  (function bottomBar() {
    var bar = document.getElementById('callbar');
    if (!bar) return;
    var foot = document.querySelector('.foot');
    var footTop = Infinity;
    function measure() { if (foot) footTop = foot.getBoundingClientRect().top + window.scrollY; }
    measure();
    window.addEventListener('resize', measure);
    window.addEventListener('load', measure);

    function tick() {
      var y = window.scrollY, vh = window.innerHeight;
      var past = y > Math.min(vh * 0.55, 520);
      var atFoot = (y + vh) > (footTop + 180);
      var on = past && !atFoot;
      bar.classList.toggle('show', on);
      document.body.classList.toggle('bar-on', on);
    }
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('ans:intro-done', function () { measure(); tick(); });
    setTimeout(function () { measure(); tick(); }, 900);
    tick();
  })();

  /* ---------------- chatbot launchers --------------- */
  document.querySelectorAll('[data-bot]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      if (window.ANSBot) window.ANSBot.toggle();
    });
  });

  /* ---------------- sticky side-nav highlight --------------- */
  var sideLinks = document.querySelectorAll('.side-nav a[href^="#"]');
  if (sideLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    sideLinks.forEach(function (a) {
      var s = document.querySelector(a.getAttribute('href'));
      if (s) map[s.id] = a;
    });
    var ao = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) {
          sideLinks.forEach(function (a) { a.classList.remove('on'); });
          if (map[en.target.id]) map[en.target.id].classList.add('on');
        }
      });
    }, { rootMargin: '-25% 0px -65% 0px' });
    Object.keys(map).forEach(function (id) { ao.observe(document.getElementById(id)); });
  }

  /* ---------------- smooth anchor offset --------------- */
  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var tgt = document.querySelector(a.getAttribute('href'));
      if (!tgt) return;
      e.preventDefault();
      var top = tgt.getBoundingClientRect().top + window.scrollY - 104;
      window.scrollTo({ top: top, behavior: 'smooth' });
      history.replaceState(null, '', a.getAttribute('href'));
    });
  });

  /* ---------------- replay the intro (spec §3) --------------- */
  document.querySelectorAll('[data-replay-intro]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      try { sessionStorage.removeItem('ans_intro_v1'); } catch (err) {}
      location.reload();
    });
  });

  /* ---------------- current year --------------- */
  document.querySelectorAll('[data-year]').forEach(function (n) { n.textContent = new Date().getFullYear(); });

  /* ---------------- lazy map (perf) --------------- */
  var mapHost = document.querySelector('[data-map]');
  if (mapHost && 'IntersectionObserver' in window) {
    var mo = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) {
          var f = document.createElement('iframe');
          f.src = mapHost.dataset.map;
          f.loading = 'lazy';
          f.referrerPolicy = 'no-referrer-when-downgrade';
          f.title = 'ANS Capital Services location map';
          f.allowFullscreen = true;
          mapHost.prepend(f);
          mo.unobserve(mapHost);
        }
      });
    }, { rootMargin: '300px' });
    mo.observe(mapHost);
  }
})();
