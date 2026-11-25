/* ANS — preloader: logo disassembled -> converges at centre -> splash -> joins -> name reveals */
(function () {
  var pre = document.getElementById('pre');
  if (!pre) return;

  var SEEN = 'ans_intro_v1';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var repeat = false;
  try { repeat = sessionStorage.getItem(SEEN) === '1'; } catch (e) {}

  document.body.classList.add('loading');

  /* --- build stage --- */
  var stage = pre.querySelector('.pre-stage');
  var markHost = pre.querySelector('[data-mark]');
  markHost.innerHTML = window.ANSLogo('pre', { cls: 'pre-mark', pieces: true });

  var word = pre.querySelector('.pre-word');
  var w1 = word.querySelector('.pw1');
  'ANS'.split('').forEach(function (ch) {
    var s = document.createElement('span'); s.textContent = ch; w1.appendChild(s);
  });

  function finish(fast) {
    try { sessionStorage.setItem(SEEN, '1'); } catch (e) {}
    var out = function () {
      pre.classList.add('done');
      document.body.classList.remove('loading');
      document.body.classList.add('intro-done');
      setTimeout(function () { if (pre.parentNode) pre.parentNode.removeChild(pre); }, 900);
      window.dispatchEvent(new CustomEvent('ans:intro-done'));
    };
    if (fast) { out(); return; }
    if (stage.animate) {
      stage.animate(
        [{ transform: 'none', opacity: 1, filter: 'blur(0px)' },
         { transform: 'scale(1.09) translateY(-14px)', opacity: 0, filter: 'blur(7px)' }],
        { duration: 760, easing: 'cubic-bezier(.65,0,.35,1)', fill: 'forwards' }
      );
    }
    setTimeout(out, 430);
  }

  /* short-circuit paths */
  if (reduce) { setTimeout(function () { finish(true); }, 240); return; }
  if (repeat) {
    // already seen this session: quick brand flash, no full assembly
    var m = markHost.firstChild;
    m.querySelectorAll('[data-piece]').forEach(function (p) { p.style.opacity = 1; });
    w1.querySelectorAll('span').forEach(function (s) { s.style.opacity = 1; s.style.transform = 'none'; });
    word.querySelector('.pw2').style.cssText = 'opacity:1;transform:none';
    word.querySelector('.pw3').style.opacity = 1;
    var p4r = word.querySelector('.pw4'); if (p4r) p4r.style.cssText = 'opacity:1;transform:none';
    word.classList.add('lines');
    setTimeout(function () { finish(); }, 520);
    return;
  }

  /* --- full assembly ---
     The splash is the first thing a visitor sees, so it is also the first
     thing a slow phone has to pay for. The whole sequence is scaled: full
     length on a desktop, a little over half on a phone, and skipped on a
     metered or 2G connection where it would simply be a blank wait. */
  var conn = navigator.connection || {};
  if (conn.saveData || /(^|-)2g$/.test(conn.effectiveType || '')) {
    setTimeout(function () { finish(true); }, 220);
    return;
  }
  var SPEED = window.innerWidth < 760 ? 0.55 : 0.78;
  var ms = function (n) { return Math.round(n * SPEED); };

  var svg = markHost.firstChild;
  var P = {};
  svg.querySelectorAll('[data-piece]').forEach(function (el) { P[el.getAttribute('data-k')] = el; });

  // scattered start state -> assembled
  var SEQ = [
    ['hand',  'translate(-340px, 200px) rotate(-26deg) scale(.55)',   0,   760],
    ['body',  'translate(300px, 180px) rotate(22deg) scale(.6)',      110, 720],
    ['roof',  'translate(-300px,-200px) rotate(-30deg) scale(.6)',    200, 720],
    ['arc',   'translate(0,-300px) rotate(-18deg) scale(.5)',         290, 760],
    ['coin',  'translate(360px,-120px) rotate(170deg) scale(.25)',    390, 700],
    ['win',   'translate(0, 180px) scale(.15)',                       500, 560],
    ['rupee', 'scale(.25) rotate(-25deg)',                            640, 520]
  ];

  var LAND = 0;
  SEQ.forEach(function (s) {
    var el = P[s[0]]; if (!el) return;
    var end = ms(s[2]) + ms(s[3]); if (end > LAND) LAND = end;
    el.animate(
      [{ transform: s[1], opacity: 0, filter: 'blur(5px)' },
       { transform: 'none', opacity: 1, filter: 'blur(0px)' }],
      { duration: ms(s[3]), delay: ms(s[2]), easing: 'cubic-bezier(.17,.85,.3,1)', fill: 'both' }
    );
  });

  /* splash at the moment the mark completes */
  var splashAt = LAND - ms(170);

  setTimeout(function () {
    var flash = pre.querySelector('.pre-flash');
    if (flash && flash.animate) {
      flash.animate([{ opacity: 0 }, { opacity: .85, offset: .12 }, { opacity: 0 }],
        { duration: 620, easing: 'ease-out' });
    }
    // concentric gold rings
    for (var i = 0; i < 3; i++) {
      (function (n) {
        var ring = document.createElement('i');
        ring.className = 'pre-splash';
        stage.appendChild(ring);
        if (ring.animate) {
          ring.animate(
            [{ transform: 'translate(-50%,-50%) scale(.2)', opacity: .95, borderWidth: '3px' },
             { transform: 'translate(-50%,-50%) scale(' + (16 + n * 11) + ')', opacity: 0, borderWidth: '1px' }],
            { duration: 1050 + n * 230, delay: n * 110, easing: 'cubic-bezier(.16,1,.3,1)', fill: 'forwards' }
          );
        }
        setTimeout(function () { ring.remove(); }, 1500 + n * 240);
      })(i);
    }
    // impact bounce on the assembled mark
    if (svg.animate) {
      svg.animate(
        [{ transform: 'scale(.9)' }, { transform: 'scale(1.07)', offset: .4 }, { transform: 'scale(1)' }],
        { duration: 760, easing: 'cubic-bezier(.17,.9,.32,1)' }
      );
    }
  }, splashAt);

  /* wordmark */
  var wordAt = LAND + ms(150);
  setTimeout(function () {
    w1.querySelectorAll('span').forEach(function (s, i) {
      if (!s.animate) { s.style.opacity = 1; s.style.transform = 'none'; return; }
      s.animate(
        [{ transform: 'translateY(100%) rotate(7deg)', opacity: 0 },
         { transform: 'none', opacity: 1 }],
        { duration: 620, delay: i * 85, easing: 'cubic-bezier(.17,.85,.3,1)', fill: 'both' }
      );
    });
    var p2 = word.querySelector('.pw2'), p3 = word.querySelector('.pw3'), p4 = word.querySelector('.pw4');
    if (p2.animate) {
      p2.animate([{ opacity: 0, transform: 'translateY(12px)', letterSpacing: '.75em' },
                  { opacity: 1, transform: 'none', letterSpacing: '.42em' }],
        { duration: 820, delay: 300, easing: 'cubic-bezier(.17,.85,.3,1)', fill: 'both' });
      p3.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 620, delay: 620, easing: 'ease-out', fill: 'both' });
      if (p4) p4.animate([{ opacity: 0, transform: 'translateY(10px)' }, { opacity: 1, transform: 'none' }],
        { duration: 760, delay: 880, easing: 'cubic-bezier(.17,.85,.3,1)', fill: 'both' });
    } else { p2.style.opacity = 1; p3.style.opacity = 1; if (p4) p4.style.opacity = 1; }
    setTimeout(function () { word.classList.add('lines'); }, ms(560));
  }, wordAt);

  var total = wordAt + ms(1500);
  var timer = setTimeout(function () { finish(); }, total);

  /* skip */
  function skip() { clearTimeout(timer); finish(); }
  window.ANSReplayIntro = function () {
    try { sessionStorage.removeItem(SEEN); } catch (e) {}
    location.reload();
  };
  pre.addEventListener('click', skip);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' || e.key === 'Enter') skip(); }, { once: true });

  /* safety net — never trap the visitor */
  setTimeout(function () { if (!pre.classList.contains('done')) finish(true); }, 7000);
})();
