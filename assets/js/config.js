/* ==========================================================
   Cloud.Design — SITE CONFIG (edit this file only to go live)
   Everything below is safe to leave blank; features degrade
   gracefully (ads show placeholders, forms fall back to email).
   ========================================================== */
window.CD_CONFIG = {
  siteName: "Cloud.Design",
  domain: "cloud.design",
  contactEmail: "hello@cloud.design",            // shown publicly + mailto fallback

  /* --- Google AdSense --- get it at adsense.google.com */
  adsenseClient: "",                              // e.g. "ca-pub-1234567890123456"
  adSlots: {                                      // ad unit IDs from AdSense → Ads → By ad unit
    header: "", inContent: "", sidebar: "", footer: ""
  },

  /* --- Analytics (optional) --- */
  ga4Id: "",                                      // e.g. "G-XXXXXXX"

  /* --- Form backends ---
     Free options that work on GitHub Pages:
       Formspree   → https://formspree.io/f/xxxxxxx
       Getform     → https://getform.io/f/xxxxxxx
       Web3Forms   → https://api.web3forms.com/submit (set web3formsKey)
       Google Apps Script web app URL (writes to a Google Sheet)
     One endpoint per form type; "default" is used when a type is blank. */
  forms: {
    default: "",
    lead: "",          // Get Matched wizard + quote requests (highest value)
    newsletter: "",
    contact: "",
    sponsor: "",
    contest: "",
    careers: "",
    listing: ""
  },
  web3formsKey: "",

  /* --- Donations / support --- paste your real links */
  donate: {
    githubSponsors: "https://github.com/sponsors/WEBWORKSA1",
    buyMeACoffee: "",   // https://buymeacoffee.com/yourname
    kofi: "",           // https://ko-fi.com/yourname
    paypal: "",         // https://paypal.me/yourname
    stripe: "",         // Stripe Payment Link (supports custom amounts)
    patreon: "",
    crypto: ""          // wallet address (shown with copy button)
  },
  fundGoal: { raised: 0, goal: 5000, label: "Server, tooling & content fund — 2026" },

  /* --- Social / YouTube --- */
  social: {
    youtube: "https://www.youtube.com/@clouddesign",
    x: "https://x.com/clouddesign",
    linkedin: "https://www.linkedin.com/company/clouddesign",
    github: "https://github.com/WEBWORKSA1/cloud-design",
    discord: ""
  },

  /* --- Contest --- */
  contest: {
    name: "Cloud Architecture Challenge — Season 1",
    endsAt: "2026-12-15T23:59:00Z",
    prizePool: "$5,000"
  }
};
