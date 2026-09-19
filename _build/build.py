#!/usr/bin/env python3
"""Cloud.Design static site generator.
Run:  python3 _build/build.py   → writes all .html pages to the repo root.
Add a page: write a function returning (filename, title, description, body) and append it to PAGES.
"""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, page_hero, ad, ad_raw, wizard, lead_band, SITE
from guides import GUIDES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HERO_SVG = """<svg viewBox="0 0 520 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Example cloud architecture diagram">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#3b5bfd"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs>
<rect x="10" y="10" width="500" height="340" rx="18" fill="none" stroke="url(#g)" stroke-dasharray="6 6" opacity=".6"/>
<text x="28" y="38" font-size="12" font-weight="700" fill="currentColor" opacity=".6">REGION · us-east-1</text>
<g font-size="12" font-weight="600" fill="currentColor" text-anchor="middle">
<rect x="30" y="150" width="90" height="56" rx="12" fill="#06b6d4" fill-opacity=".14" stroke="#06b6d4"/><text x="75" y="182">Users</text>
<rect x="160" y="150" width="100" height="56" rx="12" fill="#3b5bfd" fill-opacity=".14" stroke="#3b5bfd"/><text x="210" y="176">CDN + WAF</text><text x="210" y="192" font-size="10" opacity=".7">edge</text>
<rect x="300" y="70" width="100" height="56" rx="12" fill="#7c3aed" fill-opacity=".14" stroke="#7c3aed"/><text x="350" y="102">Web tier</text>
<rect x="300" y="150" width="100" height="56" rx="12" fill="#7c3aed" fill-opacity=".14" stroke="#7c3aed"/><text x="350" y="182">API tier</text>
<rect x="300" y="230" width="100" height="56" rx="12" fill="#7c3aed" fill-opacity=".14" stroke="#7c3aed"/><text x="350" y="262">Workers</text>
<rect x="430" y="110" width="70" height="56" rx="12" fill="#10b981" fill-opacity=".14" stroke="#10b981"/><text x="465" y="142">DB</text>
<rect x="430" y="200" width="70" height="56" rx="12" fill="#f59e0b" fill-opacity=".14" stroke="#f59e0b"/><text x="465" y="232">Queue</text>
</g>
<g stroke="currentColor" stroke-opacity=".35" stroke-width="1.6" fill="none">
<path d="M120 178H160"/><path d="M260 178C280 178 280 98 300 98"/><path d="M260 178H300"/><path d="M260 178C280 178 280 258 300 258"/>
<path d="M400 98C415 98 415 138 430 138"/><path d="M400 178C415 178 415 138 430 138"/><path d="M400 178C415 178 415 228 430 228"/><path d="M400 258C415 258 415 228 430 228"/>
</g>
<g><rect x="300" y="306" width="200" height="30" rx="8" fill="#10b981" fill-opacity=".14"/><text x="400" y="326" font-size="12" font-weight="700" fill="#10b981" text-anchor="middle">Est. $1,284/mo · 99.95% SLA</text></g>
</svg>"""


