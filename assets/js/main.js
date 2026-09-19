/* ==========================================================
   Cloud.Design — main.js (no dependencies)
   ========================================================== */
(function(){
"use strict";
const C = window.CD_CONFIG || {}, D = window.CD_DATA || {};
const $ = (s,r=document)=>r.querySelector(s), $$ = (s,r=document)=>Array.from(r.querySelectorAll(s));
const esc = s => String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const store = {get(k,d){try{const v=localStorage.getItem("cd_"+k);return v===null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem("cd_"+k,JSON.stringify(v))}catch(e){}}};
const money = (n,dec=0)=>"$"+Number(n).toLocaleString("en-US",{minimumFractionDigits:dec,maximumFractionDigits:dec});
const PROV = {aws:"AWS",azure:"Azure",gcp:"Google Cloud",multi:"Multi-cloud"};

function toast(msg){let t=$(".toast");if(!t){t=document.createElement("div");t.className="toast";t.setAttribute("role","status");document.body.appendChild(t)}t.textContent=msg;t.classList.add("show");clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove("show"),2600)}
window.cdToast = toast;

/* ---------- Theme ---------- */
const root=document.documentElement, saved=store.get("theme",null);
if(saved) root.setAttribute("data-theme",saved);
$$("[data-theme-toggle]").forEach(b=>b.addEventListener("click",()=>{
  const dark = root.getAttribute("data-theme")==="dark" || (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches);
  const next = dark?"light":"dark"; root.setAttribute("data-theme",next); store.set("theme",next);
}));

/* ---------- Nav ---------- */
const burger=$(".burger"), menu=$(".menu");
if(burger&&menu){burger.addEventListener("click",()=>{const o=menu.classList.toggle("open");burger.setAttribute("aria-expanded",o)});
  $$(".menu a").forEach(a=>a.addEventListener("click",()=>menu.classList.remove("open")));}
const here=location.pathname.split("/").pop()||"index.html";
$$(".menu a").forEach(a=>{if(a.getAttribute("href")===here)a.setAttribute("aria-current","page")});
$$("[data-year]").forEach(e=>e.textContent=new Date().getFullYear());

/* ---------- Reveal on scroll ---------- */
if("IntersectionObserver" in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{threshold:.12});$$(".reveal").forEach(e=>io.observe(e))}else $$(".reveal").forEach(e=>e.classList.add("in"));

/* ---------- Counters ---------- */
$$("[data-count]").forEach(el=>{const end=+el.dataset.count,suf=el.dataset.suffix||"";let s=null;
  const step=t=>{if(!s)s=t;const p=Math.min((t-s)/1400,1);el.textContent=Math.floor(end*p).toLocaleString()+suf;if(p<1)requestAnimationFrame(step)};
  const io=new IntersectionObserver(e=>{if(e[0].isIntersecting){requestAnimationFrame(step);io.disconnect()}});io.observe(el)});

/* ---------- Consent, AdSense, Analytics ---------- */
function loadScript(src,attrs={}){const s=document.createElement("script");s.async=true;s.src=src;Object.entries(attrs).forEach(([k,v])=>s.setAttribute(k,v));document.head.appendChild(s);return s}
function initAds(personalized){
  if(!C.adsenseClient){return}
  window.adsbygoogle=window.adsbygoogle||[];
  if(!personalized) window.adsbygoogle.requestNonPersonalizedAds=1;
  loadScript("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client="+C.adsenseClient,{crossorigin:"anonymous"});
  $$(".ad-slot").forEach(slot=>{
    const id=(C.adSlots||{})[slot.dataset.ad||"inContent"]; if(!id) return;
    slot.classList.add("live"); slot.innerHTML='<ins class="adsbygoogle" style="display:block" data-ad-client="'+C.adsenseClient+'" data-ad-slot="'+id+'" data-ad-format="auto" data-full-width-responsive="true"></ins>';
    try{(window.adsbygoogle=window.adsbygoogle||[]).push({})}catch(e){}
  });
}
function initGA(){if(!C.ga4Id)return;loadScript("https://www.googletagmanager.com/gtag/js?id="+C.ga4Id);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag("js",new Date());gtag("config",C.ga4Id,{anonymize_ip:true})}
function track(ev,params){try{window.gtag&&gtag("event",ev,params||{})}catch(e){}}
window.cdTrack=track;
const consent=store.get("consent",null), ck=$(".cookie");
function applyConsent(v){store.set("consent",v);ck&&ck.classList.remove("show");if(v==="all"){initGA();initAds(true)}else initAds(false)}
if(consent) applyConsent(consent); else if(ck) setTimeout(()=>ck.classList.add("show"),900);
$$("[data-consent]").forEach(b=>b.addEventListener("click",()=>applyConsent(b.dataset.consent)));

