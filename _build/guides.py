"""Long-form guide content. Each guide becomes /guides/<slug>.html.
Keep slugs in sync with CD_DATA.guides in assets/js/data.js."""

GUIDES = [
{"slug": "cloud-migration-checklist", "title": "The 2026 Cloud Migration Checklist (47 steps)", "cat": "Migration", "mins": 14, "service": "migration",
 "excerpt": "Discovery, TCO, wave planning, cutover and hypercare — the exact checklist consultancies charge for.",
 "html": """
<p>Most failed migrations don't fail on migration day. They fail during discovery, when nobody finds the hard-coded IP in a batch job or the licence that can't move to shared tenancy. This checklist is ordered to find those problems early.</p>
<h2>Phase 1 — Discovery &amp; business case (steps 1–12)</h2>
<ol><li>Define measurable goals: exit a data center by a date, cut TCO by X%, improve release frequency.</li><li>Nominate an executive sponsor and a single accountable migration lead.</li><li>Run automated discovery (agent or agentless) for at least 2–4 weeks to capture peak utilization.</li><li>Build an application inventory: owner, criticality, RTO/RPO, data classification.</li><li>Map dependencies — network flows, shared databases, file shares, batch schedules.</li><li>Audit licences (Windows, SQL Server, Oracle) for cloud portability and BYOL eligibility.</li><li>Capture compliance scope: PCI, HIPAA, SOC 2, GDPR data residency.</li><li>Baseline current costs: hardware depreciation, facilities, power, staff, support contracts.</li><li>Build a TCO model with right-sized cloud targets (not 1:1 VM sizes).</li><li>Assign one of the 7 Rs to each application: retire, retain, rehost, relocate, repurchase, replatform, refactor.</li><li>Identify quick wins (low complexity, low risk) for the first wave.</li><li>Secure funding — check provider migration-incentive programs.</li></ol>
<h2>Phase 2 — Foundation (steps 13–24)</h2>
<ol start="13"><li>Design the landing zone: account/subscription hierarchy, guardrails, SSO.</li><li>Design networking: IP plan without overlaps, hub-and-spoke or transit, hybrid connectivity (VPN/Direct Connect/ExpressRoute).</li><li>Set up centralized logging, audit trails and security tooling.</li><li>Define a tagging standard (owner, cost center, environment, application) and enforce it with policy.</li><li>Establish IaC repositories and CI/CD pipelines.</li><li>Configure backup and DR policies per criticality tier.</li><li>Set budgets, anomaly alerts and cost dashboards from day one.</li><li>Define identity federation and least-privilege roles.</li><li>Harden base images and patching workflows.</li><li>Document the shared responsibility model for your team.</li><li>Train the operations team on the target platform.</li><li>Run a pilot migration of a non-critical app end-to-end.</li></ol>
<h2>Phase 3 — Migration waves (steps 25–38)</h2>
<ol start="25"><li>Group apps into waves by dependency, not by department.</li><li>Agree change windows and communication plans per wave.</li><li>Replicate data continuously to shorten cutover.</li><li>Lower DNS TTLs 48 hours before cutover.</li><li>Write a runbook with named owners and a go/no-go checklist.</li><li>Define rollback criteria and test rollback.</li><li>Run performance and load tests on the target environment.</li><li>Validate security controls and vulnerability scans.</li><li>Execute cutover; freeze writes on source.</li><li>Run smoke tests and business validation.</li><li>Switch DNS / traffic.</li><li>Monitor error rates, latency and cost for 72 hours.</li><li>Close the wave with a retrospective.</li><li>Update the CMDB and architecture diagrams.</li></ol>
<h2>Phase 4 — Optimize &amp; hypercare (steps 39–47)</h2>
<ol start="39"><li>Rightsize after 2–4 weeks of real utilization data.</li><li>Purchase commitments (Savings Plans / Reservations) for steady state.</li><li>Move eligible workloads to spot or ARM instances.</li><li>Tier storage and set lifecycle policies.</li><li>Decommission source hardware and cancel contracts.</li><li>Review egress paths and add caching/CDN.</li><li>Run a Well-Architected review.</li><li>Report achieved savings against the business case.</li><li>Plan the modernization roadmap (replatform/refactor candidates).</li></ol>
<h2>Where teams go wrong</h2><p>The expensive mistakes are 1:1 sizing, which carries on-prem over-provisioning into the cloud; skipping the tagging standard; and leaving the cost model until after cutover. Fix those three and most of the business case holds.</p>
"""},
{"slug": "reduce-cloud-bill", "title": "17 Proven Ways to Cut Your Cloud Bill by 30%+", "cat": "Cost", "mins": 11, "service": "cost",
 "excerpt": "Rightsizing, commitments, spot, storage tiering, egress and the tagging discipline that makes it stick.",
 "html": """
<p>Industry surveys such as Flexera's <em>State of the Cloud</em> keep finding that organizations believe roughly a quarter to a third of their cloud spend is wasted. The levers below are ordered roughly by effort-to-impact ratio.</p>
<h2>Quick wins (week 1)</h2><ol><li><b>Delete idle resources</b> — unattached volumes, old snapshots, idle load balancers, unused elastic IPs.</li><li><b>Schedule non-production</b> — shutting dev/test down nights and weekends cuts their compute cost by ~65%.</li><li><b>Rightsize</b> — instances averaging under 20% CPU are candidates to go one or two sizes down.</li><li><b>Move to current-generation instances</b> — newer families usually deliver better price-performance.</li><li><b>Adopt ARM</b> — Graviton, Cobalt and Axion-class instances are typically cheaper per unit of performance for compatible workloads.</li></ol>
<h2>Commitments (month 1)</h2><ol start="6"><li><b>Savings Plans / Reservations</b> for your steady-state baseline — commit to roughly the floor of usage, not the average.</li><li><b>Spot / preemptible</b> for stateless, fault-tolerant, batch and CI workloads.</li><li><b>Database reservations</b> — often forgotten, often large.</li></ol>
<h2>Storage &amp; data (month 1–2)</h2><ol start="9"><li><b>Lifecycle policies</b> to infrequent-access and archive tiers.</li><li><b>Intelligent tiering</b> where access patterns are unknown.</li><li><b>Compress and deduplicate logs</b>; cut retention to what compliance requires.</li><li><b>Reduce egress</b> with CDNs, regional affinity and private connectivity.</li><li><b>Watch NAT gateway data processing</b> — use VPC endpoints for object storage traffic.</li></ol>
<h2>Architecture (quarter 1)</h2><ol start="14"><li><b>Go serverless for spiky, low-duty-cycle workloads.</b></li><li><b>Autoscale on real metrics</b> rather than static peak capacity.</li><li><b>Cache aggressively</b> to shrink database tiers.</li></ol>
<h2>Make it stick</h2><ol start="17"><li><b>Tag everything and show teams their own spend.</b> Unit economics (cost per customer, per transaction) turn cost from a finance problem into an engineering metric.</li></ol>
<p>Try our <a href="../tools.html#estimator">multi-cloud estimator</a> to model commitment discounts, or get a <a href="../get-matched.html?service=cost">free cost review</a>.</p>
"""},
{"slug": "aws-vs-azure-vs-gcp", "title": "AWS vs Azure vs Google Cloud: An Architect's Comparison", "cat": "Comparison", "mins": 16, "service": "architecture",
 "excerpt": "Service parity, pricing models, networking, AI stacks and enterprise fit — decided by workload.",
 "html": """
<p>All three hyperscalers can run almost any workload. The real question is which one fits <em>your</em> workload, team and commercial situation best.</p>
<h2>At a glance</h2>
<div class="table-wrap"><table><thead><tr><th></th><th>AWS</th><th>Azure</th><th>Google Cloud</th></tr></thead><tbody>
<tr><td>Strength</td><td>Breadth &amp; maturity of services</td><td>Microsoft ecosystem &amp; enterprise identity</td><td>Data, analytics, Kubernetes, global network</td></tr>
<tr><td>Compute</td><td>EC2, Lambda, ECS/EKS, Fargate</td><td>VMs, Functions, AKS, Container Apps</td><td>Compute Engine, Cloud Run, GKE</td></tr>
<tr><td>Data warehouse</td><td>Redshift</td><td>Synapse / Fabric</td><td>BigQuery</td></tr>
<tr><td>Identity</td><td>IAM + Identity Center</td><td>Entra ID</td><td>Cloud IAM + Identity Platform</td></tr>
<tr><td>Commitments</td><td>Savings Plans, RIs</td><td>Reservations, Savings Plan</td><td>Committed + sustained use discounts</td></tr>
<tr><td>Best fit</td><td>Cloud-native startups, broad enterprise</td><td>Windows/.NET, M365 shops, hybrid</td><td>Data/ML-heavy, container-first teams</td></tr>
</tbody></table></div>
<h2>How to decide</h2><ol><li><b>Team skills.</b> Retraining is a real cost; the cloud your team already knows usually wins close calls.</li><li><b>Existing licences and agreements.</b> Microsoft licensing benefits can swing Windows/SQL Server economics toward Azure.</li><li><b>Data gravity.</b> Keep compute where the largest datasets live — egress is expensive.</li><li><b>Managed-service fit.</b> Map your top five workloads to specific services on each cloud.</li><li><b>Commercial leverage.</b> Enterprise discounts and migration credits can outweigh list-price differences.</li></ol>
<h2>Multi-cloud?</h2><p>Deliberate multi-cloud (a specific workload on the best cloud for it) works. Accidental multi-cloud — the same app spread thin for "portability" — usually doubles operational cost. Choose a primary cloud; add others for a clear reason.</p>
<p>Compare actual prices with our <a href="../tools.html#instances">instance price index</a>.</p>
"""},
{"slug": "serverless-vs-containers", "title": "Serverless vs Containers: A Decision Framework", "cat": "Architecture", "mins": 9, "service": "architecture",
 "excerpt": "Traffic shape, latency budgets, team skills and cost curves — when each one wins.",
 "html": """
<p>Serverless and containers aren't rivals so much as points on a spectrum of control versus convenience. Use these five questions.</p>
<h2>1. What does your traffic look like?</h2><p>Spiky or low duty-cycle traffic (webhooks, internal tools, scheduled jobs) favors functions that scale to zero. High, steady throughput favors containers on reserved or spot capacity, where per-request pricing becomes more expensive than always-on compute.</p>
<h2>2. What is your latency budget?</h2><p>Cold starts can add hundreds of milliseconds to seconds, depending on runtime and package size. Provisioned concurrency mitigates this at a cost. Containers keep warm processes.</p>
<h2>3. How long do requests run?</h2><p>Function platforms cap execution time. Long-running jobs, streaming connections and heavy CPU/GPU work belong in containers.</p>
<h2>4. How portable must you be?</h2><p>Containers on Kubernetes move between clouds more easily. Serverless apps tie into provider event sources and IAM.</p>
<h2>5. What can your team operate?</h2><p>Kubernetes needs platform-engineering maturity. A small team with no ops capacity ships faster on serverless or on serverless containers (Cloud Run, Fargate, Azure Container Apps), which combine container portability with scale-to-zero convenience.</p>
<h2>The pragmatic default</h2><p>Start with serverless containers for APIs, functions for event glue, and graduate to Kubernetes only when you have multiple teams, complex networking or cost pressure at scale.</p>
"""},
{"slug": "well-architected-review", "title": "How to Run a Well-Architected Review in One Day", "cat": "Governance", "mins": 8, "service": "architecture",
 "excerpt": "The six pillars, the questions that matter and how to turn findings into a prioritized backlog.",
 "html": """
<p>A Well-Architected review is a structured conversation that turns vague unease into a ranked backlog of risks. Here's a one-day format that works.</p>
<h2>Before the day</h2><ul><li>Pick one workload — not the whole estate.</li><li>Gather the current architecture diagram, cost report and the last three incidents.</li><li>Invite the tech lead, an ops/SRE engineer, a security representative and a product owner.</li></ul>
<h2>Morning — walk the pillars (3 hours)</h2><ul><li><b>Operational excellence:</b> IaC coverage, deployment safety, runbooks, post-incident reviews.</li><li><b>Security:</b> identity, detective controls, data protection, incident response.</li><li><b>Reliability:</b> multi-AZ, backups tested, quotas, failure-mode testing.</li><li><b>Performance efficiency:</b> right resource types, caching, load testing.</li><li><b>Cost optimization:</b> tagging, commitments, rightsizing, unit economics.</li><li><b>Sustainability:</b> utilization, efficient instance families, data lifecycle.</li></ul>
<h2>Afternoon — prioritize (2 hours)</h2><p>Rate each finding as high or medium risk. Score by impact × likelihood ÷ effort. Keep the top 10 and write each one as a ticket with an owner and a date.</p>
<h2>After</h2><p>Re-run the review every six months or after a major change. Want a baseline first? Take our <a href="../tools.html#quiz">2-minute Well-Architected score</a>.</p>
"""},
{"slug": "genai-architecture", "title": "Designing Production-Grade GenAI (RAG) Systems", "cat": "AI & ML", "mins": 13, "service": "ai",
 "excerpt": "Chunking, embeddings, vector stores, guardrails, evals and cost control for LLM apps.",
 "html": """
<p>A demo RAG app takes an afternoon. A production one takes careful architecture. Here are the components and the decisions that matter.</p>
<h2>1. Ingestion</h2><p>Parse documents into clean text, keeping structure (headings, tables). Chunk by semantic boundaries with modest overlap, and store metadata (source, date, access control) with each chunk.</p>
<h2>2. Embeddings &amp; vector store</h2><p>Choose an embedding model for domain fit and cost. Vector options range from managed search services and PostgreSQL with pgvector to dedicated vector databases. Hybrid search (keyword + vector) with re-ranking usually beats pure vector search.</p>
<h2>3. Orchestration</h2><p>Put a stateless API between users and the model: authentication, tenant isolation, prompt templates, retrieval, tool calls and response streaming. Enforce document-level permissions at retrieval time — never rely on the model to hide data.</p>
<h2>4. Guardrails</h2><p>Validate inputs for prompt injection, filter outputs, cite sources, and fall back gracefully when retrieval confidence is low.</p>
<h2>5. Evaluation</h2><p>Build a golden question set. Measure retrieval recall, answer faithfulness and helpfulness on every change to prompts, chunking or models. Log traces for offline review.</p>
<h2>6. Cost control</h2><ul><li>Cache frequent answers and embeddings.</li><li>Route easy queries to smaller, cheaper models.</li><li>Cap context size; retrieve fewer, better chunks.</li><li>Track cost per conversation as a first-class metric.</li></ul>
<p>See the <a href="../architectures.html#rag-genai">GenAI RAG reference architecture</a> or <a href="../get-matched.html?service=ai">get matched with an AI platform partner</a>.</p>
"""},
]