def p_index():
    b = ""
    body = f"""
<section class="hero"><div class="container split">
<div><span class="badge">● New: 2026 Multi-Cloud Price Index</span>
<h1 class="mt1">Design the cloud <span class="grad">right the first time.</span></h1>
<p class="lead">Free reference architectures, cost calculators and design patterns for AWS, Azure and Google Cloud — plus on-demand access to vetted cloud architects when you need hands on keyboards.</p>
<form class="search-hero mt2" data-search role="search"><input type="search" placeholder="Search architectures: serverless, RAG, landing zone…" aria-label="Search architectures"><button class="btn btn-primary btn-sm" type="submit">Search</button></form>
<div class="hero-cta"><a class="btn btn-primary" href="get-matched.html">Get a free architecture review →</a><a class="btn btn-ghost" href="tools.html#estimator">Estimate my cloud bill</a></div>
<div class="trust"><span><b data-count="18">18</b> reference architectures</span><span><b data-count="20">20</b> design patterns</span><span><b data-count="30">30</b> vetted tools</span><span><b>100%</b> free</span></div>
</div>
<div class="hero-visual reveal">{HERO_SVG}</div>
</div></section>

{ad('header')}

<section class="section"><div class="container">
<div class="section-head"><span class="eyebrow">Everything in one place</span><h2>From whiteboard to production</h2><p>Official provider docs are scattered across three clouds. Cloud.Design puts the diagrams, decisions and dollar figures side by side.</p></div>
<div class="grid g3">
<a class="card reveal" href="architectures.html"><div class="ico">📐</div><h3>Reference Architectures</h3><p class="small mb0">Battle-tested blueprints with diagrams, trade-offs and real monthly cost ranges. Download as SVG.</p></a>
<a class="card reveal" href="tools.html#estimator"><div class="ico">💲</div><h3>Multi-Cloud Cost Estimator</h3><p class="small mb0">Price the same workload on AWS, Azure and GCP in seconds — including egress and commitments.</p></a>
<a class="card reveal" href="tools.html#quiz"><div class="ico">🛡️</div><h3>Well-Architected Score</h3><p class="small mb0">12 questions, 6 pillars. Get a scored report with prioritized fixes.</p></a>
<a class="card reveal" href="patterns.html"><div class="ico">🧩</div><h3>Design Pattern Catalog</h3><p class="small mb0">Circuit breaker, saga, CQRS, strangler fig and more — problem, solution, when to use.</p></a>
<a class="card reveal" href="tools.html#instances"><div class="ico">📊</div><h3>Instance Price Compare</h3><p class="small mb0">Sortable VM pricing across clouds, per hour, month or year. Export to CSV.</p></a>
<a class="card reveal" href="get-matched.html"><div class="ico">🤝</div><h3>Expert Matching</h3><p class="small mb0">Describe your project in 60 seconds; meet up to 3 certified partners who fit your budget.</p></a>
</div></div></section>

<section class="section alt"><div class="container">
<div class="flex between"><div><span class="eyebrow tag">Library</span><h2 class="mt1">Popular reference architectures</h2></div><a class="btn btn-ghost" href="architectures.html">View all →</a></div>
<div class="grid g3 mt2" id="arch-grid" data-limit="6"></div>
</div></section>

{lead_band(b)}

<section class="section"><div class="container">
<div class="section-head"><span class="eyebrow">Watch &amp; learn</span><h2>Cloud architecture, explained on video</h2><p>Hand-picked explainers on the Well-Architected Framework, migrations and modern design.</p></div>
<div class="grid g3" id="video-grid" data-limit="3"></div>
<div class="center mt2"><a class="btn btn-ghost" href="learn.html#videos">More videos →</a> <a class="btn btn-ghost" data-social="youtube" href="#" target="_blank" rel="noopener">▶ Subscribe on YouTube</a></div>
</div></section>

{ad('inContent')}

<section class="section alt"><div class="container">
<div class="flex between"><h2>Latest guides</h2><a class="btn btn-ghost" href="learn.html">All guides →</a></div>
<div class="grid g3 mt2" id="guide-grid" data-limit="3"></div>
</div></section>

<section class="section"><div class="container grid g3">
<div class="card"><div class="ico">🏆</div><h3>Win up to $2,500</h3><p class="small">Design the most resilient, cost-efficient architecture for our quarterly challenge. Judged by working architects.</p><div class="countdown mt1" data-countdown></div><a class="btn btn-primary btn-sm mt2" href="contests.html">Enter the challenge →</a></div>
<div class="card"><div class="ico">❤️</div><h3>Keep Cloud.Design free</h3><p class="small">No paywalls. Supporters fund new architectures, tools and open-source diagrams.</p><a class="btn btn-ghost btn-sm mt1" href="support.html">Support the project →</a></div>
<div class="card"><div class="ico">💼</div><h3>Hiring cloud talent?</h3><p class="small">Post roles to an audience of practicing architects, SREs and DevOps engineers — or join our contributor network.</p><a class="btn btn-ghost btn-sm mt1" href="careers.html">Hire or get hired →</a></div>
</div></section>

<section class="section alt"><div class="container" style="max-width:860px">
<div class="section-head"><h2>Frequently asked questions</h2></div>
<details><summary>Is Cloud.Design really free?</summary><div>Yes. Every architecture, calculator and guide is free. We are funded by clearly labeled ads, sponsorships, partner referral fees and community donations.</div></details>
<details><summary>Are you affiliated with AWS, Microsoft or Google?</summary><div>No. Cloud.Design is independent, which is why we can compare all three clouds honestly. Trademarks belong to their owners.</div></details>
<details><summary>How does expert matching work?</summary><div>You fill a 60-second brief. A human reviews it and introduces up to three certified partners who fit your cloud, budget and timeline. It is free for you; partners pay us for qualified introductions.</div></details>
<details><summary>How accurate are the cost estimates?</summary><div>They use public on-demand list prices for US regions and are meant for early-stage comparison. Always validate with the provider's official calculator before committing budget.</div></details>
<details><summary>Can I contribute an architecture?</summary><div>Yes — submit via the <a href="contact.html">contact form</a> or open a pull request on our GitHub. Accepted contributors get author credit and a backlink.</div></details>
</div></section>
"""
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "name": "Cloud.Design", "url": SITE + "/", "potentialAction": {"@type": "SearchAction", "target": SITE + "/architectures.html?q={search_term_string}", "query-input": "required name=search_term_string"}},
        {"@type": "Organization", "name": "Cloud.Design", "url": SITE + "/", "logo": SITE + "/assets/img/favicon.svg"}]}
    return ("index.html", "Cloud.Design — Cloud Architecture Diagrams, Cost Calculators & Expert Help",
            "Free AWS, Azure & Google Cloud reference architectures, multi-cloud cost estimator, design patterns and vetted cloud architects. Design the cloud right the first time.", body, schema)


def p_architectures():
    body = page_hero("Cloud Reference Architectures", "Production-grade blueprints for AWS, Azure, Google Cloud and multi-cloud — each with an interactive diagram, trade-offs and realistic monthly cost.", "Architectures") + f"""
<section class="section"><div class="container">
<div class="filters"><input type="search" id="arch-q" placeholder="Search e.g. kubernetes, RAG, DR…" aria-label="Search architectures">
<select id="arch-provider" aria-label="Provider"><option value="">All clouds</option><option value="aws">AWS</option><option value="azure">Azure</option><option value="gcp">Google Cloud</option><option value="multi">Multi-cloud</option></select>
<select id="arch-cat" aria-label="Category"><option value="">All categories</option></select>
<select id="arch-level" aria-label="Level"><option value="">All levels</option><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select>
<span class="muted small" id="arch-count" aria-live="polite"></span></div>
<div class="grid g3" id="arch-grid"></div>
{ad_raw('inContent')}
<div class="card mt2 flex between"><div><h3 class="mb0">Need a custom architecture?</h3><p class="small mb0">A certified architect will design, cost and document it for your exact workload.</p></div><a class="btn btn-primary" href="get-matched.html?service=architecture">Get a free proposal →</a></div>
</div></section>"""
    return ("architectures.html", "Cloud Reference Architectures for AWS, Azure & GCP | Cloud.Design",
            "Browse interactive cloud reference architectures: serverless, Kubernetes, data lakehouse, GenAI RAG, landing zones and DR — with diagrams and cost ranges.", body, None)


def p_patterns():
    body = page_hero("Cloud Design Patterns", "The proven solutions to recurring problems in distributed cloud systems — resilience, data, integration, security, cost and migration.", "Patterns") + f"""
<section class="section"><div class="container with-side"><div>
<div class="filters" id="pattern-cats"></div>
<div class="grid g2" id="pattern-grid"></div></div>
<aside><div class="sticky"><div class="card"><h3>Stuck choosing a pattern?</h3><p class="small">Book a free 30-minute design session with a certified architect.</p><a class="btn btn-primary btn-block" href="get-matched.html?service=architecture">Book free session</a></div>{ad_raw('sidebar')}</div></aside>
</div></section>"""
    return ("patterns.html", "Cloud Design Patterns Catalog (Resilience, Data, Integration) | Cloud.Design",
            "Circuit breaker, saga, CQRS, event sourcing, strangler fig, bulkhead and more cloud design patterns — problem, solution and when to use each.", body, None)


