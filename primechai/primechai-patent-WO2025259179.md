# Primech AI patent: WO 2025/259179 "A System and Method for Making a Fluid Connection Between a Cleaning Robot and a Base Station"

[← Primech AI profile](primechai.md) · [← Master document](../COMPETITOR_INTELLIGENCE.md) · Sister patent: [WO 2025/259178](primechai-patent-WO2025259178.md) · Source: **[S054]** · **Added:** 2026-10-06

**Files:**
- Original scan (no text layer): [WO_2025259179_A1.pdf](WO_2025259179_A1.pdf)
- **Searchable copy (OCR text layer):** [WO2025259179_OCR.pdf](WO2025259179_OCR.pdf)
- Plain text by page: [WO2025259179_OCR.txt](WO2025259179_OCR.txt)
- Drawing sheets as images: [patent_figures/](patent_figures/) (`WO2025259179_drawing_sheet_p20–p24.png`)

**Review coverage:** all 26 pages read on 2026-10-06. That includes the full OCR text (description, 24 claims, search report) and all 6 drawing sheets viewed as images. The search report's citation categories were checked against the original scan, because the OCR dropped one category letter. Page numbers below are **PDF pages**.

---

## Bibliographic data `[V]` (p.1)

| Field | Value |
|---|---|
| Publication | **WO 2025/259179 A1**, published **18 Dec 2025** (same day as WO 2025/259178) |
| Application | PCT/SG2025/050334, filed **15 May 2025** (next number after 259178's PCT/SG2025/050333) |
| Priority | **SG 10202401737P, 14 Jun 2024** (next number after 259178's SG 10202401736R, same day) |
| Applicant | Primech AI Pte. Ltd., 23 Ubi Crescent, Singapore 408579 |
| Inventors | **Zhang Youwei, Ng Chew Poh, Ho Kin Wai**, the same three as 259178 |
| Agent | Yusarn Audrey LLC, Singapore |
| IPC | B25J 9/16 (programme control of manipulators), B25J 11/00, B25J 13/08, B25J 15/00, A47L 11/40 |
| Designated states | All PCT states incl. **IN (India)**, US, CN, JP, KR, EP |
| Search authority | Korean IPO, 13 Aug 2025 |

**These are twin filings** (consecutive numbers, same day, same inventors). Together they describe one robot: 259178 covers the **cleaning system** (ozone water, arm, tool dock); 259179 covers **docking for refilling and draining**.

## What it claims (p.15–18)

The robot **uses its own arm to plug itself into the docking station** for water refill and waste drain. There are no fixed ports.

| Claim(s) | What | Page |
|---|---|---|
| **1** (method) | Robot drives to the base station → **its arm picks up a connector from the station** → plugs it into a connector on the robot → fluid transfers through it. The arm may alternatively be on the station. | p.15 |
| 2–4 | Robot-side connector **slides out through a spring-loaded trap door**, and retracts after use | p.15 |
| 5–8 | **Connection check:** robot sends a signal through the connector and the station loops it back; if the robot reads it, the connection is good | p.15–16 |
| **9** (system) | Station with a removable connector + robot with a connector + an arm (on either) that joins them | p.16 |
| 10–15 | As 2–8, system version | p.16–17 |
| **16** (robot) | Robot with a **retractable connector** that extends out of the body | p.17 |
| 17–20 | Actuator, **guide rails**, trap door, electrical check contacts | p.17–18 |
| **21** (base station) | Station with a connector that **sits removable on a support** | p.18 |
| 22–24 | Connector has a **grip handle**, a **marker for locating it**, and looped contacts | p.18 |

## How it works (description, p.3–14)

| Topic | Detail | Page |
|---|---|---|
| **⭐ Robot arm supplier** | "The robotic arm 10 may be any suitable robotic arm, **such as those supplied by Elite Robots (Shanghai, China)**." | p.9 |
| **Camera** | A camera is **mounted on the robot arm**, with "a vision system implemented therein". Same wrist-camera placement as 259178 | p.9, 11 |
| **Docking navigation** | The base station's location and the path to it are **stored in the robot's memory**. Near the station, the robot uses the arm camera to find a **QR code (first marker) on the station**, works out its exact position, aligns, and drives in so the station's **charging terminals plug into the robot's charging ports** | p.11 |
| **Grabbing the connector** | Robot tells the station over **wireless** that it needs a refill or drain → the station **opens a motorised cover** → the arm camera finds a **second QR code on the connector** → the gripper takes the connector's handle (shaped so the two-jaw gripper can't slip) → it is lifted off a **magnetic** support | p.10–12 |
| **Robot-side connector** | A block with **3 ports** (clean water, liquid detergent, waste water), each sealed with a Y-shaped ring. It slides on guide rails, driven by a **lead-screw linear actuator**, and pushes open a spring-loaded trap door | p.9–10 |
| **Connection check** | Robot puts **+5 V** on one contact; the station connector shorts it back; robot reads it. If it fails, the arm puts the connector back and retries. **After more than ~2 attempts it aborts and messages an operator.** | p.10, 12–13 |
| **Fluid transfer** | Robot tells the station over wireless to pump in clean water and/or detergent; the robot pumps out waste water. Can be one after another or simultaneous | p.13 |
| **Base station** | Housing holding a **clean-water supply tank and a liquid-detergent supply tank**; the waste line goes by hose to a **drainage pipe**. Has a lid over the connector and **2 charging terminals** | p.10–11 |
| **Claimed precision** | "With the vision system and robotic arm 10, a **docking accuracy of about 0.02 mm** may be achieved." | p.14 |
| **When it docks** | Low battery, low clean water or detergent, or full waste tank. Afterwards it **resumes the job where it left off** | p.11, 13 |
| **⚠️ Cleaning cycle described** | "the **liquid detergent** is drawn … and sprayed onto a cleaning surface. The robot picks up a **brush** … and scrubs … then draws water from the **clean water tank** and sprays it … to rinse off the liquid detergent. The robot cleans the brush by spraying the liquid detergent and/or the clean water on the brush." **No ozone, e-water or electrolysis is mentioned anywhere in this patent.** | p.9 |
| **Prior art they criticise** | CN220024922U (Lee et al., "water changing base station"): blind docking is inaccurate; ports stick out (bigger footprint, safety hazard); seals only press together (leak risk) | p.3 |

## Drawings (p.19–24) `[V]`

- **Fig. 2A/2B (p.20):** same robot as 259178: a box body on a separate wheeled base, with a multi-joint arm on top. The base shows **two large wheel arches per side** plus a front bumper. In 2B the arm holds the station's connector over the robot's extended connector. The **base station is a small box** with a hinged lid and **charging terminals at the bottom** where the robot docks.
- **No LiDAR, navigation sensor or body camera is drawn.** Same as 259178.
- Figs. 3–8: the connector, linear actuator, trap door and gripper handle (cross-ribbed, matching 259178's jaw grooves). A faint word, **"since", appears on the mounting plate in Fig. 7 (p.23)**. It could be a part-maker's stamp, but it's unreadable and unidentified.

## Search report (p.25–26) `[V]` (categories checked on the scan)

| Citation | Category | Against claims |
|---|---|---|
| **KR 10-2014-0036653 A (LG Electronics, 2014)** | **X** (not new / not inventive on its own) | **16–17** (the retractable robot connector + actuator) |
| same LG document | Y | 2–5, 10–12, 19 |
| US 2007-0051757 A1 (Lim et al., 2007) | Y (not inventive when combined) | 1–5, 9–12, 19, 21–23 |
| US 2024-0066707 A1 (Samsung, 2024) | Y | 1–5, 9–12, 21–23 |
| KR 10-2023-0139407 A (**Doosan Robotics**, 2023) | A (background) | 1–24 |
| CN 205521358 U (Zhou Ying, 2016) | A | 1–24 |

**Not hit by X or Y:** claims **6–8, 13–15, 20, 24** (the looped-signal connection check) and **18** (guide rails). These narrower claims have the best chance of surviving examination `[INF]`.

---

## Analysis `[INF]`: what's interesting

1. **First named hardware supplier for the robot itself: Elite Robots (Shanghai).** It's worded as an example ("such as"), not a definitive statement, but **companies usually name the arm they actually built with**. Elite Robots makes 6-axis collaborative arms (CS/EC series; general knowledge). Combined with the 259178 drawing, which looks like a 6-axis cobot, **Elite is now the leading candidate for HYTRON's arm**. *Strength: patent text, `[V]` that it's named; that the shipping HYTRON uses Elite is `[INF]`, likely.*
2. **⚠️ Contradiction with the sister patent and the marketing:** this patent describes a **detergent → brush → clean-water rinse** cycle and **never mentions ozone or e-water**. WO 2025/259178 (same day, same inventors) is built around ozone water, and the website says "self-generation of electrolyzed water". Possible explanations: the two filings describe different stages of the prototype; the docking embodiment was written generically; or ozone/e-water was added later. **Either way, chemical detergent is part of the cycle in both patents.** That fits the website's 1.5 L detergent tank and undercuts any pure "chemical-free" pitch.
3. **The arm does triple duty:** cleaning, tool changing, *and* plugging into its own dock. This is a clever way to avoid fixed docking ports, but it means **every refill costs arm time** (find QR, grab connector, plug in, check, retry). It also explains the website's "automated water and wastewater handling".
4. **Their perception is QR codes plus a wrist camera.** Docking uses QR markers on both the station and the connector. That's robust but basic: there's **no learned perception** here either, consistent with 259178.
5. **"0.02 mm docking accuracy" is implausible** for a mobile robot plus cobot plus wrist camera. That's about the stated repeatability of a good cobot arm alone (general knowledge). Treat it as a marketing-grade claim; no test data is given.
6. **The base station needs plumbing or manual refilling.** It holds its own clean-water and detergent supply tanks, and drains to a drainage pipe. Deployment needs a drain point near the station, which is a **real installation constraint** for restrooms.
7. **Failure handling is minimal:** two connection attempts, then "send an appropriate error message to an operator". A human is still in the loop.
8. **The connection check (claims 6–8, 13–15, 20, 24) is the only part not hit by prior art.** It's a simple signal loop-back; even if granted, it's **easy to design around**. The core idea (claims 1, 9, 16, 21) faces LG, Samsung and Lim prior art.
9. **India is designated again.** National-phase deadline ≈ **14 Jan 2027** (31 months from 14 Jun 2024; general knowledge of Indian rules), the same as 259178.
10. **Every inventor is now either the CEO, the Primech AI COO, or the fired ex-CTO who is suing** (S044). Zhang claims some IP pre-dates his employment, which could affect both patents' ownership.

## Missing info / gaps about the robot and its tech

| Gap | Why it matters | Where to look |
|---|---|---|
| **Which Elite arm model** (payload, reach) | Cost, reach into toilet bowls, safety | HYTRON photos (Elite arms have recognisable joints and branding); Elite Robots case studies |
| **Ozone vs detergent: what the shipping robot actually uses** | The core hygiene claim | Datasheet; ask a distributor; the >99% test report |
| **Navigation sensors** (LiDAR model, depth cameras) | Not shown in either patent's drawings | Photos; Josef's Hesai work is a candidate (S048) |
| **Base station plumbing**: mains water / drain or tank-only? | Installation cost | Datasheet; the website's "Water Supply & Discharge: Automatic" |
| **Time per refill/drain cycle** | Throughput (8 L tank, see analysis in profile) | Demo video |
| **Wireless link robot ↔ station** (Wi-Fi? BLE? proprietary) | Integration and reliability | Not stated |
| **Charging power / port design** | Downtime | Not stated (website: 2 h charge) |
| **The "since" marking in Fig. 7** | Possible component-maker clue | Original high-res drawings (Patentscope) |
| **Grant status in any country** | Freedom to operate | Patentscope national phase tab (after Dec 2026 / Jan 2027) |
