# Cloud.Design

**Cloud architecture diagrams, cost calculators, design patterns, and matching with vetted experts.** Covers AWS, Azure, and Google Cloud.

This is a static, dependency-free site that is free to host on **GitHub Pages**.
Strategy, research, and the phase-wise build prompts are in [`PROMPTS.md`](PROMPTS.md).

## What's inside

| Page | Purpose | Revenue |
|---|---|---|
| `index.html` | Hero, tools, library preview, lead wizard, videos, FAQ | Ads, leads |
| `architectures.html` | Filterable library of 18 reference architectures, with SVG diagram modals | Ads, leads |
| `tools.html` | Cost estimator, Well-Architected quiz, instance price index, migration ROI | Leads (gated report), ads |
| `get-matched.html` | 7-step lead wizard with lead scoring | **Lead sales** |
| `partners.html` | Pay-per-lead, featured-partner, and revenue-share plans | **B2B subscriptions** |
| `directory.html` | Tools directory with sponsored slots, plus partner directory | Affiliate, sponsorship |
| `patterns.html`, `learn.html`, `glossary.html`, `guides/*` | SEO content and videos | Ads, YouTube |
| `support.html` | Donations, sponsor pledges, advertising packages | Donations, ads sales |
| `contests.html` | Challenge with countdown, prizes, and rules | Sponsors, email list |
| `careers.html` | Hiring and talent network | Job posts |

## Go-live checklist (edit `assets/js/config.js` only)

1. **Forms:** create a free endpoint on [Formspree](https://formspree.io), Getform, Web3Forms, or a Google Apps Script web app. Paste the URL into `forms.default`, or set one per form type. Until you do, forms fall back to opening the visitor's email client.
2. **AdSense:** set `adsenseClient` (`ca-pub-…`) and the `adSlots` IDs. Then put your publisher ID into `ads.txt`.
3. **Analytics:** set `ga4Id`.
4. **Donations:** paste your Stripe Payment Link, PayPal.me, Buy Me a Coffee, Ko-fi, and Patreon links.
5. **Social / YouTube:** set your channel URLs.
6. **Custom domain:** add a file named `CNAME` containing `cloud.design`, then set these DNS records:
   - `A` records for `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` for `www` → `webworksa1.github.io`

   Finally, enable **Enforce HTTPS** under Settings → Pages.

## Editing content

- Architectures, patterns, tools, prices, glossary, videos, and guide cards live in `assets/js/data.js`.
- Page layouts live in `_build/build.py` and `_build/layout.py`. Guide articles live in `_build/guides.py`.
- After editing a page layout or guide, rebuild with `python3 _build/build.py`.

## Deploy

GitHub Pages publishes from the `gh-pages` branch (root), or from `main` (root) if you prefer. You can change this under **Settings → Pages → Build and deployment**.

---
Independent project. Not affiliated with Amazon Web Services, Microsoft, or Google.