/* ---------- Forms (static-host friendly) ---------- */
function endpointFor(type){const f=C.forms||{};return f[type]||f.default||""}
function utm(){const p=new URLSearchParams(location.search),o={};["utm_source","utm_medium","utm_campaign","utm_term","utm_content","ref"].forEach(k=>{if(p.get(k))o[k]=p.get(k)});
  const first=store.get("utm",null); if(!first&&Object.keys(o).length) store.set("utm",o); return Object.assign({},first||{},o)}
utm();
async function submitData(type,data){
  data=Object.assign({form_type:type,page:location.href,submitted_at:new Date().toISOString(),referrer:document.referrer||""},store.get("utm",{}),data);
  const url=endpointFor(type);
  const queue=store.get("outbox",[]);queue.push(data);store.set("outbox",queue.slice(-50));
  if(url){
    const body=Object.assign({},data); if(C.web3formsKey&&/web3forms/.test(url)){body.access_key=C.web3formsKey;body.subject="Cloud.Design — "+type}
    const r=await fetch(url,{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(body)});
    if(!r.ok) throw new Error("Network error ("+r.status+")");
    track("generate_lead",{form_type:type});
    return "sent";
  }
  // Fallback: open the visitor's mail client with a prefilled message
  const lines=Object.entries(data).map(([k,v])=>k+": "+v).join("\n");
  const mail="mailto:"+(C.contactEmail||"")+"?subject="+encodeURIComponent("Cloud.Design — "+type)+"&body="+encodeURIComponent(lines);
  window.location.href=mail; track("generate_lead",{form_type:type,fallback:"mailto"});
  return "mailto";
}
window.cdSubmit=submitData;
function formToObj(form){const o={};new FormData(form).forEach((v,k)=>{if(k==="_gotcha")return;o[k]=o[k]?o[k]+", "+v:v});return o}
function msg(form,ok,text){let m=$(".form-msg",form);if(!m){m=document.createElement("div");m.className="form-msg";m.setAttribute("role","alert");form.appendChild(m)}m.className="form-msg "+(ok?"ok":"err");m.textContent=text}
$$("form[data-form]").forEach(form=>form.addEventListener("submit",async e=>{
  e.preventDefault();
  if(form._gotcha&&form._gotcha.value) return; // bot
  if(!form.checkValidity()){form.reportValidity();return}
  const btn=$("button[type=submit]",form),txt=btn&&btn.textContent; if(btn){btn.disabled=true;btn.textContent="Sending…"}
  try{const how=await submitData(form.dataset.form,formToObj(form));
    msg(form,true,form.dataset.success||(how==="mailto"?"Almost done — send the email that just opened and we'll reply within 1 business day.":"Thanks! We'll be in touch within 1 business day."));
    form.reset(); if(form.dataset.form==="newsletter") store.set("subscribed",true);
    const m=form.closest(".modal"); if(m) setTimeout(()=>m.classList.remove("open"),1800);
  }catch(err){msg(form,false,"Something went wrong: "+err.message+". Please email "+(C.contactEmail||"us")+".")}
  finally{if(btn){btn.disabled=false;btn.textContent=txt}}
}));

/* ---------- Lead wizard (multi-step) ---------- */
$$("[data-wizard]").forEach(wz=>{
  const steps=$$(".step",wz), bar=$(".progress span",wz), cnt=$("[data-step-count]",wz), back=$("[data-back]",wz), next=$("[data-next]",wz);
  let i=0;
  const pre=new URLSearchParams(location.search).get("service");
  if(pre){const r=$('input[name="service"][value="'+pre+'"]',wz);if(r)r.checked=true}
  function show(n){i=n;steps.forEach((s,k)=>s.classList.toggle("active",k===i));bar.style.width=((i+1)/steps.length*100)+"%";
    if(cnt)cnt.textContent="Step "+(i+1)+" of "+steps.length;back.style.visibility=i?"visible":"hidden";
    next.textContent=i===steps.length-1?(wz.dataset.cta||"Get my free matches →"):"Continue →";
    const f=$("input,select,textarea",steps[i]); if(f&&n>0) setTimeout(()=>f.focus({preventScroll:true}),50)}
  function valid(){const req=$$("[required]",steps[i]);for(const f of req){if(f.type==="radio"){if(!$('input[name="'+f.name+'"]:checked',steps[i])){toast("Please choose an option");return false}}else if(!f.checkValidity()){f.reportValidity();return false}}return true}
  // auto-advance on single choice
  $$('.step input[type=radio]',wz).forEach(r=>r.addEventListener("change",()=>{if(i<steps.length-1)setTimeout(()=>{if(valid())show(i+1)},220)}));
  back.addEventListener("click",()=>show(Math.max(0,i-1)));
  next.addEventListener("click",async()=>{
    if(!valid())return;
    if(i<steps.length-1){show(i+1);track("wizard_step",{step:i+1});return}
    if(wz._gotcha&&wz._gotcha.value) return;
    const data=formToObj(wz);
    // lead score for routing/pricing to partners
    let score=0;const b=data.budget||"",t=data.timeline||"",s=data.size||"";
    score+= /200k|50k/.test(b)?40:/10k/.test(b)?25:10; score+= /ASAP|1 month/.test(t)?30:/3 months/.test(t)?20:5; score+= /1000|201/.test(s)?20:/51/.test(s)?12:5;
    data.lead_score=score; data.lead_grade=score>=70?"A":score>=45?"B":"C";
    next.disabled=true;next.textContent="Matching…";
    try{const how=await submitData("lead",data);
      wz.innerHTML='<div class="center"><div style="font-size:3rem">🎉</div><h3>You\'re matched!</h3><p>'+(how==="mailto"?"Send the pre-filled email that just opened and":"")+' a Cloud.Design architect will review your brief and introduce up to 3 vetted cloud partners within 1 business day.</p><p class="small muted">Reference: CD-'+Date.now().toString(36).toUpperCase()+'</p><a class="btn btn-ghost" href="architectures.html">Browse reference architectures while you wait</a></div>';
    }catch(err){toast("Could not send: "+err.message);next.disabled=false;next.textContent="Try again"}
  });
  show(0);
});

