# Fonda Global + A*STAR: ALAC

[← Back to master document](../COMPETITOR_INTELLIGENCE.md) · [Sources](../SOURCES.md) · **Last updated:** 2026-10-19

Tags: `[V]` verified · `[3P]` third-party · `[CC]` company claim · `[INF]` inferred · `[UNV]` unverified · `[CONFLICT]` · `[INT]` internal observation / opinion from our team. `[S012*]` = cited by S001, not yet opened by us.

## Snapshot

| | |
|---|---|
| **HQ** | Singapore |
| **Company** | Fonda Global Engineering Pte Ltd |
| **Product** | **ALAC** (Automated Lavatory Cleaning robot); **ALAC 2.0** by 2025 |
| **Partner** | **A\*STAR, Advanced Remanufacturing and Technology Centre (ARTC)** `[V][S026]` |
| **Architecture** | Semi-autonomous / hybrid, focused on the **toilet bowl only** |
| **Public since** | **23 Apr 2024**: prototype demonstrated at **Temasek Polytechnic** (Enviro Tech Innovation Hub working visit) to Senior Minister of State **Dr Amy Khor**; Fonda signed an **MOU with Temasek Polytechnic** and **an MOU with 11 industry partners** to advance ALAC and its **commercialisation** `[3P][S099]`. Fonda's own article is dated 12 Jul 2024 `[V][S026]` |
| **Award** | **MUSE Design Awards 2025, Gold**, Product Design – Robotics: "ALAC 2.0 – Automated Lavatory Cleaning Robot" (entrant: A\*STAR; client: Fonda) `[V][S070]` |
| **Folder** | [fonda-global-alac/](./) |

## Product & technology

**5 tasks ("five-in-one")** `[CC][S026]`: (1) remove stains on toilet seat covers, (2) dry the seat cover, (3) lift the seat cover, (4) remove stains inside the bowl rim, (5) remove internal bowl stains.

**ALAC 2.0** `[CC][S070]`:
- A **3D fringe scanner** maps each bowl to plan its cleaning sequence (structured light; general knowledge).
- **Scannable QR codes** assigned to bowls **track cleaning status and maintenance history**.
- Data stored on a **central server for analytics** to plan cleaning operations.
- Built for heavy commercial use.

Not stated: robot-arm brand, mobility, perception of dirt.

## Operating model (AI summary, partly checked) `[UNV][S098]`

Vishal pasted an AI-generated overview (2026-10-19). Claims checked against our sources:

| AI claim | Check | Verdict |
|---|---|---|
| Fonda + A*STAR public-private R&D; "five-in-one" tasks | S026, S070 | ✅ Consistent |
| A*STAR software came "primarily from **SIMTech / I2R**" | Fonda's own article names **A*STAR ARTC** (Advanced Remanufacturing and Technology Centre) `[V][S026]` | ❌ **`[CONFLICT]`**: keep **ARTC** (primary source). The AI likely guessed common A*STAR institutes |
| Debuted at **CleanEnviro Summit Singapore (CESG) mid-2024** | No evidence found. The earliest known showcase is **Temasek Polytechnic, 23 Apr 2024** (S099). Web results list *Primech's* robot at CESG 2024, not ALAC | ⚠️ Unverified; probably confused with Primech |
| Cycle **under 5 min per toilet** | Not in S026/S070 | ⚠️ Unverified |
| **Human-in-the-loop co-bot:** janitor wheels it into the stall; it cleans the bowl while the cleaner does sinks, mirrors and restocking | Consistent with "semi-autonomous", bowl-only scope (S026) and no mobility stated | 🟡 Plausible `[INF]`, not sourced |
| Deployed **internally on Fonda's own FM contracts**; no VC raise; no overseas rollouts | Fits Fonda being an IFM/M&E contractor and the absence of funding news. 11-partner MOU aimed at commercialisation (S099) | 🟡 Plausible, unverified. **No named deployment site found** |
| Adoption depends on NEA **Productivity Solutions Grant (PSG)**; LionsBot floor scrubbers widely PSG-listed | General Singapore context | ⚠️ Unverified for ALAC |
| Peers Hivebotics "zero-shot" mapping, 173 °C steam | 173 °C is right (S061); "zero-shot" is the AI's wording | — |

**Analysis** `[INF]`:
- ALAC is a **captive productivity tool of an FM contractor** (like Primech's HYTRON inside Primech's cleaning business) rather than a robot sold on the open market.
- That means **low external threat** but a **real buyer signal**: Singapore FM contractors want *assisted* bowl cleaning even without full autonomy.
- **Temasek Polytechnic's Enviro Tech Innovation Hub** hosted both ALAC (Apr 2024) and a Primech HYTRON deployment (late 2024, per web results). It is a **test-bed / showcase node for Singapore restroom robots**, worth knowing for any Singapore entry.

## People Directory

| Photo | Name | Role | Org | Sources |
|---|---|---|---|---|
| — | **Eugene Lee Joon Kiat** | Senior Research Engineer (credited designer, ALAC 2.0) | A\*STAR | S070 |
| — | **Leng Wai Hoong** | Lead Research Engineer (credited designer, ALAC 2.0) | A\*STAR | S070 |
| — | **Darren Ong** | Deputy Director (credited, ALAC 2.0); posted about the Apr 2024 Temasek Polytechnic showcase on LinkedIn | Fonda Global Engineering · [LinkedIn](https://sg.linkedin.com/in/ongdarren) | S070, S099 |

*Note: Gemini's made-up Primech AI engineer "Leow Joon Kait" (S055) is very likely a garbled "Eugene Lee Joon Kiat" `[INF]`.*

## Links to other competitors

- **Hypothesis from Vishal (2026-10-08) `[INT][S064]`:** Hivebotics' early engineer **Zhicheng Lin** interned at A\*STAR (May – Aug 2021), so there may be a link with ALAC. **Evaluation:** his internship was generic UR5 grasping and RL research, his A\*STAR institute isn't named, and ALAC surfaced publicly only in 2024. **No evidence of a link yet.** Full reasoning in [hivebotics.md → Internal notes](../hivebotics/hivebotics.md#internal-notes--opinions).

## Assessment `[INF]`

- An example of **narrow scope**: it automates the hardest, dirtiest subtask (the toilet bowl) rather than the whole restroom.
- **Interesting for Ubanthu:** ALAC 2.0 **tracks cleaning status per bowl** (QR plus a central server) and **scans each bowl in 3D**. That's another competitor moving toward **measured or audited cleaning**, though there's no evidence of contamination detection itself.

## Open questions

- [ ] Is ALAC commercially deployed, and where? Price? (AI says internal Fonda FM contracts only, unverified, S098)
- [ ] Who are the 11 industry MOU partners (Apr 2024)? What came of the Temasek Polytechnic MOU?
- [ ] Is it mobile, wheeled by the cleaner, or fixed? Cycle time (AI: < 5 min)?
- [ ] Arm/hardware supplier; is it mobile or fixed?
- [ ] When did ALAC development start (relevant to the Hivebotics/A\*STAR hypothesis)?
