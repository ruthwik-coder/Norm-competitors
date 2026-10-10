# Competitor Intelligence: Restroom / Toilet Cleaning Automation

**Owner:** Ubanthu Robotics · **Last updated:** 2026-09-30 · **Sources:** [SOURCES.md](SOURCES.md) · **Rules:** [CLAUDE.md](CLAUDE.md)

**Confidence tags:** `[V]` verified · `[3P]` third-party report · `[CC]` company or institution claim · `[INF]` inferred · `[UNV]` unverified · `[CONFLICT]` sources disagree
**Citations:** `[S012]` = source ID in SOURCES.md. An asterisk (`[S012*]`) means the source was cited by an AI summary (S001) and **nobody here has opened it yet**.

> ⚠️ **Evidence status (2026-09-30):** Everything below currently comes from one ChatGPT web-research summary ([S001](_general/2026-09-30_S001_chatgpt-india-restroom-robotics-landscape.md)). No primary source has been checked yet. Read everything as provisional until specific company material is added.

---

## Executive Overview

- **India has several restroom-automation efforts but few mature direct competitors** `[3P][S001]`. Most Indian cleaning robots target floors. Fixture-level robotic cleaning (toilets, urinals, sinks) is rare.
- **Closest Indian players to a mobile manipulator robot:** Sketch Robotics (startup, incorporated May 2025) and Amrita's Sudha (academic prototype). IIT Madras has a TRL-2 patent application.
- **Closest Indian commercial player overall:** HapiHygi (HygiSeat), but it is a *fixed retrofit seat cleaner*, not a mobile robot.
- **Internationally the field is further ahead.** Hivebotics (Singapore, Abluo) is the main benchmark: deployed in hospitals and airports, and a reported US$6M Series A in Sep 2026 to move toward volume production `[3P][S011*]`.
- **No verified presence of the international players in India** `[3P][S001]`. RIFE Technologies claims to sell a washroom robot in India but this is unverified.

## Competitive Landscape

### Framework: three architectures `[INF][S001]`

| Architecture | Idea | Players |
|---|---|---|
| **1. Mobile manipulator robot** | A robot drives into the restroom and cleans the fixtures | Hivebotics, Eternia/TCR-H, Primech HYTRON, ZeeqClean, Senxeed, Sketch Robotics, Amrita Sudha, IIT Palakkad, IIT Madras (concept) |
| **2. Fixed fixture automation** | The toilet/seat cleans itself | HapiHygi, Hachimichi, ATSC, VAATA (chemical dosing only) |
| **3. Human + machine hybrid** | Semi-autonomous machine assists a cleaner | Fonda Global ALAC |
| *Adjacent: sanitation infrastructure* | Sewer and septic robots | Genrobotics, Solinas |

### Master table

