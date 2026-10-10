# [S001] ChatGPT web research: India toilet/restroom automation landscape

- **Type:** AI-generated research summary (ChatGPT with web search), pasted by the user into Claude
- **Received:** 2026-09-30
- **Status:** Raw source, preserved as received. Its citations are listed as S002–S033 in `SOURCES.md` and **have not yet been independently checked**. Claims here are tagged `[3P]` or `[UNV]` in the master document until they are verified.
- **Known issues found during processing:** see "Processing notes" at the bottom.

---

I did a live web investigation. The important finding is that **India does have several efforts in toilet/restroom automation, but the field is still very fragmented**. I found only a small number of Indian entities working on actual fixture-level automation, and fewer still with evidence of commercial deployment.

## 1. Executive summary

The Indian landscape currently breaks into four distinct groups:

**A. Actual mobile toilet/restroom robotics**

* **Sketch Robotics — Kerala**: an early-stage Indian company publicly listed by Kerala Startup Mission with an AMR + 6-DOF arm for autonomous washroom cleaning, including toilets and sinks. [1]
* **Amrita Vishwa Vidyapeetham — Kerala**: developed **Sudha**, an autonomous toilet-cleaning robot using a robotic arm, camera-based perception, obstacle sensing, spraying, scrubbing and wiping. [2]
* **IIT Palakkad**: built an automated toilet-cleaning robot as an Inter-IIT project in 2017–18. [3]
* **IIT Madras**: has a new patent/application for an autonomous toilet-cleaning system, but it is only **TRL 2** according to IITM's technology-transfer office. [4]

**B. Automated toilet/fixture cleaning, but not mobile robots**

* **HapiHygi Innovations — Gujarat**: **HygiSeat**, a retrofit automated toilet-seat cleaning system using spraying, wiping, drying and UV-C disinfection. MeitY Startup Hub says it has reached TRL 7 and has had 500+ beneficiaries through pilots. [5]
* **Hachimichi — Maharashtra**: **SeatO'fresh**, a retrofit automated toilet seat designed for B2B washrooms. Historical evidence indicates 84 units in the market by 2021. [6]
* **VAATA — Chennai**: DryTab automatically doses cleaning/disinfectant into the toilet cistern. This is automation, but not robotic cleaning machinery. [7]
* **ATSC / i-Hub Gujarat**: patent-pending fully autonomous toilet-seat cleaning system, still under development. [8]

**C. Indian sanitation robotics adjacent to toilets**

* **Genrobotics** and **Solinas** are highly relevant from a robotics and sanitation standpoint, but their products focus on sewers, septic tanks and confined sanitation infrastructure rather than cleaning toilets/urinals/sinks. [9]

**D. Strong international competitors**
The international market is substantially further along. The most relevant companies I found are:

* **Hivebotics — Singapore — Abluo**
* **Eternia Robotics / Cleaning Robotics — Singapore — TCR-H**
* **Primech AI — Singapore/US-linked operation — HYTRON**
* **Fonda Global + A*STAR — Singapore — ALAC**
* **ZeeqClean — Asia — ZC-01**
* **Senxeed Robotics — Japan — WUUMIE**

These are much closer to the architectural direction of a mobile robot that navigates a restroom and physically cleans individual fixtures. [10]

---

# 2. Indian companies / projects

