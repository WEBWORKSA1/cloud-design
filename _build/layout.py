"""Shared layout partials for Cloud.Design static site generator."""
import json

SITE = "https://cloud.design"
NAV = [
    ("architectures.html", "Architectures"),
    ("patterns.html", "Patterns"),
    ("tools.html", "Free Tools"),
    ("directory.html", "Directory"),
    ("learn.html", "Learn"),
    ("contests.html", "Contests"),
    ("support.html", "Support"),
]

LOGO_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.1 9.1 4.5 4.5 0 0 0 7 18Z" fill="#fff"/></svg>'


def head(title, desc, path, base="", schema=None, og_type="website"):
    url = f"{SITE}/{path}".replace("/index.html", "/")
    ld = ""
    if schema:
        ld = f'<script type="application/ld+json">{json.dumps(schema)}</script>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#3b5bfd">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Cloud.Design">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{base}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css">
<script>try{{var t=localStorage.getItem("cd_theme");if(t)document.documentElement.setAttribute("data-theme",JSON.parse(t))}}catch(e){{}}</script>
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(base=""):
    links = "".join(f'<li><a href="{base}{h}">{t}</a></li>' for h, t in NAV)
    return f"""<div class="topbar">🏆 The <b>Cloud Architecture Challenge</b> is live — $5,000 in prizes. <a href="{base}contests.html">Enter free →</a></div>
<header class="site"><div class="container nav">
<a class="logo" href="{base}index.html" aria-label="Cloud.Design home"><span class="mark">{LOGO_SVG}</span><span>Cloud<span class="dot">.</span>Design</span></a>
<ul class="menu" id="menu">{links}<li><a href="{base}partners.html">For Partners</a></li></ul>
<div class="nav-actions">
<button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg></button>
<a class="btn btn-primary btn-sm btn-sm-hide" href="{base}get-matched.html">Get Expert Help</a>
<button class="icon-btn burger" aria-label="Open menu" aria-controls="menu" aria-expanded="false"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></div></header>
<main id="main">
"""