/* ---------- Diagram renderer ---------- */
function diagramSVG(flow,provider){
  const colors={aws:"#ff9900",azure:"#0078d4",gcp:"#34a853",multi:"#7c3aed"},col=colors[provider]||"#3b5bfd";
  const W=760,colW=W/flow.length,H=Math.max(...flow.map(c=>c.length))*74+40;
  let s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Architecture diagram" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="currentColor" opacity=".5"/></marker></defs>';
  const pos=flow.map((c,ci)=>c.map((n,ni)=>{const h=c.length*74;return{x:ci*colW+10,y:(H-h)/2+ni*74+10,w:colW-20,h:54,n}}));
  pos.forEach((c,ci)=>{if(ci===pos.length-1)return;c.forEach(a=>pos[ci+1].forEach(b=>{s+='<path d="M'+(a.x+a.w)+','+(a.y+27)+' C'+(a.x+a.w+18)+','+(a.y+27)+' '+(b.x-18)+','+(b.y+27)+' '+(b.x-2)+','+(b.y+27)+'" fill="none" stroke="currentColor" stroke-opacity=".35" stroke-width="1.5" marker-end="url(#ar)"/>'}))});
  pos.forEach((c,ci)=>c.forEach(b=>{const first=ci===0;
    s+='<rect x="'+b.x+'" y="'+b.y+'" rx="10" width="'+b.w+'" height="'+b.h+'" fill="'+(first?"none":col)+'" fill-opacity="'+(first?0:.12)+'" stroke="'+col+'" stroke-width="1.5"/>';
    const words=b.n.split(" "),lines=[];let cur="";words.forEach(w=>{if((cur+" "+w).trim().length>16){lines.push(cur.trim());cur=w}else cur+=" "+w});lines.push(cur.trim());
    lines.slice(0,3).forEach((l,li)=>{s+='<text x="'+(b.x+b.w/2)+'" y="'+(b.y+27+(li-(Math.min(lines.length,3)-1)/2)*14+4)+'" text-anchor="middle" font-size="11.5" font-weight="600" fill="currentColor">'+esc(l)+'</text>'})}));
  return s+"</svg>";
}
window.cdDiagram=diagramSVG;

/* ---------- Modal helper ---------- */
function openModal(html){let m=$("#cd-modal");if(!m){m=document.createElement("div");m.id="cd-modal";m.className="modal";m.innerHTML='<div class="box" role="dialog" aria-modal="true"><button class="icon-btn x" aria-label="Close">✕</button><div class="mc"></div></div>';document.body.appendChild(m);
  m.addEventListener("click",e=>{if(e.target===m||e.target.closest(".x"))m.classList.remove("open")});document.addEventListener("keydown",e=>{if(e.key==="Escape")m.classList.remove("open")})}
  $(".mc",m).innerHTML=html;$(".box",m).style.maxWidth="860px";m.classList.add("open");return m}

