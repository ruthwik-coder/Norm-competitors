# Hivebotics / NUS patent: WO 2023/075687 "Robot Alignment and Manipulation"

[← Hivebotics profile](hivebotics.md) · [← Master document](../COMPETITOR_INTELLIGENCE.md) · Sources: **[S065]** patent, **[S066]** Google Patents status · **Added:** 2026-10-08

**Files:**
- Original scan (no text layer): [WO_2023075687_A2.pdf](WO_2023075687_A2.pdf)
- **Searchable copy (OCR):** [WO2023075687_OCR.pdf](WO2023075687_OCR.pdf) · plain text by page: [WO2023075687_OCR.txt](WO2023075687_OCR.txt)
- Selected drawing pages: [patent_figures/](patent_figures/) (`WO2023075687_p*.png`)

**Review coverage:** all 65 pages. Full OCR text read (description, 21 claims); key drawings viewed (Figs. 1, 3, 5, 14, 23, 26, 33, 34). ~19 pages are drawings and UI screenshots with little OCR text. Page numbers are **PDF pages**.

---

## Bibliographic data `[V]` (p.1; status from Google Patents S066)

| Field | Value |
|---|---|
| Publication | **WO 2023/075687 A2**, 4 May 2023, published **without** search report; **A3** (with search report) 13 Jul 2023 |
| Application | PCT/SG2022/050762, filed **25 Oct 2022** |
| Priority | **SG 10202112046S, 29 Oct 2021** |
| **Applicant / owner** | **National University of Singapore (NUS)**, *not* Hivebotics |
| Inventors | **Rishab Patwari** (NUS ECE), **Nguyen Tuan Dung** (NUS ME), **Zhicheng Lin** (NUS ME), **Praveenkumar Seenivasan** (NUS ECE) |
| Agent | Davies Collison Cave Asia, Singapore |
| Designated | All PCT states incl. IN, US, CN, EP |
| **Status** | **"Ceased"**; anticipated expiration **2024-04-29**; Google lists **only the WO filing, no national-phase entries** `[V][S066]` |
| Cited prior art (Google) | iRobot US10878294B2; Karasikov US20190246858A1 ("Cleaning robot with arm and tool receptacles"); Panasonic JP7316567B2; Nanjing Inst. Tech. CN109691935A (sanitary-ware cleaning robot); Shenzhen Guaichong CN113414157A |
| Cited by | SoftBank Group WO2025263611A1 "Robot" (2025) |

### Why it says "Ceased" (your question)

