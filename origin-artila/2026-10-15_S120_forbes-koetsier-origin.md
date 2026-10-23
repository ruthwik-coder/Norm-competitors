# Forbes (John Koetsier), "This Robot Finishes Drywall 3X Faster Than Humans. Now It Has $20 Million To Learn More Trades" — 15 Oct 2026

[← Origin profile](origin-artila.md) · Source **S120** · https://www.forbes.com/sites/johnkoetsier/2026/10/15/this-robot-finishes-drywall-3x-faster-than-humans-now-it-has-20-million-to-learn-more-trades/ · Text supplied by Vishal 2026-10-24. **Summary and short quotes only** (Forbes copyright; the full text is kept locally and not pushed).

Koetsier is a Forbes **senior contributor**; the article is based on the press release plus an email Q&A with CEO Yogesh Ghaturle `[3P]` (claims inside are `[CC]`).

## New facts (not in earlier sources)

| Topic | What the article says |
|---|---|
| **3× claim, defined** | Measured "across a complete shift, including human setup, tool changes, material replacement and end-of-day maintenance" (Ghaturle) |
| **Not fully autonomous** | An **existing crew member doubles as the robot's operator**: maps the space with the robot, checks the tool, picks the work area, brings materials, does extra tool changes and maintenance. After setup, OG-1 works on its own |
| **Perception** | Recognises **200 kinds of job-site objects**; skips windows, doors and openings; **"checks the quality of its own work as it goes"** |
| **Hardware** | **Three-wheeled base, counterbalanced structure, a lift and an arm**; fits through doors, reaches 14 ft; holds a tool against a wall with steady force. Wheeled base chosen for stability and battery life (vs humanoids) |
| **No cordoned area** | Other trades keep working around it |
| **Training data** | Mostly their own, gathered three ways: (1) live deployments: 3D scans, site images, depth, robot behaviour, **tool contact forces and finished-surface quality**; (2) a lab where a **dedicated construction crew builds and resets job-site environments** for expert demos and teleop; (3) high-fidelity simulation from real site scans + construction **world models**. Also public video and open-source pretrained models for some perception |
| **Generalisation claim** | Can start on a new site "without retraining or post-training" |
| **Site types** | Commercial spaces, multifamily apartments, **data centres**, hotels, **warehouses** |
| **Roadmap (2027)** | After wall finishing and painting: **taping, drywall installation, stud installation, drilling, conduit installation**, same hardware with interchangeable tools. This confirms the roadmap in the earlier AI summary (S108) |
| **Board** | **Vivin Hegde (Zacua) has joined Origin's board**, which confirms the earlier unverified claim (S109) |
| **Economics** | RaaS only, no upfront purchase; customers save **20% from day one** *after* the RaaS fee and the operator's time. Claim: contractor net margins from **5–7% to 15–25%** |
| **Fleet** | Website listed **four active robots** and 100,000+ sq ft delivered (Dealroom/Mint said six, S113) `[CONFLICT]`, probably different dates |
| **Timing** | Founded early 2025; first robots on NY job sites **within 10 months** |
| **Market** | Zacua / Hilti Ventures / 94 Ventures report: construction robotics raised **US$1.36B in Q1–Q3 2025**, up 125% on all of 2024; robots are < 0.03% of global construction spending |
| **Peers named** | **Canvas** (drywall finishing), **Zinova** ("tool intelligence" for ordinary power tools) |

## Lessons Ghaturle states (useful for Ubanthu) `[CC]`

1. "If a robot performs the final task well but needs frequent manual intervention to get there, customers will not adopt it." Robust on **every subtask**, not just the headline one (same lesson as Peanut's CTO, S096/S097).
2. **Utilisation:** a single-task robot sits idle when the site moves to another trade; multi-trade keeps it working.

## Analysis `[INF]`

- "Checks the quality of its own work as it goes" + "finished-surface quality" logged as training data = **verification loop as both product feature and data source**, the same idea as Ubanthu's contamination verification.
- The honest operator model (one crew member runs the robot) is a realistic template for restroom robots too: a cleaner supervises 1+ robots rather than full autonomy from day one.
