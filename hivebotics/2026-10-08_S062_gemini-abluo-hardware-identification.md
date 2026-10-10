# [S062] Gemini answer: identifying Abluo Mk2 hardware from its spec sheet

- **Type:** AI-generated analysis (Google Gemini) of spec-table images from the Abluo MK-2 brochure (S061), pasted by User (Vishal) on 2026-10-08.
- **Status:** Raw, preserved as received (the original's garbled math formatting has been cleaned). Claude's verification is in [hivebotics-abluo-mk2-specs.md](hivebotics-abluo-mk2-specs.md).
- **Verified:** arm = UFACTORY 850 (specs match; UR5e excluded), LiDAR = Livox Mid-360 (specs match).
- **Wrong:** "225 kg" vehicle weight (brochure: 180 kg dry / 200 kg full).
- **Unsupported:** custom chassis built on hub motors from ZLAC / Robomodule / Oriental Motor.

---

## User's prompts and Gemini's answers (text as pasted)

**Prompt:** this is the specs of the 3d lidar used by hivebotics... can you reverse search the exact hardware used by them?

**Answer:** The exact hardware sensor shown in the spec sheet is the Livox Mid-360 (manufactured by Livox Tech, an autonomous sensing sub-brand backed by DJI). Every specification in the table matches the Livox Mid-360 datasheet:

| Parameter in table | Value in table | Livox Mid-360 official OEM datasheet spec |
|---|---|---|
| Field of View | 360° × 59° | 360° (horizontal) × 59° (vertical: −7° to 52°) |
| Scan / detection range | 0.1–40 m | 0.1 m minimum blind zone, 40 m range (@ 10% reflectivity) |
| Accuracy / range precision | 2 cm | ≤2 cm (1σ @ 10 m) |
| Frame rate | 10 Hz | 10 Hz (typical non-repetitive scanning pattern) |
| Power consumption | 6.5 W | 6.5 W (average operating power) |
| IP rating | IP67 | IP67 |

Why Hivebotics selected this specific unit: ultra-wide vertical FOV (59°) vs mechanical spinning LiDARs (Velodyne, Hesai XT16/32) with 16°–31°; tiny blind zone (0.1 m) for 1.2 m-wide cubicles; 6.5 W and 265 g preserves battery runtime vs 15–30 W industrial sensors; IP67 for steam (173 °C) and spray environments.

**Prompt:** what about amr ..

**Answer:** The specifications describe the mobility chassis (AMR base). Rather than an off-the-shelf branded industrial mobile robot (like a MiR or Clearpath), this points to a custom-integrated heavy-duty Mecanum / omni-directional drive base.

| Parameter | Value | Engineering interpretation |
|---|---|---|
| Drive system | Omni-directional drive | 4-wheel Mecanum or powered caster/omni-wheel layout; full 3-DoF planar mobility |
| Turning angle | 0° (zero turning radius) | Rotates on its own centre |
| Speed (max) | 0.8 m/s (≈2.9 km/h) | Capped for safety in enclosed, wet spaces |
| Max floor clearance | 5 cm | Clears thresholds, drainage slopes, small steps |
| Slope tolerance | 7° (≈12.3% grade) | Above ADA 1:12 (≈4.8°); "ensures the loaded 225 kg platform won't stall" |
| Accuracy tolerance | 3 cm | Coarse base positioning before the 6-DoF arm takes over |

Hardware architecture: not an off-the-shelf complete AMR (AgileX Ranger, Slamtec Athena and MiR250 list 10–12° slope, 10–20 mm clearance, 1.2 m/s). A custom base suits heavy water/chemical payloads ("225 kg total vehicle weight"). Typically built on industrial hub-motor mecanum assemblies, "commonly sourced from suppliers like ZLAC / Robomodule / Oriental Motor", in a custom stainless/aluminium water-resistant sub-chassis.

**Prompt:** i got info from sources that hivebotics uses UFACTORY xArm... not sure which one... the image is from their website... confirm whether they ufactory by reverse searching specific models

**Answer:** Confirmed. The exact robotic arm model shown in the spec sheet is the UFACTORY 850.

| Spec in table | Value in table | UFACTORY 850 datasheet | UFACTORY xArm 6 |
|---|---|---|---|
| Working range (reach) | 850 mm | 850 mm | 700 mm (rule-out) |
| Repeatability | 0.02 mm | ±0.02 mm | ±0.1 mm (rule-out) |
| Payload | 5 kg | 5 kg | 5 kg |
| DOF | 6 | 6 | 6 |
| Max TCP speed | 1 m/s | 1 m/s | 1 m/s |

Why not the standard xArm 6: 850 vs 700 mm reach matters in stalls; harmonic drives give ±0.02 vs ±0.1 mm; UFACTORY sells the 850 with a wide-input DC control box (48–72 V DC) that plugs into an AMR battery pack.
