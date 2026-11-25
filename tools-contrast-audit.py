import asyncio, glob, os
from playwright.async_api import async_playwright
PAGES = sorted(os.path.basename(f) for f in glob.glob("/home/claude/ans/*.html"))

AUDIT = r"""()=>{
  function lum(c){
    const m=c.match(/[\d.]+/g); if(!m) return null;
    const [r,g,b]=m.slice(0,3).map(Number);
    const a=m.length>3?Number(m[3]):1;
    if(a<0.12) return null;
    const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)};
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b);
  }
  function bgOf(el){
    let n=el;
    while(n && n!==document.documentElement){
      const cs=getComputedStyle(n);
      // an element painted with a gradient is its own backdrop; we cannot
      // resolve its average colour here, so exclude it rather than compare
      // the text against something it is not sitting on
      if(cs.backgroundImage && cs.backgroundImage.indexOf('gradient')>-1) return 'SKIP';
      const c=cs.backgroundColor;
      const m=c.match(/[\d.]+/g);
      if(m && (m.length<4 || Number(m[3])>0.55)) return c;
      n=n.parentElement;
    }
    return getComputedStyle(document.body).backgroundColor;
  }
  const out=[];
  document.querySelectorAll('p,li,a,span,h1,h2,h3,h4,b,td,th,label,small,button').forEach(el=>{
    if(!el.textContent.trim()) return;
    const r=el.getBoundingClientRect();
    if(r.width<4||r.height<4) return;
    const cs=getComputedStyle(el);
    if(cs.visibility==='hidden'||cs.display==='none'||+cs.opacity<0.15) return;
    if(el.children.length && el.textContent.trim()!==(el.firstChild&&el.firstChild.nodeValue||'').trim()) {
      // only leaf-ish text
      let hasText=false;
      el.childNodes.forEach(n=>{ if(n.nodeType===3 && n.nodeValue.trim()) hasText=true; });
      if(!hasText) return;
    }
    if(cs.webkitTextFillColor==='rgba(0, 0, 0, 0)') return;   // gradient text
    const bgc=bgOf(el); if(bgc==='SKIP') return;
    const L1=lum(cs.color); const L2=lum(bgc);
    if(L1===null||L2===null) return;
    const ratio=(Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
    const size=parseFloat(cs.fontSize), bold=+cs.fontWeight>=600;
    const large = size>=24 || (size>=18.66 && bold);
    const need = large?3.0:4.5;
    if(ratio < need) out.push({t:el.textContent.trim().slice(0,46), r:+ratio.toFixed(2), need, c:cs.color, bg:bgc, size});
  });
  return out;
}"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--no-sandbox","--use-gl=swiftshader","--enable-unsafe-swiftshader"])
        pg = await (await b.new_context(viewport={"width":1440,"height":950}, locale="en-IN")).new_page()
        total=0
        for i,f in enumerate(PAGES):
            await pg.goto(f"http://127.0.0.1:8787/{f}", wait_until="networkidle")
            await pg.wait_for_timeout(6200 if i==0 else 1100)
            await pg.evaluate("document.querySelectorAll('[data-rv],.mask-ready').forEach(n=>n.classList.add('in'))")
            await pg.wait_for_timeout(250)
            r = await pg.evaluate(AUDIT)
            # the menu overlay is hidden until opened, so audit it too
            try:
                await pg.click(".burger", timeout=2000)
                await pg.wait_for_timeout(700)
                r += await pg.evaluate(AUDIT)
                await pg.keyboard.press("Escape")
                await pg.wait_for_timeout(300)
            except Exception: pass
            uniq={}
            for x in r: uniq[(x['t'],x['r'])]=x
            if uniq:
                total+=len(uniq)
                print(f"\n{f}  ({len(uniq)} issues)")
                for x in list(uniq.values())[:6]:
                    print(f"   {x['r']:>5} (need {x['need']}) {x['size']:.0f}px  '{x['t']}'  {x['c']} on {x['bg']}")
        print("\n=== total low-contrast text nodes:", total, "===")
        await b.close()
asyncio.run(main())