| Entity                         | Location             | Product                            | Type                              | Technology                                                                   | Stage                       |
| ------------------------------ | -------------------- | ---------------------------------- | --------------------------------- | ---------------------------------------------------------------------------- | --------------------------- |
| **Sketch Robotics**            | Kochi, Kerala        | Autonomous Washroom Cleaning Robot | **Mobile robot**                  | AMR + 6-DOF arm + targeted spray + UV-C + VLM perception                     | Early-stage                 |
| **HapiHygi Innovations**       | Gandhinagar, Gujarat | HygiSeat                           | Fixed/retrofit fixture automation | Spray + wipe + dry + UV-C                                                    | **TRL 7 claimed**           |
| **Amrita Vishwa Vidyapeetham** | Kerala               | Sudha                              | **Mobile robot**                  | Robotic arm + camera + object detection + stain detection + spray/scrub/wipe | Research/prototype          |
| **IIT Madras**                 | Chennai              | Autonomous Toilet Cleaning System  | Fixture/mobile automation concept | Mechanical actuator + adaptive cleaning                                      | **TRL 2**                   |
| **IIT Palakkad**               | Palakkad             | Automated Toilet Cleaning Robot    | Mobile robot                      | Autonomous navigation, floor/seat cleaning, trash pickup                     | Student prototype           |
| **Hachimichi**                 | Pune                 | SeatO'fresh                        | Retrofit automated seat           | Automated seat replacement/cleaning                                          | Commercialized historically |
| **ATSC / i-Hub Gujarat**       | Gujarat              | Automatic Toilet Seat Cleaner      | Fixed toilet system               | Autonomous seat cleaning                                                     | Under development           |
| **VAATA Smart**                | Chennai              | DryTab                             | In-tank automation                | Automated chemical dosing                                                    | Commercial product          |

### Sketch Robotics

This is one of the more interesting Indian companies I found.

Kerala Startup Mission describes its **Autonomous Washroom Cleaning Robot** as an AMR-based system with a **6-DOF robotic arm**, targeted spray cleaning, floor scrubbing and UV-C disinfection. It claims perception based on VLM technology for recognizing sinks and toilets and adapting to different restroom layouts. [1]

Sketch Robotics itself describes its business as robotics/AI engineering and identifies Muhammed Faisal P K, Romal Josbin and Muhammed Siyad P as founders. [11]

The company was incorporated in May 2025, so this appears to be a very young venture rather than an established commercial competitor. [12]

**Assessment:** **Direct competitor candidate**, but public evidence of scaled commercial deployment is limited.

---

### HapiHygi Innovations

This one is particularly relevant because it has moved beyond a student project.

Its **HygiSeat** is a retrofit automated toilet-seat cleaning system. MeitY Startup Hub describes automated **spraying, wiping, drying and UV-C disinfection**, with 500+ beneficiaries through pilot deployments and TRL progressing from 4 to 7. [13]

HapiHygi's own site identifies it as an early-stage startup backed by IIT Bombay, based in Gandhinagar, with Anurag Agrawal and Renuka as co-founders. [5]

VIT's TBI also lists HygiSeat as a fully automated retrofit system operating on battery or direct power. [14]

**Assessment:** **Adjacent competitor**, not a mobile restroom robot. Its product attacks the same hygiene/automation problem from a fixed-fixture architecture.

---

### Amrita — Sudha

Amrita's **Sudha** is probably one of the closest Indian academic systems to a true robotic restroom cleaner.

The university describes:

* robotic arm
* end-effector camera
* object detection
* computer vision
* toilet-surface and stain recognition
* obstacle detection and navigation
* automated spraying
* scrubbing
* wiping
* cleanliness monitoring

[2]

It is therefore conceptually much closer to the **perception → manipulation → cleaning → verification** loop than ordinary floor-cleaning robots.

**Assessment:** Technologically relevant research/prototype; no public evidence from the sources I found of scaled commercial deployment.

Images included in the original: https://webfiles.amrita.edu/2026/06/sr-service-robot.jpg (plus two images hosted on images.openai.com, not preserved; temporary links).

---

### IIT Madras

IIT Madras has a particularly interesting development because it is recent and formally being offered for technology transfer.

The technology is titled **"A System and Method for Autonomous Toilet Cleaning."** IITM lists:

* IDF 3060
* Indian patent application **IN 202541062468**
* Robotics & Automation category
* Research lab under Prof. Jayaganthan
* **TRL 2**

[4]

The patent application was filed on **30 June 2025** and published on 11 July 2025. [15]

The IITM description explicitly discusses the limitations of existing systems, including adaptability across toilet types, coverage and dirt detection. [16]

**Assessment:** Very relevant IP/research signal, but nowhere near a production competitor yet based on the disclosed TRL.

---

### IIT Palakkad

IIT Palakkad publicly documented its participation in the 2018 Inter-IIT Tech Meet, where its team built a robot to automatically clean a toilet. [3]

