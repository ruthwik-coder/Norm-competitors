# Hivebotics GitHub (github.com/hivebotics): what the code reveals

[← Hivebotics profile](hivebotics.md) · [← Master document](../COMPETITOR_INTELLIGENCE.md) · Sources: **[S071]** GitHub org + fork diffs, **[S072]** camera spec check · **Added:** 2026-10-08

**What was examined (2026-10-08, via the GitHub API):**
- Org profile and all 5 public repos.
- **Every branch compared against its upstream** (commits ahead, authors, dates, files changed).
- Key diffs read in full (DepthAI, Orbbec, the RealSense commit).
- All 7 contributor profiles.

All repos are **forks of hardware-driver repos**. Hivebotics' own robot code (e.g. `hivebotics_description`, referenced in a commit) is **private**.

## 1. Org

| | |
|---|---|
| Org | **hivebotics** ("HiveBotics", "Autonomous Bathroom Cleaning Robots", Singapore) |
| Created | **20 Jun 2021** (matches "founded 2021") |
| Public repos | 5 (all forks) |
| Public member | **kuralme** (M. Ege Kural) |

## 2. Repos, newest first

| Last push | Repo (fork of) | Hivebotics' own work | Reveals |
|---|---|---|---|
| **21 Sep 2026** | **xarm_ros2** (xArm-Developer = **UFACTORY's official ROS 2 driver**) | **14 branches**, ~20 own commits, Dec 2025 → Sep 2026 | **UF850 arm**, mecanum base, force/torque sensing, compliance control, seat-lift sim, MoveIt Pro, wrist RealSense (sim) |
| **9 Sep 2026** (commits Mar–Jul) | **OrbbecSDK_ROS2** (Orbbec) | 4 commits; merged PR #1 (30 Jul 2026) | **Orbbec Gemini 335Le** depth camera (named in their config) |
| 25 Jan 2026 | **depthai-ros** (Luxonis) | `hivebotics-humble`, `hivebotics-kilted` branches | **Luxonis OAK-D S2 PoE** camera (model file wired into their URDF) |
| Jan 2024 | descartes_capability (MoveIt Cartesian-path add-on) | **No own commits** (extra commits are another fork's) | Weak: Cartesian path tooling explored in 2024 (ROS Noetic era) |
| May 2024 | ydlidar_ros2_driver (YDLIDAR) | **No own commits** | Weak: a **YDLIDAR 2D LiDAR** on an older prototype? `[INF]` |

### Why "xarm" if they use the UFACTORY 850? (Vishal's question)
**`xarm_ros2` is UFACTORY's official ROS 2 package for *all* its arms**: xArm 5/6/7, Lite 6 **and UFACTORY 850**. The name is historical. Hivebotics' commits edit **UF850-specific files**: `xarm_controller/config/uf850_controllers.yaml`, `xarm_description/urdf/uf850/uf850.ros2_control.xacro`, and new low-poly UF850 meshes (`xarm_description/meshes/uf850/collision/link*_low.stl`). Commit: "config(uf850): drop 8.x leftovers from the admittance controller". **This is code-level confirmation of the UF850** `[V][S071]`. Together with the brochure spec match (S061/S063), the arm is now **confirmed**.

## 3. xarm_ros2: branch-by-branch timeline `[V][S071]`

| Date | Author | Commit (abridged) | Meaning `[INF]` |
|---|---|---|---|
| 28–29 Dec 2025 | Arshad Khan | "updated xarm_ros2 package to work internally"; bio_gripper API fix | Fork adopted for production |
| 8 Jan 2026 | Arshad Khan | "added camera name according to rs_launch.py" → RealSense **D435i** macro gets `camera_name:='wrist_mounted'` | **Intel RealSense D435i as wrist camera** (in robot description / Gazebo sim) |
| 20 Jan 2026 | Arshad Khan | "relax some constraints on traj execution to avoid **MTC** failure" | Uses **MoveIt Task Constructor** |
| 1–9 Feb 2026 | Arshad Khan | "added extra joints for **wheel** in joint broadcasters"; "added joint_velocity_controller as **mecanum** won't work"; "removed base joints from arm joints control" | **Mecanum-wheel base** in the same ros2_control setup as the arm |
| 3 Mar 2026 | Cherie (cheriehu) | "use low poly arm meshes for collision and visual geometries" (UF850 meshes) | Faster collision checking |
| 5–16 Mar 2026 | Arshad Khan | added controllers; "**ros2 state interface for topic-based FT sensor**"; platform controllers; joint2 sim pose | **Force/torque sensing** integrated |
| 18 Mar 2026 | kendrickchin | "enable initial pose reading from **hivebotics_description**" | Private robot-description package exists |
| 1 Apr 2026 | yqchau | "updated controller params" | — |
| 16 Jun 2026 | kuralme | "init **moveitpro 9** build" | Testing **PickNik MoveIt Pro 9** (commercial motion-planning platform; general knowledge) |
| 26 Jul 2026 | Dmitri Manajev | "config(uf850): drop 8.x leftovers from the **admittance controller**"; "fix **jtac** warnings" | Admittance (compliant) control. "JTAC" is likely MoveIt Pro's joint-trajectory admittance controller `[INF]` |
| 6 Aug 2026 | shalman-khan | "feat(uf850): add **cartesian_compliance_controller (FDCC)**" | Forward-dynamics compliance control (open-source FZI controller; general knowledge) |
| 11–12 Aug 2026 | shalman-khan, kendrickchin | "enable **ft_sensor_enable/set_zero**, collision_sensitivity/rebound, get_ft_sensor_data services for **real-hardware FT streaming**"; "enable **ft_sensor_iden_load/cali_load** for payload gravity compensation" | These are **UFACTORY's own FT-sensor API calls**, so the robot very likely uses **UFACTORY's 6-axis F/T sensor** on real hardware `[INF]` |
| 13 Sep 2026 | Dmitri Manajev | "fix(ft): align broadcaster frame with Gazebo sensor origin" | — |
| **21 Sep 2026** | shalman-khan | "Add FDCC compliance controller config and **seat-lift sim** hooks" (branch `feat-FDCC-Seat-Lift-Sim-Site`) | **Lifting the toilet seat with force-compliant control**, in simulation |

**Analysis** `[INF]`:
- **Contact-rich manipulation is current R&D** (Mar → Sep 2026): F/T sensing, admittance/compliance control, seat lifting.
- This fits the brochure's "seat lifting, flushing" claims, and suggests those tasks **were still being engineered in Aug–Sep 2026**, after the Mar 2026 Mk2 brochure.
- "Contactless" applies to the *cleaning*; *seat lifting* is contact-based and force-controlled.

## 4. Cameras

| Camera | Evidence | When | Status |
|---|---|---|---|
| **Luxonis OAK-D S2 PoE** (auto-focus) | Their DepthAI fork wires `OAK-D-S2-POE.stl` into the robot URDF as `link_camera` (Arshad Khan, "changes to include this camera in hivebotics") `[V][S071]`. **The brochure's camera specs match it exactly** `[S072]`: stereo **OV9282 1280×800 @120 fps, global shutter, 89.5° DFOV**; colour **IMX378 4056×3040 @60 fps, rolling shutter, 78° DFOV** (78° = AF variant) | Dec 2025 – Jan 2026 | **Confirmed** (code + spec match) as the **Mk2 brochure's depth + RGB camera** |
| **Orbbec Gemini 335Le** (Ethernet) | Named in Hivebotics' added `mode_config.yaml` ("setting these does nothing on gemini 335Le"); custom passive/active/adaptive stream modes to save bandwidth `[V][S071]` | Mar – Jul 2026 | **In use as of Jul 2026.** Possibly additional or replacing the OAK-D. Newer than the brochure |
| **Intel RealSense D435i** | Robot description: `camera_name:='wrist_mounted'` on UF850's D435i macro `[V][S071]` | Jan 2026 | **Wrist camera in the robot model/sim.** Real-hardware use not proven |
| YDLIDAR (2D) | Fork with no own commits | 2024 | Weak: older prototype? |

Not visible on GitHub: the **3D LiDAR** (Livox Mid-360 per brochure, S061). There's no Livox driver fork; they may use upstream `livox_ros_driver2` unmodified `[INF]`.

## 5. Software stack (from code) `[V][S071]`, `[INF]` where marked

**ROS 2 Humble** (Ubuntu 22.04; also building on Kilted) · **ros2_control** (arm + mecanum wheels) · **MoveIt 2** + **MoveIt Task Constructor** · **MoveIt Pro 9** (being tested, Jun 2026) · admittance controller ("JTAC") + **FDCC cartesian compliance controller** · **Gazebo** simulation (toilet / seat-lift sim sites) · Docker/CI · private `hivebotics_description`.

## 6. Contributors `[V][S071]`

| GitHub | Name | Profile says | Hivebotics work | Window |
|---|---|---|---|---|
| **arsh09** | **Muhammad Arshad Khan** | Senior Software Engineer, **JABAS.AI**, **Lincoln, UK** | Initial integration of xarm_ros2, DepthAI and Orbbec forks; mecanum/FT/controllers | Dec 2025 – Mar 2026. Possibly a contractor or remote engineer `[INF]` |
| **kendrickchin** | **Kendrick Chin** | (empty) | Merges PRs; hivebotics_description; real-hardware FT | Jan – Aug 2026. **Head of Engineering** (LinkedIn, S064) |
| **yqchau** | **Yuan Qi Chau** | Company: **"@hivebotics"**; bio "Optimizing Signal v. Noise" | Controller params | Apr 2026 |
| **legalaspro** | **Dmitri Manajev** | Zurich/Remote; manajev.com | Admittance controller, FT frame | Jul – Sep 2026 (joined May 2026, S067) |
| **shalman-khan** | **Shalman Khan** | (empty) | **FDCC compliance, FT services, seat-lift sim; Orbbec stream modes** | Jul – Sep 2026 |
| **cheriehu** | **Cherie Hu** | (empty) | Low-poly UF850 meshes | Mar 2026 |
| **kuralme** | **M. Ege Kural** | kuralme.github.io; **only public org member** | MoveIt Pro 9 build | Jun 2026 |

## 7. What this means for Ubanthu `[INF]`

1. **Hardware is now fully mapped and commodity:**
   - arm: UFACTORY 850 (+ likely UFACTORY F/T sensor);
   - cameras: Luxonis OAK-D S2 PoE → Orbbec Gemini 335Le, plus a RealSense D435i on the wrist;
   - LiDAR: Livox Mid-360;
   - compute: AMD Ryzen + NVIDIA GPU;
   - base: custom mecanum.

   Everything is off the shelf.
2. **Their engineering focus in 2026 is manipulation control** (force/compliance, seat lifting, motion planning), **not perception**. **Nothing public touches contamination detection or the "scored before/after check"**; that code (if it exists) is private.
3. **Small, distributed, partly remote team** (Singapore, Zurich, UK, US field), with a tooling choice of a commercial planner (MoveIt Pro).
4. **Camera churn** (OAK-D → Orbbec within ~6 months, plus a RealSense) suggests **perception hardware is still being iterated**.

## Open questions
- [ ] Is the Orbbec Gemini 335Le replacing the OAK-D S2 or added alongside it (e.g. base vs. arm)?
- [ ] Does the real robot have the RealSense D435i at the wrist?
- [ ] Which UFACTORY F/T sensor (model, range)?
- [ ] Do Arshad Khan (UK, JABAS.AI) and others work for Hivebotics as employees or contractors?
- [ ] Any public repos by Kendrick Chin, Shalman Khan, Yuan Qi Chau or Cherie Hu with more Hivebotics work?