| Company | Region | Product | Architecture | Stage | Relevance to us | Folder |
|---|---|---|---|---|---|---|
| [Sketch Robotics](sketch-robotics/sketch-robotics.md) | 🇮🇳 Kochi, Kerala | Autonomous Washroom Cleaning Robot | Mobile manipulator | Early startup (inc. May 2025); no prototype seen; ~₹10–15L KSM `[INT]` | 🔴 Direct on paper · 🟡 low near-term threat `[INT]` | [sketch-robotics/](sketch-robotics/) |
| [Amrita Vishwa Vidyapeetham: Sudha](amrita-sudha/amrita-sudha.md) | 🇮🇳 Kerala | Sudha service robot | Mobile manipulator | Research prototype | 🟠 Tech benchmark | [amrita-sudha/](amrita-sudha/) |
| [HapiHygi Innovations](hapihygi/hapihygi.md) | 🇮🇳 Gandhinagar, Gujarat | HygiSeat | Fixed retrofit | TRL 7 claimed, pilots | 🟠 Adjacent | [hapihygi/](hapihygi/) |
| [IIT Madras](iit-madras/iit-madras.md) | 🇮🇳 Chennai | Autonomous toilet-cleaning system (patent) | Concept | TRL 2 | 🟡 IP watch | [iit-madras/](iit-madras/) |
| [IIT Palakkad](iit-palakkad/iit-palakkad.md) | 🇮🇳 Palakkad | Inter-IIT toilet-cleaning robot | Mobile | Student prototype (2018) | ⚪ Historical | [iit-palakkad/](iit-palakkad/) |
| [Hachimichi](hachimichi/hachimichi.md) | 🇮🇳 Pune | SeatO'fresh | Fixed retrofit | Commercial (84 units, 2021) | 🟡 Adjacent | [hachimichi/](hachimichi/) |
| [ATSC / i-Hub Gujarat](atsc-ihub-gujarat/atsc-ihub-gujarat.md) | 🇮🇳 Gujarat | Automatic Toilet Seat Cleaner | Fixed | Under development | 🟡 Adjacent | [atsc-ihub-gujarat/](atsc-ihub-gujarat/) |
| [VAATA](vaata/vaata.md) | 🇮🇳 Chennai | DryTab | Cistern dosing | Commercial | ⚪ Low | [vaata/](vaata/) |
| [RIFE Technologies](rife-technologies/rife-technologies.md) | 🇮🇳 | "Washroom Cleaning Robot" | Unknown | Claimed deployments `[UNV]` | 🟠 Verify: possible reseller | [rife-technologies/](rife-technologies/) |
| [Genrobotics](genrobotics/genrobotics.md) | 🇮🇳 Kerala | Sewer/manhole robots | Adjacent | Commercial | ⚪ Adjacent | [genrobotics/](genrobotics/) |
| [Solinas](solinas/solinas.md) | 🇮🇳 Chennai (IITM incubator) | Septic-tank cleaning robot | Adjacent | Commercial | ⚪ Adjacent | [solinas/](solinas/) |
| [Hivebotics](hivebotics/hivebotics.md) | 🇸🇬 Singapore (NUS spin-out, 2021) | Abluo (Mark 1 / Mark II) | Mobile manipulator, **contactless** | US$6M Series A (Sep 2026: Vertex, Farglory, Rigel); ~10,000 h, 20+ sites | 🔴 **Main benchmark**; claims scored before/after verification | [hivebotics/](hivebotics/) |
| [Eternia Robotics / Cleaning Robotics](eternia-robotics/eternia-robotics.md) | 🇸🇬 Singapore | TCR-H | Mobile | Being productised | 🔴 Benchmark | [eternia-robotics/](eternia-robotics/) |
| [Primech AI](primechai/primechai.md) | 🇸🇬 Singapore / US-listed parent | HYTRON | Mobile manipulator | Early commercial: US$12k robot revenue FY26; **suing ex-CTO over HYTRON development** | 🟠 Benchmark; delivery doubtful `[INF]` | [primechai/](primechai/) |
| [Fonda Global + A*STAR](fonda-global-alac/fonda-global-alac.md) | 🇸🇬 Singapore | ALAC | Hybrid / semi-autonomous | Unknown | 🟡 Benchmark | [fonda-global-alac/](fonda-global-alac/) |
| [ZeeqClean](zeeqclean/zeeqclean.md) | Asia (Taiwan? `[INF]`) | ZC-01 | Mobile | Unknown | 🟠 Benchmark | [zeeqclean/](zeeqclean/) |
| [Senxeed Robotics](senxeed-robotics/senxeed-robotics.md) | 🇯🇵 Japan | WUUMIE | Mobile, multi-tool | Unknown | 🟠 Benchmark | [senxeed-robotics/](senxeed-robotics/) |

*Relevance ratings are our own first-pass analysis `[INF]`, not source facts.*

---

# Company Profiles

Each company has its own file with its full profile, its people and its open questions. **Anything new about a company goes into its file.** This master doc only carries the overview, comparisons and findings.