A project description from one participant says the system:

* cleaned the toilet floor
* picked up tissue
* cleaned the toilet seat
* operated autonomously
* informed the user when the task was complete

[17]

This is important historically, but there is no evidence that this became a company.

---

### Hachimichi / SeatO'fresh

Hachimichi was founded in 2018 in Pune and developed **SeatO'fresh**, a retrofit automated toilet seat for B2B washrooms. [18]

A 2021 startup profile reported **84 units running in the market**, with a recurring-consumption business model based around replacement rolls. [6]

This is a useful example of a different architectural approach:

**Don't make a robot clean an existing toilet → make the toilet itself partially robotic.**

That distinction matters strategically.

---

# 3. Direct vs adjacent Indian competition

### Direct / closest

**Sketch Robotics**: Mobile robot, Manipulator, Toilet recognition, Restroom navigation, Cleaning

**Amrita Sudha**: Mobile robot, Manipulator, Vision, Toilet/stain recognition, Cleaning

These are the two Indian projects I would investigate most closely from a technology standpoint.

### Adjacent

**HapiHygi**: Fixture automation, No mobile robot, Stronger evidence of commercial pilots

**Hachimichi**: Automated toilet-seat architecture, Retrofit, Historically commercialized

**ATSC**: Automated toilet-seat system, Patent-pending, Under development

**VAATA**: Automatic chemical dosing, Not robotics

### Research/IP rather than competitor

**IIT Madras**: Patent, TRL 2

**IIT Palakkad**: Historic student prototype

---

# 4. International competition

## Hivebotics — Abluo

This is currently one of the strongest benchmarks for the category.

Abluo covers: toilets, urinals, sinks, floors

The current product page describes AI vision, steaming, chemical jetting, vacuuming and autonomous navigation. The newer Mark 2 adds LiDAR/3D SLAM, a 6-DOF arm and 173°C steam sanitation. [19]

Hivebotics reports deployments across multiple countries and, in September 2026, announced a **US$6 million Series A** led by Vertex Ventures Southeast Asia & India. The funding announcement says Abluo is moving from pilots toward volume production. [10]

Its disclosed deployments include hospitals, airports and other high-traffic facilities. [20]

**This is probably the closest international benchmark to the full architecture you're describing.**

---

## Eternia Robotics / Cleaning Robotics — TCR-H

Eternia says it acquired the engineering foundation represented by **TCR-H**, originally from Cleaning Robotics.

TCR-H performs: autonomous movement, toilet bowl cleaning, urinal cleaning, floor cleaning, brush disinfection

Eternia says the platform is being productised as its first autonomous robot platform. [21]

The original Cleaning Robotics site describes: autonomous movement through washrooms, toilet/urinal identification, flushing, lid lifting, rim cleaning, internal bowl cleaning, external cleaning, floor cleaning/drying, brush disinfection [22]

---

## Primech AI — HYTRON

HYTRON is another substantial international benchmark.

Primech describes it as an autonomous commercial cleaning robot with: toilet bowl sanitization, high-pressure e-water jetting, floor mopping, autonomous navigation, self-charging, water management, blower drying, mirror polishing [23]

Primech has also disclosed that its facilities-services operation used HYTRON as part of its cleaning-robot fleet as of March 2026. [24]

---

## Fonda Global / A*STAR — ALAC

ALAC is a much more focused machine.

It performs five semi-autonomous tasks:

1. Seat-cover stain removal
2. Seat drying
3. Seat lifting
4. Internal rim cleaning
5. Bowl-internal stain removal

[25]

It was developed by Fonda Global in collaboration with A*STAR's Advanced Remanufacturing and Technology Centre. [25]

This is a good example of a **narrower automation strategy instead of trying to automate the entire restroom**.

---

## ZeeqClean — ZC-01

ZeeqClean claims its ZC-01 offers: fully automatic or human-assisted operation, pressurized contactless cleaning, drying, UV irradiation, toilet-lid detection/lifting, toilet bowl and urinal cleaning, floor cleaning, odor control

It also claims IoT/AI integration and usage-driven cleaning. [26]

