# Primech AI

[← Back to master document](../COMPETITOR_INTELLIGENCE.md) · [Sources](../SOURCES.md) · **Last updated:** 2026-10-03

Tags: `[V]` verified · `[3P]` third-party · `[CC]` company claim · `[INF]` inferred · `[UNV]` unverified · `[CONFLICT]` · `[INT]` internal observation / opinion from our team. `[S012*]` = cited by S001, not yet opened by us.

**Deep dives:** [Patent WO 2025/259178, "A Cleaning Robot"](primechai-patent-WO2025259178.md) · [Patent WO 2025/259179, arm-plugged docking](primechai-patent-WO2025259179.md) · [SEC filings: 20-F FY2026 + 6-Ks](primechai-sec-filings.md)

> ⚠️ **Key finding (2026-10-02):** Primech is **suing HYTRON's former CTO, Zhang Youwei**, over missed development milestones, **source code** and IP. He counter-claims that some IP pre-dates his employment. HYTRON earned only **US$12k of lease revenue in FY2026**, and the robotics segment lost **US$2.5M**. Details: [SEC deep dive §1, §5](primechai-sec-filings.md).

## Snapshot

| | |
|---|---|
| **Legal name** | Primech AI Pte. Ltd. `[V][S041]` |
| **Address** | 23 Ubi Crescent, Singapore 408579 (patent, 2025) `[V][S041]`. Group HQ moved in 2026 to 60 MacPherson Road, Siemens Centre #04-08, Singapore 348615 `[V][S043]` |
| **Ownership** | **51% Primech Holdings, 49% Zhang Youwei** (former CTO) `[V][S043]`. Set up 29 May 2024 |
| **Parent** | **Primech Holdings Ltd** (Nasdaq: PMEC). FY2026 revenue **US$78.0M**, net loss US$3.0M; 99.7% of revenue from Singapore cleaning services `[V][S043]` |
| **Product** | **HYTRON** (Mark 1 & Mark 2), an autonomous commercial restroom-cleaning robot |
| **Stage** | **Early commercial / largely pre-revenue.** HYTRON is in Primech's own fleet (31 Mar 2026). Robot lease revenue FY2026 = **US$12k**; robotics segment loss **US$2.48M**; R&D US$0.41M `[V][S043]`. Deployments announced: a Singapore army camp (lease, Nov 2025); a "leading hospital in Singapore"; Nina Tower 1, Hong Kong (MoU) `[CC][S044]` |
| **Funding model** | RaaS (robots leased as a service); MoU to **tokenise robots via crypto (GAIB)**; convertible notes from WELLE Environmental (China) `[CC][S044]` |
| **Compute** | NVIDIA Jetson Orin "Super" module `[CC][S044]` |
| **Website** | https://primech.ai/ |
| **IP** | Twin PCT filings, same day and inventors: **WO 2025/259178** (cleaning robot: ozone water, arm, tool changer) `[V][S041]` and **WO 2025/259179** (robot uses its arm to plug a fluid connector into the docking station for refill/drain) `[V][S054]`. Priority 14 Jun 2024; India designated |
| **Folder** | [primechai/](./) |

## Products & technology

### HYTRON: official product page `[CC][S042]`
Raw text: [2026-10-02_S042_primech-website-hytron-page.md](2026-10-02_S042_primech-website-hytron-page.md)

**Positioning:** "AI Powered Bathroom Cleaning Robot". **"Covers up to 70% of bathroom cleaning tasks."**

**Smart functions listed:** blower (air-drying) · surface wiping · mirror wiping · toilet-bowl flushing · **urinal brushing** · **e-water jetting** · floor mopping · navigating · **door opening** · self-charging + water refill/discharge.

**Claims:**
- **Self-generated electrolysed water** ("e-water") for eco-friendly cleaning
- "High precision **contactless and contact-based** cleaning remove stubborn stain": jetting plus brushing/wiping
- **Self-cleaning** functions sanitise the cleaning tools after use
- "AI-optimized routines minimize water and energy usage"
- Multiple sensors for **obstacle detection and avoidance**
- Air-drying and mopping to reduce slip hazards

**Specifications** `[CC][S042]` (values paired with labels by order; see the processing note in S042)