def p_tools():
    body = page_hero("Free Cloud Architecture Tools", "Estimate costs across clouds, compare VM prices, score your architecture against the Well-Architected Framework and model migration savings.", "Free Tools") + f"""
<section class="section" id="estimator"><div class="container">
<div class="section-head"><span class="eyebrow">Calculator</span><h2>Multi-Cloud Cost Estimator</h2><p>Price the same workload on AWS, Azure and Google Cloud side by side.</p></div>
<div class="split" style="align-items:start"><form class="card form" id="estimator" onsubmit="return false">
<div class="row2"><div class="field"><label>Virtual machines</label><input type="number" name="vms" value="4" min="0"></div><div class="field"><label>vCPU per VM</label><input type="number" name="cpu" value="2" min="1"></div></div>
<div class="row2"><div class="field"><label>RAM per VM (GiB)</label><input type="number" name="ram" value="8" min="1"></div><div class="field"><label>Disk per VM (GB SSD)</label><input type="number" name="disk" value="100" min="0"></div></div>
<div class="row2"><div class="field"><label>Object storage (GB)</label><input type="number" name="obj" value="500" min="0"></div><div class="field"><label>Egress / month (GB)</label><input type="number" name="egress" value="1000" min="0"></div></div>
<div class="row2"><div class="field"><label>Managed DB instances</label><input type="number" name="db" value="1" min="0"></div><div class="field"><label>Load balancers</label><input type="number" name="lbs" value="1" min="0"></div></div>
<div class="field"><label>Commitment discount</label><select name="commit"><option value="0">On-demand (0%)</option><option value="28">1-yr commitment (~28%)</option><option value="45">3-yr commitment (~45%)</option><option value="70">Spot / preemptible (~70%)</option></select></div>
<p class="small muted mb0">Indicative US-region list prices. First 100 GB egress free.</p></form>
<div><div class="grid" id="est-out"></div><div class="card mt2"><h3>Want the exact number?</h3><p class="small">A FinOps specialist will build a line-item estimate and a savings plan for your real workload — free.</p><a class="btn btn-primary" href="get-matched.html?service=cost">Get a free cost review →</a></div></div></div>
</div></section>

{ad('inContent')}

<section class="section alt" id="quiz"><div class="container" style="max-width:860px">
<div class="section-head"><span class="eyebrow">Assessment</span><h2>Well-Architected Score</h2><p>12 questions across the 6 pillars. Takes 2 minutes.</p></div>
<div class="wizard" id="wa-quiz"><div class="progress"><span id="quiz-bar"></span></div><div id="quiz-box" class="mt1"></div></div>
</div></section>

<section class="section" id="instances"><div class="container">
<div class="section-head"><span class="eyebrow">Price index</span><h2>Cloud Instance Price Comparison</h2><p>On-demand Linux prices, US East. Click a column to sort. Updated {datetime.date.today():%B %Y} — verify before purchase.</p></div>
<div class="filters"><select id="inst-provider" aria-label="Provider"><option value="">All providers</option><option>AWS</option><option>Azure</option><option>GCP</option></select>
<select id="inst-class" aria-label="Class"><option value="">All classes</option></select>
<select id="inst-mode" aria-label="Period"><option value="hour">Per hour</option><option value="month">Per month</option><option value="year">Per year</option></select>
<input type="search" id="inst-q" placeholder="Filter instance…" aria-label="Filter instance"><button class="btn btn-ghost btn-sm" id="inst-export">⬇ CSV</button></div>
<div class="table-wrap"><table id="instance-table"><thead><tr><th data-k="0">Provider</th><th data-k="1">Instance</th><th data-k="2">vCPU</th><th data-k="3">Memory</th><th data-k="4">Price <span id="inst-unit"></span></th><th>$/vCPU·mo</th><th data-k="5">Class</th></tr></thead><tbody></tbody></table></div>
</div></section>

<section class="section alt" id="migration"><div class="container">
<div class="section-head"><span class="eyebrow">ROI</span><h2>Cloud Migration Savings Calculator</h2><p>Model your on-prem total cost of ownership against a right-sized cloud footprint.</p></div>
<form class="card form" id="migration-calc" onsubmit="return false"><div class="grid g3">
<div class="field"><label>Servers</label><input type="number" name="servers" value="40"></div>
<div class="field"><label>Hardware cost / server ($)</label><input type="number" name="hw" value="9000"></div>
<div class="field"><label>Data center / colo per month ($)</label><input type="number" name="dc" value="6500"></div>
<div class="field"><label>Ops staff cost per month ($)</label><input type="number" name="staff" value="18000"></div>
<div class="field"><label>Licenses &amp; support per month ($)</label><input type="number" name="lic" value="4000"></div></div></form>
<div id="mig-out" class="mt2"></div>
<div class="center mt2"><a class="btn btn-primary" href="get-matched.html?service=migration">Get a free migration assessment →</a></div>
</div></section>"""
    schema = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Multi-Cloud Cost Estimator", "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": SITE + "/tools.html"}
    return ("tools.html", "Free Cloud Cost Calculator, Instance Price Comparison & Well-Architected Quiz | Cloud.Design",
            "Compare AWS vs Azure vs Google Cloud costs, VM instance prices, migration savings and your Well-Architected score with free interactive tools.", body, schema)