---

## Senxeed Robotics — WUUMIE

Senxeed's WUUMIE is another interesting benchmark because its design specifically focuses on multi-fixture cleaning.

The company says it can clean mirrors, washbasins and toilets, and automatically change cleaning tools, using 3D spatial measurement and visual positioning. [27]

---

# 5. International presence in India

**I did not find strong public evidence of Abluo, HYTRON, TCR-H, ALAC or WUUMIE having an established Indian distributor or publicly documented Indian deployment.**

That does **not** prove that none exist; it means I could not verify one from reliable public sources in this search.

There is one Indian company, **RIFE Technologies**, that advertises a "Washroom Cleaning Robot" and claims deployments across airports, malls, hospitals and corporate campuses in India. However, its broader company materials are primarily about healthcare workstations, smart lockers and floor-cleaning robots, and I found no independently corroborated evidence identifying the restroom robot's manufacturer/model or demonstrating actual fixture-cleaning deployments. [28]

So I would treat RIFE's restroom-robot claim as **unverified / requiring direct validation**, rather than putting it on the same evidence level as Sketch, HapiHygi, or the academic projects.

---

# 6. Patent / research landscape

### IIT Madras

**IN 202541062468 — "A System and Method for Autonomous Toilet Cleaning"**. Filed 2025, currently disclosed by IITM at TRL 2. [15]

### Smart Toilet — SNJB's / Indian inventors

Patent application **IN 201821008841**, titled around a smart automatic toilet-cleaning system for Indian Railways, dates to 2018. Patent-related records and institutional documentation confirm the application. [29]

The associated technical concept used: robotic arm, brush, water jets, sensors, automatic door locking, IoT monitoring [30]

### Academic research

India also has research work on automated toilet cleaning, while international research is considerably broader. For example, research at Tokyo Metropolitan University has demonstrated restroom cleaning systems combining fixture mechanisms and floor-cleaning robots, with experimental cleaning performance reported. [31]

---

# 7. What the market actually looks like

**India has automation around toilets, but very little mature productisation of a general-purpose mobile restroom manipulator.**

Fixed fixture automation → HapiHygi, Hachimichi, ATSC, VAATA
Mobile robotics research → Amrita, IIT Palakkad, IIT Madras
Emerging commercial robotics → Sketch Robotics
Sanitation robotics adjacent to toilets → Genrobotics, Solinas

Whereas overseas, companies such as Hivebotics, Eternia/Deep Robotics lineage, Primech and ZeeqClean are much more explicitly pursuing:

**Navigation → fixture recognition → tool selection → manipulation → cleaning → verification → reporting**

---

# 8. Technology comparison (as given by the source)

| Capability                     | Sketch                | HapiHygi         | Amrita Sudha        | IITM               | Hivebotics | Eternia/TCR-H         | Primech    |
| ------------------------------ | --------------------- | ---------------- | ------------------- | ------------------ | ---------- | --------------------- | ---------- |
| Mobile platform                | ✓                     | ✗                | ✓                   | Concept            | ✓          | ✓                     | ✓          |
| Robotic arm                    | ✓                     | ✗                | ✓                   | Concept            | ✓          | ✓                     | ✓          |
| Toilet cleaning                | ✓                     | Seat             | ✓                   | ✓                  | ✓          | ✓                     | ✓          |
| Urinal cleaning                | Claimed               | ✗                | Not clearly stated  | Not clearly stated | ✓          | ✓                     | ✓          |
| Sink cleaning                  | ✓                     | ✗                | Not clearly stated  | —                  | ✓          | Future/full platform  | ✓          |
| Floor cleaning                 | ✓                     | ✗                | Not clearly stated  | —                  | ✓          | ✓                     | ✓          |
| Vision / perception            | VLM claimed           | Basic automation | ✓                   | Concept            | ✓          | ✓                     | ✓          |
| Stain recognition              | Not clearly verified  | ✗                | ✓                   | Intended           | ✓          | Not clearly disclosed | ✓          |
| Steam                          | Not publicly verified | ✗                | Not publicly stated | —                  | ✓          | Not clearly stated    | —          |
| High-pressure water            | Spray claimed         | Spray            | Spray               | —                  | Jetting    | —                     | ✓          |
| UV-C                           | ✓                     | ✓                | —                   | —                  | —          | —                     | —          |
| Commercial deployment evidence | Limited               | ✓ pilots claimed | Not found           | ✗                  | ✓          | ✓/pilot-history       | ✓          |
| Public TRL                     | Not found             | 7 claimed        | Not found           | 2                  | Commercial | Commercialisation     | Commercial |