| Spec | HYTRON robot |
|---|---|
| Dimensions | **733 L × 409 W × 1311 H mm** |
| Weight | **128 kg** |
| Max speed | 0.6 m/s |
| Autonomous obstacle avoidance | Yes |
| **Elevator ride** | **Yes** |
| Fresh water tank | **8 L** |
| Waste water tank | 5 L |
| Detergent tank | **1.5 L** |
| Battery life | **4 h** |
| Charging time | 2 h |
| **Service range** | Sink, countertop, urinal, toilet bowl, **squat toilet**, floor, mirror |

| Spec | Docking station |
|---|---|
| Dimensions | 230 L × 460 W × 590 H mm |
| Water supply & discharge, battery charging | Automatic, 2 h |

**Typical execution time** `[CC][S042]`: **toilet ~6 min · wash basin ~3 min · urinal ~3 min**

**Software: "Hytron Task Management"** `[CC][S042]`
- Tracks task status (done or pending) for each robot across multiple sites
- Real-time dashboard of each robot's status
- Alerts on battery and water-tank levels and other problems
- "Data analytics": integrates with **IoT and building management systems (BMS)**
- **No cleanliness or hygiene reporting is mentioned.** The reports cover task status and robot health, not how clean the restroom is.

**Analysis** `[INF]`:
- **Throughput:** about 6 min per toilet and 3 min per basin or urinal. A restroom with 4 toilets, 4 urinals and 4 basins takes about 48 min of robot time. The 4 h battery could cover roughly 4–5 such restrooms per charge.
- **The 8 L water tank is probably the real limit, not the battery.** At the patent's ~1 L/min ozone-water flow, 8 L is about 8 minutes of jetting in total. That means a return to the dock for refills, or very sparing jetting. *This assumes the production robot uses the patent's flow rate.*
- **"70% of tasks"** means a cleaner is still needed for the remaining 30%, probably consumables, bins and heavy dirt.
- **Footprint:** 409 mm wide fits through a standard stall door. 1.31 m tall and 128 kg is heavy, so it needs level floors and lifts (consistent with the "elevator ride" claim).
- **Squat-toilet support is claimed.** It is the **first competitor in our files to claim it**, which matters for India.

### Earlier second-hand feature list `[CC][S024*]` (via S001)
Toilet-bowl sanitising; "high-pressure e-water jetting"; floor mopping; autonomous navigation; self-charging; water management; blower drying; mirror polishing. *The official page text (S042) says "E-water Jetting" with **no "high-pressure"**. The patent's ~1 L/min flow is low (S041). Treat "high-pressure" as unconfirmed `[UNV]`.*

### Robot described in the patent `[V][S041]`
Full detail in the [patent deep dive](primechai-patent-WO2025259178.md).
- **4-wheel mobile base** with a box-shaped body on top, and a **multi-joint arm** that looks like a collaborative ("cobot") arm `[INF]`
- **Automatic tool changer:** about 4 enclosed tool slots on the body. Tools disclosed: a **motorised rotating brush** and a **fan for drying**. Tools attach mechanically and electrically.
- **Ozone water made from tap water** in an on-board electrolytic generator (~24 V, ~1 L/min). Used to rinse fixtures and to **wash the tools inside the robot**. There is also a **separate chemical tank** and a **waste tank**.
- Jets are mounted on the arm tip, and a nozzle doubles as a "finger" to **press the toilet flush button**
- **Camera ("identification reader") recognises fixture types:** toilet bowl, urinal, basin, mirror
- **May** detect stains and **may** check that no stains remain before finishing (description only; not claimed)
- Pre-programmed cleaning routine per fixture. Can run anywhere from operator-pushed + Start button to fully autonomous.
- **Docking station:** charges, refills tanks, empties waste

> **Arm (updated 2026-10-02):** the website still never *names* an arm, but its listed functions (urinal brushing, surface/mirror wiping, **door opening**, tool self-sanitising, contact-based cleaning) need a manipulator. Together with the patent drawings (S041), **HYTRON very likely has an arm** `[INF]`. This is no longer treated as a conflict, but still needs a photo or video to confirm.
> **E-water:** the website's "self-generation of electrolyzed water" matches the patent's **electrolytic ozone generator** (S041). "E-water" ≈ the patent's ozone water `[INF]`.
> **Navigation:** the website claims autonomous navigation, obstacle avoidance, door opening and riding elevators (S042). None of the patent drawings show navigation sensors, so **the production robot has sensors the patent doesn't show** `[INF]`.

