# Primech AI patent: WO 2025/259178 "A Cleaning Robot"

[← Primech AI profile](primechai.md) · [← Master document](../COMPETITOR_INTELLIGENCE.md) · Twin patent: [WO 2025/259179](primechai-patent-WO2025259179.md) (docking; names Elite Robots arm; describes a detergent cycle with no ozone) · Source: **[S041]** · **Added:** 2026-10-02

**Files:**
- Original scan: [WO2025259178-PAMPH-20251218-0050.pdf](WO2025259178-PAMPH-20251218-0050.pdf). Image-only, not searchable.
- **Searchable copy (OCR text layer):** [WO2025259178_OCR.pdf](WO2025259178_OCR.pdf)
- Plain text by page: [WO2025259178_OCR.txt](WO2025259178_OCR.txt)
- Drawing sheets as images: [patent_figures/](patent_figures/)

Page numbers below are **PDF pages** (p.1 = cover).

**Review coverage:** all 45 pages were read on 2026-10-02: the full OCR text (description, claims, search report) and all 5 drawing sheets (Figs. 1–15, viewed as images).
- **Known OCR errors:** the drawing sheets (p.38–42) have little readable text because they are figures. A few typos also appear in the text, e.g. "[oca9]" for [0009] and "Limin" for L/min. Check the original scan for exact wording before quoting a figure label or number.

---

## Bibliographic data `[V]` (p.1)

| Field | Value |
|---|---|
| Publication | **WO 2025/259178 A1**, published **18 Dec 2025** |
| Application | PCT/SG2025/050333, filed **15 May 2025** |
| Priority | **SG 10202401736R, 14 Jun 2024** |
| Applicant | **Primech AI Pte. Ltd.**, 23 Ubi Crescent, Singapore 408579 |
| Inventors | **Zhang Youwei**, **Ng Chew Poh**, **Ho Kin Wai** (all at the Primech address) |
| Agent | Yusarn Audrey LLC, Singapore |
| IPC classes | B25J 11/00, B25J 13/08, B25J 15/00 (robot manipulators); A47L 11/40 (floor-cleaning machines) |
| Designated states | All PCT states, **including IN (India)**, US, CN, JP, EP, etc. |
| Search authority | Korean IPO. Search report dated 18–19 Aug 2025 (p.43–45) |

## What the patent actually claims (p.33–37)

**Core claim (Claim 1):** a mobile cleaning robot with a water tank, an **ozone generator** that turns the tank water into **aqueous ozone** (ozone dissolved in water), and an outlet that sprays that ozonated water to clean. Claim 21 is the matching *method* claim.

So **the invention is centred on the ozone-water chemistry, not on vision or manipulation.** The arm, tools and camera appear only in dependent claims (claims that add detail on top of claim 1):

| Claim | Adds | Page |
|---|---|---|
| 2–6 | **Electrolytic** ozone generator (makes ozone by passing current through the water); on only while water is pumped; **about 24 V**; chamber **about 500–1000 mL (pref. 700–800 mL)** | p.33–34 |
| 7 | All tank water must pass through the ozone generator; no bypass | p.34 |
| 8–10 | Second outlet that washes the **robot's own tools** with ozone water; waste tank for the dirty runoff | p.34 |
| 11 | Separate **chemical cleaning-liquid tank** and outlet | p.35 |
| 12 | **Movable arm** on the body, with the tip moving in several directions | p.35 |
| 13–16 | **Tool dock** on the body; arm picks up and puts down tools; tool attaches mechanically *and* electrically; gripper stops the tool twisting or sliding | p.35 |
| 17 | **"Identification reader"** that identifies the environment or its features | p.35 |
| 18–19 | Ozone-water and chemical outlets are mounted on the arm tip | p.35 |
| 20 | Removable, rechargeable battery | p.36 |
| 22–27 | Method: pick up a **rotating brush tool** and press it on the surface; return the tool to the dock and wash it with ozone water; **fan tool** for drying; apply chemical | p.36–37 |

## How the robot works (description, p.3–30)