/* ---------- Architecture library ---------- */
const archGrid=$("#arch-grid");
if(archGrid&&D.architectures){
  const q=$("#arch-q"),fp=$("#arch-provider"),fc=$("#arch-cat"),fl=$("#arch-level"),count=$("#arch-count");
  const cats=[...new Set(D.architectures.map(a=>a.category))].sort();
  if(fc) cats.forEach(c=>fc.insertAdjacentHTML("beforeend",'<option>'+esc(c)+'</option>'));
  const params=new URLSearchParams(location.search); if(params.get("q")&&q)q.value=params.get("q"); if(params.get("provider")&&fp)fp.value=params.get("provider");
  const limit=+archGrid.dataset.limit||0;
  function render(){
    const term=(q&&q.value||"").toLowerCase();
    let list=D.architectures.filter(a=>(!fp||!fp.value||a.provider===fp.value)&&(!fc||!fc.value||a.category===fc.value)&&(!fl||!fl.value||a.level===fl.value)&&(!term||(a.title+" "+a.desc+" "+a.category+" "+a.industry+" "+a.flow.flat().join(" ")).toLowerCase().includes(term)));
    if(limit) list=list.slice(0,limit);
    if(count) count.textContent=list.length+" architectures";
    archGrid.innerHTML=list.length?list.map(a=>'<article class="card reveal in"><div class="flex between"><span class="tag '+a.provider+'">'+PROV[a.provider]+'</span><span class="meta">'+esc(a.level)+'</span></div><h3 class="mt1"><a href="#'+a.id+'" data-arch="'+a.id+'">'+esc(a.title)+'</a></h3><p class="small">'+esc(a.desc.slice(0,140))+'…</p><div class="flex between"><span class="meta">💲 '+esc(a.cost)+'</span><button class="btn btn-ghost btn-sm" data-arch="'+a.id+'">View diagram</button></div><div class="tags"><span class="tag">'+esc(a.category)+'</span><span class="tag">'+esc(a.industry)+'</span></div></article>').join(""):'<div class="empty">No matches. <a href="get-matched.html">Ask an architect to design it for you →</a></div>';
  }
  [q,fp,fc,fl].forEach(el=>el&&el.addEventListener("input",render));
  render();
  document.addEventListener("click",e=>{const t=e.target.closest("[data-arch]");if(!t)return;e.preventDefault();showArch(t.dataset.arch)});
  function showArch(id){const a=D.architectures.find(x=>x.id===id);if(!a)return;history.replaceState(null,"","#"+id);track("view_architecture",{id});
    openModal('<span class="tag '+a.provider+'">'+PROV[a.provider]+'</span> <span class="tag">'+esc(a.category)+'</span> <span class="tag">'+esc(a.level)+'</span><h2 class="mt1">'+esc(a.title)+'</h2><p>'+esc(a.desc)+'</p><div class="diagram">'+diagramSVG(a.flow,a.provider)+'</div><div class="grid g2 mt2"><div><h3>✅ Strengths</h3><ul class="list">'+a.pros.map(p=>"<li>"+esc(p)+"</li>").join("")+'</ul></div><div><h3>⚠️ Trade-offs</h3><ul>'+a.cons.map(p=>"<li>"+esc(p)+"</li>").join("")+'</ul></div></div><p><b>Typical monthly cost:</b> '+esc(a.cost)+' · <b>Industry fit:</b> '+esc(a.industry)+'</p><div class="flex mt2"><a class="btn btn-primary" href="get-matched.html?service=architecture&ref='+a.id+'">Get this built by vetted experts →</a><button class="btn btn-ghost" data-dl="'+a.id+'">⬇ Download SVG</button><button class="btn btn-ghost" data-share>🔗 Copy link</button></div><div class="ad-slot" data-ad="inContent"></div>');
  }
  document.addEventListener("click",e=>{
    const d=e.target.closest("[data-dl]");if(d){const a=D.architectures.find(x=>x.id===d.dataset.dl);const svg=diagramSVG(a.flow,a.provider).replace(/currentColor/g,"#0d1224");const url=URL.createObjectURL(new Blob([svg],{type:"image/svg+xml"}));const l=document.createElement("a");l.href=url;l.download=a.id+".svg";l.click();URL.revokeObjectURL(url);track("download_diagram",{id:a.id})}
    if(e.target.closest("[data-share]")){navigator.clipboard&&navigator.clipboard.writeText(location.href).then(()=>toast("Link copied"))}
  });
  if(location.hash&&D.architectures.some(a=>"#"+a.id===location.hash)) showArch(location.hash.slice(1));
}

/* ---------- Patterns ---------- */
const patGrid=$("#pattern-grid");
if(patGrid&&D.patterns){const cats=["All",...new Set(D.patterns.map(p=>p.cat))];const bar=$("#pattern-cats");let cur="All";
  function r(){patGrid.innerHTML=D.patterns.filter(p=>cur==="All"||p.cat===cur).map(p=>'<article class="card"><span class="tag">'+esc(p.cat)+'</span><h3 class="mt1">'+esc(p.name)+'</h3><p class="small"><b>Problem:</b> '+esc(p.problem)+'</p><p class="small mb0"><b>Solution:</b> '+esc(p.solution)+'</p></article>').join("")}
  if(bar){bar.innerHTML=cats.map(c=>'<button class="pill'+(c==="All"?" active":"")+'" data-c="'+esc(c)+'">'+esc(c)+'</button>').join("");bar.addEventListener("click",e=>{const b=e.target.closest(".pill");if(!b)return;cur=b.dataset.c;$$(".pill",bar).forEach(x=>x.classList.toggle("active",x===b));r()})}
  r();}