| 🇮🇳 India | 🌏 International |
|---|---|
| [Sketch Robotics](sketch-robotics/sketch-robotics.md) | [Hivebotics](hivebotics/hivebotics.md) |
| [Amrita: Sudha](amrita-sudha/amrita-sudha.md) | [Eternia Robotics / Cleaning Robotics](eternia-robotics/eternia-robotics.md) |
| [HapiHygi Innovations](hapihygi/hapihygi.md) | [Primech AI](primechai/primechai.md) |
| [IIT Madras](iit-madras/iit-madras.md) | [Fonda Global + A*STAR: ALAC](fonda-global-alac/fonda-global-alac.md) |
| [IIT Palakkad](iit-palakkad/iit-palakkad.md) | [ZeeqClean](zeeqclean/zeeqclean.md) |
| [Hachimichi](hachimichi/hachimichi.md) | [Senxeed Robotics](senxeed-robotics/senxeed-robotics.md) |
| [ATSC / i-Hub Gujarat](atsc-ihub-gujarat/atsc-ihub-gujarat.md) | |
| [VAATA](vaata/vaata.md) | |
| [RIFE Technologies](rife-technologies/rife-technologies.md) | |
| [Genrobotics](genrobotics/genrobotics.md) | |
| [Solinas](solinas/solinas.md) | |

---

# Cross-Competitor Comparisons

### Capability matrix (corrected against source text)

`✓` stated by a source · `✗` stated absent / not applicable · `?` claimed by S001's table but **not supported by the cited text** · `—` no info

| Capability | Sketch | Amrita Sudha | HapiHygi | IITM | Hivebotics | Eternia TCR-H | Primech HYTRON | ZeeqClean | Fonda ALAC |
|---|---|---|---|---|---|---|---|---|---|
| Mobile platform | ✓ | ✓ | ✗ | concept | ✓ | ✓ | ✓ | ✓ | — |
| Robotic arm | ✓ 6-DOF | ✓ | ✗ | concept | ✓ 6-DOF (Mk2) | ? | ✓ patent; functions on site imply arm `[INF]` | — | — |
| Toilet | ✓ | ✓ | seat only | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Urinal | ? | — | ✗ | — | ✓ | ✓ | ✓ brushing (site) | ✓ | — |
| Sink / basin | ✓ | — | ✗ | — | ✓ | — | ✓ sink + countertop (site) | — | — |
| Floor | ✓ | — | ✗ | — | ✓ | ✓ | ✓ mopping + blower drying | ✓ | — |
| **Squat (Indian/Asian) toilet** | — | — | — | — | not listed in Mk2 brochure `[S061]`; no evidence | — | **✓ claimed (S042)** | — | — |
| Mirror | — | — | — | — | ✓ "sinks & mirrors" `[S061]` | — | ✓ wiping | — | — |
| Doors / elevators | — | — | ✗ | — | **same floor only** (no lift claim) `[S061]` | — | ✓ both claimed | — | — |
| Fixture recognition | ✓ VLM | ✓ | ✗ | — | AI vision | ✓ | ✓ camera (patent) | lid detection | — |
| **Stain / dirt detection** | — | **✓** | ✗ | intended | fixture ID by vision; stain-specific not stated | — | "may" (patent); "UV bacteria detection" listed for Mark 2 (deck) | — | stain *removal* |
| Cleanliness verification | — | **✓** | — | — | **✓ "scored before-and-after check" every job** (S056) | — | "may" (patent) | — | QR-tracked cleaning status per bowl (ALAC 2.0) `[S070]` |
| Lid / seat lifting | — | — | — | — | — | ✓ | — | ✓ | ✓ |
| Steam | — | — | ✗ | — | ✓ **173 °C**, 3/5/8 bar, 75 g/min (7 min start-up) `[S061]` | — | — | — | — |
| Jet / spray | spray | spray | spray | — | **contactless:** high-pressure steam + chemical jet + vacuum + blow-dry; **no brushes** | — | e-water (electrolysed/ozone) jetting + detergent; "high-pressure" unconfirmed | pressurised | — |
| UV-C | ✓ | — | ✓ | — | — | — | — | ✓ | — |
| Tool disinfection | — | — | — | — | — | ✓ brush | ✓ ozone wash in dock (patent) | — | — |
| Cleanliness / hygiene reporting | — | — | — | — | ✓ "outcomes can be audited"; HiveIntelligence validates jobs (S056) | — | not mentioned; dashboard shows task status only | — | — |
| Time per toilet | — | — | — | — | **5 min** (urinal 3–5, sink 2–4) `[S061]` | — | ~6 min (basin/urinal ~3) | — | — |
| Commercial deployments | none found | none found | pilots (claimed) | ✗ | ✓ ~10,000 h, 20+ sites, 4 continents (S056) | pilot history | early: army-camp lease, SG hospital; US$12k lease revenue FY26 | — | — |

