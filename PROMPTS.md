# Cloud.Design — Strategy & Phase-wise Build Prompts

## 1. The concept (and why this one)

**Cloud.Design = the independent, vendor-neutral hub for designing, costing and building cloud architecture on AWS, Azure and Google Cloud, plus a lead-gen marketplace that sends qualified projects to certified consultancies.**

The domain has two possible meanings: "cloud-based design tools" (the Canva/Figma space) or "designing cloud infrastructure". The second is far more valuable:

| Metric | Cloud architecture / FinOps niche | Design-tools niche |
|---|---|---|
| Ad CPC: "cloud migration" | ~$53 | — |
| Ad CPC: "cloud cost optimization" | ~$43 | — |
| Ad CPC: "cloud security solutions" | up to ~$160 | — |
| Ad CPC: typical design keywords | — | ~$1–5 |
| B2B lead value (IT services) | $385–$617 per lead | low |
| Typical consulting project | $10k–$49.9k (Clutch) | small |
| Referral fee | 5–15% of deal | — |

Sources: SEOJuice cloud-computing keyword data, Arvow/ppc.io high-CPC lists, WordStream 2026 benchmarks, Martal and Focus Digital cost-per-lead studies, Clutch cloud-consulting pricing, and Consulting Success on referral fees.

**Revenue stack, in order of expected impact:**
1. Lead sales and referral fees. Leads are graded A/B/C and sold at $149+ each, or on a 10% revenue share.
2. Featured partner subscriptions ($499/mo).
3. Google AdSense on high-CPC content.
4. Sponsorships: newsletter, tool spotlight, "architecture presented by", contest partner.
5. Affiliate links in the tools directory.
6. Paid job posts and a talent shortlist service.
7. YouTube revenue share plus the traffic it sends to the site.
8. Donations and sponsors.

## 2. Competitive research: 31 sites reviewed

- **Official hubs:** AWS Architecture Center, Azure Architecture Center, Google Cloud Architecture Center.
- **Diagram tools:** Cloudcraft, Hava, Brainboard, Cloudockit, CloudSkew, Eraser, IcePanel, Structurizr, draw.io.
- **Cost and FinOps:** Infracost, Vantage (instances), Holori, Finout, CloudZero, Flexera.
- **Learning:** ByteByteGo, Architecture Notes, martinfowler.com, c4model.com, cloudcomputingpatterns.org, Pluralsight/A Cloud Guru, InfoQ, The New Stack, TechTarget.
- **Directories:** Cloudwards, Clutch, G2, CNCF Landscape.

**Features taken from that research and built into v1:**
- A filterable architecture library with diagrams, cost ranges and trade-offs (AWS, Azure and Google centers).
- An instance price table with period toggle and CSV export (Vantage).
- A multi-cloud cost estimator (Cloudcraft, Holori).
- A pattern catalog (cloudcomputingpatterns.org, Azure).
- A Well-Architected score quiz that gates the full report behind an email (Flexera, CloudZero lead magnets).
- A tools directory with sponsored slots (G2, CNCF, Cloudwards).
- A partner directory with a "Get Matched" wizard (Clutch).
- A weekly newsletter asking for email only (Architecture Notes).
- A contest (a take on the QCon/InfoQ community model).
- Trust layer: disclosures, editorial standards, FAQ.

## 3. Phase-wise build prompts

Use each prompt in order with any AI coding agent. Each phase is independently shippable.