def p_directory():
    body = page_hero("Cloud Tools Directory", "The curated stack for designing, deploying, securing and paying for cloud infrastructure.", "Directory") + f"""
<section class="section"><div class="container">
<div class="filters"><input type="search" id="tool-q" placeholder="Search tools…" aria-label="Search tools"></div>
<div class="filters" id="tool-cats"></div>
<div class="card sponsor-card mb0" style="margin-bottom:22px"><div class="flex between"><div><span class="badge sp">SPONSORED SLOT</span><h3 class="mt1 mb0">Your cloud product here</h3><p class="small mb0">Reach architects and engineering leaders actively evaluating tools.</p></div><a class="btn btn-ghost" href="support.html#advertise">Advertise →</a></div></div>
<div class="grid g3" id="tool-grid"></div>
<p class="small muted mt2">Disclosure: some outbound links may be affiliate links. Rankings are editorial and never for sale; sponsored placements are always labeled.</p>
</div></section>
<section class="section alt"><div class="container">
<div class="section-head"><span class="eyebrow">Consultancies</span><h2>Certified Cloud Partner Directory</h2><p>We are onboarding a limited number of verified AWS, Azure and Google Cloud consultancies. Listings open by region.</p></div>
<div class="grid g3">
<div class="card"><span class="badge">Open</span><h3 class="mt1">North America</h3><p class="small">Migration, FinOps, Kubernetes, data &amp; AI partners.</p><a class="btn btn-ghost btn-sm" href="partners.html">Apply for listing</a></div>
<div class="card"><span class="badge">Open</span><h3 class="mt1">Europe &amp; UK</h3><p class="small">GDPR-ready, sovereign cloud and public-sector specialists.</p><a class="btn btn-ghost btn-sm" href="partners.html">Apply for listing</a></div>
<div class="card"><span class="badge">Open</span><h3 class="mt1">Asia-Pacific &amp; India</h3><p class="small">Cost-efficient delivery centers and 24/7 managed services.</p><a class="btn btn-ghost btn-sm" href="partners.html">Apply for listing</a></div>
</div>
<div class="card mt2"><h3>Suggest a tool</h3><form class="form" data-form="listing" data-success="Thanks! Our editors review every submission within 7 days."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><div class="row2"><div class="field"><label>Tool name</label><input type="text" name="tool" required></div><div class="field"><label>Website</label><input type="url" name="url" required placeholder="https://"></div></div><div class="row2"><div class="field"><label>Category</label><select name="category"><option>Diagramming</option><option>Infrastructure as Code</option><option>Cost &amp; FinOps</option><option>Observability</option><option>Security</option><option>DevOps</option><option>Networking &amp; Edge</option><option>Other</option></select></div><div class="field"><label>Your email</label><input type="email" name="email" required></div></div><button class="btn btn-primary" type="submit">Submit tool</button></form></div>
</div></section>"""
    return ("directory.html", "Best Cloud Architecture Tools Directory 2026 (Diagramming, IaC, FinOps) | Cloud.Design",
            "Curated directory of the best cloud tools: diagramming, Terraform & IaC, FinOps cost management, observability, security and DevOps.", body, None)


def p_learn():
    body = page_hero("Learn Cloud Architecture", "Deep-dive guides, video explainers and a plain-English glossary — from first VPC to multi-region, multi-cloud platforms.", "Learn") + f"""
<section class="section"><div class="container"><h2>Guides</h2><div class="grid g3 mt2" id="guide-grid"></div></div></section>
{ad('inContent')}
<section class="section alt" id="videos"><div class="container"><div class="flex between"><h2>Videos</h2><a class="btn btn-ghost btn-sm" data-social="youtube" href="#" target="_blank" rel="noopener">▶ Subscribe</a></div><div class="grid g3 mt2" id="video-grid"></div></div></section>
<section class="section"><div class="container split">
<div><h2>Certification roadmap</h2><p>The most in-demand credentials for cloud architects, in the order we recommend.</p>
<ol class="small"><li><b>Foundational:</b> AWS Cloud Practitioner · Azure AZ-900 · Google Cloud Digital Leader</li><li><b>Associate:</b> AWS Solutions Architect – Associate · Azure AZ-104 · Google Associate Cloud Engineer</li><li><b>Professional:</b> AWS Solutions Architect – Professional · Azure AZ-305 · Google Professional Cloud Architect</li><li><b>Specialty:</b> Kubernetes (CKA/CKAD), Terraform Associate, FinOps Certified Practitioner</li></ol>
<a class="btn btn-ghost" href="glossary.html">Browse the glossary →</a></div>
<div class="card"><h3>📬 The Architecture Teardown</h3><p class="small">One real-world architecture dissected every week — diagram, costs, what we'd change.</p><form class="form" data-form="newsletter"><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="email" name="email" placeholder="you@company.com" required aria-label="Email"><select name="role" aria-label="Role"><option value="">Your role (optional)</option><option>Architect</option><option>Developer</option><option>DevOps / SRE</option><option>CTO / Eng. leader</option><option>Student</option></select><button class="btn btn-primary" type="submit">Subscribe free</button></form></div>
</div></section>"""
    return ("learn.html", "Learn Cloud Architecture — Guides, Videos & Certification Roadmap | Cloud.Design",
            "Free cloud architecture guides, video explainers and certification roadmap for AWS, Azure and Google Cloud architects.", body, None)


def p_glossary():
    body = page_hero("Cloud Architecture Glossary", "Plain-English definitions of the terms architects use every day.", "Glossary") + f"""
<section class="section"><div class="container with-side"><div>
<div class="filters"><input type="search" id="gl-q" placeholder="Search terms…" aria-label="Search glossary"></div><div class="filters" id="gl-az"></div>
<div id="glossary"></div></div>
<aside><div class="sticky">{ad_raw('sidebar')}<div class="card mt1"><h3>Talk to an architect</h3><p class="small">Turn terminology into a working design.</p><a class="btn btn-primary btn-block" href="get-matched.html">Free consult</a></div></div></aside>
</div></section>"""
    return ("glossary.html", "Cloud Computing Glossary: 40+ Architecture Terms Explained | Cloud.Design",
            "Definitions of cloud architecture terms: availability zone, landing zone, FinOps, RPO/RTO, service mesh, RAG, GitOps and more.", body, None)


