# Origin (Artila Robotics, Inc.): OG-1 interior-construction robot

[← Back to master document](../COMPETITOR_INTELLIGENCE.md) · [Sources](../SOURCES.md) · **Last updated:** 2026-10-23

Tags: `[V]` verified · `[3P]` third-party · `[CC]` company claim · `[INF]` inferred · `[UNV]` unverified · `[CONFLICT]` · `[INT]` internal observation / opinion from our team.

**Threat level:** ⚪ **Adjacent (different job, same robot).** Origin does drywall finishing, not restrooms. Its architecture is the closest analogue in the KB to a restroom mobile manipulator: wheeled base + tall arm + **swappable tool station** + learned policy + teleop + **per-pass quality grading**. Relevant as (1) a template for how a well-funded team builds this stack, (2) a **talent competitor in Bengaluru**, and (3) a possible future entrant: its pitch is "**One Robot. Any Trade.**" `[INF]`

<img src="screenshots/2026-10-23_og1-youtube-drywall-workflow_1m45s.jpg" width="640">

*OG-1 sanding a drywall seam (Origin YouTube video "Origin OG1 | Inside a Full Drywall Finishing Workflow with an Autonomous Robot", frame at 1:45 of 2:15; screenshot from Vishal) `[V][S107]`.*

## Snapshot

| | |
|---|---|
| **Brand / legal entity** | **Origin** (origin.tech); legal entity **Artila Robotics, Inc.** (site footer) `[V][S105]`, Delaware per AI summary `[UNV][S109]`. Indian subsidiary **"Artila Robotics Private Limited"** (Bengaluru, inc. Nov 2024) claimed `[UNV][S109]`: not found in a web search; check MCA / Tofler. Job board uses the slug "origin-10x" `[3P][S110]` |
| **HQ** | **San Francisco** `[3P][S106]`; team in **San Francisco · New York · Bengaluru** (careers page) `[V][S105]`. One aggregator lists Cambridge, Maryland `[CONFLICT][S106]` |
| **Founded** | **Dec 2024** (company timeline: "Started in Dec 2024") `[CC][S105]`; press says "early 2025" `[3P][S106]` |
| **Founders** | **Yogesh Ghaturle** (CEO; ex-co-founder **Perpule**, acquired by Amazon 2021), **Tushar Makkar** (CTO; ex-**Eightfold AI**), **Ashish Daga** (hardware; ex-**Morphle Labs**) `[3P][S106][S110]` |
| **Market** | Interior construction. First application: **drywall finishing**: joint compound (L4/L5), sanding (L4/L5), priming `[CC][S105]` |
| **Customers** | "Two of the largest drywall finishing contractors in the US" (unnamed); pilots planned in **Germany, Sweden, France, Saudi Arabia** `[3P][S106]` |
| **Traction claims** | **100k+ sq ft completed; 5,000 hours worked**; "5× time saved", "300% margin expansion", "20% cost reduction" `[CC][S105]`; "3× faster than humans" (Forbes headline, company claim; not independently confirmed) `[3P][S106]` |
| **Target** | **150 robots deployed by end-2027** `[3P][S106]` |
| **Website** | https://origin.tech/ · sales@origin.tech · LinkedIn, X, YouTube linked from site |
| **Folder** | [origin-artila/](./) |

## Funding

