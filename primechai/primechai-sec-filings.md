# Primech Holdings: SEC filings deep dive (20-F + 6-Ks)

[← Primech AI profile](primechai.md) · [← Master document](../COMPETITOR_INTELLIGENCE.md) · Sources: **[S043]** 20-F FY2026, **[S044]** 6-K press releases · **Added:** 2026-10-02

**How this was read:** Claude opened each filing on sec.gov in the built-in browser and searched the full text: the 20-F is ~493k characters, and 26 6-Ks were filed between Feb 2025 and Sep 2026. Quotes are short excerpts; figures are copied from the filing tables. SEC company page: CIK 0001891944 (Nasdaq: PMEC).
- A first pass with an automated web summariser **missed most mentions** (it reported "HYTRON not found"), so none of its output was used.
- **Gemini's descriptions of individual 6-Ks were wrong** (e.g. it said the Feb 2025 filing covered "pilot trials"; it is actually an investor presentation).

---

## 1. Financials (20-F, FY ended 31 Mar 2026) `[V][S043]`

| US$ thousands | FY2026 | FY2025 |
|---|---|---|
| **Total revenue** | **78,009** | 74,349 |
| Facilities services | 63,940 | 58,594 |
| Stewarding | 6,242 | 8,354 |
| Office tenancy cleaning | 7,563 | 7,089 |
| Sales of products | 252 | 312 |
| **Leasing of cleaning robots** | **12** | – |
| **Net loss** | **(2,967)** | (2,220) |

**Robotics segment, FY2026** (segment note, F-24):

| US$ thousands | Robotic |
|---|---|
| Revenue | **12** |
| Gross profit/(loss) | (145) |
| Sales & marketing | (374) |
| G&A | (1,476) |
| **R&D** (incl. staff) | **(414)** |
| **Segment loss** | **(2,479)** |

- R&D was "not significant" in FY2025 and ~$0.4M in FY2026.
- 99.7% of revenue comes from Singapore.
- Contracted backlog is ~$177.7M, almost all cleaning services.
- **Robots were first sold or leased in FY2026, with "no significant revenue".**

**Analysis** `[INF]`: HYTRON earned about **US$12k of lease revenue in a full year**. That is roughly one or two robots on lease. Compare the Mar 2025 announcement of a plan to roll out **300 robots** across Singapore, Hong Kong and Dubai. The robotics unit loses about **$2.5M a year**, funded by a cleaning business with thin margins.

## 2. Corporate structure `[V][S043]`

- **Primech AI Pte. Ltd.** was set up on **29 May 2024**. **Primech Holdings owns 51%.** The other **49% is held by Zhang Youwei** (see section 5).
- Primech AI Holdings Ltd and Primech AI Investments Ltd were incorporated 28 Mar 2024. On **16 Apr 2024** an MOU was signed with "an independent third party" to "jointly introduce an eco-friendly and fully automatic AI-powered toilet cleaning robot". The 20-F doesn't name the party. Possibly Zhang `[INF]`.
- **Primech USA Inc.** was incorporated 12 Sep 2025 (North America).
- **Primech HK Ltd** was incorporated May 2024.
- Headquarters moved in 2026 to **60 MacPherson Road, Siemens Centre #04-08, Singapore 348615**. The patent and older filings give 23 Ubi Crescent.
- Primech AI has small HSBC import-finance and term loans (~S$0.5M each), personally guaranteed by Ho Kin Wai and Kwek Jin Ngee Vernon (an indirect major shareholder).
- IPO proceeds were partly used for "establishing our team of software developers, programmers, and engineers to build our own robots".

## 3. HYTRON in the 20-F `[V][S043]`

- "Our flagship product, Hytron, is an AI-powered autonomous restroom cleaning robot designed to clean toilets, urinals, sinks, mirrors, and surrounding floor areas … **without requiring pre-programmed routes. Initial on-site mapping is performed by a technician at deployment.**"
- Listed in Primech's own robot fleet as of 31 Mar 2026 ("Washroom Cleaning Robot – Hytron"), alongside **bought-in** floor robots: Avidbot, Ecobot Scrub 50/75, Cenobots L50/L4, Metabot M45, Phantas, Kabam Manny, Max Robot, **LionsBot R3 Vac**, Zaco X1000, Simpple Udeer.
- **`[CONFLICT]` within the 20-F:**
  - One passage says the fleet robots are "purchase[d] from third parties".
  - Another says "We design, developed and manufacture cleaning robots … since FY 2026".
  - Likely explanation `[INF]`: the floor robots are bought in, and HYTRON is in-house.
- The 20-F names no patents ("does not own or use any trademark, patent or other license which is material"). The PCT application WO 2025/259178 isn't mentioned.
- Plans stated: expand HYTRON beyond Singapore; explore removable batteries; "we also intend to develop an autonomous toilet cleaning robot" (wording carried over from older filings).
- Risk factors: robots may become obsolete; repair costs once the warranty ends; robot purchases depend on **Singapore government grants**.