## Hardware & supply chain

**Supplier summary (as of 2026-10-06):**

| Supplier | Component | Status | Source |
|---|---|---|---|
| **Elite Robots** (Shanghai, China) | Robot arm (6-axis cobot) | **Named by Primech** as the example arm in its patent ("such as"); likely, not confirmed for the shipping unit | WO 2025/259179 p.9 `[V][S054]` |
| **NVIDIA** | Jetson Orin "Super" compute | **Named by Primech** | 6-K Aug 2025 `[CC][S044]` |
| Unnamed **China contract manufacturer** | Production / assembly ("300 robots' initial capacity") | **Named by Primech** (partner unnamed) | FY2025 results `[CC][S044]` |
| **SEER Robotics** (Shanghai, China) | Navigation controller (Roboshop), mecanum AGV | Candidate: engineer's résumé; not tied to HYTRON | `[S049]` |
| **Hesai** (Shanghai, China) | 3D LiDAR, model unknown | Candidate: engineer's driver work; not tied to HYTRON | `[S048]` |
| **Kunwei** (China; believed maker of KWR75) | 6-axis force/torque sensor | Candidate: engineer's driver work | `[S048]` |

*Built from scattered evidence. Each line shows how solid it is.*

> **⚠️ Caveat (2026-10-03, raised by Vishal):** the engineer evidence (S047–S049) shows what **Primech AI's robotics team** works with. It does **not** prove which robot each part belongs to.
> - His résumé lists the **"mecanum wheeled AGV"** (SEER navigation) and the **"fleet of toilet-cleaning robots"** (Open-RMF) as **separate bullets**, so they may be different robots.
> - The Hesai LiDAR work (driver repo) and the HYTRON setup script (a different repo) are **never connected in any file**. A content search of all his text files on 2026-10-03 found no file mentioning both HYTRON and Hesai, SEER or mecanum.
> - Primech AI may have other robot projects, e.g. the WELLE industrial-robot JV (Dec 2025).
> - **Treat every row below marked "HYTRON `[INF]`" as a candidate, not a finding.** Only a photo, datasheet or certification record of HYTRON itself can confirm a part.

