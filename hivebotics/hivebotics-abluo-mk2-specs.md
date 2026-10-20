# Hivebotics Abluo Mark 2: specifications and hardware identification

[← Hivebotics profile](hivebotics.md) · [← Master document](../COMPETITOR_INTELLIGENCE.md) · Sources: **[S061]** brochure, **[S062]** Gemini analysis, **[S063]** web spec checks · **Added:** 2026-10-08

**Source document:** [65b2242e9_ABLUO_wf_3_compressed.pdf](65b2242e9_ABLUO_wf_3_compressed.pdf), "**Abluo MK-2 Brochure | March 2026**", 6 pages, from the Hivebotics website (per Vishal). Page images: [brochure_pages/](brochure_pages/). The PDF has a real text layer, so all numbers below were **read directly from the text**, not from an image. All values are company claims `[CC][S061]`.

---

## 1. Hardware identification (the main question)

### Summary

| Component | Brochure says | Identified as | Confidence | Evidence |
|---|---|---|---|---|
| **Robot arm** | 850 mm reach, 0.02 mm repeatability, 6 DOF, 5 kg payload, 1 m/s | **UFACTORY 850** (UFACTORY, Shenzhen, China) | **High** `[INF]` | All 5 specs match UFACTORY 850 datasheet values `[S063]`. **UR5e ruled out** (same reach/payload but ±0.03 mm repeatability). xArm 6 ruled out (700 mm reach, ±0.1 mm). Brochure photos show a white arm with grey joint bands, which fits UFACTORY styling and not UR's grey/blue. CEO forked UFACTORY's `xarm_ros` in 2022 `[S059]`. **Three independent clues agree; the brand isn't named in the brochure** |
| **3D LiDAR** | 0.1–40 m, 2 cm, 360° × 59°, 10 Hz, IP67, 6.5 W | **Livox Mid-360** (Livox, DJI-affiliated, China) | **High** `[INF]` | All 6 specs match the Mid-360 manual: 360° × 59° FOV (−7° to 52°), 0.1 m blind zone, 40 m @10% reflectivity, ≤2 cm (1σ @10 m), 10 Hz, 6.5 W typical, IP67 `[S063]`. **The 360 × 59° FOV is unusual**; other common robot 3D LiDARs (Hesai JT, Unitree L1, RoboSense Airy) have ~90°+ vertical FOV (general knowledge). Not visible in brochure photos (likely inside the base `[INF]`) |
| **Compute** | **AMD Ryzen™ Embedded 8845HS** CPU + **NVIDIA "Quadro RTX A400"** GPU | Named directly | **Named** `[CC][S061]` | x86 + discrete NVIDIA workstation GPU. **Not a Jetson** (unlike Primech's Jetson Orin). "Quadro" is an outdated prefix; NVIDIA sells it as "RTX A400" (general knowledge) |
| **Depth camera** | 1280 × 800 @120 fps, 89.5° FOV, global shutter | **Luxonis OAK-D S2 PoE** (stereo OV9282) | **Confirmed (2026-10-08)** | Specs match exactly (S072), and the model is wired into Hivebotics' URDF on GitHub (S071). See [GitHub deep dive](hivebotics-github.md). Orbbec Gemini 335Le appears later (Jul 2026) |
| **RGB camera** | 4056 × 3040 @60 fps, 78° FOV, rolling shutter | **Luxonis OAK-D S2 PoE (auto-focus)** colour sensor IMX378 | **Confirmed (2026-10-08)** | 78° DFOV = AF variant (S072); same device as depth |
| **Mobile base (AMR)** | Omni-directional drive, 0.8 m/s, zero turning radius, 5 cm clearance, 7° slope, ±3 cm accuracy | **Mecanum drive** (custom; supplier unidentified) | Mecanum confirmed | GitHub commits reference mecanum wheels in ros2_control (S071) |
| **Steam + vacuum unit** | 3/5/8 bar, 173 °C max, 75 g/min, wet & dry vacuum | **Kärcher SGV 8/5** (candidate) | **Inferred (2026-10-20)** | Pressure and max temperature match the SGV 8/5 datasheet exactly (S104). Kärcher is the named MOU partner |
| **Cleaning tools** | Steam, vacuum, chemical jet, floor nozzle | **Kärcher** | **Named** (Series A deck, S075) | "MOU partner and supplier for integration of Kärcher equipment"; CSO Vincent Sim is ex-MD Kärcher Singapore |
| **Safety sensors** | Ultrasound 2–300 cm (±1 cm, <750 ms); cliff sensors 20–150 cm, 360°; bumper | Unidentified | — | Generic |
| **Battery** | 7,560 Wh, 50.4 V; **swappable** modules (3 drawers in photo) | Unidentified | — | 50.4 V = a 12-cell lithium-ion pack (12 × 4.2 V; general knowledge) `[INF]`; ~150 Ah |

### Gemini's analysis (S062): what held up

| Gemini claim | Check |
|---|---|
| Arm = UFACTORY 850 | ✅ Specs confirmed against retailer datasheets; UR5e excluded by repeatability |
| LiDAR = Livox Mid-360 | ✅ Specs confirmed against the Livox manual |
| "Loaded 225 kg platform" | ❌ **Wrong.** Brochure: **180 kg without water, 200 kg full** |
| Base is custom; hub motors from ZLAC / Robomodule / Oriental Motor | ⚠️ Speculation. Nothing in the brochure supports it |
| Slope "complies with ADA"; UF850 sold with 48–72 V DC control box | ⚠️ General claims, not from the brochure; not checked |
| Did not attempt cameras or compute | — Done here (compute named; cameras unidentified) |

---

## 2. Full specification table `[CC][S061]` (brochure p.6)

**Dimensions & weight:** 46 W × 75 L × 150 H cm · 180 kg (no water) / 200 kg (full water & chemical)

**Battery & power:** 7,560 Wh · 50.4 V · 3 h per charge · 2.5 h to full · charging by **battery swap, wall plug, or docking station**

**Computing:** AMD Ryzen Embedded 8845HS · NVIDIA (Quadro) RTX A400

**Cleaning system**

| Item | Value |
|---|---|
| Modes | Steam · hot-water spray · cold-water spray · chemical spray · **wet & dry vacuum** · blow drying |
| Water tank | **13 L** |
| Waste tank | 5 L |
| Chemical tank | 2 L |
| Detergent flow | 550 ml/min |
| Water-jet flow | 550 ml/min |
| Steam pressure | 3 / 5 / 8 bar (3 modes) |
| Steam temperature (max) | **173 °C** |
| Steam volume | 75 g/min |
| **Steam start-up time** | **7 min** |
| Hot / cold water | 70 °C / 24 °C |
| Vacuum (max) | 25.4 kPa |
| Noise | 67 dB(A) |

**Network:** 4G LTE Cat 4 · Wi-Fi 4 (802.11b/g/n), WPA2-Enterprise · GPS optional · configurable geofencing

**AMR:** omni-directional drive · 0.8 m/s max · 0° turning angle · 5 cm floor clearance · 7° slope · ±3 cm accuracy

**Sensors:** 3D LiDAR (see above) · ultrasound · cliff sensors (360°) · bumper · depth camera · RGB camera

**Robot arm:** 850 mm reach · 1 m/s · 0.02 mm repeatability · 6 DOF · 5 kg payload

**Performance (estimates)**

| Task | Time | Water |
|---|---|---|
| Toilet bowl | **5 min** | 0.2 L |
| Urinal | 3–5 min | 0.2 L |
| Sink | 2–4 min | 0.5 L |
| Floor (per m²) | 0.3 min | 0.075 L |
| **Cleaning cycle** (3 toilets + 3 urinals + 3 sinks + 30 m²) | **~40 min** | **~5 L** |
| Refill water / chemical | 3 min / 2 min | — |
| Waste disposal | 5 min | — |
| Cycles per water refill | 2–3 | — |
| Cycles per waste disposal | ~8–12 | — |

---

## 3. Other brochure content `[CC][S061]`

- **Offices:** Singapore HQ, **81 Ayer Rajah Crescent #03-64, Singapore 139967** (consistent with Gemini's "LaunchPad @ one-north") · **US office:** 8 The Green Street, Dover, Delaware (a common registered-agent address `[INF]`) · **Hong Kong office:** 29 Austin Road, Tsim Sha Tsui
- **Software name:** "**HiveOS**", the "proprietary AI operating system". The Vertex release calls it "HiveIntelligence" (S056); different names or layers `[INF]`
- **Cleaning sequence:** "seat lifting, flushing, contactless steam cleaning, chemical jetting, and blow drying"
- **Claims:** "Cuts labor intervention in restroom cleaning by approximately **60–70%**"; "consistent and measurable hygiene"; "real-time data for performance tracking"
- **Navigation:** "3D LiDAR, depth cameras, and ultrasonic sensors" with 3D SLAM; "Fully autonomous movement **within same floor** and within restrooms", i.e. **no multi-floor or lift operation claimed** (contrast Primech's "elevator ride")
- **Modes:** automatic; **manual** (a cleaner pushes it by handles, p.5 photo); touchscreen or mobile app
- **Docking station is optional.** It recharges, refills water and replenishes chemicals
- **Cleaning zones:** urinals, toilet bowls, floors, sinks & mirrors. **No squat toilets** mentioned
- ⚠️ **Hidden "LIONSCLEAN APP" text (p.5):** the phrase sits in the PDF's text layer under "Intuitive Controls" but **is not visible on the rendered page**. LionsClean is the control app of **LionsBot**, another Singapore cleaning-robot company (S063). Most likely a **leftover from a design template or copied layout** `[INF]`. A partnership is possible but has no evidence. Worth asking about
- Page 5 lifestyle photos look like **renders or composites** `[INF]`; typos ("maintenace", "touchsreen", "timestampped")

---

## 4. Abluo Mk2 vs Primech HYTRON (spec sheets)

| | Abluo Mk2 `[S061]` | HYTRON `[S042]` |
|---|---|---|
| Size (L × W × H) | 75 × 46 × 150 cm | 73.3 × 40.9 × 131.1 cm |
| Weight | 180 kg (200 full) | 128 kg |
| Max speed | 0.8 m/s | 0.6 m/s |
| Battery | 3 h; **swappable**; 2.5 h charge | 4 h; 2 h charge |
| Fresh / waste / chemical tanks | **13 / 5 / 2 L** | 8 / 5 / 1.5 L |
| Toilet time | **5 min** | ~6 min |
| Urinal / sink | 3–5 / 2–4 min | ~3 / ~3 min |
| Arm | **UFACTORY 850** (identified) | Elite Robots (named example in patent) |
| LiDAR | **Livox Mid-360** (identified) | Hesai (candidate, unconfirmed) |
| Compute | AMD Ryzen 8845HS + NVIDIA RTX A400 | NVIDIA Jetson Orin "Super" |
| Main cleaning method | **Steam 173 °C** + chemical jet + vacuum + blow-dry | Brush + detergent (+ e-water / ozone claim) |
| Multi-floor | Not claimed ("within same floor") | Elevator ride + door opening claimed |
| Squat toilet | Not listed | Listed |

## Open questions

- [ ] Confirm the arm by photo of the base label or logo (UFACTORY prints its logo on the base)
- [ ] Confirm Livox Mid-360 placement (inside the base?) and any second LiDAR
- [x] ~~Identify the depth and RGB cameras~~: **Luxonis OAK-D S2 PoE (AF)**, confirmed 2026-10-08 via GitHub + spec match (S071, S072)
- [ ] Mobile base supplier (mecanum confirmed via GitHub, S071)
- [ ] LionsClean text: template leftover or LionsBot relationship?
- [ ] Steam start-up takes 7 min. How does that affect on-demand cleaning?