### What stands out `[INF]`
- **⚠️ Updated 2026-10-06: post-clean verification is no longer unclaimed.** **Hivebotics** says "every job ends with a scored before-and-after check, so cleaning outcomes can be audited" (S056), and Amrita Sudha claims cleanliness monitoring. **The differentiator for Ubanthu must now be the *quality* of contamination detection** (what is detected, how accurately, what evidence), not merely having verification. How Hivebotics scores is unknown.
- **Indian (squat) toilets:** **Primech HYTRON is the only competitor on file that claims squat-toilet support** `[CC][S042]`. No Indian player claims it. Unverified: we have no demo.
- **Fleet dashboards:** Primech's reports task status only `[CC][S042]`; **Hivebotics claims audited cleaning outcomes** via HiveIntelligence `[CC][S056]`.

### Hardware & manufacturing suppliers

**Legend:** **Named** = the company or its own document names the supplier · **Candidate** = indirect evidence (e.g. an employee's work), not tied to the product itself · — = no info. Details and evidence are in each company file.

| Component | Primech HYTRON | Hivebotics Abluo | Sketch Robotics | Others |
|---|---|---|---|---|
| **Manufacturer / assembly** | **Named:** unnamed China production partner, "300 robots' initial capacity" (Jul 2025) `[CC][S044]` | — | — | — |
| **Robot arm** | **Named (as example):** **Elite Robots, Shanghai** ("such as those supplied by…", patent WO 2025/259179 p.9) `[V][S054]`. Likely, not confirmed for the shipping unit | **Confirmed: UFACTORY 850**. Brochure specs match (S061/S063) + UF850 config/URDF edits in their GitHub fork of UFACTORY's `xarm_ros2` `[V][S071]`. *History:* Elephant Robotics myCobot 320 M5 in 2021–22 NUS patent `[V][S065]` | 6-DOF arm, supplier unknown `[CC][S002*]` | — |
| **Compute** | **Named:** NVIDIA Jetson Orin "Super" `[CC][S044]` | **Named:** AMD Ryzen Embedded 8845HS + NVIDIA RTX A400 `[CC][S061]` | — | — |
| **Navigation controller / base** | **Candidate:** SEER Robotics (Roboshop), mecanum-wheel AGV, from an engineer's résumé; not tied to HYTRON `[S049]` | **Mecanum** base in ros2_control (custom; supplier unidentified) `[V][S071]`; 0.8 m/s `[S061]` | — | — |
| **3D LiDAR** | **Candidate:** Hesai (model unknown), from an engineer's driver work; not tied to HYTRON `[S048]` | **Identified (high confidence): Livox Mid-360**. All 6 brochure specs match, incl. distinctive 360°×59° FOV `[S061][S063]` | — | — |
| **Force/torque sensor** | **Candidate:** KWR75 (believed Kunwei, China), from an engineer's driver work `[S048]` | Likely **UFACTORY 6-axis F/T sensor** (UFACTORY FT API enabled for real hardware, Aug 2026) `[INF][S071]` | — | — |
| **Camera** | Wrist camera on arm; brand unknown `[V][S041][S054]` | **Confirmed: Luxonis OAK-D S2 PoE** (brochure depth+RGB; code + exact spec match) `[V][S071][S072]` · **Orbbec Gemini 335Le** (Jul 2026, code) `[V][S071]` · RealSense D435i wrist (robot model/sim) `[S071]` | VLM perception claimed; camera unknown | — |
| **Fleet software** | Open-RMF (from engineer's résumé) `[S049]`; own task-management dashboard `[CC][S042]` | Own: **HiveOS** (brochure) / **HiveIntelligence** (Vertex release) `[CC][S061][S056]` | — | — |

**Legend addition:** **Identified** = the model is pinned down by matching published specs (the company didn't name it).

**Pattern so far** `[INF]`: **Hivebotics' hardware is now fully mapped from public code + brochure: UFACTORY 850 + Livox Mid-360 + Luxonis OAK-D S2 / Orbbec Gemini 335Le + AMD/NVIDIA compute + custom mecanum base.** **Both leading competitors build on Chinese off-the-shelf cobot arms and LiDARs**: Primech (Elite Robots arm named; Hesai candidate; SEER candidate) and Hivebotics (**UFACTORY 850 + Livox Mid-360**). Compute differs: Primech = NVIDIA Jetson Orin; Hivebotics = **x86 AMD Ryzen + NVIDIA RTX A400 GPU**. **Arm + LiDAR + compute is commodity hardware, roughly US$10–15k of bill of materials** (general-knowledge price estimate, unverified). **Differentiation is in the end-effector/cleaning system and software**, which is where Ubanthu competes.

### Pricing
_No pricing data yet for any competitor._

### Target markets
- Airports and hospitals: Hivebotics `[CC]`; airports, malls, hospitals, corporate campuses: RIFE `[UNV]`
- B2B washrooms: Hachimichi
- Railways: SNJB patent (research)

---

## Patent / Research Landscape

| ID | Title | Owner | Filed | Status | Source |
|---|---|---|---|---|---|
| **WO 2023/075687** | Robot Alignment and Manipulation: YOLOv5 fixture detection + 3-step alignment; point-cloud waypoint cleaning (MoveIt); pneumatic tool changer with disposable brush heads; arm = myCobot 320. **Applicant NUS**; inventors incl. Hivebotics founders. [Deep dive](hivebotics/hivebotics-patent-WO2023075687.md) | NUS (Hivebotics founders) | 2022-10-25 (priority 2021-10-29) | **Ceased** (~Apr 2024): no national-phase entries, so free prior art | S065, S066 |
| **WO 2025/259179** | Fluid connection between cleaning robot and base station: **robot's arm picks up the station's connector and plugs it into the robot** for water refill and waste drain; QR-code docking; connection check. **Names Elite Robots (Shanghai) as example arm.** Describes detergent→brush→rinse, **no ozone**. India designated. [Deep dive](primechai/primechai-patent-WO2025259179.md) | Primech AI | 2025-05-15 (priority 2024-06-14) | Published 2025-12-18. Search report: LG KR 10-2014-0036653 "X" vs claims 16–17; Lim/Samsung "Y" vs 1–5, 9–12, 21–23 | S054 |
| **WO 2025/259178** | A Cleaning Robot: mobile robot with **ozone water made on board** (core claim); arm, tool changer (brush and fan), fixture-recognition camera in dependent claims. Stain detection mentioned but **not claimed**. **India designated.** [Deep dive](primechai/primechai-patent-WO2025259178.md) | Primech AI | 2025-05-15 (priority 2024-06-14) | Published 2025-12-18. Search report: core claims 1–7, 20, 21 already shown by CN 111466837 A | S041 |
| IN 202541062468 | A System and Method for Autonomous Toilet Cleaning | IIT Madras | 2025-06-30 | Published 2025-07-11, TRL 2 | S005*, S016* |
| IN 201821008841 | Smart (automatic) toilet cleaning for Indian Railways: robotic arm, brush, water jets, sensors, door lock, IoT | SNJB's college / Indian inventors | 2018 | Application | S030*, S031* |
| ATSC patent | Autonomous toilet-seat cleaner | ATSC (i-Hub Gujarat) | — | Patent-pending | S009* |
| Paper | Restroom cleaning system for convenience stores (fixture mechanisms + floor robot), *Advanced Robotics* 36(23), 2022 | Tokyo Metropolitan Univ. | — | Published | S032* |

---

## People

Each company file has its own **People Directory**. There is no combined list.

| Company | People on file |
|---|---|
| [Sketch Robotics](sketch-robotics/sketch-robotics.md#people-directory) | 11 (3 founders, 6 team, 2 mentors) |
| [HapiHygi](hapihygi/hapihygi.md#people-directory) | 2 |
| [Hivebotics](hivebotics/hivebotics.md#people-directory) | 20 (8 current named staff on LinkedIn + 5 GitHub-only engineers; 2 advisors; 5 former/early; 9 photos) |
| [IIT Madras](iit-madras/iit-madras.md#people-directory) | 1 |
| [Primech AI](primechai/primechai.md#people-directory) | 10 (CEO, Primech AI COO, ex-CTO, 3 execs, 4 technical hires from Mar–Jul 2026) |

## Important Findings

1. **Hivebotics raised a US$6M Series A (4 Sep 2026)** led by Vertex (remit covers SEA *and India*), with strategic co-investors **Rigel** (restroom-fixture maker) and **Farglory** (property) `[V][S056]`. It claims ~10,000 operating hours at 20+ sites and **scored before/after verification of every job**, so it is **the most direct threat to Ubanthu's contamination-verification positioning**. Most likely foreign entrant into India.
2. **The only Indian startup building a mobile restroom manipulator is Sketch Robotics**, incorporated May 2025 `[3P]`. But it is a 9-person team fresh out of CUSAT with no visible prototype and an estimated ₹10–15 lakh of KSM funding `[INT][S040]`. It is a watch-list item, not an imminent threat.
3. **Contamination detection and cleaning verification are thinly claimed across the field** `[INF]`. This is a possible positioning angle for Ubanthu.
4. **Primech's patent (WO 2025/259178) centres on ozone water, not perception.** It shows an arm with a tool changer and a fixture-recognition camera. Stain detection and cleaning verification are only mentioned as possibilities and are not claimed. The core claims already face strong prior art. India is designated `[V][S041]`, `[INF]`.
5. **Hivebotics' public GitHub (S071) shows its 2026 engineering focus is force-compliant manipulation** (F/T sensing, admittance/FDCC compliance control, toilet-seat lifting sim; MoveIt Pro), **not perception**. Nothing public touches contamination detection. Cameras changed within ~6 months (OAK-D S2 → Orbbec Gemini 335Le).
5. **Hivebotics' core patent lapsed** `[V][S065][S066]`. WO 2023/075687 (NUS-owned; founders as inventors) ceased ~Apr 2024 with no national filings, so its alignment, waypoint and tool-changer methods are **free prior art**. It also shows Hivebotics **switched from disposable-brush contact cleaning (myCobot arm, 2021–22) to contactless steam (UFACTORY 850, 2026)**. Field deployment confirmed in **Orlando, FL** (S068).
5. **Primech's HYTRON is far less mature than its marketing** `[V][S043][S044]`. FY2026 robot revenue was US$12k and the robotics segment lost US$2.48M, against a 300-robot rollout plan and a ">99% disinfection" claim (lab not named). Primech is **suing its former Primech AI CTO** (49% shareholder, lead patent inventor) over missed HYTRON milestones and source code; he counter-claims IP ownership. See [SEC deep dive](primechai/primechai-sec-filings.md).
6. **S001's comparison table overstates capabilities** for Primech, Eternia and Hivebotics compared with its own cited text. The corrected matrix is above. Don't reuse the original table.

## Open Questions / Information Gaps

**Verification (high priority)**
- [ ] Open S002, S003, S005, S011, S020 (the primary sources behind the key claims) and upgrade `*` to checked
- [ ] Find the original MeitY post for HapiHygi's TRL 7 / 500+ claim (S014 is a mirror)
- [ ] Find a real WUUMIE source for Senxeed (S028 is the wrong page)
- [ ] RIFE: identify the actual washroom robot model and its maker
- [x] ~~Confirm the `primechai/` folder = Primech AI~~ (confirmed by its contents: patent and filings)

**Missing data**
- [ ] Pricing / business model for every competitor (sale vs. RaaS vs. lease)
- [ ] Funding for HapiHygi, Eternia, ZeeqClean, Senxeed
- [ ] Teams and founders for Hivebotics, Primech, Eternia, ZeeqClean, Senxeed, Hachimichi, ATSC
- [ ] Amrita Sudha: lab, professor, papers
- [ ] Squat toilets: Primech claims support (S042). Does anyone else? How well does it work?
- [ ] Any international player with an Indian distributor or deployment?

---

## Change Log

| Date | Change | Source |
|---|---|---|
| 2026-09-30 | Knowledge base created. | — |
| 2026-09-30 | Processed ChatGPT India landscape report: 17 organisations profiled, 33 sources registered, capability matrix corrected, 6 people added, folders created per company. | S001 |
| 2026-09-30 | Sketch Robotics: added team page and 3 LinkedIn screenshots. Founder names confirmed; titles, backgrounds and 8 photo crops added; 2 CUSAT mentors and 1 possible team member added. | S034–S037 |
| 2026-09-30 | **Restructured:** each company moved to its own file (`<company>/<company>.md`); master doc keeps overview, comparisons, findings; combined People Directory replaced by one per company. | — |
| 2026-09-30 | Sketch Robotics: office address and Street View added; 6 more team members with photos; Sajeem confirmed as Hardware Engineer; internal notes (no prototype media, same-college team, ~₹10–15L KSM estimate, execution doubts) added. Threat downgraded to low near-term. | S038–S040 |
| 2026-10-02 | Primech AI: OCR'd and analysed patent WO 2025/259178 (deep-dive file created); arm, tool changer, ozone-water system and inventors added; arm conflict vs. website recorded; capability matrix and patent table updated. | S041 |
| 2026-10-02 | Primech AI: official HYTRON page added (specs, functions, squat-toilet support, ~6 min/toilet, task-management software); arm conflict downgraded to "very likely has arm"; capability matrix extended (squat toilet, mirror, doors/elevators, hygiene reporting, time per toilet). | S042 |
| 2026-10-02 | Primech AI: SEC 20-F FY2026 and 26 6-Ks read (deep-dive file created): financials (robot revenue US$12k, segment loss US$2.48M), 51/49 ownership, management, partners (Chinachem, Savills, Aramark, GAIB, WELLE), >99% disinfection claim, **lawsuit vs former CTO**. Threat rating lowered. | S043, S044 |
| 2026-10-02 | Correction: Zhang Youwei's employment dates. "May 2024 – Mar 2026" was wrong. Mar 2026 is when he moved from Primech to Primech AI's payroll; he was later **suspended and terminated** by Primech AI (date not disclosed, before 7 Aug 2026). Fixed in the Primech profile and SEC deep dive. | S044 |
| 2026-10-02 | Primech AI: searched all filings for HYTRON unit counts and found **none**. Added named deployment sites (Temasek Polytechnic, Singapore mall, large Singapore hospital), Japan/Europe partners (Golden Rim, TCOrobotics), China production partner, and HYTRON Lite. | S044 |
| 2026-10-03 | Primech AI: South Korea distribution agreement added (unnamed distributor; trial first; "projected ~US$4.08M over 3 years", conditional; **not in SEC filings**). Region-by-region deployment table added to the Primech profile. | S045, S046 |
| 2026-10-03 | Primech AI: engineer Josef Gstoettner profiled (LinkedIn, GitHub, public résumé). **First supply-chain evidence:** SEER Robotics navigation controller (Roboshop), mecanum-wheel AGV base, Hesai LiDAR driver work, KWR75 force/torque sensor, Open-RMF fleet management; Hong Kong engineering team since Mar 2026. New "Hardware & supply chain" section in Primech profile. | S047–S049 |
| 2026-10-03 | Primech AI: LiDAR evidence re-checked. Hesai link = medium (real hardware, model unknown, not directly tied to HYTRON); laser_filters downgraded to no evidence; new **`hytron.yml` / host `hytron8`** proves engineer works on HYTRON robots. | S048 |
| 2026-10-03 | Primech AI: caveat added to supply-chain section. Engineer evidence shows Primech AI team's components, **not** which robot they're on (mecanum/SEER AGV and toilet-cleaning fleet are separate résumé bullets; Hesai and HYTRON never co-mentioned). Rows downgraded to "HYTRON candidates". | S047–S049 |
| 2026-10-06 | Primech AI: 3 more staff profiled: Patrick Yeung (Head of System Architect, HK), Ivan Immanuel (Robotics SW Eng, CV/ML, SG), Mohamad Hafizuddin Majek (Robotics Service Eng, SG). Team analysis: 4 technical hires Mar–Jul 2026, i.e. a rebuild after the CTO exit; no senior CV/perception lead visible. | S050–S053 |
| 2026-10-06 | Primech AI: second patent WO 2025/259179 OCR'd and analysed (deep-dive file). **Elite Robots (Shanghai) named as arm**; arm-plugged docking; detergent cycle with no ozone (conflict with 259178/website); base-station design; gaps listed. | S054 |
| 2026-10-06 | New master table **Hardware & manufacturing suppliers** (cross-competitor, Named vs Candidate). Primech supplier summary added at top of its supply-chain section; Elite Robots added to the analysis. | S041–S054 |
| 2026-10-06 | Primech AI: LinkedIn URLs added for Patrick Yeung, Ivan Immanuel, Mohamad Hafizuddin Majek. | S050–S052 |
| 2026-10-06 | **Hivebotics** profile rebuilt: Gemini team/timeline (S055) organised and fact-checked against the Vertex Series A release (S056, now read) and web search (S057). New: co-investors Farglory + Rigel, 10,000 h / 20+ sites, contactless method, **scored before/after check**, team of 6 named, Hivebotics-vs-Primech comparison. Master capability matrix and "what stands out" corrected (verification no longer unique). | S055–S057 |
| 2026-10-06 | Hivebotics: CEO Rishab Patwari profiled (LinkedIn, GitHub, personal site); **first photo of Abluo** (from his LinkedIn banner); arm supplier candidate UFACTORY xArm added to supplier table (weak). Gemini claim "Series A–C startup engineer" not supported. | S058–S060 |
| 2026-10-08 | **Hivebotics hardware identified** from Abluo MK-2 brochure (S061) + spec checks (S063): arm **UFACTORY 850**, LiDAR **Livox Mid-360** (high confidence), compute **AMD Ryzen 8845HS + NVIDIA RTX A400** (named). Gemini analysis (S062) verified except "225 kg" (wrong) and AMR-supplier speculation. Full spec deep-dive file; supplier table and capability matrix updated; Abluo vs HYTRON spec comparison. | S061–S063 |
| 2026-10-08 | **Hivebotics:** Vishal's notes docx processed (S064); patent WO 2023/075687 OCR'd and analysed (ceased, NUS-owned, myCobot 320, disposable brushes) (S065, S066); 7 new people incl. CTO photo, Head of Eng. Kendrick Chin, Sales & Service Dir. Cawley Mah, Dmitri Manajev (Zurich), Peera Tienthong (Orlando deployment), ex-engineer Zhicheng Lin (S067–S069); A*STAR/Fonda hypothesis evaluated (no evidence yet). **Fonda ALAC** profile updated: ALAC 2.0, MUSE Gold 2025, A*STAR credits (S026, S070). Patent table, capability matrix, supplier table, findings updated. | S064–S070 |
| 2026-10-08 | **Correction:** the 2023 Hivebotics prototype photo (S064) shows a **Western toilet seen top-down**, not a squat toilet (spotted by Vishal). Removed the squat-toilet claim from the Hivebotics profile and the capability matrix. Primech remains the only competitor claiming squat-toilet support. | S064 |
| 2026-10-08 | **Hivebotics GitHub** (github.com/hivebotics) analysed: all 5 forks and 14+ branches compared with upstream (S071). **UF850 confirmed by code**; mecanum base; UFACTORY F/T sensor (likely); compliance control + seat-lift sim; MoveIt Pro 9; cameras **Luxonis OAK-D S2 PoE** (confirmed: code + spec match, S072), **Orbbec Gemini 335Le**, RealSense D435i (wrist, sim). 5 new engineers from commits. Supplier table, specs file, findings updated. | S071, S072 |
