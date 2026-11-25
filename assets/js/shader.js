/* ANS — hero: a macro, rim-lit coin edge in darkness.
   Rendered rather than photographed, so it costs nothing to licence and
   scales to any viewport. Falls back to a CSS gradient without WebGL. */
(function () {
  var cv = document.getElementById('shader');
  if (!cv) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function fallback() {
    cv.style.background =
      'radial-gradient(70% 90% at 72% 44%, #6A4A1C 0%, #2A1C0C 42%, #0A0806 76%),' +
      'radial-gradient(40% 50% at 18% 18%, rgba(212,160,58,.18), transparent 60%),' +
      'linear-gradient(160deg,#0A0806,#15100A)';
  }

  var gl = cv.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'high-performance' })
        || cv.getContext('experimental-webgl');
  if (!gl) { fallback(); return; }

  var VS = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';

  var FS = [
'precision highp float;',
'uniform vec2 u_res; uniform float u_t; uniform vec2 u_m;',

'float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453123);}',
'float noise(vec2 p){vec2 i=floor(p),f=fract(p);vec2 u=f*f*(3.-2.*f);',
'  return mix(mix(hash(i),hash(i+vec2(1,0)),u.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),u.x),u.y);}',
'float fbm(vec2 p){float v=0.,a=.5;mat2 r=mat2(.8,.6,-.6,.8);',
'  for(int i=0;i<4;i++){v+=a*noise(p);p=r*p*2.02;a*=.5;}return v;}',

/* height field of a coin: flat face, milled (reeded) rim, bevel between */
'float coinH(vec2 p, float rad, out float mask){',
'  float r=length(p); float a=atan(p.y,p.x);',
'  float edge0=rad*0.80, edge1=rad;',
'  mask=1.0-smoothstep(edge1-0.004,edge1+0.004,r);',
'  float face=1.0-smoothstep(edge0-0.03,edge0+0.02,r);',
'  float reeds=sin(a*210.0)*0.5+0.5;',             /* milled edge grooves */
'  float band=smoothstep(edge0-0.01,edge0+0.03,r)*mask;',
'  float bevel=1.0-smoothstep(edge0,edge1,r);',
'  float h=face*0.9 + bevel*0.35 + band*reeds*0.34;',
   /* relief on the face: concentric micro-rings, like a struck surface */
'  h+=face*sin(r*96.0)*0.03;',
'  h+=face*fbm(p*18.0)*0.05;',
'  return h*mask;',
'}',

'void main(){',
'  vec2 uv=(gl_FragCoord.xy-0.5*u_res)/u_res.y;',
'  float t=u_t*0.06;',
'  vec2 mo=u_m*0.045;',

   /* the coin sits off to the right, tilted, filling the frame */
'  vec2 cp=uv-vec2(0.46+mo.x,-0.04+mo.y);',
'  cp*=mat2(0.97,-0.24,0.24,0.97);',
'  cp.y/=0.93;',
'  float rad=0.92;',

'  float m; float h=coinH(cp,rad,m);',
'  vec2 e=vec2(0.0016,0.0);',
'  float m2;',
'  float hx=coinH(cp+e.xy,rad,m2)-coinH(cp-e.xy,rad,m2);',
'  float hy=coinH(cp+e.yx,rad,m2)-coinH(cp-e.yx,rad,m2);',
'  vec3 n=normalize(vec3(-hx*7.0,-hy*7.0,1.0));',

   /* one warm key from upper right, one cool fill from lower left */
'  vec3 key=normalize(vec3(0.56,0.70,0.58));',
'  vec3 fil=normalize(vec3(-0.70,-0.42,0.42));',
'  float dk=max(dot(n,key),0.0);',
'  float df=max(dot(n,fil),0.0);',

'  vec3 metal=vec3(0.62,0.44,0.19);',
'  vec3 warm =vec3(1.00,0.74,0.36);',
'  vec3 cool =vec3(0.22,0.30,0.44);',

'  vec3 col=metal*(0.10+dk*0.95)+warm*pow(dk,7.0)*0.85+cool*df*0.17;',

   /* rim light along the silhouette, the thing that makes it read as metal */
'  float r=length(cp);',
'  float rim=smoothstep(rad*0.985,rad,r)*m;',
'  col+=warm*rim*1.5;',
'  float outer=smoothstep(rad+0.055,rad,r)*(1.0-m);',
'  col+=warm*outer*0.16;',

'  col*=m;',

   /* background: deep warm dark with a slow drift, plus the coin glow */
'  float bgn=fbm(uv*1.25+vec2(t,t*0.6));',
'  vec3 bg=mix(vec3(0.030,0.022,0.016),vec3(0.085,0.055,0.030),bgn*0.9);',
'  bg+=warm*0.055*(1.0-smoothstep(0.0,1.5,distance(uv,vec2(0.5,0.0))));',
'  bg+=cool*0.05*(1.0-smoothstep(0.0,1.3,distance(uv,vec2(-0.9,-0.5))));',
'  col=mix(bg,col,m);',

   /* depth of field: soften the far lower-left of the frame */
'  float foc=smoothstep(1.5,0.1,distance(uv,vec2(0.35,0.05)));',
'  col=mix(col*0.76,col,0.35+foc*0.65);',

   /* readable area behind the headline */
'  col*=1.0-0.40*smoothstep(0.9,-0.65,uv.x)*smoothstep(0.95,-0.1,abs(uv.y));',

   /* vignette, grain, filmic curve */
'  col*=1.0-0.52*dot(uv*0.72,uv*0.72);',
'  float g=hash(gl_FragCoord.xy+fract(u_t)*vec2(13.1,7.7));',
'  col+=(g-0.5)*0.035;',
'  col=col/(col+vec3(0.82));',
'  col=pow(max(col,0.0),vec3(0.86));',
'  gl_FragColor=vec4(col,1.0);',
'}'].join('\n');

  function sh(t, src) {
    var s = gl.createShader(t); gl.shaderSource(s, src); gl.compileShader(s);
    return gl.getShaderParameter(s, gl.COMPILE_STATUS) ? s : null;
  }
  var vs = sh(gl.VERTEX_SHADER, VS), fs = sh(gl.FRAGMENT_SHADER, FS);
  if (!vs || !fs) { fallback(); return; }
  var pr = gl.createProgram();
  gl.attachShader(pr, vs); gl.attachShader(pr, fs); gl.linkProgram(pr);
  if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) { fallback(); return; }
  gl.useProgram(pr);

  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(pr, 'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

  var uRes = gl.getUniformLocation(pr, 'u_res'),
      uT = gl.getUniformLocation(pr, 'u_t'),
      uM = gl.getUniformLocation(pr, 'u_m');
  /* Render scale, chosen for the device rather than fixed: a fragment shader
     is fill-rate bound, so halving the pixel count roughly halves its cost.
     Weak or small devices get a softer, cheaper image rather than a slideshow. */
  var cores  = navigator.hardwareConcurrency || 4;
  var memory = navigator.deviceMemory || 4;
  var small  = Math.min(screen.width, screen.height) < 820;
  var weak   = cores <= 4 || memory <= 4;
  var scale  = weak ? (small ? 0.4 : 0.5) : (small ? 0.5 : 0.68);
  var dpr = Math.min(window.devicePixelRatio || 1, 1.75) * scale;

  /* the hero shader is decorative: 30fps is indistinguishable here and
     leaves the main thread free for scrolling */
  var FPS = weak ? 24 : 30, STEP = 1000 / FPS, acc = 0;
  var onScreen = true;

  function size() {
    var w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.max(1, Math.round(w * dpr));
    cv.height = Math.max(1, Math.round(h * dpr));
    gl.viewport(0, 0, cv.width, cv.height);
    gl.uniform2f(uRes, cv.width, cv.height);
  }
  size();
  if (window.ResizeObserver) new ResizeObserver(size).observe(cv);
  else window.addEventListener('resize', size);

  var mx = 0, my = 0, tx = 0, ty = 0;
  window.addEventListener('pointermove', function (e) {
    tx = (e.clientX / window.innerWidth - .5) * 2;
    ty = (.5 - e.clientY / window.innerHeight) * 2;
  }, { passive: true });

  var vis = true, raf, time = 0, last = performance.now();
  document.addEventListener('visibilitychange', function () {
    vis = !document.hidden;
    if (vis && !reduce) { last = performance.now(); raf = requestAnimationFrame(loop); }
    else cancelAnimationFrame(raf);
  });
  function loop(now) {
    var dt = Math.min((now - last) / 1000, .05); last = now;
    if (vis && !reduce && onScreen) raf = requestAnimationFrame(loop);
    acc += dt * 1000;
    if (acc < STEP) return;            /* hold at the target frame rate */
    acc = 0;
    time += dt;
    mx += (tx - mx) * .035; my += (ty - my) * .035;
    gl.uniform1f(uT, time); gl.uniform2f(uM, mx, my);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }

  /* stop entirely once the hero has scrolled away */
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        onScreen = e.isIntersecting;
        cancelAnimationFrame(raf);
        if (onScreen && vis && !reduce) { last = performance.now(); raf = requestAnimationFrame(loop); }
      });
    }, { threshold: 0 }).observe(cv);
  }
  if (reduce) { gl.uniform1f(uT, 4.0); gl.uniform2f(uM, 0, 0); gl.drawArrays(gl.TRIANGLES, 0, 3); }
  else raf = requestAnimationFrame(loop);
})();
