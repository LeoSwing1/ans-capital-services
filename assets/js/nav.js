/* ANS — menu ornament: drifting rupee glyphs, and the indicative rate meter */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Decorative canvases are capped well below display refresh and stop when
     the tab is hidden. They are ornament: spending a full 60fps budget on
     them is what makes a page feel heavy while scrolling. */
  var hidden = document.hidden;
  document.addEventListener('visibilitychange', function () { hidden = document.hidden; });
  var PHONE = window.innerWidth < 760 || matchMedia('(pointer: coarse)').matches;
  var CANVAS_FPS = PHONE ? 20 : ((navigator.hardwareConcurrency || 4) <= 4 ? 24 : 30);
  function gate() {
    var step = 1000 / CANVAS_FPS, prev = -1e9;
    return function (t) { if (t - prev < step) return false; prev = t; return true; };
  }

  /* ------------------------------------------------------------------
     Rupee field — glyphs wandering inside the circle behind the panels
     ------------------------------------------------------------------ */
  (function rupees() {
    var cv = document.querySelector('[data-rupees]');
    if (!cv || reduce) return;
    var ctx = cv.getContext('2d');
    if (!ctx) return;

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, glyphs = [], raf = null, running = false;

    function size() {
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = Math.max(1, W * dpr); cv.height = Math.max(1, H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function orbRect() {
      var orb = document.querySelector('.sheet-orb');
      if (!orb) return { cx: W * 0.28, cy: H * 0.5, r: Math.min(W, H) * 0.34 };
      var r = orb.getBoundingClientRect(), s = cv.getBoundingClientRect();
      return { cx: r.left - s.left + r.width / 2, cy: r.top - s.top + r.height / 2, r: r.width / 2 };
    }

    function build() {
      var o = orbRect();
      var n = W < 700 ? 11 : 20;
      glyphs = [];
      for (var i = 0; i < n; i++) {
        var a = Math.random() * Math.PI * 2;
        var rr = Math.sqrt(Math.random()) * o.r * 1.04;
        glyphs.push({
          x: o.cx + Math.cos(a) * rr,
          y: o.cy + Math.sin(a) * rr,
          vx: (Math.random() - .5) * 0.22,
          vy: (Math.random() - .5) * 0.22,
          s: 13 + Math.random() * 30,
          o: 0.08 + Math.random() * 0.28,
          rot: (Math.random() - .5) * 0.5,
          vr: (Math.random() - .5) * 0.004,
          ph: Math.random() * Math.PI * 2,
          sp: 0.4 + Math.random() * 0.8
        });
      }
    }

    var okMenu = gate();
    function frame(t) {
      raf = requestAnimationFrame(frame);
      if (hidden || !okMenu(t)) return;
      ctx.clearRect(0, 0, W, H);
      var o = orbRect();
      var time = t * 0.001;

      for (var i = 0; i < glyphs.length; i++) {
        var g = glyphs[i];
        /* wander: drift plus a slow sinusoidal sway, so paths look organic */
        g.x += g.vx + Math.sin(time * g.sp + g.ph) * 0.18;
        g.y += g.vy + Math.cos(time * g.sp * 0.8 + g.ph) * 0.15;
        g.rot += g.vr;

        /* keep them loosely gathered in the circle */
        var dx = g.x - o.cx, dy = g.y - o.cy;
        var d = Math.sqrt(dx * dx + dy * dy) || 1;
        if (d > o.r * 1.06) {
          g.vx -= (dx / d) * 0.012;
          g.vy -= (dy / d) * 0.012;
        }
        g.vx *= 0.995; g.vy *= 0.995;

        var fade = 1 - Math.max(0, (d - o.r * 0.82) / (o.r * 0.42));
        fade = Math.max(0, Math.min(1, fade));

        ctx.save();
        ctx.translate(g.x, g.y);
        ctx.rotate(g.rot);
        ctx.font = '500 ' + g.s + 'px Outfit, Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(232,190,110,' + (g.o * fade).toFixed(3) + ')';
        ctx.fillText('₹', 0, 0);
        ctx.restore();
      }
    }

    function start() {
      if (running) return;
      running = true; size(); build();
      raf = requestAnimationFrame(frame);
    }
    function stop() {
      running = false;
      if (raf) cancelAnimationFrame(raf);
      ctx.clearRect(0, 0, W, H);
    }

    /* only animate while the menu is open */
    var mo = new MutationObserver(function () {
      document.body.classList.contains('menu-open') ? start() : stop();
    });
    mo.observe(document.body, { attributes: true, attributeFilter: ['class'] });
    window.addEventListener('resize', function () { if (running) { size(); build(); } });
  })();

  /* ------------------------------------------------------------------
     Rate meter — indicative market starting rates, plotted 7%–24%
     These are published market figures, not ANS's own terms.
     ------------------------------------------------------------------ */
  /* Indian digit grouping: 23,893 / 1,23,893 — not the western 123,893 */
  function inr(n) {
    n = Math.round(n); var s = String(n);
    if (s.length <= 3) return '\u20B9' + s;
    var last3 = s.slice(-3), rest = s.slice(0, -3);
    return '\u20B9' + rest.replace(/\B(?=(\d{2})+(?!\d))/g, ',') + ',' + last3;
  }
  /* standard reducing-balance EMI — arithmetic on a published market rate */
  function emiOf(P, rate, months) {
    var r = rate / 1200;
    return P * r * Math.pow(1 + r, months) / (Math.pow(1 + r, months) - 1);
  }

  [].slice.call(document.querySelectorAll('[data-meter]')).forEach(function meter(root) {
    var nameEl = root.querySelector('[data-meter-name]'),
        valEl  = root.querySelector('[data-meter-val]'),
        fill   = root.querySelector('[data-meter-fill]'),
        knob   = root.querySelector('[data-meter-knob]'),
        emiEl  = root.querySelector('[data-meter-emi]'),
        onEl   = root.querySelector('[data-meter-on]'),
        live   = root.hasAttribute('data-meter-live');

    var MIN = 7, MAX = 24;
    /* name, starting rate, a representative ticket size, tenure in months */
    var items = [
      ['Home Loan',             7.35, 3000000, 240],
      ['Car Loan',              7.40,  800000,  84],
      ['Business (secured)',    8.25, 2500000, 120],
      ['Loan Against Property', 8.60, 4000000, 180],
      ['Personal Loan',        10.25,  500000,  60],
      ['Business (unsecured)', 14.00, 1000000,  36]
    ];
    var i = 0, timer = null, countRaf = null;

    function pct(v) { return ((v - MIN) / (MAX - MIN)) * 100; }

    function countTo(target) {
      var start = parseFloat(valEl.textContent) || MIN, t0 = null, dur = 700;
      cancelAnimationFrame(countRaf);
      function step(ts) {
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var e = 1 - Math.pow(1 - p, 3);
        valEl.textContent = (start + (target - start) * e).toFixed(2);
        if (p < 1) countRaf = requestAnimationFrame(step);
      }
      countRaf = requestAnimationFrame(step);
    }

    function show(n) {
      var it = items[n];
      nameEl.style.opacity = 0;
      setTimeout(function () { nameEl.textContent = it[0]; nameEl.style.opacity = 1; }, 180);
      var p = pct(it[1]);
      fill.style.width = p + '%';
      knob.style.left = p + '%';
      if (reduce) valEl.textContent = it[1].toFixed(2); else countTo(it[1]);
      if (emiEl) emiEl.textContent = inr(emiOf(it[2], it[1], it[3])) + '/mo';
      if (onEl)  onEl.textContent  = 'on ' + inr(it[2]) + ' \u00B7 ' + (it[3] / 12) + ' yrs';
    }

    function run() {
      show(i);
      if (!timer) timer = setInterval(function () { i = (i + 1) % items.length; show(i); }, 2600);
    }
    function halt() { clearInterval(timer); timer = null; }

    /* the hero meter runs whenever it is on screen; the menu one only while open */
    if (live) {
      show(0);
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) {
          es.forEach(function (e) { e.isIntersecting ? run() : halt(); });
        }, { threshold: 0.2 }).observe(root);
      } else run();
      root.addEventListener('pointerenter', halt);
      root.addEventListener('pointerleave', run);
      return;
    }

    var mo = new MutationObserver(function () {
      if (document.body.classList.contains('menu-open')) { if (!timer) run(); }
      else halt();
    });
    mo.observe(document.body, { attributes: true, attributeFilter: ['class'] });

  });

  (function ratePill() {
  /* the pill in the bar cycles the same two headline figures */
  var a = document.querySelector('[data-rate-a]'), b = document.querySelector('[data-rate-b]');
  if (a && b && !reduce) {
    var pairs = [['7.35%', '10.25%'], ['7.40%', '8.25%'], ['8.60%', '14.00%']];
    var lbl = document.querySelector('.rp-lbl');
    var names = ['Home / Personal', 'Car / Business', 'Property / Unsecured'];
    var k = 0;
    setInterval(function () {
      k = (k + 1) % pairs.length;
      [a, b, lbl].forEach(function (el) { if (el) el.style.opacity = 0; });
      setTimeout(function () {
        a.textContent = pairs[k][0]; b.textContent = pairs[k][1];
        if (lbl) lbl.textContent = names[k];
        [a, b, lbl].forEach(function (el) { if (el) el.style.opacity = 1; });
      }, 260);
    }, 4200);
  }
  })();
})();

