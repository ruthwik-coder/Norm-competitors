# Fonda Global + A*STAR: ALAC

[← Back to master document](../COMPETITOR_INTELLIGENCE.md) · [Sources](../SOURCES.md) · **Last updated:** 2026-10-08

Tags: `[V]` verified · `[3P]` third-party · `[CC]` company claim · `[INF]` inferred · `[UNV]` unverified · `[CONFLICT]` · `[INT]` internal observation / opinion from our team. `[S012*]` = cited by S001, not yet opened by us.

## Snapshot

| | |
|---|---|
| **HQ** | Singapore |
| **Company** | Fonda Global Engineering Pte Ltd |
| **Product** | **ALAC** (Automated Lavatory Cleaning robot); **ALAC 2.0** by 2025 |
| **Partner** | **A\*STAR, Advanced Remanufacturing and Technology Centre (ARTC)** `[V][S026]` |
| **Architecture** | Semi-autonomous / hybrid, focused on the **toilet bowl only** |
| **Public since** | Fonda article dated **12 Jul 2024** `[V][S026]` |
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

## People Directory

| Photo | Name | Role | Org | Sources |
|---|---|---|---|---|
| — | **Eugene Lee Joon Kiat** | Senior Research Engineer (credited designer, ALAC 2.0) | A\*STAR | S070 |
| — | **Leng Wai Hoong** | Lead Research Engineer (credited designer, ALAC 2.0) | A\*STAR | S070 |
| — | **Darren Ong** | Deputy Director (credited, ALAC 2.0) | Fonda Global Engineering | S070 |

*Note: Gemini's made-up Primech AI engineer "Leow Joon Kait" (S055) is very likely a garbled "Eugene Lee Joon Kiat" `[INF]`.*

## Links to other competitors

- **Hypothesis from Vishal (2026-10-08) `[INT][S064]`:** Hivebotics' early engineer **Zhicheng Lin** interned at A\*STAR (May – Aug 2021), so there may be a link with ALAC. **Evaluation:** his internship was generic UR5 grasping and RL research, his A\*STAR institute isn't named, and ALAC surfaced publicly only in 2024. **No evidence of a link yet.** Full reasoning in [hivebotics.md → Internal notes](../hivebotics/hivebotics.md#internal-notes--opinions).

## Assessment `[INF]`

- An example of **narrow scope**: it automates the hardest, dirtiest subtask (the toilet bowl) rather than the whole restroom.
- **Interesting for Ubanthu:** ALAC 2.0 **tracks cleaning status per bowl** (QR plus a central server) and **scans each bowl in 3D**. That's another competitor moving toward **measured or audited cleaning**, though there's no evidence of contamination detection itself.

## Open questions

- [ ] Is ALAC commercially deployed, and where? Price?
- [ ] Arm/hardware supplier; is it mobile or fixed?
- [ ] When did ALAC development start (relevant to the Hivebotics/A\*STAR hypothesis)?