/* ---------- Tools directory ---------- */
const toolGrid=$("#tool-grid");
if(toolGrid&&D.tools){const cats=["All",...new Set(D.tools.map(t=>t.cat))];const bar=$("#tool-cats"),q=$("#tool-q");let cur="All";
  function r(){const term=(q&&q.value||"").toLowerCase();const list=D.tools.filter(t=>(cur==="All"||t.cat===cur)&&(!term||(t.name+t.desc+t.cat).toLowerCase().includes(term)));
    toolGrid.innerHTML=list.map(t=>'<article class="card"><div class="flex between"><span class="tag">'+esc(t.cat)+'</span><span class="badge">'+esc(t.price)+'</span></div><h3 class="mt1">'+esc(t.name)+'</h3><p class="small">'+esc(t.desc)+'</p><a class="btn btn-ghost btn-sm" href="'+esc(t.url)+'" target="_blank" rel="noopener sponsored" data-out="'+esc(t.name)+'">Visit site ↗</a></article>').join("")||'<div class="empty">No tools found.</div>'}
  if(bar){bar.innerHTML=cats.map(c=>'<button class="pill'+(c==="All"?" active":"")+'" data-c="'+esc(c)+'">'+esc(c)+'</button>').join("");bar.addEventListener("click",e=>{const b=e.target.closest(".pill");if(!b)return;cur=b.dataset.c;$$(".pill",bar).forEach(x=>x.classList.toggle("active",x===b));r()})}
  q&&q.addEventListener("input",r);r();
  toolGrid.addEventListener("click",e=>{const a=e.target.closest("[data-out]");if(a)track("outbound_tool",{tool:a.dataset.out})});}

/* ---------- Instance comparison table ---------- */
const it=$("#instance-table");
if(it&&D.instances){const tb=$("tbody",it),fp=$("#inst-provider"),fcl=$("#inst-class"),fm=$("#inst-mode"),fq=$("#inst-q");let sortK=4,asc=true;
  const classes=[...new Set(D.instances.map(r=>r[5]))];classes.forEach(c=>fcl&&fcl.insertAdjacentHTML("beforeend","<option>"+esc(c)+"</option>"));
  function r(){const mode=fm?fm.value:"hour",mult={hour:1,month:730,year:8760}[mode];const q=(fq&&fq.value||"").toLowerCase();
    let rows=D.instances.filter(x=>(!fp.value||x[0]===fp.value)&&(!fcl.value||x[5]===fcl.value)&&(!q||x[1].toLowerCase().includes(q)));
    rows.sort((a,b)=>(a[sortK]>b[sortK]?1:a[sortK]<b[sortK]?-1:0)*(asc?1:-1));
    tb.innerHTML=rows.map(x=>'<tr><td><span class="tag '+(x[0]==="AWS"?"aws":x[0]==="Azure"?"azure":"gcp")+'">'+x[0]+'</span></td><td><code>'+esc(x[1])+'</code></td><td>'+x[2]+'</td><td>'+x[3]+' GiB</td><td><b>'+money(x[4]*mult,mode==="hour"?4:0)+'</b></td><td>'+money(x[4]/x[2]*730,2)+'</td><td>'+esc(x[5])+'</td></tr>').join("");
    const u=$("#inst-unit");if(u)u.textContent={hour:"/ hour",month:"/ month",year:"/ year"}[mode]}
  [fp,fcl,fm,fq].forEach(e=>e&&e.addEventListener("input",r));
  $$("th[data-k]",it).forEach(th=>th.addEventListener("click",()=>{const k=+th.dataset.k;asc=sortK===k?!asc:true;sortK=k;r()}));
  const ex=$("#inst-export");ex&&ex.addEventListener("click",()=>{const csv="Provider,Instance,vCPU,Memory GiB,USD/hour,Class\n"+D.instances.map(x=>x.join(",")).join("\n");const l=document.createElement("a");l.href=URL.createObjectURL(new Blob([csv],{type:"text/csv"}));l.download="cloud-instance-prices.csv";l.click();track("export_csv")});
  r();}

