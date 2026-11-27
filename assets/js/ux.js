/* ANS — UX layer: transitions, prefetch, progress, focus management, affordances */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var PHONE = (window.ANS && window.ANS.phone) || '919319667592';
  var PHONE_D = (window.ANS && window.ANS.phoneDisplay) || '+91 93196 67592';

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html) n.innerHTML = html;
    return n;
  }

  /* ---------------- scroll progress ---------------- */
  var bar = el('div', 'progress');
  bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);

  /* ---------------- back to top ---------------- */
  var top = el('button', 'totop',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>');
  top.type = 'button';
  top.setAttribute('aria-label', 'Back to top');
  top.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
    var h1 = document.querySelector('h1');
    if (h1) { h1.setAttribute('tabindex', '-1'); h1.focus({ preventScroll: true }); }
  });
  document.body.appendChild(top);

  /* The bar is scaled, not resized: width is a layout property and changing it
     on every scroll frame relayouts the document, while a transform stays on
     the compositor. The page height is measured once per resize rather than
     once per frame, so scrolling never reads layout at all. */
  var docH = 0;
  function measure() { docH = document.documentElement.scrollHeight - window.innerHeight; }
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var p = docH > 0 ? Math.min(window.scrollY / docH, 1) : 0;
      bar.style.transform = 'scaleX(' + p.toFixed(4) + ')';
      bar.classList.toggle('on', window.scrollY > 120);
      top.classList.toggle('on', window.scrollY > window.innerHeight * 0.9);
      ticking = false;
    });
  }
  measure();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function () { measure(); onScroll(); });
  if ('ResizeObserver' in window) new ResizeObserver(measure).observe(document.body);
  onScroll();

  /* ---------------- page transitions + prefetch ---------------- */
  var fade = el('div', 'page-fade');
  fade.setAttribute('aria-hidden', 'true');
  document.body.appendChild(fade);

  var prefetched = {};
  function prefetch(href) {
    if (!href || prefetched[href]) return;
    prefetched[href] = 1;
    var l = document.createElement('link');
    l.rel = 'prefetch';
    l.href = href;
    l.as = 'document';
    document.head.appendChild(l);
  }

  function isInternal(a) {
    if (!a || !a.href) return false;
    if (a.target === '_blank' || a.hasAttribute('download')) return false;
    if (a.dataset.enquire !== undefined) return false;
    var u;
    try { u = new URL(a.href, location.href); } catch (e) { return false; }
    if (u.origin !== location.origin) return false;
    if (!/\.html?$/.test(u.pathname) && u.pathname !== '/' ) return false;
    if (u.pathname === location.pathname && u.hash) return false;  // same-page anchor
    return true;
  }

  document.addEventListener('pointerover', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (isInternal(a)) prefetch(a.href);
  }, { passive: true });

  /* Where the browser can cross-fade between documents itself, the click goes
     straight through: the navigation is immediate and the fade is the
     browser's, which is smoother than holding the page back for 220 ms. */
  var nativeVT = 'startViewTransition' in document &&
                 window.CSS && CSS.supports && CSS.supports('view-transition-name', 'none');

  if (!reduce && !nativeVT) {
    document.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      var a = e.target.closest && e.target.closest('a');
      if (!isInternal(a)) return;
      e.preventDefault();
      document.body.classList.add('leaving');
      setTimeout(function () { location.href = a.href; }, 220);
      // safety: if navigation is blocked, restore the page
      setTimeout(function () { document.body.classList.remove('leaving'); }, 2500);
    });
    window.addEventListener('pageshow', function (ev) {
      if (ev.persisted) document.body.classList.remove('leaving');
    });
  }

  /* ---------------- nav dropdown: hover intent + keyboard ---------------- */
  document.querySelectorAll('.nav-menu li.has-drop').forEach(function (li) {
    var btn = li.querySelector('button');
    var drop = li.querySelector('.drop');
    if (!btn || !drop) return;
    var inT, outT;

    function open() { li.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    function shut() { li.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }

    if (window.matchMedia('(hover:hover)').matches) {
      li.addEventListener('pointerenter', function () {
        clearTimeout(outT);
        inT = setTimeout(open, 90);                  // intent delay: no flicker in passing
      });
      li.addEventListener('pointerleave', function () {
        clearTimeout(inT);
        outT = setTimeout(shut, 180);                // forgiving exit
      });
    }

    // keyboard: arrows move through the links, Escape closes back to the trigger
    li.addEventListener('keydown', function (e) {
      var links = Array.prototype.slice.call(drop.querySelectorAll('a'));
      var i = links.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') {
        e.preventDefault(); open();
        (links[i + 1] || links[0]).focus();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (i <= 0) { btn.focus(); shut(); } else links[i - 1].focus();
      } else if (e.key === 'Escape') {
        shut(); btn.focus();
      } else if (e.key === 'Tab' && i === links.length - 1 && !e.shiftKey) {
        shut();
      }
    });
  });

  /* ---------------- focus trap: mobile drawer ---------------- */
  var sheet = document.getElementById('sheet');
  var burger = document.querySelector('.navtoggle');
  if (sheet && burger) {
    document.addEventListener('keydown', function (e) {
      if (!document.body.classList.contains('menu-open')) return;
      if (e.key === 'Escape') {
        document.body.classList.remove('menu-open');
        document.documentElement.style.overflow = '';
        burger.setAttribute('aria-expanded', 'false');
        burger.focus();
        return;
      }
      if (e.key !== 'Tab') return;
      var f = sheet.querySelectorAll('a[href],button:not([disabled]),input,select');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    // move focus into the drawer when it opens
    burger.addEventListener('click', function () {
      if (!document.body.classList.contains('menu-open')) return;
      setTimeout(function () {
        var a = sheet.querySelector('a[href]');
        if (a) a.focus();
      }, 420);
    });
  }

  /* ---------------- scrollable tables: edge fade + swipe hint ---------------- */
  document.querySelectorAll('.tbl-wrap').forEach(function (w) {
    function sync() {
      var over = w.scrollWidth > w.clientWidth + 4;
      w.classList.toggle('scrollable', over);
      w.classList.toggle('scrolled-end', w.scrollLeft + w.clientWidth >= w.scrollWidth - 6);
    }
    w.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
    if (!w.nextElementSibling || !w.nextElementSibling.classList.contains('swipe-hint')) {
      var hint = el('p', 'swipe-hint',
        'Swipe to see more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>');
      w.parentNode.insertBefore(hint, w.nextSibling);
    }
  });

  /* ---------------- map: reveal once loaded ---------------- */
  var mapHost = document.querySelector('[data-map]');
  if (mapHost) {
    var mo = new MutationObserver(function () {
      var f = mapHost.querySelector('iframe');
      if (f) {
        f.addEventListener('load', function () { mapHost.classList.add('loaded'); });
        setTimeout(function () { mapHost.classList.add('loaded'); }, 4000);  // never stay shimmering
        mo.disconnect();
      }
    });
    mo.observe(mapHost, { childList: true });
  }

  /* ---------------- desktop: tapping Call copies the number too ---------------- */
  if (window.matchMedia('(min-width:961px)').matches && navigator.clipboard) {
    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
      a.addEventListener('click', function () {
        navigator.clipboard.writeText(PHONE_D).then(function () {
          if (window.ANS && window.ANS.toast) window.ANS.toast('Number copied — ' + PHONE_D);
        }).catch(function () {});
      });
    });
  }

  /* ---------------- cursor-aware sheen on cards ---------------- */
  if (window.matchMedia('(hover:hover) and (min-width:960px)').matches && !reduce) {
    document.querySelectorAll('.card,.svc,.post').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      }, { passive: true });
    });
  }

  /* ---------------- headings rise out of their own baseline ----------------
     Progressive enhancement, deliberately. The hidden state is added here, in
     script, and only once we know IntersectionObserver works — so a JS failure
     leaves headings visible rather than blank. The heading also clips itself to
     zero height while hidden, so it can never satisfy a threshold on itself:
     we observe an unclipped ancestor instead. */
  (function headingReveal() {
    if (reduce || !('IntersectionObserver' in window)) return;

    var heads = [];
    document.querySelectorAll('main h1, main h2').forEach(function (h) {
      if (h.closest('.acc-q')) return;
      heads.push(h);
    });
    if (!heads.length) return;

    function show(h) {
      h.classList.add('mask-ready');          // ensure the transition has a from-state
      requestAnimationFrame(function () { h.classList.add('in'); });
    }

    var groups = new Map();
    heads.forEach(function (h) {
      var anchor = h.parentElement || h;
      if (!groups.has(anchor)) groups.set(anchor, []);
      groups.get(anchor).push(h);
    });

    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        (groups.get(en.target) || []).forEach(function (h) {
          if (document.body.classList.contains('loading')) {
            window.addEventListener('ans:intro-done', function () {
              setTimeout(function () { show(h); }, 140);
            }, { once: true });
            setTimeout(function () { show(h); }, 5200);
          } else {
            show(h);
          }
        });
        io.unobserve(en.target);
      });
    }, { threshold: 0, rootMargin: '0px 0px -6% 0px' });

    // hide only what is genuinely below the fold; anything already on screen
    // is revealed on the next frame so nothing flashes or sticks
    heads.forEach(function (h) {
      if (h.getBoundingClientRect().top > window.innerHeight * 0.92) h.classList.add('mask-ready');
    });
    groups.forEach(function (_, anchor) { io.observe(anchor); });

    // final guarantee: nothing stays hidden, whatever happens
    setTimeout(function () {
      document.querySelectorAll('h1.mask-ready:not(.in),h2.mask-ready:not(.in)').forEach(function (h) {
        if (h.getBoundingClientRect().top < window.innerHeight * 1.6) h.classList.add('in');
      });
    }, 6500);
    window.addEventListener('beforeprint', function () {
      document.querySelectorAll('.mask-ready').forEach(function (h) { h.classList.add('in'); });
    });
  })();

  /* ---------------- articles: mark for the reading bar ---------------- */
  if (document.querySelector('.prose') && /blog|loan-guide|emi|credit-score|documents-checklist|car-loan-mistakes|business-loan-documents/.test(location.pathname)) {
    document.body.classList.add('is-article');
  }
})();