/* ANS — trust components: starfield behind the rating pill, orbital promise ring */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hidden = document.hidden;
  document.addEventListener('visibilitychange', function () { hidden = document.hidden; });
  var PHONE = window.innerWidth < 760 || matchMedia('(pointer: coarse)').matches;
  var CANVAS_FPS = PHONE ? 20 : ((navigator.hardwareConcurrency || 4) <= 4 ? 24 : 30);
  function gate() {
    var step = 1000 / CANVAS_FPS, prev = -1e9;
    return function (t) { if (t - prev < step) return false; prev = t; return true; };
  }

  /* ---------- starfield ---------- */
  (function stars() {
    var cv = document.querySelector('[data-stars]');
    if (!cv || PHONE) return;
    var ctx = cv.getContext('2d'); if (!ctx) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2), W = 0, H = 0, pts = [], raf;

    function build() {
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = Math.max(1, W * dpr); cv.height = Math.max(1, H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.min(150, Math.round(W * H / 5200));
      pts = [];
      for (var i = 0; i < n; i++) {
        pts.push({ x: Math.random() * W, y: Math.random() * H,
                   r: Math.random() * 1.25 + .25,
                   o: Math.random() * .6 + .12,
                   sp: Math.random() * 1.6 + .4,
                   ph: Math.random() * Math.PI * 2 });
      }
    }
    var okStars = gate();
    function draw(t) {
      if (!reduce) raf = requestAnimationFrame(draw);
      if (hidden || !okStars(t)) return;
      ctx.clearRect(0, 0, W, H);
      var time = t * 0.001;
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        var tw = reduce ? 1 : (0.55 + 0.45 * Math.sin(time * p.sp + p.ph));
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, 6.2832);
        ctx.fillStyle = 'rgba(244,239,233,' + (p.o * tw).toFixed(3) + ')';
        ctx.fill();
      }
    }
    build();
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) { cancelAnimationFrame(raf); raf = requestAnimationFrame(draw); }
          else cancelAnimationFrame(raf);
        });
      }, { threshold: 0 }).observe(cv);
    } else raf = requestAnimationFrame(draw);
    window.addEventListener('resize', build);
  })();

  /* ---------- promise ring ---------- */

  /* ------------------------------------------------------------------
     Ring icon field — many small finance marks drifting in the band
     between the orbit edge and the centred text. The canvas is clipped
     to that annulus with an even-odd path, so a glyph can never be
     painted over a letter of the readout.
     ------------------------------------------------------------------ */

  /* ------------------------------------------------------------------
     Hero rupees — a field of rupee marks rising across the top of the
     site. Each glyph fades to nothing as it nears the headline, the
     sub-copy, the buttons or the meter, so no letter is ever obscured.
     ------------------------------------------------------------------ */
  (function heroRupees() {
    var cv = document.querySelector('[data-herorupees]');
    if (!cv || reduce) return;
    var ctx = cv.getContext('2d');
    if (!ctx) return;

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, marks = [], raf = null, live = false, keepOut = [];

    /* the boxes a glyph must not be drawn over, in canvas coordinates */
    function readKeepOut() {
      var base = cv.getBoundingClientRect();
      keepOut = [];
      ['.hero-h', '.hero-sub', '.hero-cta', '.hero-foot', '.hmeter', '.strip-grid', '.rate-pill']
        .forEach(function (sel) {
          var el = document.querySelector(sel);
          if (!el) return;
          var r = el.getBoundingClientRect();
          if (!r.width || !r.height) return;
          keepOut.push({ x: r.left - base.left, y: r.top - base.top, w: r.width, h: r.height });
        });
    }

    /* 0 near the text, 1 well away from it — a soft margin, not a hard edge */
    function clearance(x, y) {
      var m = 34, min = 1;
      for (var i = 0; i < keepOut.length; i++) {
        var b = keepOut[i];
        var dx = Math.max(b.x - x, 0, x - (b.x + b.w));
        var dy = Math.max(b.y - y, 0, y - (b.y + b.h));
        var d  = Math.hypot(dx, dy);
        var f  = d >= m ? 1 : d / m;
        if (f < min) min = f;
        if (min === 0) return 0;
      }
      return min;
    }

    function size() {
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = Math.max(1, W * dpr); cv.height = Math.max(1, H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      readKeepOut();
    }

    function spawn(seed) {
      return {
        x: Math.random() * W,
        y: seed ? Math.random() * H : H + 40,
        s: 11 + Math.random() * 34,
        o: 0.07 + Math.random() * 0.3,
        vy: -(0.14 + Math.random() * 0.5),
        drift: (Math.random() - .5) * 0.28,
        rot: (Math.random() - .5) * 0.5,
        vr: (Math.random() - .5) * 0.0045,
        ph: Math.random() * 6.3,
        sp: 0.3 + Math.random() * 0.7
      };
    }

    function build() {
      var n = PHONE ? 11 : 34;
      marks = [];
      for (var i = 0; i < n; i++) marks.push(spawn(true));
    }

    var okHero = gate();
    function frame(t) {
      raf = requestAnimationFrame(frame);
      if (hidden || !okHero(t)) return;
      ctx.clearRect(0, 0, W, H);
      var time = t * 0.001;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      for (var i = 0; i < marks.length; i++) {
        var g = marks[i];
        g.y += g.vy;
        g.x += g.drift + Math.sin(time * g.sp + g.ph) * 0.22;
        g.rot += g.vr;
        if (g.y < -50) marks[i] = spawn(false);
        if (g.x < -60) g.x = W + 50;
        if (g.x > W + 60) g.x = -50;

        var a = g.o * clearance(g.x, g.y);
        if (a < 0.004) continue;
        /* fade in at the foot and out at the head of the hero */
        a *= Math.min(1, (H - g.y) / 120) * Math.min(1, g.y / 90 + .25);

        ctx.save();
        ctx.translate(g.x, g.y);
        ctx.rotate(g.rot);
        ctx.font = '600 ' + g.s.toFixed(1) + 'px Inter, "Noto Sans Devanagari", sans-serif';
        ctx.fillStyle = 'rgba(232,190,110,' + a.toFixed(3) + ')';
        ctx.fillText('₹', 0, 0);
        ctx.restore();
      }
    }

    function start() { if (live) return; live = true; size(); build(); raf = requestAnimationFrame(frame); }
    function stop()  { live = false; if (raf) cancelAnimationFrame(raf); ctx.clearRect(0, 0, W, H); }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? start() : stop(); });
      }, { threshold: 0.02 }).observe(cv);
    } else start();
    window.addEventListener('resize', function () { if (live) { size(); build(); } });
    /* the layout settles after fonts and the preloader, so re-read the boxes */
    window.addEventListener('load', function () { setTimeout(readKeepOut, 400); });
    /* reading layout on a timer forces a reflow against whatever the page is
       doing; folding it into the animation frame costs nothing extra */
    var kcount = 0;
    var origFrame = frame;
    frame = function (t) { if ((kcount = (kcount + 1) % 40) === 0) readKeepOut(); origFrame(t); };
  })();

  (function ringField() {
    var cv = document.querySelector('[data-ringfield]');
    if (!cv || reduce || PHONE) return;
    var ctx = cv.getContext('2d');
    if (!ctx) return;

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, R = 0, INNER = 0, bits = [], raf = null, live = false;

    /* simple paths so nothing depends on a font shipping the glyph */
    function house(c, s) {
      c.beginPath(); c.moveTo(0, -s); c.lineTo(s, 0); c.lineTo(s * .62, 0);
      c.lineTo(s * .62, s * .8); c.lineTo(-s * .62, s * .8); c.lineTo(-s * .62, 0);
      c.lineTo(-s, 0); c.closePath(); c.stroke();
    }
    function car(c, s) {
      c.beginPath(); c.moveTo(-s, s * .3); c.lineTo(-s * .7, -s * .25);
      c.lineTo(s * .7, -s * .25); c.lineTo(s, s * .3); c.closePath(); c.stroke();
      c.beginPath(); c.arc(-s * .55, s * .45, s * .2, 0, 6.3); c.stroke();
      c.beginPath(); c.arc(s * .55, s * .45, s * .2, 0, 6.3); c.stroke();
    }
    function bag(c, s) {
      c.strokeRect(-s, -s * .45, s * 2, s * 1.4);
      c.beginPath(); c.moveTo(-s * .4, -s * .45); c.lineTo(-s * .4, -s * .85);
      c.lineTo(s * .4, -s * .85); c.lineTo(s * .4, -s * .45); c.stroke();
    }
    function shield(c, s) {
      c.beginPath(); c.moveTo(0, -s); c.lineTo(s * .8, -s * .6); c.lineTo(s * .8, s * .2);
      c.quadraticCurveTo(s * .8, s, 0, s * 1.1);
      c.quadraticCurveTo(-s * .8, s, -s * .8, s * .2);
      c.lineTo(-s * .8, -s * .6); c.closePath(); c.stroke();
    }
    function bars(c, s) {
      [[-s * .7, s * .5], [0, s * 1.1], [s * .7, s * 1.5]].forEach(function (b, i) {
        c.strokeRect(b[0] - s * .22, s * .6 - b[1], s * .44, b[1]);
      });
    }
    function doc(c, s) {
      c.strokeRect(-s * .62, -s, s * 1.24, s * 2);
      c.beginPath();
      c.moveTo(-s * .3, -s * .35); c.lineTo(s * .3, -s * .35);
      c.moveTo(-s * .3, s * .1);  c.lineTo(s * .3, s * .1);
      c.moveTo(-s * .3, s * .55); c.lineTo(s * .1, s * .55);
      c.stroke();
    }
    function coin(c, s) {
      c.beginPath(); c.arc(0, 0, s, 0, 6.3); c.stroke();
      c.font = '700 ' + (s * 1.15).toFixed(1) + 'px Inter, "Noto Sans Devanagari", sans-serif';
      c.textAlign = 'center'; c.textBaseline = 'middle';
      c.fillText('₹', 0, s * .06);
    }
    function glyph(ch) {
      return function (c, s) {
        c.font = '600 ' + (s * 2.1).toFixed(1) + 'px Inter, "Noto Sans Devanagari", sans-serif';
        c.textAlign = 'center'; c.textBaseline = 'middle';
        c.fillText(ch, 0, 0);
      };
    }
    var KINDS = [coin, coin, coin, glyph('₹'), glyph('₹'), glyph('%'), glyph('%'),
                 house, car, bag, shield, bars, doc];

    function size() {
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = Math.max(1, W * dpr); cv.height = Math.max(1, H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      R = Math.min(W, H) / 2;
      var read = document.querySelector('.ring-read');
      var orbit = cv.getBoundingClientRect();
      if (read) {
        var b = read.getBoundingClientRect();
        /* the circle that encloses the text, plus a margin */
        INNER = Math.hypot(b.width, b.height) / 2 + 14;
      } else INNER = R * 0.52;
      INNER = Math.min(INNER, R * 0.86);
    }

    function build() {
      var n = W < 620 ? 22 : 52;
      bits = [];
      for (var i = 0; i < n; i++) {
        var a = Math.random() * Math.PI * 2;
        var rr = INNER + Math.random() * Math.max(10, (R - INNER));
        bits.push({
          a: a, r: rr,
          va: (Math.random() < .5 ? -1 : 1) * (0.00028 + Math.random() * 0.0007),
          vr: (Math.random() - .5) * 0.09,
          s: 5 + Math.random() * 11,
          o: 0.16 + Math.random() * 0.34,
          rot: Math.random() * 6.3,
          vrot: (Math.random() - .5) * 0.006,
          k: KINDS[(Math.random() * KINDS.length) | 0],
          ph: Math.random() * 6.3
        });
      }
    }

    var okRing = gate();
    function frame(t) {
      raf = requestAnimationFrame(frame);
      if (hidden || !okRing(t)) return;
      ctx.clearRect(0, 0, W, H);
      var cx = W / 2, cy = H / 2, time = t * 0.001;

      /* clip to the band: outer disc minus the disc that holds the words */
      ctx.save();
      ctx.beginPath();
      ctx.arc(cx, cy, R - 1, 0, Math.PI * 2);
      ctx.arc(cx, cy, INNER, 0, Math.PI * 2, true);
      ctx.clip('evenodd');

      for (var i = 0; i < bits.length; i++) {
        var g = bits[i];
        g.a += g.va;
        g.r += g.vr * 0.1 + Math.sin(time * 0.5 + g.ph) * 0.12;
        if (g.r < INNER + 4) { g.r = INNER + 4; g.vr = Math.abs(g.vr); }
        if (g.r > R - 6)     { g.r = R - 6;     g.vr = -Math.abs(g.vr); }
        g.rot += g.vrot;

        var x = cx + Math.cos(g.a) * g.r, y = cy + Math.sin(g.a) * g.r;
        var tw = 0.65 + 0.35 * Math.sin(time * 1.1 + g.ph);

        ctx.save();
        ctx.translate(x, y); ctx.rotate(g.rot);
        ctx.lineWidth = 1.1;
        ctx.strokeStyle = 'rgba(232,190,110,' + (g.o * tw).toFixed(3) + ')';
        ctx.fillStyle   = 'rgba(232,190,110,' + (g.o * tw).toFixed(3) + ')';
        g.k(ctx, g.s);
        ctx.restore();
      }
      ctx.restore();
    }

    function start() { if (live) return; live = true; size(); build(); raf = requestAnimationFrame(frame); }
    function stop()  { live = false; if (raf) cancelAnimationFrame(raf); ctx.clearRect(0, 0, W, H); }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? start() : stop(); });
      }, { threshold: 0.1 }).observe(cv);
    } else start();
    window.addEventListener('resize', function () { if (live) { size(); build(); } });
  })();

  (function ring() {
    var root = document.querySelector('[data-ring]');
    if (!root) return;
    var nodes = [].slice.call(root.querySelectorAll('.ring-node'));
    var items = [].slice.call(root.querySelectorAll('.ring-item'));
    var nEl = root.querySelector('[data-ring-n]');
    if (!nodes.length || !items.length) return;

    var i = 0, timer = null, HOLD = 1800;

    function show(k, manual) {
      i = (k + items.length) % items.length;
      nodes.forEach(function (n, j) { n.classList.toggle('on', j === i); });
      items.forEach(function (n, j) { n.classList.toggle('on', j === i); });
      if (nEl) nEl.textContent = String(i + 1).padStart(2, '0');
      if (manual) restart();
    }
    function next() { show(i + 1); }
    function start() { if (!timer && !reduce) timer = setInterval(next, HOLD); }
    function stop() { clearInterval(timer); timer = null; }
    function restart() { stop(); start(); }

    nodes.forEach(function (n, j) {
      n.addEventListener('click', function () { show(j, true); });
      n.addEventListener('focus', function () { show(j, true); });
    });
    root.addEventListener('pointerenter', stop);
    root.addEventListener('pointerleave', start);

    show(0);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? start() : stop(); });
      }, { threshold: 0.25 }).observe(root);
    } else start();
  })();
})();