| Date | Round | Amount | Investors | Source |
|---|---|---|---|---|
| Jan 2025 | First raise ("Fundraising and HQ Opening") | Not disclosed | — | `[CC][S105]` |
| **15 Oct 2026** (announced, emerged from stealth) | Total to date; labelled **seed** by Fundz and a job board, "Series A" by one aggregator `[CONFLICT]` | **US$20M total** | **Accel** and **Zacua Ventures** (co-leads); **Unilazer Ventures** (Ronnie Screwvala's fund, India `[INF]`), Schema Ventures, Z21; angels from **Anduril, Skild AI, 1X, Tesla** | `[3P][S106]` |

**Use of funds:** build and deploy the OG-1 fleet, large pilots in the US and Europe, extend to new interior trades `[3P][S106]`.

**Board:** an AI summary says Zacua partner **Vivin Hegde** joined the board `[UNV][S109]`. Press only quotes him as an investor `[3P][S106]`.

## Business model

- **RaaS / lease, not outright sale**, working alongside crews without safety cages; **dust-free sanding** via a vacuum shroud `[UNV][S109]`. Vacuum-captured sanding itself is visible in the video `[V][S107]`; the commercial model is not confirmed.
- **Site types:** commercial offices, hotels, multifamily, **data centres**; first runs in New York `[UNV][S109]` (NY deployment Nov 2025 is on the company timeline `[CC][S105]`).
- **Market claim:** drywall mudding/taping is "60–65% of interior finishing timelines" `[UNV][S109]`: no source given.

## Their competitors (construction robotics) `[UNV][S109]` + general knowledge

| Company | Note |
|---|---|
| **Canvas** (US) | Closest predecessor in commercial drywall finishing; boom-lift robot, later partnered with JLG. Origin's angle: smaller, doorway-sized base + one AI policy across mudding, sanding and priming |
| **PaintJet** (US) | Exterior coatings |
| **Okibo** (Israel) | Plastering / finishing |

*Relevance for us `[INF]`:* same pattern as restrooms: an earlier slow/struggling pioneer (Canvas ↔ Peanut) followed by a new, AI-first, well-funded wave (Origin ↔ Loki / Hivebotics).

## Timeline (company "Zero to Infinity" page) `[CC][S105]`

| Date | Milestone |
|---|---|
| Dec 2024 | Started |
| Jan 2025 | Fundraising and HQ opening |
| Mar 2025 | First prototype |
| May 2025 | First test-site autonomy |
| Jul 2025 | First customer-site deployment |
| Sep 2025 | Customer-ready product live |
| Nov 2025 | First deployment in New York |
| Oct 2026 | Emerges from stealth with US$20M |

**Speed:** prototype in ~3 months, customer site in ~7 months. Faster than any restroom competitor on file `[INF]`.

## Product: OG-1

**Official spec (product page)** `[CC][S105]`:

| Item | Value |
|---|---|
| Footprint | **30 × 35 in** (~76 × 89 cm), fits through doors |
| Reach | **Up to 14 ft** (~4.3 m) |
| Base | Wheeled robot base |
| Sensors | Camera and LiDAR |
| Tools | **Swappable tool station + swappable end effector** |
| Tasks today | Joint compound (spray), sanding, priming. Handles high walls, corners, pillars, soffits, edges `[3P][S106]` |

**From the video frame (S107)** `[V]` / `[INF]`:
- **Tall vertical column** on a grey/white base (black/yellow hazard stripes, e-stop button, vents). The arm is mounted high on the column, which is how it reaches 14 ft `[INF]`.
- **6-axis cobot-style arm, white/silver with black joints, branded "origin"** on the forearm. Make not identifiable from the frame; could be a re-branded commercial cobot or their own `[INF]`.
- **End effector: yellow round sanding head with a vacuum hose** ("Vacuum Captured Sanding"). The yellow/black style resembles a Mirka wall sander `[INF]`, unconfirmed.
- **Tool station on the base:** yellow-and-black tools and coiled hoses on the left side.
- **Mast-top sensor** (thin pole with a small head at top-left of the base): likely the LiDAR or a camera `[INF]`.
- An operator in hi-vis holds a tablet (supervision / teleop) `[V]`.

### AI: "Construction Action Model" (CAM) `[CC][S105]`

| Layer | What it does |
|---|---|
| **Training data** | High-fidelity simulation (RL in randomised rooms); 3D site mapping (handheld + robot scans); live deployments (robot + teleop data) |
| **Reasoning system** | Plans construction subtasks: locate seams and fasteners, plan spray passes, "spray, then inspect" |
| **Action policy** | Navigate, use tools, inspect; seam and wall detection. VLA pre-training, imitation learning, RL in sim, real-to-sim |
| **Controller** | Closed-loop motion: tool standoff, **Diff-IK**, position and **admittance** control, real-time servoing |
| **Human-in-the-loop** | Remote teleop (drive + dock), **semantic correction** (relabel seams and screws), map cleaning (validate planes, remove noise) |
| **Learning loop** | ⭐ **"Quality map: scan and grade each pass"** gives reward labels; **residual RL policy over a classical planner** in sim; **DAgger** adds operator corrections to the training data |

## Relevance to Ubanthu `[INF]`

- **Same blueprint, different room.** Base + tall arm + tool station + force control + learned policy + teleop fallback is exactly the restroom-robot architecture (Loki, Hivebotics, Peanut). Origin shows how fast a funded team can field it: customer site in ~7 months.
- ⭐ **"Scan and grade each pass" is their verification loop.** It is the construction equivalent of our contamination verification: a post-task quality map that both proves the work and trains the policy. This validates our thesis that **verification data = training signal**, and it shows investors already understand the idea.
- **"One Robot. Any Trade."** Restroom cleaning is not on their list today (interior trades: board hanging, drilling, conduit per the pasted summary `[UNV][S108]`). A pivot into facility cleaning is possible but unsignalled.
- **Bengaluru engineering team:** competes with us for robotics / CV / embedded talent in India. Indian-origin founders and an Indian fund (Unilazer) on the cap table `[INF]`.
- **Not plotted on the quadrant** (different problem).

## People Directory

| Photo | Name | Role | Background | Links | Sources |
|---|---|---|---|---|---|
| — | **Yogesh Ghaturle** | Co-founder & CEO | Co-founder of **Perpule** (Bengaluru retail-tech, UltraPOS; co-founders Abhinav Pathak, Saketh BSV), **acquired by Amazon Mar 2021 for ₹107.6 cr (~US$14.7M)** `[3P][S110]`. Reported as expected to join Amazon after the deal; "several years at Amazon" per AI summary `[UNV][S109]` | — | S106, S110 |
| — | **Tushar Makkar** | Co-founder & CTO; leads autonomy / CAM | Previously led AI teams at **Eightfold AI** (HR-tech AI) `[3P][S110]` | — | S106, S110 |
| — | **Ashish Daga** | Co-founder; leads hardware (mechanical, tooling, chassis) | Previously at **Morphle Labs** (digital-pathology scanners, Bengaluru) `[3P][S110]` | — | S106, S110 |

**Team pattern `[INF]`:** software/AI founders with an Indian startup exit plus a precision-hardware engineer, Bengaluru-built. A close analogue to an Indian robotics team, and proof that such a team can raise US$20M from Accel for a US-first go-to-market.

## Unverified (pasted AI summaries, S108, S109) `[UNV]`

**S109 check (2026-10-23):** ✅ founders' backgrounds (Perpule → Amazon, Eightfold, Morphle) confirmed in press · ✅ investors, 150-robot target, pilot countries · ⚠️ "Series A" stage `[CONFLICT]` (others say seed/early) · ❌ not found: Indian subsidiary, Delaware, Vivin Hegde board seat, RaaS model, "60–65%" stat, "$1.3B+" sector funding.

**S108:** most of it matches the website. Not found on origin.tech: a roadmap to "board hanging, drilling, and conduit placement"; "high-density 3D LiDAR"; base "designed to traverse construction debris, cords". Treat these as unconfirmed.

## Open questions

- [ ] Which arm (re-branded cobot? own design?) and which column/lift; sanding head brand
- [x] ~~Founder backgrounds~~: Perpule/Amazon, Eightfold AI, Morphle Labs (S110)
- [ ] Indian entity: confirm "Artila Robotics Private Limited" on MCA (CIN, directors, date); Bengaluru headcount
- [ ] Board composition (Vivin Hegde?)
- [ ] Named US contractors; pricing model (RaaS per sq ft?)
- [ ] Any patents (Artila Robotics, Inc.; inventors Ghaturle / Daga / Makkar)?
- [ ] Any signal of moving into facility cleaning / restrooms?
- [ ] Read the Forbes piece ("This Robot Finishes Drywall 3X Faster Than Humans…") for more detail
