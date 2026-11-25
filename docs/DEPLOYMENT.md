# Deployment

## The short version

It is a static site. Upload the folder. There is no build step, no Node, no database.

## Hostinger / cPanel
1. File Manager → `public_html`
2. Upload everything **except** the `build_*.py`, `gen_*.py`, `data_products.py` and `docs/` files
   (harmless if uploaded, but they serve no purpose in production)
3. Confirm `index.html` is at the root
4. Enable the free SSL certificate and force HTTPS

## Netlify
Drag the folder onto the Netlify dashboard. Add your domain under Domain settings. Done.

## Vercel
```bash
cd ans
vercel deploy --prod
```

## After deploying — verify these

- [ ] `https://yourdomain.com/sitemap.xml` loads and lists 25 URLs
- [ ] `https://yourdomain.com/robots.txt` loads and points at the sitemap
- [ ] HTTPS is forced, and `www` redirects to the apex domain (or the reverse — just pick one)
- [ ] The intro animation plays once, then not again on subsequent pages
- [ ] Call and WhatsApp buttons open correctly on a real phone
- [ ] Submit a test enquiry end to end
- [ ] Run the homepage through PageSpeed Insights

## Performance

Already handled: lazy-loaded map, non-blocking fonts, SVG artwork instead of photographs,
`prefers-reduced-motion` support, no JS framework, no jQuery.

The largest asset is `assets/img/og-cover.jpg` (~82 KB) and it is only fetched by social
crawlers, not by visitors.

If you later add photographs, export them as WebP at the size they are displayed, and add
`loading="lazy"` to every `<img>` below the fold.