- A PCT application is never a patent by itself. It must enter the **national phase** in each country, usually by **30 months from priority** (31 in India and some others; general knowledge).
- Priority **29 Oct 2021 + 30 months = 29 Apr 2024**, exactly Google's "anticipated expiration". Google shows **no national-phase filings in any country**.
- So **the application lapsed everywhere** around Apr–May 2024 `[INF]`, most likely because NUS and the founders chose not to pay for national filings (cost or strategy), or filed somewhere Google hasn't picked up yet. To confirm, check WIPO Patentscope's "National Phase" tab.
- **What it means:**
  1. **Hivebotics has no patent protection from this filing.**
  2. **Everything in it is now public prior art**: anyone can use these methods, and later patents (incl. Ubanthu's) can't claim them. *Not legal advice; confirm with a patent attorney.*
  3. The IP belonged to **NUS**, not Hivebotics. Whether Hivebotics licensed it is unknown.

---

## What it discloses (2021–22 prototype)

### A. Three-step vision alignment of the robot to a fixture (claims 1–7; p.3–4, 9–12)
1. **Detect the fixture:** a custom **YOLOv5** detector with classes limited to *toilet bowl, urinal, sink, mirror, shower glass panel*, plus sub-features (water cabinet/flush, bowl inner/outer, lid/seat, tap, sink surface, mirror surface).
2. **Square up to it:** edge segmentation finds straight edges (e.g. the cistern's horizontal edges). The **depth camera** measures distances to two points on an edge; if they're equal, the robot faces the fixture squarely.
3. **Centre and set distance:** the bounding-box centre must sit within a margin of the image centre line, then distance is checked against a preset range per fixture.

**The robot was pushed by a person at that time.** The UI (Figs. 16–22) shows "MOVE LEFT" guidance and alignment percentages, then "**Lock Wheels then Press Next**". This was **semi-autonomous: a cleaner wheels it to the toilet** (p.15–16, Table II–III).

### B. Vision-guided arm cleaning path (claims 8–11; p.10–13)
- **Wrist-mounted depth camera** takes a point cloud from an "observe pose" → 3D model in **MoveIt** → edge segmentation fits **ellipses** to the bowl rim → **waypoints** along the surface → **OMPL** inverse kinematics.
- Each surface point is stored as **(xyz, pass_count)**, a per-point **"cleaning status"** record. The path spirals down the bowl one brush-radius at a time until the bowl depth or arm reach is exceeded.
- Safety: the path is collision-checked in MoveIt; **if any joint deviates >4° from plan, it stops and alerts the operator**.
- **Real-time surface-normal estimation** keeps a constant tool distance and force.
- ⚠️ **"Cleaning status" here = coverage tracking (which points the brush has passed), *not* dirt detection.** There is **no stain or contamination detection** anywhere in this patent `[V]`.

### C. Tool management (claims 14–20; p.17–23)
- **Arm named: "elephant robotics mycobot 320 M5 robotic arm"** (p.17) `[V]`.
- **Pneumatic tool changer**: matching base plates on arm and tool, locked by compressed air from a central compressor. An **8-pin electrical module** passes power and signals to a per-tool control box.
- **Tools (Fig. 26):** motor-spun **toilet brush with *Clorox* disposable heads** · gripper for **flush and toilet lid** · spin mop/duster with internal water and detergent pipe · dry sponge · linear-actuated **wiper for mirror and glass** · separate **utilities tool** spraying water, detergent or air.
- **Magnetic horizontal tool rack**; **disposable brush-head dispenser** with linear actuator; **disposal bin with an aligner** that strips used heads into a bag. A dust bin is mentioned too.
- ROS nodes: camera publisher, CV scene detector (YOLO), CV alignment.

### D. Claims summary
| Claims | Scope |
|---|---|
| 1–7 | Alignment method (edge + bounding box + distance) |
| 8–11 | Point-cloud surface modelling → waypoints → end-effector path |
| 12–13 | System / robot running those methods |
| 14–20 | Robot with arm + **disposable tool-head dispenser + disposal unit**; pneumatic coupling; utilities lines |
| 21 | Robot combining the above |

---

## Analysis `[INF]`

1. **It shows Hivebotics' technical evolution.** Treat the dates as rough; they come from the patent (2021–22), the NUS post (Apr 2023) and the brochure (Mar 2026).

   | | 2021–22 (this patent) | 2023 (NUS iDP showcase photo, S064) | 2026 Mark 2 (brochure S061) |
   |---|---|---|---|
   | Arm | **Elephant Robotics myCobot 320 M5** (small desktop cobot; ~350 mm reach / ~1 kg payload per general knowledge) | White xArm-style arm on a black box base | **UFACTORY 850** (850 mm, 5 kg) |
   | Mobility | **Wheeled trolley pushed by a cleaner**; wheels locked during cleaning | Box base, likely still manual `[INF]` | Autonomous omni-drive base, 3D SLAM, Livox Mid-360 |
   | Cleaning | **Contact**: spinning brush with **disposable Clorox heads**, mop, sponge, wiper | — | **Contactless**: 173 °C steam, chemical jet, vacuum, blow-dry |
   | Perception | YOLOv5 fixture detection; depth-camera point clouds; coverage tracking | — | "AI vision"; claims **scored before/after check** |

   **So Hivebotics completely changed its cleaning method**, from disposable brushes to contactless steam. The "no brushes or cloths" marketing (S056) describes the *current* design, not the original.
2. **Their 2021–22 perception was classical CV** (YOLO boxes + geometric edges + point-cloud ellipses), not contamination detection. The "scored before/after check" (S056) must be **newer work**, and its method is still unknown.
3. **No patent protection.** Ceased everywhere, NUS-owned, and a long time since priority. Unless Hivebotics has *other* filings, **its moat is execution, data and know-how, not IP**. Worth searching for newer Hivebotics or NUS filings by these inventors.
4. **Useful for Ubanthu as prior art.** The alignment, waypoint and tool-changer ideas are public, and can't be claimed by Ubanthu or competitors.
5. **The design was already multi-fixture in 2021:** toilet, urinal, sink, mirror, glass panel. It also handled the **flush and lid with a gripper**, which the Mk2 brochure also lists ("seat lifting, flushing").

## Open questions
- [ ] Confirm "no national phase" on WIPO Patentscope (National Phase tab)
- [ ] Any newer patents by Hivebotics, Patwari, Nguyen Tuan Dung or NUS on restroom robots (2023–26)?
- [ ] Did Hivebotics license this IP from NUS?
- [ ] When and why the switch from myCobot to UFACTORY, and from brushes to steam?
