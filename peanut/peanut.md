# Peanut Robotics (San Francisco, USA): hotel bathroom-cleaning mobile manipulator (wound down)

[← Back to master document](../COMPETITOR_INTELLIGENCE.md) · [Sources](../SOURCES.md) · **Last updated:** 2026-10-19

Tags: `[V]` verified · `[3P]` third-party · `[CC]` company claim · `[INF]` inferred · `[UNV]` unverified · `[CONFLICT]` · `[INT]` internal observation / opinion from our team.

**Threat level:** ⚪ **Not an active competitor** (operations wound down, ~2024 `[INF]`). 🔴 **But highly relevant**:
1. It is the **closest historical precedent** to what Ubanthu, Hivebotics and Somatic are building: an AI mobile manipulator cleaning **hotel bathrooms**, with **~13,000 deployed hours**.
2. It holds **two active US patents (to 2040) whose claims include before/after imaging of the cleaned room** (see [Patents](#patents)).
3. Its founders publish lessons on why it failed.

## Snapshot

| | |
|---|---|
| **Status** | **Terminated / wound down** per Vishal's tracker `[INT][S088]`. Key staff left Apr – Jul 2024 (S089, S090). An unsourced AI summary says operations "wound down" after COVID and failed 2022 fundraising `[UNV][S091]` |
| **HQ** | 51 Federal Street, Suite 100, San Francisco, CA 94107 `[S088]` |
| **Founded** | **2018** (CTO résumé: "2018 – Present"; first round Jun 2018) `[S090][S075]`. Tracxn says 2016 `[3P][S091]` `[CONFLICT]`. The 2018-12-10 patent priority fits 2018 |
| **Website** | https://peanutrobotics.com/ (per CTO résumé) `[S090]` |
| **Product** | Autonomous **mobile manipulator for hotel housekeeping, specifically bathroom cleaning** (toilet, sink, shower/bath, mirror; also floors). Arm grasps handheld tools from a tool carrier `[V][S089][S092]` |
| **Customers** | **RLH Corporation** (Red Lion Hotels) housekeeping-robot pilot (Hotel Management article) `[S088]`; "trials at hotels and **national chains**" `[S088]`; "deployments in **hotels, restaurants and offices**"; "a **$1M ARR contract**" `[CC][S090]` |
| **Scale** | "**Over 13,000 hours** at hotel sites"; "first AI-driven cleaning mobile manipulator to earn revenue with customers" `[CC][S088][S090]` |
| **Business model** | Robotics-as-a-Service (monthly lease) `[UNV][S091]` |
| **Unit cost** | **BOM < US$10k per robot** ("revolutionary at the time"); contract manufacturing set up (co-founder Stephen Hansen) `[CC][S088]` |
| **Folder** | [peanut/](./) |

## Funding

| Date | Round | Amount | Valuation | Source |
|---|---|---|---|---|
| 25 Jun 2018 | Accelerator (Berkeley SkyDeck) | $0.10M | post $2.0M | `[3P][S075]` (PitchBook screenshot in Hivebotics deck); Tracxn: $100K SkyDeck `[S091]` |
| 5 Feb 2021 | Grant | $0.05M | — | `[3P][S075]` |
| 24 Feb 2021 | Seed | **$5.0M** | pre $15M / post $20M | `[3P][S075]` |
| 13 May 2022 | Seed | **$4.5M** | **pre $35.5M / post $40M** | `[3P][S075]` |
| **Total** | | **~$9.5–9.6M** | | S075; CTO résumé "$9M in VC funding" `[S090]` |

**Investors named in an unsourced AI summary** `[UNV][S091]`: **Kärcher New Venture** (Kärcher's corporate VC), Ulu Ventures, Creative Ventures, Grep VC, Asymmetry Ventures, Guindy Alumni Angels. **To verify.**

*If Kärcher invested here, note that Kärcher is also Hivebotics' tool supplier and MOU partner (S075). Kärcher would be the common strategic thread in restroom robotics `[INF]`.*

**Other unsourced AI claims, not used as facts** `[UNV][S091]`:
- Peak ARR "$2–5M" (compare the CTO's own "$1M ARR contract").
- CEO funded the company with "a huge amount" of personal savings in 2022.
- COVID shut down the hotel market in 2020–21.

## Products & technology

**From an engineer's résumé (Harsh Dhruva, Robotics Engineer, Jul 2022 – Apr 2024)** `[V][S089]`:
- "Commercially deployed **mobile manipulator for hotel bathroom cleaning**". He owned the arm software: **TOPPRA** trajectory generation, **ros_control**, synchronised tool control.
- **Perception:** a CV pipeline to handle **geometric variation between hotel bathrooms** using **ICP + RANSAC point-cloud registration**.
- **Cameras:** evaluated 6 depth-camera systems and chose **Orbbec Gemini 2**, with a C++ bring-up layer with auto-recovery for **4 simultaneous cameras**.
- **Calibration:** OptiTrack motion capture to measure **arm droop** and validate calibration (suggests a low-cost, compliant arm `[INF]`).
- ⭐ **Deployment bottleneck:** **operator training took 2–4 hours per surface**. He built a **live trajectory-recording ("teach") system that cut it to 15 min per surface**. So cleaning motions were **taught per bathroom surface by a human operator**, not fully autonomous `[INF]`.

**From the CTO's résumé (Ashis Ghosh, 2018 – 2024)** `[CC][S090]`:
- "Over 13,000 hours of commercial deployment".
- Perception reworked to use **VLMs, VSLAM and ML** for semi-dense human environments. **Synthetic training images from MuJoCo / Isaac Sim** → "resulted in a $1M ARR contract".
- "**RoboAI**": an LLM-based robot skill library (multimodal transformers, vector DB, RL) for unstructured tasks.
- Classical stack: time-optimal manipulation trajectories, **MPC navigation for holonomic robots**, point-cloud registration for visual servoing.
- Low-parameter VLMs on **< US$500 hardware** for real-time inference (MLC).
- Release cycle cut from 6 to 2 weeks; distributed/remote teams.

**From co-founder Stephen Hansen (LinkedIn quote)** `[CC][S088]`: "built and shipped one of the first commercially-available mobile autonomous cleaning robots with manipulators". He invented the planning algorithm and built vision-based grasping, kept the BOM below $10k, set up contract manufacturing, and got robots into trials at hotels and national chains. He is named inventor on two granted US patents.

**From the patents** `[V][S092][S093]`:
- **Base:** wheeled transportation assembly.
- **Arm:** a robotic arm, in patent 1 **mounted on a vertical "conveyor"** (a linear axis that moves the arm up and down).
- **Tools:** a modular tool carrier. Tools listed: vacuum, broom, **toilet brush**, sponge, wedge, motorised/rotating scrubber, brush, abrasive pad, **spray bottle**, hook.
- **Gripper:** grasps tools and objects, and moves clutter aside and back.
- **Fluid line:** a tank with pipes **routed through the arm** to a nozzle.
- **Pad changer:** an automatic **pad remover/installer** that swaps used cleaning pads.
- **Safety:** a "virtual safety cage" from distance sensors.
- **Navigation:** a baseline image map of the room to detect clutter.
- **Verification:** cameras capture the room **before and after the task for comparison**.

## Patents

| Patent | Title | Inventors | Priority / filed | Granted | Status | Current assignee |
|---|---|---|---|---|---|---|
| **US 11,407,118 B1** | Robot for performing dextrous tasks and related methods and systems | Joseph E. Augenbraun, Ashis Ghosh, Stephen J. Hansen, Achille Verheye | 2018-12-10 / 2019-12-10 | **2022-08-09** | **Active, expires 2040-10-01** | "Individual" (no company assignment recorded) |
| **US 12,397,440 B1** (continuation-in-part) | same title | + Dalia MacPhee, Lief Terry, Fang-Ting Kao, Edmund Kelly Friese | 2018-12-10 / 2022-07-06 | **2025-08-26** | **Active** | "Individual" |

**What the independent claims require** `[V][S092][S093]`:
- **US 11,407,118, claim 1:** wheeled base + **a conveyor perpendicular to the base with the arm travelling along it** + imaging system + station/path navigation + arm task control. **"Wherein the imaging system is configured to capture images of the room prior to completion of the task and after completion of the task for comparison."** Dependent claims: cleaning toilets, sinks, mirrors, baths/showers, floors (claim 3); tool carrier (4); clutter detection vs a baseline map (5–6); tool grasp and return (7–9).
- **US 12,397,440, claim 1:** wheeled base + arm + imaging + navigation + **a holder that engages a "surface interface object" (cleaning pad), with an automatic remover and installer for used/new pads**; imaging "during completion of the task". Dependent claims: fluid tank with pipes through the arm to a nozzle; distance sensors / virtual safety cage.

**Analysis for Ubanthu** `[INF]` (not legal advice; for a patent attorney to confirm):
- **This is the first patent on file whose independent claim includes before/after image comparison of a cleaning robot's work.** It is US-only and expires in 2040.
- **But each claim needs *all* its elements.** Claim 1 of '118 also needs the **vertical conveyor-mounted arm**. Claim 1 of '440 needs the **automatic pad swap**. A robot without those elements would likely fall outside these claims.
- **Still, it is prior art (2018 priority) for "before/after image verification" in robotic bathroom cleaning.** That limits what Ubanthu can claim broadly; it must patent the *specific* contamination-detection method.
- **"Individual" assignee + company wound down**: the patents may be owned by a founder (likely CEO Augenbraun) and could be **for sale or licence**. Worth checking USPTO assignment records.
- Cited later by **Somatic Holdings' "Bathroom cleaning robot"** (WO 2025/035010; US 12,440,076 B2), so Somatic's examiner saw Peanut's patent.

## People Directory

| Photo | Name | Role at Peanut | Background (short) | Links | Sources |
|---|---|---|---|---|---|
| — | **Joe (Joseph E.) Augenbraun** | **CEO**; patent inventor | — | [LinkedIn](https://www.linkedin.com/in/jaugenbraun) | S088, S091, S092 |
| — | **Ashis Ghosh** | **Co-Founder & CTO** (Feb 2018 – Jul 2024); patent inventor | UC Berkeley MEng (BEST Lab, 2017–18); U. Toronto Mech. Eng. + robotics minor; earlier co-founded Axial.gg (esports) and Smirk (chatbot); Bombardier; SkyDeck, StartX, Next 36 cohorts; Forbes Technology Council member | [X](https://x.com/ashis_ghosh_) · [bio.site](https://bio.site/ashis) · [GitHub](https://github.com/AshisGhosh) | S088, S090 |
| — | **Mike Bruno** | **President & Co-Founder** | — | [LinkedIn](https://www.linkedin.com/in/mike-bruno-a526491/) | S088 |
| — | **Achille Verheye** | **Co-Founder**; patent inventor | Has a public CV site | [Site](https://www.achille.fyi/home) · [CV](https://www.achille.fyi/curriculum-vitae) | S088, S092 |
| — | **Stephen (Steve) J. Hansen** | **Co-Founder**; planning algorithm, vision-based grasping, BOM < $10k, contract manufacturing; patent inventor | Forbes Technology Council article on deep-tech PMF (Aug 2025) | [LinkedIn](https://www.linkedin.com/in/stephenjhansen8/) | S088, S092 |
| — | **Harsh Dhruva** | **Robotics Engineer** (Jul 2022 – Apr 2024): arm software, ICP+RANSAC perception, 4× Orbbec Gemini 2, teach-recording system | CMU MS Mech. Eng. (Robotics), 2022; Rose-Hulman BS; now Robotics Systems Engineer at Autoroboto (Google), Jul 2024 – | (LinkedIn, portfolio, GitHub per résumé) | S089 |
| — | **Parth Sanghvi** | Machine Learning Engineer | — | LinkedIn (per tracker) | S088 |
| — | **Jay Karimi** | ML Engineer | — | LinkedIn, site (per tracker) | S088 |
| — | **Zach Price** | Robot Operator & Trainer | — | LinkedIn, site, GitHub (per tracker) | S088 |
| — | **Lu Lu** | Senior Contractor, Robotics | — | [LinkedIn](https://www.linkedin.com/in/lu-lu-502b116b/) | S088 |
| — | **Rene Orantes** | Robotics Technician | — | [LinkedIn](https://www.linkedin.com/in/rene-orantes-374b09154/) | S088 |
| — | Dalia MacPhee · Lief Terry · Fang-Ting Kao · Edmund Kelly Friese | Co-inventors on US 12,397,440 | — | — | S093 |

*Résumés (S089, S090) contain personal phone numbers and emails. **Not recorded here; the résumé files are kept local only** (gitignored).*

## Why it failed: lessons `[INF]` + founder writing

Evidence-based picture so far:
- **Labour-intensive deployment:** 2–4 h of operator teaching **per surface** (cut to 15 min). Every new hotel bathroom needed human setup. That is a scaling problem.
- **The hotel market collapsed in 2020–21 (COVID)**, Peanut's core vertical `[UNV][S091]`. Yet it still raised $9.5M in 2021–22 at a $40M post-money valuation.
- **Hardware compromises:** a sub-$10k BOM, plus arm droop that needed motion-capture calibration.
- **CTO's Forbes Technology Council articles (2026)**, not yet read (forbes.com blocked for automated fetch):
  - "**Why Robotics Demos Fail In The Real World**" (2 Apr 2026);
  - "**Commercial Cleaning Robots Are More Viable Than You Think—And What Will Separate The Winners**" (12 Mar 2026).
  - Co-founder Hansen: "**Four Hard-Won Lessons On Product-Market Fit For Deep Tech Startups**" (7 Aug 2025).
  - **Worth reading:** first-hand failure lessons from the closest precedent to Ubanthu.

## Internal notes / opinions

- **Vishal (2026-09-02 → 2026-09-19)** `[INT][S087][S088]`:
  - Built an outreach tracker for Peanut ("Target Company Deep-Dive & Outreach Tracker"); **no one contacted yet**.
  - Rated outreach priority: Ashis Ghosh **very high** (technical, former CTO); Augenbraun, Bruno, Verheye, Hansen and Harsh Dhruva **high**.
  - Notes: "Ashis … has written articles that hint at why Peanut failed".
- **Analysis** `[INF]`: Peanut's ex-team (CTO, engineers) has **direct hands-on experience with hotel-bathroom robot deployment, perception (Orbbec, ICP) and failure modes**. They are good candidates for advisory or expert calls, and possibly hires.

## Open questions

- [ ] Read the 3 Forbes articles (Ghosh ×2, Hansen ×1) and extract the failure lessons
- [ ] Confirm investors (Kärcher New Venture? Ulu? Creative Ventures? Grep VC?) via Crunchbase/PitchBook
- [ ] Who owns the two patents now? (USPTO assignment search) Are they for sale or licence?
- [ ] What robot arm and base did they use? Any photos or video of the robot (YouTube link in Harsh's résumé)?
- [ ] Exact shutdown date and cause; what happened to the robots/IP
- [ ] RLH article details (date, number of hotels)