| Component | Evidence | Confidence |
|---|---|---|
| **Compute** | **NVIDIA Jetson Orin "Super"** module | `[CC][S044]` named by Primech |
| **Manufacturing** | Unnamed **China production partner**, "targeting 300 robots' initial production capacity" (Jul 2025) | `[CC][S044]` |
| **Mobile base / navigation controller** | An engineer's résumé: "Configure **Seer-roboshop** navigation & SLAM for **mecanum wheeled AGV**" at Primech AI (2026). **Roboshop is the configuration software for SEER Robotics' (仙工智能, Shanghai) AMR navigation controllers** (general knowledge) | `[V][S049]` that Primech AI uses SEER software. **That it's HYTRON's base is `[INF]`**: same résumé entry mentions the toilet-cleaning robot fleet, but Primech AI may have other robots |
| **Wheels** | **Mecanum** (omnidirectional) wheels. Consistent with the patent's 4-wheel base that "permits movement in a plurality of directions" | `[V][S049]` + `[V][S041]`; link to HYTRON `[INF]` |
| **3D LiDAR** | Primech AI's engineer added a `set_standby` service to the **Hesai LiDAR ROS 2 driver** (10 Jul 2026). It sends Hesai's standby command straight to the device, which only makes sense with **real Hesai hardware connected**. Hesai is a Chinese LiDAR maker, Shanghai. **The model isn't identified**: the change touches no configuration, and the standby command works on all Hesai ranges (Pandar, QT, XT, AT, FT, JT). Checked 2026-10-03 | `[V][S048]` that he works with a physical Hesai LiDAR at Primech. **That HYTRON uses it is `[INF]`, likely but unproven**: no file links the two directly |
| **2D laser scanner** | laser_filters fork (Jul 2026) has **no changes of his own** (0 commits ahead of upstream) | **No evidence**, just a bookmark-style fork |
| **Force/torque sensor** | ROS 2 driver for the **KWR75** 6-axis force/torque sensor, forked and fixed in May 2026. KWR75 is believed to be made by **Kunwei (坤维科技), China** (general knowledge; verify). Probably sits at the arm's wrist to control brush pressure `[INF]` | `[V][S048]` that he works with it; HYTRON use `[INF]` |
| **Direct HYTRON link** | His workstation-setup repo has **`hytron.yml`** ("Hytron setup", 15 Jun 2026), which installs Docker on hosts in a group called `robots`. The listed host is named **`hytron8`**, user `hytron` | `[V][S048]`. Proves he works on HYTRON robots' onboard computers. **"hytron8" hints that at least ~8 units have been numbered** `[INF]` (could include prototypes) |
| **Fleet management** | **Open-RMF** (open-source fleet middleware that integrates lifts and doors) for "an autonomous fleet of toilet-cleaning robots". **This explains the "elevator ride" and "door opening" claims** `[INF]` | `[V][S049]` |
| **Robot arm** | **Elite Robots (Shanghai, China)** is named as the example arm: "any suitable robotic arm, such as those supplied by Elite Robots (Shanghai, China)" (WO 2025/259179, p.9). The drawings in both patents look like a 6-axis cobot | `[V][S054]` that Elite is named. **That the shipping HYTRON uses Elite is `[INF]`, the leading candidate**; the wording is "such as" |
| **Camera** | Wrist camera on the gripper (patent); brand unknown | `[V][S041]` |
| **Ozone / e-water** | On-board electrolytic generator, ~24 V; supplier unknown `[V][S041]`. **`[CONFLICT]`:** the twin patent WO 2025/259179 describes a **detergent → brush → clean-water rinse** cycle and never mentions ozone or e-water `[V][S054]` | `[V][S041]`, `[S054]` |
| **Docking station** | Website: 230×460×590 mm, automatic water supply/discharge and charging `[CC][S042]`. Patent: holds **clean-water and detergent supply tanks**, drains via hose to a **drainage pipe**, motorised lid, 2 charging terminals. Robot docks using **QR codes + wrist camera**; the arm plugs a 3-port connector (clean / detergent / waste) into the robot; wireless link robot↔station | `[V][S054]` |
| **Import finance** | HSBC import-finance facility S$0.5M for Primech AI | `[V][S043]` |

**Analysis** `[INF]`:
- **Primech AI's robotics team** works with a largely Chinese component set: **Elite Robots arm**, SEER navigation controller, Hesai LiDAR, Kunwei F/T sensor, plus a China contract manufacturer. **Tied to HYTRON by Primech itself: the China manufacturer, Jetson Orin compute, and Elite Robots (named in its patent as the example arm)**; the rest are HYTRON *candidates* (see caveat above). **Primech's own value-add looks like integration, the cleaning tools and e-water module, and software** (ROS 2, Open-RMF, Docker).
- **There's a Hong Kong engineering team** (Josef, at HK Science Park, since Mar 2026). That is the same month Zhang Youwei moved to Primech AI's payroll before being terminated, which suggests Primech **rebuilt or expanded the software team in Hong Kong** after the CTO dispute.
- **For Ubanthu:** *if* HYTRON uses this kit, its navigation stack is largely off-the-shelf (SEER + Hesai + Open-RMF). Even if it doesn't, the team's skills point the same way. Primech's moat isn't navigation. It's distribution plus the cleaning end-effector. **Contamination perception isn't in any of this evidence.**

**How to firm this up:**
- Find HYTRON photos and videos and look for a SEER controller, a Hesai LiDAR (JT-series mini LiDARs are a common fit for cleaning robots) and a Kunwei sensor at the wrist.
- Check other Primech AI engineers' LinkedIn and GitHub profiles.
- Check Josef's blog for project posts.

## Business / customers / deployments

- **Captive demand:** the parent is a facilities-services company and runs HYTRON in its own cleaning fleet `[V][S043]`
- **Unit counts: none disclosed anywhere** (checked all SEC filings, 2026-10-02). FY2026 robot lease revenue was US$12k `[V][S043]`. Pricing: _unknown_

### Deployments and market-entry deals, by region