| Capability | What the patent says | Page |
|---|---|---|
| **Form factor** | Box-shaped body on a separate **4-wheel mobile base**. A **multi-joint arm** is mounted on top. Angled touchscreen and a physical emergency-stop button. The body and base can be separated for repair | p.10–11, 20–21; Figs. 1–4 (p.38–39) |
| **Arm** | Multi-segment arm with several rotating joints, reaching in x/y/z for "three-dimensional cleaning" of toilet bowls, urinals and basins. The arm's maker and number of joints are **not stated**. The drawing looks like a 6-axis collaborative ("cobot") arm `[INF]` | p.21; Fig. 1–2 |
| **Tool changing** | **Tool dock** holds tools upright in enclosed slots, so dirty tool heads never touch anything outside the robot. Fig. 4 shows **about 4 slots** `[INF]`. Tool positions are **pre-set**, so the arm finds tools by stored position, not by vision. A **two-jaw gripper** with cross-shaped grooves locks onto each tool's handle; electrical contacts power the tool | p.12, 22–24, 28 |
| **Tools disclosed** | **Brush tool** (motorised rotating brush head; liquid can come out at the bristle base) and **fan tool** (motorised impeller for drying). No other tools are described | p.23–26 |
| **Liquids** | (1) **Ozone water** from **tap water** at about **1 L/min**, through an electrolytic generator. Used for pre-rinsing, rinsing during brushing, and washing tools in the dock. (2) Separate **chemical** tank for degreasing, stain removal and deodorising. (3) **Waste tank** for tool-washing runoff | p.12–19 |
| **Arm-tip nozzles** | Ozone-water jet and chemical spray sit side by side on the arm tip. The chemical nozzle sticks out further so it can act as a **"finger" to press the toilet's flush button** | p.18 |
| **Vision / sensing** | The "identification reader" **"may be a camera"** and identifies fixture types: **toilet bowl, mirror, basin, urinal**. Other optional sensors listed: image, line, proximity, flow, pressure, temperature, tank level | p.22, 29–30 |
| **Stain detection** | The robot **"may be configured to detect stained areas"** and aim the brush at them | p.27 |
| **Cleaning verification** | The robot may decide a fixture is clean "by determining whether there are still any stained areas present", **or** simply finish a fixed series of steps | p.28 |
| **Autonomy** | Described as anything from remote-controlled to semi-autonomous to fully autonomous. An operator **may push it to the toilet and press Start**. Cleaning routines are **pre-programmed per fixture** (e.g. brush first, then fan). The user may enter the **toilet bowl's dimensions and shape** | p.11, 27–28 |
| **Camera placement** | The identification reader (label 320) sits on the **underside of the gripper housing, between the two jaws**, so it is a wrist-mounted camera that looks at whatever the arm points at. **No body-mounted camera, LiDAR or navigation sensor is drawn** | Fig. 10 (p.41) |
| **Tool shapes** | The brush tool has a **dome-shaped head** on a short motor-driven shaft, like a toilet-bowl brush `[INF]`. The fan tool is a compact box with a side air intake and an impeller at the bottom. Each tool has a cross-ribbed handle that matches the gripper's cross-shaped grooves | Figs. 11–15 (p.41–42) |
| **Ozone generator** | A small flanged box with an inlet and outlet pipe, sitting inline in the water line | Figs. 5, 7–8 (p.40–41) |
| **Docking station** | Charges the battery, refills both tanks, empties the waste tank; may also store tools | p.29–30 |
| **Mirror cleaning** | Mirrors are mentioned only as a fixture the camera can recognise. No mirror tool is described | p.3, 22 |

## Prior art cited by the search authority (p.43–45)

The Korean search authority listed one document, **CN 111466837 A** (Guangzhou Deposon Electric Technology, 2020), as making **claims 1–7, 20 and 21 not new or not inventive on their own** ("X" category). Those are the core ozone-robot claims. It and **CN 218484463 U** (Shenzhen Goodix, 2023) were cited against the arm and tool claims 12–13, 15–18 and 22–24 ("Y" category: not inventive when combined with other documents).

Also cited as background ("A" category): US 2023-0270905 A1 (Samsung), WO 2018-019775 A1 (I.M.A. Industria Macchine Automatiche), US 2016-0368135 A1 (Tadayon).

---

## Analysis `[INF]`: what this means for Ubanthu

These are Claude's interpretations, not legal advice. A patent attorney should review before any decision on freedom to operate (the risk of infringing someone's patent).

1. **The patent's protection centres on the ozone-water system, not on perception.** Stain detection and checking cleanliness are mentioned only as "may be configured" in the description. They are **not claimed**, and **no method is disclosed** (no model, dataset, camera setup or algorithm). If granted in this form, **this patent does not appear to cover contamination-detection computer vision.** It does show Primech is thinking about it, and the published text may count as prior art against broad claims we might file on the bare idea of a robot that detects stains and checks its work. Our claims would need to be specific about *how*.
2. **The core claims look weak.** The search authority found that a 2020 Chinese patent already shows claims 1–7, 20 and 21. Expect those claims to be narrowed or dropped when the patent is examined in each country.
3. **India is a designated state.** Primech can still enter **India's national phase**, i.e. file the patent in India specifically. India's deadline is **31 months from the 14 Jun 2024 priority date, about 14 Jan 2027** (deadline from general knowledge of Indian patent rules). Check the Indian patent office (InPASS) after that date to see whether they filed. If they did, it signals real plans for India.
4. **Their perception looks basic.** Tools are found by stored position; the user may enter the bowl's size and shape; cleaning follows a fixed routine for each fixture type. Together this suggests their autonomy relies on **pre-programmed routines with fixture recognition**, not on mapping contamination. If so, that's where we can differentiate.
   - *Update 2026-10-02:* the official product page (S042) claims autonomous navigation, obstacle avoidance, door opening and riding elevators. The production HYTRON therefore has **navigation sensors that the patent doesn't show**. The point above applies to how it *cleans* (fixture routines, stored tool positions), not to how it gets around the building.
5. **The background section admits a weakness in robots like theirs** (p.3): an arm that keeps swapping between a water gun and other tools makes cleaning slow. Their fix is mounting the jets permanently on the arm tip. Cleaning time per toilet is still unknown.

## Open questions

- [ ] Does HYTRON in production actually have this arm? The website features list (S024*) mentions no arm. The patent may describe a newer version or prototype.
- [ ] Read CN 111466837 A (the Guangzhou Deposon ozone cleaning robot). It is a possible design-around reference and another competitor to look at.
- [ ] Has Primech entered national phase in India, the US, China or Europe? (check after Dec 2026 / Jan 2027)
- [ ] Any other Primech patents? Search the 3 inventor names and the applicant on Google Patents / WIPO Patentscope.
- [ ] Get the Singapore priority application SG 10202401736R if it is published.