### Phase 1: Foundation and design system
> Build a static, dependency-free website for **cloud.design**. It must be hostable free on GitHub Pages.
> - Structure: a Python generator in `_build/` renders shared header, footer and SEO partials into root-level `.html` pages.
> - Design system: one CSS file with tokens (light/dark via `prefers-color-scheme` plus a manual toggle), Inter font, a gradient brand (#3b5bfd → #7c3aed → #06b6d4), cards, buttons, forms, tables and modals.
> - Layout: sticky glass header, a promo top bar, mobile burger menu, 5-column footer with newsletter signup.
> - Accessibility: skip links and reduced-motion support. No horizontal scroll at 360px.

### Phase 2: Content engine
> Create `assets/js/data.js` as the single source of truth for content: reference architectures (provider, category, level, cost, flow tiers, pros/cons), design patterns, tools directory, instance prices, glossary, YouTube videos and guides.
> - Render diagrams from the `flow` arrays as SVG, with a download button.
> - Build these pages: Architectures (search plus provider, category and level filters, deep-linkable modal), Patterns (category pills), Directory, Learn (guides, videos, certification roadmap), Glossary (A–Z plus search).
> - Write six long-form SEO guides with Article schema.

### Phase 3: Interactive tools (traffic magnets)
> Build the Tools page with four tools:
> 1. A multi-cloud cost estimator (VMs, vCPU, RAM, disk, object storage, egress, DB, load balancers, commitment discount) comparing AWS, Azure and GCP live.
> 2. A 12-question Well-Architected quiz with a conic score ring and per-pillar meters. The full report is gated behind a lead form.
> 3. An instance price index: sortable, filterable, hour/month/year toggle, CSV export.
> 4. A migration savings calculator showing 3-year savings.

### Phase 4: Lead generation (the money page)
> Build a 7-step lead wizard (service, cloud, spend, budget, timeline, company size, contact).
> - One question per step, clickable choice cards that auto-advance, a progress bar, and a "60 seconds" promise.
> - Trust guarantees, a consent checkbox, a honeypot field, UTM capture and a lead score/grade (A/B/C) calculated on the client.
> - Pre-select the service from `?service=`.
> - Embed the wizard on the home page as a gradient "lead band" and on a dedicated `get-matched.html` page.
> - Add a Partners page (pay-per-lead, featured, revenue share) with an application form.
> - Add an exit-intent lead magnet modal and a sticky CTA.
> - All forms post JSON to configurable endpoints (Formspree, Getform, Web3Forms or Google Apps Script), with a mailto fallback.

### Phase 5: Monetization layer
> - Load Google AdSense only after consent. Use non-personalized ads when the visitor chooses "Essential only". Add labeled ad slots (header, in-content, sidebar) configured in `config.js`, plus `ads.txt`.
> - Load GA4 after consent, with events: generate_lead, wizard_step, quiz_complete, video_play, outbound_tool, donate_click.
> - Load YouTube embeds through a lite facade (nocookie).
> - Build a Support page: donation tiers, custom amount, one-time or monthly, links to GitHub Sponsors, Stripe, PayPal, BMC, Ko-fi and Patreon, a crypto copy button, a fund meter, a use-of-funds table and an invoice pledge form.
> - Add an advertising packages section with a media-kit form.

### Phase 6: Community, contests and hiring
> - Contests page: live countdown, prize tiers, judging criteria, official rules, registration form, sponsor call-to-action.
> - Careers page: open freelance roles and an application form; a hire-talent service with a request form.

### Phase 7: SEO, legal and launch
> - Per-page title and meta description, canonical URL, Open Graph and Twitter tags. JSON-LD for WebSite with SearchAction, Organization, WebApplication, Service, Event and Article.
> - Generate `sitemap.xml`. Add `robots.txt`, `site.webmanifest`, a 404 page, and privacy (with AdSense cookie disclosure), terms and about pages.
> - Deploy to GitHub Pages. Add the custom domain through a `CNAME` file and DNS records.

### Phase 8: Growth roadmap (post-launch)
- Programmatic SEO pages: "X vs Y" comparisons (e.g. "m7i.large vs D2s v5") generated from the instance data.
- Individual architecture pages (one URL per architecture) for long-tail ranking.
- A drag-and-drop diagram editor (Eraser/CloudSkew style) with AI "describe → diagram".
- Partner profiles with reviews (Clutch style) and verified badges.
- A yearly gated "State of Cloud Architecture" report as a flagship lead magnet.
- A YouTube channel: weekly "Architecture Teardown" videos that funnel viewers to the tools.
- Automated lead routing, using Apps Script or n8n to push leads to a CRM and partner webhooks.