| Region | Status | Detail | Sources |
|---|---|---|---|
| Singapore | **Deployments claimed** | Temasek Polytechnic, a major mall, one of the largest hospitals (Jul 2025); army camp lease (Nov 2025); own fleet | `[CC][S044]`, `[V][S043]` |
| Hong Kong | MoU | Chinachem / Nina Tower 1 (Mar 2025); no deployment confirmed since | `[CC][S044]` |
| Greater China | Distribution MoU | Savills (Aug 2025) | `[CC][S044]` |
| **South Korea** | **Distribution agreement** (~Mar–Apr 2026 `[INF]`) | Unnamed local distributor: marketing, sales, deployment, support, local certification. **Starts with a trial period and a trial order.** Only "upon successful market validation" *may* it become exclusive and multi-year with minimum order commitments. **"Projected ~US$4.08M over 3 years"** depends on that conversion, so it is **not a committed order** `[INF]`. **Not disclosed in the 20-F or any 6-K.** | `[3P][S045][S046]` |
| Japan | "Partnership" | Golden Rim Investment; Tokyo expo | `[CC][S044]` |
| EU (DE/AT/CH) | Distributor only | TCOrobotics GmbH; Berlin trade show; **no sale or CE marking evidenced** | `[CC][S044]` |
| Dubai | Plan only | In the Mar 2025 "300 robots" plan | `[CC][S044]` |
| US | Market entry | Primech USA; Aramark forum; CES Jan 2026 | `[CC][S044]` |

**Korea deal analysis** `[INF]`:
- The US$4.08M is the *maximum* if every phase converts. That's about **US$1.4M a year**, which is significant next to the US$12k of FY2026 robot revenue.
- Primech left it out of its SEC filings despite the size. That suggests either it isn't treated as committed or material, or it hadn't been finalised.
- The distributor is **unnamed**. That matters for us: it is likely an established Korean facilities or robotics distributor.
- **The distributor will "manage local certification requirements" (KC mark).** Korean certification filings name the manufacturer, which is another possible route to Primech's Chinese production partner.

## People Directory