## 4. HYTRON announcements (6-K press releases) `[CC][S044]`

| Date | Announcement | Key details |
|---|---|---|
| Jun 2024 | (reported in the 27 Mar 2025 half-year update) | HYTRON shown at **CleanEnviro Summit Singapore 2024**. Described as in development, "with patents pending", featuring "3D-cleaning and electrolyzed water". |
| Jan 2025 | Investor presentation | "**HYTRON Mark 1 & 2**". Feature list includes smart navigation, **door handling, lid control**, auto flushing/scrubbing/drying, self-charging, **"UV bacteria detection"**, "electrolyzed, contactless cleaning", automatic water intake and waste, air blower. Labelled "NEW features coming with the Hytron Mark 2". The slide text is garbled, so *exactly which features are Mark 2-only is unclear*. Also: Primech uses **Tersano SAO** (stabilised aqueous ozone) water in its cleaning services; "Hytron 1 utilizes electrolyzed water". |
| 4 Mar 2025 | RaaS launch + **MoU with CCG Property Services (Chinachem Group, Hong Kong)** | 2-year MoU to deploy HYTRON at **Nina Tower 1**. "Initial phase" of a plan to roll out **300 cleaning robots across Singapore, Hong Kong and Dubai**. |
| 24 Jul 2025 | **FY2025 results** | "Successful deployments" at **Temasek Polytechnic**, **"a major Singapore shopping mall"** and **"one of Singapore's largest hospitals"**. Partnerships: Hong Kong (Chinachem), **Japan (Golden Rim Investment)**, **Europe (TCOrobotics GmbH: Germany, Austria, Switzerland)**. **"China production partnership targeting 300 robots' initial production capacity."** Launch of a compact **"HYTRON Lite"** model. **No unit counts given.** |
| 28 Aug 2025 | **MoU with Savills Property Management** | Distribution of HYTRON in **Greater China** on a RaaS model. **Compute: NVIDIA Jetson Orin "Super" module.** Quote from Charles Ng, COO of Primech AI. |
| 18 Sep 2025 | North America expansion | Primech USA |
| 29 Sep 2025 | **CMS Berlin 2025** | Launched the "next-generation HYTRON". Claims **250+ qualified inquiries** (hotel chains; interest from Europe, US, Middle East, Australia, **Japan**). "World Tour": Tokyo cleaning expo Nov 2025, **CES Las Vegas Jan 2026**. |
| 9 Oct 2025 | **">99% disinfection efficacy"** | "Bacterial reduction exceeding 99% in independent testing conducted by a top-tier laboratory", consistent with US hospital-grade thresholds. **The lab, test method, organisms and protocol are not named.** References a deployment "in a leading hospital in Singapore". |
| 16 Oct 2025 | MoU with **GAIB** | **Crypto tokenisation of HYTRON robots** for fractional ownership and on-chain credit, to fund deployment. |
| 22 Oct 2025 | **Aramark** Facilities Innovation Forum (Michigan, USA) | Presented HYTRON; US entry on a RaaS model. |
| 17 Nov 2025 | **Lease: HYTRON at a Singapore army camp** | Full-service lease: delivery, training, maintenance. Charles Ng quoted. |
| 12 Dec 2025 | **WELLE Environmental Group** (China, 300190.SZ) strategic framework | Planned Singapore JV for **industrial** robots. Later: WELLE (Lux) securities purchase agreement 31 Dec 2025 + convertible note Jan 2026, amended Jul 2026. |
| 24 Sep 2026 | **Lawsuit against former CTO** | See section 5 |

Other 6-Ks are routine: AGM notices, Nasdaq minimum-bid-price notices (Feb 2026 deficiency; compliance regained May 2025), constitution changes.

## 5. ⚠️ Legal dispute over HYTRON's development `[V][S044]` (6-K, 24 Sep 2026)

- **Employment:** Zhang "was employed by Primech from May 2024 to March 2026 and by Primech AI thereafter". **March 2026 is when he moved from the parent's payroll to Primech AI's, not when he left.** His counterclaim refers to "the process leading to his suspension and termination" by Primech AI. So he **did not quit; he was suspended and then fired**. The exact termination date is not disclosed, but it was before 7 Aug 2026, when Primech already called him "former CTO".
- **7 Aug 2026:** Primech and Primech AI sued **Zhang Youwei, former CTO of Primech AI**, in the Singapore High Court. The claims concern **HYTRON's development**. Primech alleges he:
  1. missed contractual development milestones,
  2. **misrepresented milestone achievement and the handover of source code and technical materials**,
  3. breached contractual and IP obligations,
  4. conspired with **another HYTRON project employee** to cause loss.
- **What Primech is asking for:** his **292,036 Primech shares** returned, plus damages.
- **15 Sep 2026, Zhang's counterclaim** (against Primech, Primech AI and CEO **Ho Kin Wai personally**):
  - an unpaid **RMB 6.0M (~US$896k) completion bonus**, linked to a financing and/or **HYTRON commercial deployment** condition;
  - wrongful termination;
  - breach of trust and confidence over **funding, staffing and management of Primech AI**, including a demand to repay a shareholder loan;
  - conspiracy;
  - **IP that he says pre-dates his employment**.