def p_get_matched():
    body = f"""<section class="hero"><div class="container split" style="align-items:start">
<div><span class="badge">Free · No obligation · 60 seconds</span><h1 class="mt1">Get matched with <span class="grad">certified cloud experts</span></h1>
<p class="lead">Migration, cost optimization, Kubernetes, security or GenAI — describe your project and meet up to 3 vetted AWS, Azure or Google Cloud partners who fit your budget.</p>
<div class="grid g2 mt2">
<div class="card"><b>1. Tell us your goal</b><p class="small mb0">6 quick clicks + contact details.</p></div>
<div class="card"><b>2. Human review</b><p class="small mb0">An architect qualifies your brief — not a bot.</p></div>
<div class="card"><b>3. Meet your matches</b><p class="small mb0">Up to 3 intros within 1 business day.</p></div>
<div class="card"><b>4. You decide</b><p class="small mb0">Compare proposals. Free for you.</p></div></div>
<h3 class="mt3">What partners typically deliver</h3>
<ul class="list small"><li>Migration assessment &amp; wave plan (7 Rs)</li><li>Cost optimization review — commitments, rightsizing, spot</li><li>Well-Architected review with remediation backlog</li><li>Landing zone, Kubernetes platform &amp; IaC build-out</li><li>Security posture, compliance (SOC 2, HIPAA, ISO 27001)</li><li>GenAI / RAG platform design and MLOps</li></ul>
</div>
<div>{wizard()}</div>
</div></section>
<section class="section alt"><div class="container" style="max-width:860px">
<h2 class="center">Questions</h2>
<details><summary>Why is this free for me?</summary><div>Partners pay Cloud.Design a fee for qualified introductions. That's how we keep every tool on this site free.</div></details>
<details><summary>How do you vet partners?</summary><div>We verify provider partner tier and certifications, check client references and review delivery samples before a firm is eligible for matches.</div></details>
<details><summary>What happens to my data?</summary><div>Your brief is shared only with the partners you're matched with. We never sell lists. See our <a href="privacy.html">privacy policy</a>.</div></details>
</div></section>"""
    schema = {"@context": "https://schema.org", "@type": "Service", "name": "Cloud consulting partner matching", "provider": {"@type": "Organization", "name": "Cloud.Design"}, "areaServed": "Worldwide", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    return ("get-matched.html", "Get Matched with Certified Cloud Consultants (Free) | Cloud.Design",
            "Free matching with vetted AWS, Azure & Google Cloud consultants for migration, cost optimization, Kubernetes, security and AI projects.", body, schema)


def p_partners():
    body = page_hero("Grow with Cloud.Design", "Receive qualified, intent-verified cloud project leads — and put your brand in front of architects evaluating their next move.", "For Partners") + f"""
<section class="section"><div class="container">
<div class="grid g3">
<div class="card"><h3>Pay-per-lead</h3><div class="price">$149<small>+ / lead</small></div><p class="small">Priced by lead grade (A/B/C) based on budget, timeline and company size.</p><ul class="list small"><li>Exclusive or shared (max 3)</li><li>Budget, cloud &amp; timeline pre-qualified</li><li>Credit for invalid leads</li></ul><a class="btn btn-ghost btn-block" href="#apply">Apply</a></div>
<div class="card featured"><span class="badge">Most popular</span><h3 class="mt1">Featured Partner</h3><div class="price">$499<small>/mo</small></div><p class="small">Directory listing + priority matching in your region and specialties.</p><ul class="list small"><li>Verified badge &amp; profile page</li><li>Priority routing of A-grade leads</li><li>Case-study feature in newsletter</li></ul><a class="btn btn-primary btn-block" href="#apply">Apply</a></div>
<div class="card"><h3>Revenue share</h3><div class="price">10%<small> of closed</small></div><p class="small">No upfront fee — pay only when a matched project closes.</p><ul class="list small"><li>Ideal for large migrations</li><li>Quarterly reconciliation</li><li>Co-marketing options</li></ul><a class="btn btn-ghost btn-block" href="#apply">Apply</a></div>
</div>
<div class="card mt3" id="apply"><h2>Partner application</h2><form class="form" data-form="sponsor" data-success="Application received. We'll review your credentials within 5 business days."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="hidden" name="type" value="partner-application">
<div class="row2"><div class="field"><label>Company</label><input type="text" name="company" required></div><div class="field"><label>Website</label><input type="url" name="website" required placeholder="https://"></div></div>
<div class="row2"><div class="field"><label>Contact name</label><input type="text" name="name" required></div><div class="field"><label>Work email</label><input type="email" name="email" required></div></div>
<div class="row2"><div class="field"><label>Partner tier / certifications</label><input type="text" name="certs" placeholder="e.g. AWS Advanced Tier, Azure Expert MSP"></div><div class="field"><label>Regions served</label><input type="text" name="regions"></div></div>
<div class="field"><label>Model of interest</label><select name="model"><option>Pay-per-lead</option><option>Featured Partner</option><option>Revenue share</option><option>Not sure</option></select></div>
<button class="btn btn-primary" type="submit">Submit application</button></form></div>
</div></section>"""
    return ("partners.html", "Cloud Consulting Leads & Partner Program | Cloud.Design",
            "Get qualified cloud migration, FinOps, Kubernetes and AI project leads. Pay-per-lead, featured partner listing or revenue share.", body, None)


def p_support():
    body = page_hero("Support Cloud.Design", "Everything here is free. Your support funds servers, new architectures, open-source diagrams, contest prizes and paid contributors.", "Support") + f"""
<section class="section" id="donate"><div class="container split" style="align-items:start">
<div class="card"><h2>Make a contribution</h2>
<div class="flex mt1"><label class="check"><input type="radio" name="freq" value="once" checked> One-time</label><label class="check"><input type="radio" name="freq" value="monthly"> Monthly</label></div>
<div class="tiers mt2"><button type="button" class="tier" data-amt="5"><b>$5</b><span class="small">Coffee</span></button><button type="button" class="tier active" data-amt="25"><b>$25</b><span class="small">Diagram</span></button><button type="button" class="tier" data-amt="100"><b>$100</b><span class="small">Guide</span></button><button type="button" class="tier" data-amt="500"><b>$500</b><span class="small">Contest prize</span></button></div>
<div class="field mt2"><label for="don-custom">Custom amount (USD)</label><input id="don-custom" type="number" min="1" placeholder="Other amount"></div>
<div class="flex mt2" id="don-methods"></div>
<p class="small muted mt1">Payments are processed securely by the provider you choose. Cloud.Design never sees your card details.</p></div>
<div><div class="card" id="fund-meter"></div>
<h3 class="mt2">Where the money goes</h3><div class="table-wrap"><table><tbody><tr><td>New architectures &amp; diagrams</td><td><b>40%</b></td></tr><tr><td>Contest prizes &amp; community</td><td><b>20%</b></td></tr><tr><td>Hosting, tooling &amp; data</td><td><b>15%</b></td></tr><tr><td>Paid contributors &amp; editors</td><td><b>15%</b></td></tr><tr><td>Marketing &amp; promotion</td><td><b>10%</b></td></tr></tbody></table></div>
<div class="card mt2"><h3>Pledge by invoice</h3><p class="small">Companies can sponsor via invoice (bank transfer, card or PO).</p><form class="form" data-form="sponsor" data-success="Thanks! We'll email an invoice within 1 business day."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="hidden" name="type" value="donation-pledge"><div class="row2"><input type="text" name="name" placeholder="Name / company" required aria-label="Name"><input type="email" name="email" placeholder="Email" required aria-label="Email"></div><input type="number" name="amount" placeholder="Amount (USD)" min="1" required aria-label="Amount"><button class="btn btn-primary" type="submit">Request invoice</button></form></div></div>
</div></section>

<section class="section alt" id="advertise"><div class="container">
<div class="section-head"><span class="eyebrow">Advertise &amp; sponsor</span><h2>Reach cloud decision-makers</h2><p>Our audience: architects, platform engineers, SREs and engineering leaders with budget authority.</p></div>
<div class="grid g4">
<div class="card"><h3>Newsletter</h3><p class="small">Primary sponsor slot in the weekly Architecture Teardown.</p><b>From $750 / issue</b></div>
<div class="card"><h3>Tool spotlight</h3><p class="small">Pinned, labeled listing in the directory + comparison pages.</p><b>From $400 / mo</b></div>
<div class="card"><h3>Architecture sponsor</h3><p class="small">"Presented by" on a reference architecture and its diagram downloads.</p><b>From $1,200 / mo</b></div>
<div class="card"><h3>Contest partner</h3><p class="small">Co-brand a challenge, provide prizes, get talent and product exposure.</p><b>From $3,000 / season</b></div>
</div>
<div class="card mt2"><h2>Request the media kit</h2><form class="form" data-form="sponsor" data-success="Media kit on its way — check your inbox."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="hidden" name="type" value="advertising"><div class="row2"><div class="field"><label>Name</label><input type="text" name="name" required></div><div class="field"><label>Work email</label><input type="email" name="email" required></div></div><div class="row2"><div class="field"><label>Company</label><input type="text" name="company" required></div><div class="field"><label>Interested in</label><select name="package"><option>Newsletter</option><option>Tool spotlight</option><option>Architecture sponsor</option><option>Contest partner</option><option>Custom campaign</option></select></div></div><div class="field"><label>Monthly budget</label><select name="budget"><option>&lt; $1k</option><option>$1k–$5k</option><option>$5k–$20k</option><option>$20k+</option></select></div><button class="btn btn-primary" type="submit">Send media kit</button></form></div>
</div></section>"""
    return ("support.html", "Support, Donate & Advertise | Cloud.Design",
            "Support Cloud.Design with a one-time or monthly donation, sponsor the project, or advertise to cloud architects and engineering leaders.", body, None)


def p_contests():
    body = page_hero("Cloud Architecture Challenge", "Design. Compete. Win. Quarterly challenges judged by working cloud architects — free to enter, open worldwide.", "Contests") + f"""
<section class="section"><div class="container split" style="align-items:start">
<div><span class="badge hot">LIVE · Season 1</span><h2 class="mt1">Brief: Design a global video-streaming platform for 10M users</h2>
<p>Deliver a diagram, a 1-page design doc and a monthly cost estimate. Optimize for resilience (multi-region), latency (&lt;150 ms p95 globally) and cost.</p>
<div class="countdown mt2" data-countdown></div>
<h3 class="mt3">Prizes — $5,000 pool</h3>
<div class="grid g3"><div class="card center"><div style="font-size:2rem">🥇</div><b>$2,500</b><p class="small mb0">+ featured case study</p></div><div class="card center"><div style="font-size:2rem">🥈</div><b>$1,500</b><p class="small mb0">+ certification voucher</p></div><div class="card center"><div style="font-size:2rem">🥉</div><b>$1,000</b><p class="small mb0">+ swag pack</p></div></div>
<h3 class="mt3">Judging criteria</h3><ul class="list small"><li>Architecture quality &amp; resilience — 35%</li><li>Cost efficiency (realistic estimate) — 25%</li><li>Security &amp; compliance — 20%</li><li>Clarity of documentation — 20%</li></ul>
<details class="mt2"><summary>Official rules (summary)</summary><div>Free to enter; no purchase necessary. One entry per person or team (max 3). Entrants must be 18+ and not residents of sanctioned jurisdictions. Entries must be original work; entrants keep ownership and grant Cloud.Design a license to showcase them. Winners announced within 21 days of close. Prizes paid via bank transfer/PayPal; winners responsible for local taxes. Void where prohibited.</div></details>
</div>
<div class="card"><h2>Enter the challenge</h2><form class="form" data-form="contest" data-success="You're registered! The full brief and submission link are on the way."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off">
<div class="field"><label>Full name</label><input type="text" name="name" required></div>
<div class="field"><label>Email</label><input type="email" name="email" required></div>
<div class="row2"><div class="field"><label>Country</label><input type="text" name="country" required></div><div class="field"><label>Team size</label><select name="team"><option>Solo</option><option>2</option><option>3</option></select></div></div>
<div class="field"><label>Link to submission <span class="hint">(optional now — Drive, GitHub, Figma…)</span></label><input type="url" name="submission" placeholder="https://"></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I'm 18+ and accept the official rules.</label>
<label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Send me future challenges &amp; results.</label>
<button class="btn btn-primary btn-block" type="submit">Register free →</button></form>
<hr style="border:0;border-top:1px solid var(--line);margin:22px 0"><h3>Sponsor a prize</h3><p class="small">Put your brand in front of every entrant and the talent pool.</p><a class="btn btn-ghost btn-block" href="support.html#advertise">Become a contest partner</a></div>
</div></section>
{ad('inContent')}"""
    schema = {"@context": "https://schema.org", "@type": "Event", "name": "Cloud Architecture Challenge — Season 1", "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "startDate": "2026-09-15", "endDate": "2026-12-15", "location": {"@type": "VirtualLocation", "url": SITE + "/contests.html"}, "organizer": {"@type": "Organization", "name": "Cloud.Design", "url": SITE}}
    return ("contests.html", "Cloud Architecture Challenge — $5,000 Prize Pool | Cloud.Design",
            "Enter the free Cloud Architecture Challenge. Design a global platform, get judged by working architects and win cash prizes.", body, schema)


def p_careers():
    body = page_hero("Careers & Talent Network", "Hire vetted cloud talent, or join the network of architects, writers and engineers who build Cloud.Design.", "Careers") + f"""
<section class="section"><div class="container grid g2">
<div class="card"><h2>We're hiring (remote, freelance)</h2>
<details><summary>Cloud Architecture Writer — AWS/Azure/GCP</summary><div>Write and diagram reference architectures and deep-dive guides. Paid per piece ($300–$900). Certification preferred.</div></details>
<details><summary>YouTube Host / Video Editor</summary><div>Script, record or edit 8–15 minute architecture explainers. Paid per video.</div></details>
<details><summary>Partner Success Manager (commission)</summary><div>Onboard and vet consulting partners; commission on partner revenue.</div></details>
<details><summary>Front-end Developer (open source)</summary><div>Help build interactive calculators and the diagram editor. Paid bounties on GitHub issues.</div></details>
<h3 class="mt2">Apply</h3><form class="form" data-form="careers" data-success="Application received — we reply to every applicant within 7 days."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="hidden" name="type" value="job-application"><div class="row2"><input type="text" name="name" placeholder="Full name" required aria-label="Full name"><input type="email" name="email" placeholder="Email" required aria-label="Email"></div><select name="role" aria-label="Role"><option>Cloud Architecture Writer</option><option>YouTube Host / Video Editor</option><option>Partner Success Manager</option><option>Front-end Developer</option><option>Other</option></select><input type="url" name="portfolio" placeholder="LinkedIn / portfolio URL" required aria-label="Portfolio"><textarea name="message" placeholder="Why you? Links to 1–2 samples." aria-label="Message"></textarea><button class="btn btn-primary" type="submit">Apply</button></form></div>
<div class="card"><h2>Hire cloud talent</h2><p>Post a role to our talent network of architects, SREs, DevOps and data engineers. Or let us shortlist pre-vetted contractors.</p>
<ul class="list small"><li>Job post: featured on site + newsletter — $199 / 30 days</li><li>Shortlist service: 3 vetted candidates in 5 days</li><li>Contract-to-hire and fractional architects available</li></ul>
<form class="form" data-form="careers" data-success="Thanks! We'll send a shortlist plan within 1 business day."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="hidden" name="type" value="hire-request"><div class="row2"><input type="text" name="company" placeholder="Company" required aria-label="Company"><input type="email" name="email" placeholder="Work email" required aria-label="Work email"></div><input type="text" name="role" placeholder="Role e.g. Senior AWS Architect" required aria-label="Role"><div class="row2"><select name="type_of_hire" aria-label="Hire type"><option>Full-time</option><option>Contract</option><option>Fractional</option></select><input type="text" name="location" placeholder="Location / remote" aria-label="Location"></div><button class="btn btn-primary" type="submit">Request talent</button></form></div>
</div></section>"""
    return ("careers.html", "Cloud Architect Jobs & Talent Network | Cloud.Design",
            "Hire vetted cloud architects, DevOps and SRE talent, or apply to write, film and build for Cloud.Design.", body, None)


def p_about():
    body = page_hero("About Cloud.Design", "An independent, vendor-neutral home for cloud architecture.", "About") + """
<section class="section"><div class="container prose">
<h2>Our mission</h2><p>Cloud decisions made in the first weeks of a project lock in most of its long-term cost and risk. Yet the best guidance is scattered across three providers' documentation, paywalled courses and consultant slide decks. Cloud.Design brings it together — free, comparable and practical.</p>
<h2>What we believe</h2><ul><li><b>Vendor-neutral.</b> We compare AWS, Azure and Google Cloud on the merits of your workload.</li><li><b>Show the money.</b> Every architecture comes with a realistic cost range.</li><li><b>Trade-offs over hype.</b> Every design lists what it costs you, not just what it gives you.</li><li><b>Transparent funding.</b> Ads, sponsorships and partner fees are always labeled.</li></ul>
<h2>How we make money</h2><p>Display advertising, labeled sponsorships, affiliate links on tools we'd recommend anyway, referral fees from vetted partners when we match a project, and donations from people who find the site useful. None of these buy editorial rankings.</p>
<h2>Editorial standards</h2><p>Architectures are reviewed by certified practitioners and updated when providers change services or pricing. Spot an error? <a href="contact.html">Tell us</a> — corrections are published in the changelog.</p>
<div class="flex mt2"><a class="btn btn-primary" href="get-matched.html">Work with an architect</a><a class="btn btn-ghost" href="careers.html">Join the team</a></div>
</div></section>"""
    return ("about.html", "About Cloud.Design — Independent Cloud Architecture Hub", "Cloud.Design is an independent, vendor-neutral hub for cloud architecture, costs and expert help.", body, None)


def p_contact():
    body = page_hero("Contact us", "Questions, corrections, partnerships or press — we reply within 1 business day.", "Contact") + """
<section class="section"><div class="container split" style="align-items:start">
<form class="card form" data-form="contact"><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off">
<div class="row2"><div class="field"><label>Name</label><input type="text" name="name" required></div><div class="field"><label>Email</label><input type="email" name="email" required></div></div>
<div class="field"><label>Topic</label><select name="topic"><option>Project help / consultation</option><option>Book a 15-min call</option><option>Partnership / advertising</option><option>Correction or contribution</option><option>Press</option><option>Other</option></select></div>
<div class="field"><label>Message</label><textarea name="message" required></textarea></div>
<button class="btn btn-primary" type="submit">Send message</button></form>
<div><div class="card"><h3>Email</h3><p><a data-email href="#">hello@cloud.design</a></p><h3>Fastest route for projects</h3><p class="small">Use the 60-second brief — it goes straight to an architect.</p><a class="btn btn-primary" href="get-matched.html">Get matched →</a></div>
<div class="card mt2"><h3>Follow</h3><div class="social"><a class="icon-btn" data-social="youtube" aria-label="YouTube">▶</a><a class="icon-btn" data-social="x" aria-label="X">𝕏</a><a class="icon-btn" data-social="linkedin" aria-label="LinkedIn">in</a><a class="icon-btn" data-social="github" aria-label="GitHub">⌥</a></div></div></div>
</div></section>"""
    return ("contact.html", "Contact Cloud.Design", "Contact Cloud.Design for project help, partnerships, advertising, corrections or press.", body, None)


def p_privacy():
    d = datetime.date.today().strftime("%B %d, %Y")
    body = page_hero("Privacy Policy", f"Last updated {d}", "Privacy") + f"""
<section class="section"><div class="container prose">
<p>This policy explains what Cloud.Design ("we") collects and why. This template should be reviewed by qualified counsel for your jurisdiction before relying on it.</p>
<h2>Information you give us</h2><p>When you submit a form (expert matching, newsletter, contest, careers, contact, sponsorship) we collect the fields you enter. Matching briefs are shared only with the partners you are matched with (maximum three).</p>
<h2>Automatically collected</h2><p>With your consent we use Google Analytics to understand usage. Our hosting provider may log IP addresses for security.</p>
<h2 id="cookies">Cookies &amp; advertising</h2><p>We use Google AdSense to display ads. Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this and/or other sites. You may opt out of personalized advertising at <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener">aboutads.info</a>. If you choose "Essential only", we request non-personalized ads.</p>
<p><button class="btn btn-ghost btn-sm" onclick="localStorage.removeItem('cd_consent');location.reload()">Change cookie choice</button></p>
<h2>Your rights</h2><p>You may request access, correction or deletion of your data at any time by emailing <a data-email href="#">us</a>. EU/UK residents have GDPR rights; California residents have CCPA/CPRA rights.</p>
<h2>Retention</h2><p>Lead and contact data is kept for up to 24 months, then deleted or anonymized.</p>
<h2>Children</h2><p>This site is not directed at children under 16.</p>
</div></section>"""
    return ("privacy.html", "Privacy Policy | Cloud.Design", "How Cloud.Design collects, uses and protects your information, including cookies and advertising.", body, None)


def p_terms():
    body = page_hero("Terms of Use", "Please read these terms before using Cloud.Design.", "Terms") + """
<section class="section"><div class="container prose">
<h2>Use of content</h2><p>Content is provided for informational purposes. Diagrams you download may be used in your own projects with attribution. Cost figures are estimates; verify with providers before purchasing.</p>
<h2>No professional advice</h2><p>Nothing on this site is a guarantee of fitness for a particular purpose. Engagements with matched partners are solely between you and the partner.</p>
<h2>Trademarks</h2><p>AWS, Microsoft Azure and Google Cloud are trademarks of their respective owners. Cloud.Design is independent and not affiliated with or endorsed by them.</p>
<h2>Affiliate &amp; sponsored content</h2><p>Some links earn us a commission. Sponsored placements are labeled.</p>
<h2>Donations</h2><p>Donations are voluntary, non-refundable and not tax-deductible unless stated otherwise.</p>
<h2>Contests</h2><p>Each contest has official rules published on its page, which govern eligibility, judging and prizes.</p>
<h2>Liability</h2><p>To the maximum extent permitted by law, Cloud.Design is not liable for indirect or consequential damages arising from use of the site.</p>
</div></section>"""
    return ("terms.html", "Terms of Use | Cloud.Design", "Terms governing use of Cloud.Design content, tools, contests, donations and partner matching.", body, None)


def p_404():
    body = """<section class="hero"><div class="container center"><h1>404 — this resource was <span class="grad">terminated</span></h1><p class="lead" style="margin:0 auto">Like an unattached EBS volume, this page no longer exists.</p><div class="hero-cta" style="justify-content:center"><a class="btn btn-primary" href="index.html">Go home</a><a class="btn btn-ghost" href="architectures.html">Browse architectures</a></div></div></section>"""
    return ("404.html", "Page not found | Cloud.Design", "Page not found.", body, None)


PAGES = [p_index, p_architectures, p_patterns, p_tools, p_directory, p_learn, p_glossary, p_get_matched,
         p_partners, p_support, p_contests, p_careers, p_about, p_contact, p_privacy, p_terms, p_404]


def guide_page(g):
    base = "../"
    body = f"""<section class="page-hero"><div class="container"><nav class="crumbs"><a href="../index.html">Home</a> / <a href="../learn.html">Learn</a> / {g['cat']}</nav><span class="tag">{g['cat']}</span><h1 class="mt1">{g['title']}</h1><p class="muted small">⏱ {g['mins']} min read · Updated {datetime.date.today():%B %Y} · Cloud.Design Editorial</p>
<div class="flex small"><span>Share:</span><a data-share-to="x">X</a><a data-share-to="linkedin">LinkedIn</a><a data-share-to="reddit">Reddit</a><a data-share-to="email">Email</a></div></div></section>
<section class="section"><div class="container with-side"><article class="prose">{g['html']}
{ad_raw('inContent')}
<div class="card mt2"><h3>Want this done for you?</h3><p class="small">Get a free review from a certified architect — matched to your cloud and budget.</p><a class="btn btn-primary" href="../get-matched.html?service={g.get('service','architecture')}">Get a free review →</a></div></article>
<aside><div class="sticky">{ad_raw('sidebar')}<div class="card mt1"><h3>📬 Weekly teardown</h3><form class="form" data-form="newsletter"><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="email" name="email" placeholder="you@company.com" required aria-label="Email"><button class="btn btn-primary btn-block" type="submit">Subscribe</button></form></div></div></aside>
</div></section>"""
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["excerpt"], "author": {"@type": "Organization", "name": "Cloud.Design"}, "publisher": {"@type": "Organization", "name": "Cloud.Design"}, "datePublished": str(datetime.date.today()), "mainEntityOfPage": f"{SITE}/guides/{g['slug']}.html"}
    path = f"guides/{g['slug']}.html"
    html = head(g["title"] + " | Cloud.Design", g["excerpt"], path, base, schema, "article") + header(base) + body + footer(base)
    return path, html


def main():
    urls = []
    for fn in PAGES:
        name, title, desc, body, schema = fn()
        html = head(title, desc, name, "", schema) + header("") + body + footer("")
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(html)
        if name != "404.html":
            urls.append(name)
    os.makedirs(os.path.join(ROOT, "guides"), exist_ok=True)
    for g in GUIDES:
        path, html = guide_page(g)
        with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
            f.write(html)
        urls.append(path)
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        pr = "1.0" if u == "index.html" else "0.8"
        sm += f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>\n"
    sm += "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(sm)
    print(f"Built {len(urls) + 1} pages")


if __name__ == "__main__":
    main()