/* ---------- Multi-cloud cost estimator ---------- */
const est=$("#estimator");
if(est){const P={AWS:{vcpu:0.0504,gb:0.0063,storage:0.08,obj:0.023,egress:0.09,db:0.145,lb:18},Azure:{vcpu:0.048,gb:0.006,storage:0.075,obj:0.0208,egress:0.087,db:0.155,lb:18.25},GCP:{vcpu:0.0475,gb:0.0064,storage:0.08,obj:0.020,egress:0.12,db:0.139,lb:18.26}};
  function calc(){const v=n=>+($("[name="+n+"]",est).value||0);const vms=v("vms"),cpu=v("cpu"),ram=v("ram"),disk=v("disk"),obj=v("obj"),eg=v("egress"),db=v("db"),lbs=v("lbs"),disc=v("commit");
    const out=Object.entries(P).map(([k,p])=>{const compute=vms*(cpu*p.vcpu+ram*p.gb)*730*(1-disc/100);const storage=disk*vms*p.storage+obj*p.obj;const net=Math.max(0,eg-100)*p.egress+lbs*p.lb;const data=db*p.db*730*(1-disc/100);return{k,compute,storage,net,data,total:compute+storage+net+data}});
    const min=Math.min(...out.map(o=>o.total));
    $("#est-out").innerHTML=out.map(o=>'<div class="card'+(o.total===min?" featured":"")+'"><div class="flex between"><h3 class="mb0">'+o.k+'</h3>'+(o.total===min?'<span class="badge">Lowest</span>':'')+'</div><div class="price mt1">'+money(o.total)+'<small>/mo</small></div><p class="small mb0">Compute '+money(o.compute)+' · Storage '+money(o.storage)+'<br>Network '+money(o.net)+' · Database '+money(o.data)+'</p><p class="small muted mb0">≈ '+money(o.total*12)+' per year</p></div>').join("");
    est._last=out;}
  $$("input,select",est).forEach(i=>i.addEventListener("input",calc));calc();}

/* ---------- Migration savings calculator ---------- */
const mig=$("#migration-calc");
if(mig){function c(){const v=n=>+($("[name="+n+"]",mig).value||0);const servers=v("servers"),hw=v("hw"),dc=v("dc"),staff=v("staff"),lic=v("lic");
    const onprem=servers*hw/36+dc+staff+lic; const cloud=onprem*(1-(0.31+Math.min(servers,500)/500*0.1)); const save=onprem-cloud;
    $("#mig-out").innerHTML='<div class="grid g3"><div class="stat card"><b>'+money(onprem)+'</b><span class="small">Current monthly TCO</span></div><div class="stat card"><b>'+money(cloud)+'</b><span class="small">Projected cloud cost</span></div><div class="stat card"><b>'+money(save*36)+'</b><span class="small">3-year savings</span></div></div><p class="small muted mt1">Model assumes 31–41% TCO reduction (rightsizing + managed services), a typical range in published migration studies. Your real number depends on architecture — get a free assessment below.</p>'}
  $$("input",mig).forEach(i=>i.addEventListener("input",c));c();}

/* ---------- Well-Architected quiz ---------- */
const quiz=$("#wa-quiz");
if(quiz){const Qs=[
 ["Operational Excellence","Is all infrastructure defined as code and deployed via CI/CD?"],["Operational Excellence","Do you run post-incident reviews and track action items?"],
 ["Security","Is MFA enforced and are long-lived access keys eliminated?"],["Security","Is data encrypted at rest and in transit by default?"],
 ["Reliability","Do production workloads span at least two availability zones?"],["Reliability","Have you tested a backup restore in the last 90 days?"],
 ["Performance Efficiency","Do you load-test before major releases?"],["Performance Efficiency","Do you use caching/CDN for read-heavy paths?"],
 ["Cost Optimization","Are ≥ 90% of resources tagged with owner and cost center?"],["Cost Optimization","Do you use Savings Plans/Reserved or Spot capacity?"],
 ["Sustainability","Do you scale non-production environments down outside business hours?"],["Sustainability","Do you prefer ARM/efficient instance families where possible?"]];
  let i=0;const ans=[];const box=$("#quiz-box"),bar=$("#quiz-bar");
  function q(){if(i>=Qs.length)return done();const [p,t]=Qs[i];bar.style.width=(i/Qs.length*100)+"%";
    box.innerHTML='<p class="small muted">Question '+(i+1)+' of '+Qs.length+' · <b>'+p+'</b></p><h3>'+t+'</h3><div class="choices"><label class="choice"><input type="radio" name="qa" value="2"><span>✅ Yes, fully</span></label><label class="choice"><input type="radio" name="qa" value="1"><span>🟡 Partially</span></label><label class="choice"><input type="radio" name="qa" value="0"><span>❌ No</span></label><label class="choice"><input type="radio" name="qa" value="0"><span>🤷 Not sure</span></label></div>';
    $$("input",box).forEach(r=>r.addEventListener("change",()=>{ans.push([p,+r.value]);i++;setTimeout(q,180)}))}
  function done(){bar.style.width="100%";const tot=ans.reduce((s,a)=>s+a[1],0),pct=Math.round(tot/(Qs.length*2)*100);const pillars={};ans.forEach(([p,v])=>{pillars[p]=(pillars[p]||0)+v});
    const col=pct>=75?"var(--ok)":pct>=45?"var(--warn)":"var(--bad)";track("quiz_complete",{score:pct});
    box.innerHTML='<div class="score-ring" style="background:conic-gradient('+col+' '+pct*3.6+'deg,var(--bg-3) 0)"><span style="background:var(--bg-2);width:128px;height:128px;border-radius:50%;display:grid;place-items:center">'+pct+'%</span></div><h3 class="center">Your Well-Architected score: '+(pct>=75?"Strong":pct>=45?"At risk":"Critical gaps")+'</h3><div class="grid g3 mt1">'+Object.entries(pillars).map(([p,v])=>'<div class="card"><b>'+p+'</b><div class="meter mt1"><span style="width:'+v/4*100+'%"></span></div></div>').join("")+'</div><div class="card mt2"><h3>📩 Get your full 20-page remediation report</h3><p class="small">Prioritized fixes per pillar, estimated savings and a 90-day roadmap — free.</p><form class="form" data-form="lead" data-success="Report requested! Check your inbox within 1 business day." id="quiz-form"><input type="hidden" name="source" value="well-architected-quiz"><input type="hidden" name="quiz_score" value="'+pct+'"><div class="row2"><div class="field"><label>Work email</label><input type="email" name="email" required></div><div class="field"><label>Company</label><input type="text" name="company" required></div></div><label class="check"><input type="checkbox" name="consult" value="yes" checked> Also book a free 30-min review with a certified architect</label><button class="btn btn-primary" type="submit">Send my report →</button></form></div>';
    const f=$("#quiz-form");f.addEventListener("submit",async e=>{e.preventDefault();if(!f.checkValidity())return f.reportValidity();try{await submitData("lead",formToObj(f));msg(f,true,f.dataset.success)}catch(err){msg(f,false,err.message)}})}
  q();}