def footer(base=""):
    return f"""</main>
<footer class="site"><div class="container">
<div class="foot">
<div><a class="logo" href="{base}index.html"><span class="mark">{LOGO_SVG}</span><span>Cloud<span class="dot">.</span>Design</span></a>
<p class="small mt1">The independent hub for designing, costing and building cloud architecture on AWS, Azure and Google Cloud.</p>
<form class="form" data-form="newsletter" data-success="You're in! Check your inbox for the Architecture Starter Kit."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><div class="flex" style="flex-wrap:nowrap"><input type="email" name="email" placeholder="you@company.com" required aria-label="Email"><button class="btn btn-primary btn-sm" type="submit">Subscribe</button></div><span class="small muted">Weekly architecture teardown. 1-click unsubscribe.</span></form>
<div class="social"><a class="icon-btn" data-social="youtube" aria-label="YouTube">▶</a><a class="icon-btn" data-social="x" aria-label="X">𝕏</a><a class="icon-btn" data-social="linkedin" aria-label="LinkedIn">in</a><a class="icon-btn" data-social="github" aria-label="GitHub">⌥</a></div>
</div>
<div><h4>Design</h4><ul><li><a href="{base}architectures.html">Reference Architectures</a></li><li><a href="{base}patterns.html">Design Patterns</a></li><li><a href="{base}tools.html#estimator">Cost Estimator</a></li><li><a href="{base}tools.html#quiz">Well-Architected Score</a></li><li><a href="{base}tools.html#instances">Instance Prices</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{base}learn.html">Guides</a></li><li><a href="{base}learn.html#videos">Videos</a></li><li><a href="{base}glossary.html">Glossary</a></li><li><a href="{base}directory.html">Tools Directory</a></li><li><a href="{base}contests.html">Contests</a></li></ul></div>
<div><h4>Services</h4><ul><li><a href="{base}get-matched.html">Get Matched</a></li><li><a href="{base}get-matched.html?service=migration">Cloud Migration</a></li><li><a href="{base}get-matched.html?service=cost">Cost Optimization</a></li><li><a href="{base}partners.html">Become a Partner</a></li><li><a href="{base}careers.html">Careers &amp; Talent</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{base}about.html">About</a></li><li><a href="{base}support.html">Donate / Support</a></li><li><a href="{base}support.html#advertise">Advertise</a></li><li><a href="{base}contact.html">Contact</a></li><li><a href="{base}privacy.html">Privacy</a> · <a href="{base}terms.html">Terms</a></li></ul></div>
</div>
<div class="foot-bottom"><span>© <span data-year></span> Cloud.Design · Independent. Not affiliated with AWS, Microsoft or Google. Some links are affiliate or sponsored and clearly labeled.</span><span><a href="{base}privacy.html#cookies">Cookie settings</a></span></div>
</div></footer>

<div class="cookie" role="dialog" aria-label="Cookie consent"><p>We use cookies for analytics and to show ads that keep Cloud.Design free. Choose what you allow — see our <a href="{base}privacy.html">privacy policy</a>.</p><div class="flex"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>

<div class="modal" id="exit-modal"><div class="box" role="dialog" aria-modal="true" aria-labelledby="exit-t"><button class="icon-btn x" aria-label="Close">✕</button>
<span class="badge hot">FREE DOWNLOAD</span><h2 id="exit-t" class="mt1">Before you go — grab the Cloud Architecture Starter Kit</h2>
<p>18 editable reference diagrams, the 47-step migration checklist and a cost-optimization cheat sheet.</p>
<form class="form" data-form="newsletter" data-success="Sent! Check your inbox for the Starter Kit."><input class="hp" name="_gotcha" tabindex="-1" autocomplete="off"><input type="hidden" name="source" value="exit-intent"><input type="email" name="email" placeholder="Work email" required aria-label="Work email"><button class="btn btn-primary btn-block" type="submit">Send me the kit →</button><span class="small muted center">No spam. Unsubscribe anytime.</span></form></div></div>

<a class="btn btn-primary sticky-cta" href="{base}get-matched.html">💬 Free architecture consult</a>
<script src="{base}assets/js/config.js"></script>
<script src="{base}assets/js/data.js"></script>
<script src="{base}assets/js/main.js" defer></script>
</body></html>
"""


def page_hero(title, sub, crumb, base=""):
    return f"""<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="{base}index.html">Home</a> / {crumb}</nav><h1>{title}</h1><p class="lead" style="max-width:720px">{sub}</p></div></section>"""


def ad(kind="inContent"):
    cls = " sidebar" if kind == "sidebar" else ""
    return f'<div class="container"><div class="ad-slot{cls}" data-ad="{kind}">Ad space — configure AdSense in assets/js/config.js</div></div>'


def ad_raw(kind="inContent"):
    cls = " sidebar" if kind == "sidebar" else ""
    return f'<div class="ad-slot{cls}" data-ad="{kind}">Ad space</div>'


def choice(name, value, label, req=False):
    r = " required" if req else ""
    return f'<label class="choice"><input type="radio" name="{name}" value="{value}"{r}><span>{label}</span></label>'