- Status: early stage, pending. Both sides deny the other's claims.

**Analysis** `[INF]`:
- **The technical lead behind HYTRON is gone, and is in court with the company.** He is also the first-named inventor on WO 2025/259178 and owns 49% of Primech AI.
- Primech itself alleges that **source code and technical materials were not properly delivered** and that **milestones were misrepresented**. That casts doubt on how mature HYTRON actually is, despite the marketing (World Tour, ">99%", 300-robot plan).
- **IP ownership is contested**: Zhang claims some of the IP pre-dates his employment. That clouds the patent application and HYTRON's software.
- With US$12k of robot revenue and a $2.5M segment loss, **HYTRON is still effectively pre-commercial**, despite Primech's "commercial" positioning in our earlier notes.

## 6. People `[V][S043][S044]`

| Name | Role | Notes |
|---|---|---|
| **Kin Wai "Ken" Ho** (50) | Chairman & CEO, Primech Holdings | Patent inventor ("Ho Kin Wai"). Background: business and investment: co-founder of Sapphire Universe (major shareholder); previously CEO of Jimu Group (footwear, HKEx); programmer at JP Morgan 2000–01; BSc Management (Royal Holloway), MSc Interactive Multimedia (Middlesex). Named in Zhang's counterclaim. Received 3M Class B preference shares in FY2026 |
| **Charles Ng Chew Poh** | COO, Primech AI | Patent inventor ("Ng Chew Poh"). Quoted in the HYTRON press releases |
| **Zhang Youwei** | Former CTO, Primech AI. Employed by Primech Holdings May 2024 – Mar 2026, then by Primech AI until **suspended and terminated** (date not disclosed; before Aug 2026). **49% shareholder of Primech AI** (per the 20-F, Jul 2026) | First-named patent inventor. Got 292,036 Primech shares in FY2025. **Being sued, and counter-suing** |
| Kit Yu Lee (40) | CFO | |
| Hansel Loo (45) | SVP Operations | |
| Khazid bin Omar (61) | SVP Corporate Services | |
| Yew Jin Sng | SVP Business Development | |
| Kwek Jin Ngee Vernon | Indirect major shareholder | Guarantor of Primech AI loans |
| William Mirecki, William Yuen, Dr. Kai Yue Jason Chan | Independent directors | |

## Source documents

- 20-F FY2026 (filed 2026-07-29): https://www.sec.gov/Archives/edgar/data/1891944/000121390026082565/ea0298377-20f_primech.htm
- 6-K index list (filing index pages): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001891944&type=6-K
- Key 6-K exhibits:
  - 24 Sep 2026 legal: `000121390026102853/ea030608901ex99-1.htm`
  - 9 Oct 2025 >99%: `000121390025097799/ea026078901ex99-1_primech.htm`
  - 17 Nov 2025 army camp: `000121390025111293/ea026595601ex99-1_primech.htm`
  - 28 Aug 2025 Savills: `000121390025081404/ea025475401ex99-1_primech.htm`
  - 4 Mar 2025 Chinachem: `000121390025019775/ea023274701ex99-1_primech.htm`
  - Jan 2025 investor deck: `000121390025014875/ea023103701ex99-1_primech.htm`

  (prefix each with `https://www.sec.gov/Archives/edgar/data/1891944/`)

## Open questions from the filings

- [ ] Which lab ran the ">99%" test, and what was the protocol? Ask Primech, or check the US press materials.
- [ ] What is "UV bacteria detection" in Mark 2? It's the closest thing in any competitor's materials to contamination detection. Is it shipped, or only planned?
- [ ] How many HYTRONs are actually deployed? **No filing gives a unit count** (checked the 20-F FY2026 fleet table and every 6-K, 2026-10-02). The 20-F fleet table lists models only, with no quantities. Named sites: Temasek Polytechnic, a Singapore mall, a large Singapore hospital, a Singapore army camp, Nina Tower 1 (HK, MoU). The "300" figure is a **plan or production-capacity target**, never a deployed count. Earlier 20-Fs (FY2024, FY2025) haven't been checked yet.
- [ ] Follow the Zhang lawsuit (Singapore High Court) for HYTRON's technical status and IP ownership.
- [ ] Is HYTRON development continuing in-house after the CTO's exit, or with the "other employee"?
- [ ] Where is Zhang Youwei now? Check LinkedIn and Chinese company registries for a new robotics venture. If he starts a competitor using IP he claims is his, that matters to us. (His bonus was set in RMB, which hints at a China link `[INF]`.)
- [ ] Does Zhang still hold 49% of Primech AI? The 20-F (Jul 2026) still says so. The lawsuit targets only his 292,036 shares in the parent, Primech Holdings.
- [ ] Exact termination date (between Mar and Aug 2026)