/* ---------- Glossary ---------- */
const gl=$("#glossary");
if(gl&&D.glossary){const q=$("#gl-q"),az=$("#gl-az");const items=[...D.glossary].sort((a,b)=>a[0].localeCompare(b[0]));
  const letters=[...new Set(items.map(i=>i[0][0].toUpperCase()))];if(az)az.innerHTML=letters.map(l=>'<a class="pill" href="#gl-'+l+'">'+l+'</a>').join("");
  function r(){const t=(q&&q.value||"").toLowerCase();let last="";gl.innerHTML=items.filter(i=>!t||(i[0]+i[1]).toLowerCase().includes(t)).map(i=>{const L=i[0][0].toUpperCase();const h=L!==last?'<h3 id="gl-'+L+'" class="mt2">'+L+'</h3>':"";last=L;return h+'<details><summary>'+esc(i[0])+'</summary><div>'+esc(i[1])+'</div></details>'}).join("")}
  q&&q.addEventListener("input",r);r();}

/* ---------- Videos (lite facade = fast pages) ---------- */
const vg=$("#video-grid");
if(vg&&D.videos){const lim=+vg.dataset.limit||D.videos.length;vg.innerHTML=D.videos.slice(0,lim).map(v=>'<article><div class="video" data-yt="'+esc(v.id)+'" role="button" tabindex="0" aria-label="Play: '+esc(v.title)+'"><img loading="lazy" src="https://i.ytimg.com/vi/'+esc(v.id)+'/hqdefault.jpg" alt=""><div class="play"><span>▶</span></div></div><h3 class="mt1" style="font-size:1rem">'+esc(v.title)+'</h3><span class="tag">'+esc(v.cat)+'</span></article>').join("")}
function playYT(el){el.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+el.dataset.yt+'?autoplay=1&rel=0" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';track("video_play",{id:el.dataset.yt})}
document.addEventListener("click",e=>{const v=e.target.closest("[data-yt]");if(v&&!$("iframe",v))playYT(v)});
document.addEventListener("keydown",e=>{const v=e.target.closest&&e.target.closest("[data-yt]");if(v&&(e.key==="Enter"||e.key===" ")){e.preventDefault();playYT(v)}});

/* ---------- Guides ---------- */
const gg=$("#guide-grid");
if(gg&&D.guides){const lim=+gg.dataset.limit||D.guides.length;gg.innerHTML=D.guides.slice(0,lim).map(g=>'<article class="card"><span class="tag">'+esc(g.cat)+'</span><h3 class="mt1"><a href="guides/'+g.slug+'.html">'+esc(g.title)+'</a></h3><p class="small">'+esc(g.excerpt)+'</p><span class="meta">⏱ '+g.mins+' min read</span></article>').join("")}