---

# 9. Market gaps

The biggest gap isn't simply "there is no toilet-cleaning robot." It is the **general-purpose manipulation problem**.

Restroom mapping → fixture detection → fixture geometry estimation → contamination/stain detection → tool selection → contact planning → controlled cleaning → verification → tool disinfection → exception handling

A company that solves the complete chain reliably across **Indian toilets + Western toilets + urinals + sinks**, rather than one controlled fixture, is solving a substantially different problem from an automated toilet-seat cleaner.

---

# 10. Overall conclusion

India: real players, but very few mature direct competitors. Closest: Sketch Robotics (startup), Amrita Sudha (academic prototype), IIT Madras (IP), HapiHygi (commercial fixture automation, not mobile). Hachimichi worth studying as the "toilet itself is the machine" architecture.

Outside India: Hivebotics/Abluo most important to track (Sep 2026 US$6M Series A toward volume production). Benchmark set: Hivebotics, Eternia/TCR-H, Primech HYTRON, ZeeqClean, Fonda/A*STAR ALAC.

Most Indian cleaning robots target floors; fixture-level manipulation remains specialized. RIFE's own materials distinguish its floor-cleaning products from its separate claimed washroom offering. [32]

Three architectures framework:
1. Mobile manipulator robot: Hivebotics / TCR-H / Sketch / Sudha
2. Fixed toilet automation: HapiHygi / Hachimichi / ATSC / VAATA
3. Human + machine hybrid cleaning: Fonda ALAC and several emerging systems

---

## Citations (the source's numbering → our source IDs)

[1]→S002 · [2]→S003 · [3]→S004 · [4]→S005 · [5]→S006 · [6]→S007 · [7]→S008 · [8]→S009 · [9]→S010 · [10]→S011 · [11]→S012 · [12]→S013 · [13]→S014 · [14]→S015 · [15]→S016 · [16]→S017 · [17]→S018 · [18]→S019 · [19]→S020 · [20]→S021 · [21]→S022 · [22]→S023 · [23]→S024 · [24]→S025 · [25]→S026 · [26]→S027 · [27]→S028 · [28]→S029 · [29]→S030 · [30]→S031 · [31]→S032 · [32]→S033

Full URLs are in `SOURCES.md`.

---

## Processing notes (added by Claude, 2026-09-30)

1. **Senxeed citation mismatch:** [27] points to Senxeed's **ADIBOT** (UV-irradiation robot) page, not a WUUMIE page. The WUUMIE claims are unsupported by the cited URL.
2. **Weak HapiHygi citation:** [13] (the MeitY "TRL 7 / 500+ beneficiaries" claim) points to `ttifloorcare.mashreqdevelopments.com`, which looks like a third-party mirror of a LinkedIn post, not an official MeitY page. Find the original post.
3. **The comparison table claims more than the source's own text supports:**
   - Primech/HYTRON "Robotic arm ✓": no arm in the HYTRON feature list.
   - Primech "Sink cleaning ✓": the list has *mirror polishing*, not sinks.
   - Primech and Hivebotics "Stain recognition ✓": the text only says "AI vision"; stain recognition specifically is not stated.
   - Eternia/TCR-H "Robotic arm ✓": not stated in the TCR-H description.
   - Sketch "Urinal cleaning: Claimed": the KSM description mentions toilets and sinks only.
4. **"Eternia/Deep Robotics lineage"** appears once with no explanation or citation. Unclear.
5. **Primech name:** the report says "Primech AI". Our existing folder is `primechai/`, which we assume is the same company (Primech AI, a unit of Primech Holdings). Assumption, not verified.