| Photo | Name | Role | Background (short) | LinkedIn | Sources |
|---|---|---|---|---|---|
| — | **Kin Wai "Ken" Ho** | Chairman & CEO, Primech Holdings; patent inventor | Age 50; business and investment background (Sapphire Universe; ex-CEO of Jimu Group, a footwear company; JP Morgan programmer 2000–01) | _not captured_ | S041, S043 |
| — | **Charles Ng Chew Poh** | COO, Primech AI; patent inventor | Spokesperson in the HYTRON press releases | _not captured_ | S041, S044 |
| — | **Zhang Youwei** | **Former CTO**, Primech AI. Employed by Primech May 2024 – Mar 2026, then by Primech AI until **suspended and fired** (date not disclosed; before Aug 2026). **49% shareholder**; first-named patent inventor | **In litigation with Primech** (suit filed 7 Aug 2026; counterclaim 15 Sep 2026) | _not captured_ | S041, S043, S044 |
| — | Kit Yu Lee | CFO, Primech Holdings | | | S043 |
| — | Hansel Loo | SVP Operations | | | S043 |
| — | Yew Jin Sng | SVP Business Development | | | S043 |
| <img src="people/josef-gstoettner_linkedin.png" width="60"> | **Josef Gstoettner** | **Senior Robotics Software Engineer, Primech AI** (since Mar 2026), Hong Kong Science Park | ROS 2, SLAM & navigation; ex-HKCRC, LSCM, HKUST. **Best supply-chain lead so far** (see the card below) | [LinkedIn](https://www.linkedin.com/in/josef-gstoettner-437630172/) · [GitHub](https://github.com/JosefGst) | S047, S048, S049 |
| <img src="people/patrick-yeung_linkedin.png" width="60"> | **Patrick Yeung** | **Head of System Architect, Primech.ai** (May 2026 – present), Hong Kong | Systems/IoT architect from consumer electronics and construction tech: ex-SCIL (R&D Manager), VTech, Signify; MSc EE (CUHK) | [LinkedIn](https://www.linkedin.com/in/patrick-yeung-4b501091/) | S050 |
| <img src="people/ivan-immanuel_linkedin.png" width="60"> | **Ivan Immanuel** | **Robotics Software Engineer, Primech.ai** (Jul 2026 – present), Singapore, on-site | Headline: ROS2, **Computer Vision**, Machine Learning. Career switcher: 6 yrs semiconductor process engineer (Micron); MS Robotics & Autonomous Systems (JHU, May 2026) | [LinkedIn](https://www.linkedin.com/in/ivan-immanuel/) | S051 |
| <img src="people/mohamad-hafizuddin-majek_linkedin.png" width="60"> | **Mohamad Hafizuddin Majek** | **Robotics Service Engineer, Primech.ai** (Mar 2026 – present), Singapore, on-site | Field service for robots: ex-**KABAM Robotics** field service engineer; ex-**DF Automation & Robotics** (Malaysia) senior engineering manager, 8.5 yrs; UTM Mechatronics | [LinkedIn](https://www.linkedin.com/in/mohamad-hafizuddin-majek/) | S052, S053 |

Full management list and bios: [SEC deep dive §6](primechai-sec-filings.md).

**Team build-out, Mar – Jul 2026** `[V][S047–S053]`, `[INF]` where marked:

| Joined | Person | Role | Base |
|---|---|---|---|
| Mar 2026 | Josef Gstoettner | Senior Robotics Software Engineer (navigation/SLAM) | Hong Kong |
| Mar 2026 | Mohamad Hafizuddin Majek | Robotics Service Engineer | Singapore |
| May 2026 | Patrick Yeung | Head of System Architect | Hong Kong |
| Jul 2026 | Ivan Immanuel | Robotics Software Engineer (CV/ML) | Singapore |

- **All four joined between Mar and Jul 2026.** That is the window in which former CTO Zhang Youwei moved to Primech AI's payroll (Mar 2026) and was then suspended and fired (before Aug 2026). It looks like **a rebuilt technical team after the CTO dispute** `[INF]`.
- **Two hubs:** Hong Kong (software/architecture, at HK Science Park) and Singapore (deployment and service).
- **A field service engineer was hired**, which means robots are in the field and need maintenance `[INF]`. He came from **KABAM Robotics**, whose "Manny" robot is in Primech's own fleet (20-F), so he may already have serviced Primech sites `[INF]`.
- **The only person on file with computer vision in their profile is Ivan**: a junior robotics hire (Jul 2026), fresh from a part-time master's, previously in semiconductor process engineering. **There is no evidence of a senior CV or perception lead.** This fits the earlier finding that contamination perception is weak or absent `[INF]`.
- **Patrick's background is IoT, cloud and construction tech** (VTech, Signify, Sanfield), not robot manipulation. Under him, the "system architecture" is likely fleet, IoT and cloud integration (cf. Open-RMF, the task-management dashboard, building-system integration) `[INF]`.
- **Still unknown:** who leads mechanical and arm work, and who replaced the CTO. No one on file has a CTO title.

### Person cards

#### Josef Gstoettner: Senior Robotics Software Engineer, Primech AI
<img src="people/josef-gstoettner_linkedin.png" width="110">

| Field | Value |
|---|---|
| Current role | **Senior Robotics Software Engineer, Primech AI**, **2026/3 – present**, based at "Sciences Park" (Hong Kong Science Park `[INF]`) `[S049]`. LinkedIn shows Primech.ai as current company `[S047]` |
| Headline | Robotics Software Developer, ROS2, SLAM & Navigation, C++, Python, Docker, CI/CD `[S047]` |
| Location | Hong Kong SAR `[S047]`; GitHub location Hong Kong `[S048]` |
| Work at Primech AI (from his résumé) `[S049]` | "Set up servo motor control, navigation & SLAM for **mecanum wheeled AGV**" · "Implement **Open-RMF** to manage an autonomous **fleet of toilet-cleaning robots**" · "Configure **Seer-roboshop** navigation & SLAM for mecanum wheeled AGV" · Docker packaging; CI/CD for the whole ROS 2 software stack |
| Previous `[S049]` | **HKCRC** (Hong Kong Centre for Construction Robotics `[INF]`), Assistant Research Engineer, 2025/9 – 2026/3: water-tank cleaning robot (behaviour trees, coverage planning) · **LSCM** (HK Logistics & Supply Chain MultiTech R&D Centre `[INF]`), System Engineer, 2022/4 – 2024/8: SLAM (Cartographer, SLAM Toolbox), AprilTag docking · **HKUST** Research Assistant, 2020/7 – 2022/3: embedded/IoT |
| Languages | German (native), English, Mandarin (limited working) `[S049]` |
| GitHub activity during his Primech period `[S048]` | **Hesai LiDAR ROS 2 driver** fork (10 Jul 2026), adding his own **"standby" service** to switch the LiDAR off and on · **KWR75 force/torque sensor ROS 2 driver** fork (4 May 2026), adding his own fixes and CI · **`hytron.yml`** setup script for robot host `hytron8` (15 Jun 2026) · laser_filters fork (no changes of his own) |
| Links | [LinkedIn](https://www.linkedin.com/in/josef-gstoettner-437630172/) · [GitHub](https://github.com/JosefGst) · [Blog](https://josefgst.github.io/blog/) |
| Sources | S047 (LinkedIn screenshot, 2026-10-03), S048 (GitHub repos), S049 (public résumé in his GitHub `resume` repo) |

#### Patrick Yeung: Head of System Architect, Primech.ai
<img src="people/patrick-yeung_linkedin.png" width="110">

| Field | Value |
|---|---|
| Current role | **Head of System Architect, Primech.ai**, May 2026 – present (6 mos) `[S050]` |
| Headline | "MSc · Award-Winning Innovator · Advancing AI, Autonomous Robotics & AIoT in PropTech, ConTech & Construction" `[S050]` |
| Location | Hong Kong SAR `[S050]` |
| Previous `[S050]` | R&D Manager, **SCIL – Sanfield Construction Innovations Ltd**, May 2024 – Jan 2026 · Technical Director, **VTech** (偉易達), Sep 2023 – May 2024 · Lead System Architect, **Signify**, Mar 2022 – Sep 2023 · Consultant, VTech, Apr 2019 – Feb 2021 (Tai Po, HK). AWS listed as a skill on the VTech and Signify roles. More roles behind "Show all", not captured |
| Education | MSc Electronic Engineering, **The Chinese University of Hong Kong**, 2003 – 2005 `[S050]` |
| LinkedIn | [https://www.linkedin.com/in/patrick-yeung-4b501091/](https://www.linkedin.com/in/patrick-yeung-4b501091/) · 139 connections |
| Source | S050: LinkedIn screenshots (header + experience), captured 2026-10-06 |

#### Ivan Immanuel: Robotics Software Engineer, Primech.ai
<img src="people/ivan-immanuel_linkedin.png" width="110">

| Field | Value |
|---|---|
| Current role | **Robotics Software Engineer, Primech.ai**, full-time, **Jul 2026 – present** (4 mos), Singapore, on-site `[S051]` |
| Headline | "Robotics Software Engineer · ROS2 · **Computer Vision** · Machine Learning" `[S051]` |
| Location | Singapore `[S051]` |
| Previous `[S051]` | **Micron Technology**, Singapore, 6 yrs: Senior Process Engineer, Dec 2022 – Jan 2026 (photolithography: overlay and imaging); Process Engineer, Feb 2020 – Nov 2022 · Corporate Research Intern, **Bosch Singapore**, Jun – Dec 2018 (force-feedback and flexible-film actuators for haptics) |
| Education | **MS Robotics & Autonomous Systems, Johns Hopkins Engineering for Professionals**, Jan 2025 – May 2026, GPA 4.00 (ROS, motion planning) · BE Mechanical Engineering, **NTU Singapore**, 2016 – 2019 `[S051]` |
| LinkedIn | [https://www.linkedin.com/in/ivan-immanuel/](https://www.linkedin.com/in/ivan-immanuel/) · 289 connections · verification badge |
| Source | S051: LinkedIn screenshots (header + experience), captured 2026-10-06 |

#### Mohamad Hafizuddin Majek: Robotics Service Engineer, Primech.ai
<img src="people/mohamad-hafizuddin-majek_linkedin.png" width="110">

| Field | Value |
|---|---|
| Current role | **Robotics Service Engineer, Primech.ai**, full-time, **Mar 2026 – present** (8 mos), Singapore, on-site `[S052]` |
| Headline | "Engineering Passionate" `[S052]` |
| Location | LinkedIn: Skudai, Johore, Malaysia `[S052]`. Works on-site in Singapore |
| Previous `[S052]` | Field Services Engineer, **KABAM Robotics**, Singapore, Jun 2024 – Mar 2026 · Senior Engineering Manager, **DF Automation & Robotics**, Skudai, Johor, Malaysia, Jul 2015 – Dec 2023 (8 yrs 6 mos) |
| Education | Bachelor's, Mechatronic, **Universiti Teknologi Malaysia (UTM)**, 2012 – 2016; Diploma, Mechatronic, UTM, 2008 – 2011 `[S052]` |
| Other (Facebook, work section only) `[S053]` | Former alumnus and ex-team leader, **UTM Robocon Team**. Facebook still lists "FSE at KABAM Robotics, 25 June 2024 – Present", which is **out of date** compared with LinkedIn (Primech since Mar 2026) `[CONFLICT]`; LinkedIn is treated as current. Personal details from Facebook deliberately not recorded |
| LinkedIn | [https://www.linkedin.com/in/mohamad-hafizuddin-majek/](https://www.linkedin.com/in/mohamad-hafizuddin-majek/) · 133 connections · verification badge |
| Sources | S052 (LinkedIn screenshots), S053 (Facebook "Work" section screenshot), captured 2026-10-06 |

*Inventors are likely the core robotics/engineering team `[INF]`. Their exact roles at Primech are not known yet.*

## Assessment `[INF]`

- **(Updated 2026-10-02) HYTRON's maturity is doubtful.** The former CTO, who led its development, was suspended and fired by Primech AI (date not disclosed; before Aug 2026) and is now being sued by Primech for misrepresenting milestones and source-code delivery. Robot revenue is ~US$12k a year, against announcements of a 300-robot rollout, 250+ inquiries and a "World Tour". **Their marketing is well ahead of their delivery.** It is a weaker near-term competitor than its press releases suggest, but it has strong distribution: its own cleaning workforce, Savills, Chinachem and Aramark contacts.

- **Key advantage: captive demand.** The parent is a facilities-services company, so it deploys its own robots. Its financial filings are a good source for unit counts and economics.
- **Technology direction** (from the patent): a mobile base with an arm that swaps tools, with **ozone-water disinfection as the headline idea**. Perception appears basic: fixture-type recognition, tools found by stored position, and a fixed routine for each fixture.
- Stain detection and cleaning verification are mentioned but not developed. This is **an opening for Ubanthu's contamination-vision work**.
- **A full-restroom generalist on paper** (S042): toilets including squat, urinals, sinks, countertops, mirrors and floors, plus doors and lifts. It is the broadest service range of any competitor we have on file. Its dashboard reports task status, not cleanliness.
- India is a designated state in the patent filing. Watch for Indian national-phase entry (around Jan 2027) as a sign of plans for India.

## Open questions

- [ ] Photo or video confirming HYTRON's arm and tool changer
- [ ] Fleet size and unit economics from the 20-F (S025)
- [ ] Price / RaaS model (robot-as-a-service)
- [x] ~~Time per toilet~~: ~6 min toilet, ~3 min basin or urinal `[CC][S042]`
- [ ] Restrooms per tank fill (8 L fresh water): does it return to the dock mid-shift?
- [ ] How does it clean squat toilets (Indian or Asian style)? Demo?
- [ ] Which tasks make up the 30% it doesn't cover?
- [ ] Ozone concentration (ppm). The ">99% bacterial reduction" claim (6-K, 9 Oct 2025) names **no lab, organism or protocol** `[CC][S044]`. Get the test report.
- [ ] "UV bacteria detection" listed for HYTRON Mark 2 (Jan 2025 investor deck). What is it, and has it shipped? **This is directly relevant to Ubanthu.**
- [ ] Outcome of the Zhang lawsuit: who owns HYTRON's code and IP?
- [ ] What sensors does it use to navigate (LiDAR, cameras)? How does it open doors?
- [ ] Inventors' roles and LinkedIn profiles; CEO/CTO of Primech AI
- [ ] Other Primech patents; Indian national-phase filing for WO 2025/259178

*Note (2026-10-02): `Doc1.docx` in this folder was rechecked and is a blank Word file with no text and no images. It is not a source.*