/* ---------- Donations ---------- */
const don=$("#donate");
if(don){const dn=C.donate||{};let amt=25,monthly=false;
  $$(".tier",don).forEach(t=>t.addEventListener("click",()=>{$$(".tier",don).forEach(x=>x.classList.remove("active"));t.classList.add("active");amt=+t.dataset.amt;const c=$("#don-custom");if(c)c.value=""}));
  const cu=$("#don-custom");cu&&cu.addEventListener("input",()=>{amt=+cu.value||0;$$(".tier",don).forEach(x=>x.classList.remove("active"))});
  $$("[name=freq]",don).forEach(r=>r.addEventListener("change",()=>monthly=r.value==="monthly"));
  const links={githubSponsors:"GitHub Sponsors",stripe:"Card (Stripe)",paypal:"PayPal",buyMeACoffee:"Buy Me a Coffee",kofi:"Ko-fi",patreon:"Patreon"};
  const wrap=$("#don-methods");
  if(wrap){wrap.innerHTML=Object.entries(links).filter(([k])=>dn[k]).map(([k,l])=>'<button class="btn '+(k==="stripe"||k==="githubSponsors"?"btn-primary":"btn-ghost")+'" data-pay="'+k+'">'+l+'</button>').join("")+(dn.crypto?'<button class="btn btn-ghost" data-crypto>Crypto</button>':"");
    if(!wrap.innerHTML) wrap.innerHTML='<p class="small muted">Payment links are being set up — use the pledge form below and we\'ll email you a secure payment link.</p>';
    wrap.addEventListener("click",e=>{const b=e.target.closest("[data-pay]");if(b){let u=dn[b.dataset.pay];if(b.dataset.pay==="paypal"&&amt)u=u.replace(/\/$/,"")+"/"+amt;if(b.dataset.pay==="stripe"&&amt)u+=(u.includes("?")?"&":"?")+"__prefilled_amount="+amt*100;track("donate_click",{method:b.dataset.pay,amount:amt,monthly});window.open(u,"_blank","noopener")}
      if(e.target.closest("[data-crypto]")){navigator.clipboard&&navigator.clipboard.writeText(dn.crypto);toast("Wallet address copied")}})}
  const fg=C.fundGoal||{};const m=$("#fund-meter");if(m&&fg.goal){const p=Math.min(100,fg.raised/fg.goal*100);m.innerHTML='<div class="flex between small"><b>'+money(fg.raised)+' raised</b><span>Goal '+money(fg.goal)+'</span></div><div class="meter mt1"><span style="width:'+Math.max(p,2)+'%"></span></div><p class="small muted mt1">'+esc(fg.label||"")+'</p>'}}

/* ---------- Countdown ---------- */
$$("[data-countdown]").forEach(el=>{const end=new Date(el.dataset.countdown||(C.contest||{}).endsAt).getTime();
  function t(){let d=Math.max(0,end-Date.now());const u=[86400000,3600000,60000,1000].map(x=>{const v=Math.floor(d/x);d-=v*x;return v});
    el.innerHTML=["Days","Hours","Mins","Secs"].map((l,i)=>'<div><b>'+String(u[i]).padStart(2,"0")+'</b><small>'+l+'</small></div>').join("")}t();setInterval(t,1000)});

/* ---------- Hero search ---------- */
$$("form[data-search]").forEach(f=>f.addEventListener("submit",e=>{e.preventDefault();const q=$("input",f).value.trim();location.href="architectures.html"+(q?"?q="+encodeURIComponent(q):"")}));

/* ---------- Exit-intent + sticky CTA ---------- */
const exitM=$("#exit-modal");
if(exitM&&!store.get("subscribed",false)&&!sessionStorageSafe("exit")){
  const fire=()=>{if(sessionStorageSafe("exit"))return;sessionStorageSafe("exit",1);exitM.classList.add("open");track("exit_intent_shown")};
  document.addEventListener("mouseout",e=>{if(!e.relatedTarget&&e.clientY<8)fire()});
  setTimeout(()=>{if(window.scrollY>1400)fire()},45000);
  exitM.addEventListener("click",e=>{if(e.target===exitM||e.target.closest(".x"))exitM.classList.remove("open")});}
function sessionStorageSafe(k,v){try{if(v!==undefined){sessionStorage.setItem("cd_"+k,v);return v}return sessionStorage.getItem("cd_"+k)}catch(e){return null}}
const sc=$(".sticky-cta");if(sc&&!/get-matched/.test(here)){window.addEventListener("scroll",()=>sc.classList.toggle("show",window.scrollY>900),{passive:true})}

/* ---------- Share buttons ---------- */
$$("[data-share-to]").forEach(a=>{const u=encodeURIComponent(location.href),t=encodeURIComponent(document.title);const m={x:"https://x.com/intent/tweet?url="+u+"&text="+t,linkedin:"https://www.linkedin.com/sharing/share-offsite/?url="+u,reddit:"https://www.reddit.com/submit?url="+u+"&title="+t,email:"mailto:?subject="+t+"&body="+u};a.href=m[a.dataset.shareTo];a.target="_blank";a.rel="noopener"});

/* ---------- Social links from config ---------- */
$$("[data-social]").forEach(a=>{const u=(C.social||{})[a.dataset.social];if(u)a.href=u;else a.remove()});
$$("[data-email]").forEach(a=>{a.href="mailto:"+C.contactEmail;a.textContent=C.contactEmail});
})();