def wizard(cta="Get my free matches →"):
    def step(title, sub, name, opts):
        c = "".join(choice(name, v, l, i == 0) for i, (v, l) in enumerate(opts))
        return f'<div class="step"><h3>{title}</h3><p class="small">{sub}</p><div class="choices">{c}</div></div>'
    steps = [
        step("What do you need help with?", "Pick the closest match — you can add detail later.", "service", [
            ("migration", "🚚 Cloud migration"), ("cost", "💰 Cut cloud costs"), ("architecture", "📐 Architecture design / review"),
            ("devops", "⚙️ DevOps, Kubernetes & IaC"), ("security", "🔐 Security & compliance"), ("ai", "🤖 AI / GenAI platform")]),
        step("Which cloud?", "Not sure is a perfectly good answer.", "cloud", [
            ("AWS", "🟧 AWS"), ("Azure", "🟦 Microsoft Azure"), ("GCP", "🟩 Google Cloud"), ("Multi / not sure", "🌐 Multi-cloud / not sure")]),
        step("Current monthly cloud spend?", "Helps us match partners that fit your scale.", "spend", [
            ("Not on cloud yet", "Not on cloud yet"), ("< $1k", "Under $1k"), ("$1k–$10k", "$1k – $10k"), ("$10k–$50k", "$10k – $50k"), ("$50k+", "$50k+")]),
        step("Project budget?", "Ranges based on Clutch.co cloud-consulting benchmarks.", "budget", [
            ("< $10k", "Under $10k"), ("$10k–$49k", "$10k – $49k"), ("$50k–$199k", "$50k – $199k"), ("$200k+", "$200k+")]),
        step("When do you want to start?", "", "timeline", [
            ("ASAP", "⚡ ASAP"), ("Within 1 month", "Within 1 month"), ("Within 3 months", "Within 3 months"), ("Researching", "Just researching")]),
        step("Company size?", "", "size", [
            ("1-50", "1 – 50"), ("51-200", "51 – 200"), ("201-1000", "201 – 1,000"), ("1000+", "1,000+")]),
    ]
    contact = """<div class="step"><h3>Where should we send your matches?</h3><p class="small">A human architect reviews every brief. We never sell your data to lists.</p>
<div class="form"><div class="row2"><div class="field"><label for="w-name">Full name</label><input id="w-name" type="text" name="name" autocomplete="name" required></div>
<div class="field"><label for="w-email">Work email</label><input id="w-email" type="email" name="email" autocomplete="email" required></div></div>
<div class="row2"><div class="field"><label for="w-co">Company</label><input id="w-co" type="text" name="company" autocomplete="organization" required></div>
<div class="field"><label for="w-ph">Phone <span class="hint">(optional)</span></label><input id="w-ph" type="tel" name="phone" autocomplete="tel"></div></div>
<div class="field"><label for="w-msg">Anything else? <span class="hint">(optional)</span></label><textarea id="w-msg" name="details" placeholder="e.g. 40 VMs on VMware, SQL Server, need to exit data center by Q2"></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted by Cloud.Design and up to 3 matched partners about this request.</label></div></div>"""
    return f"""<form class="wizard" data-wizard data-cta="{cta}" novalidate onsubmit="return false">
<input class="hp" name="_gotcha" tabindex="-1" autocomplete="off">
<div class="progress"><span></span></div><div class="step-count"><span data-step-count></span><span>⏱ 60 seconds</span></div>
{''.join(steps)}{contact}
<div class="wiz-nav"><button type="button" class="btn btn-ghost" data-back>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div>
<div class="guarantee"><span>🔒 No spam, ever</span><span>✅ Free, no obligation</span><span>⭐ Vetted partners only</span></div>
</form>"""


def lead_band(base=""):
    return f"""<section class="section"><div class="container"><div class="lead-band"><div class="split">
<div><span class="badge" style="background:#ffffff26;color:#fff">FREE EXPERT MATCHING</span>
<h2 class="mt1">Get your cloud project designed, costed &amp; built by vetted experts</h2>
<p>Tell us what you're building. Within 1 business day we introduce up to 3 certified AWS, Azure or Google Cloud partners that fit your budget — with a free architecture review.</p>
<ul class="checks"><li>Certified partners only — AWS, Microsoft &amp; Google credentials verified</li><li>Organizations waste ~29% of cloud spend (Flexera State of the Cloud) — our partners target that first</li><li>You choose. Zero obligation, zero cost to you</li></ul>
<p class="small">Prefer to talk? <a href="{base}contact.html" style="color:#fff;text-decoration:underline">Book a 15-min call</a></p></div>
<div>{wizard()}</div></div></div></div></section>"""
