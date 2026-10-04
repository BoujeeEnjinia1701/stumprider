---
doc_id: SMR-REQ-001
title: StumpRider requirements
project: StumpRider
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2; targets kept, design canoe and snag cases defined, concept status for each requirement
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 status from SMR-CAL-001 on the constructable design; R1, R3, R7 and R10 not met or at risk, each a decision for Amish
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish's decisions of 2026-10-03 (10B, 11A then C, 12A, 13C; SMR-DDR-003) carried out; R3 and R7 restated, R10 verification on the local variant; status from SMR-CAL-001 v0.2
- version: "0.5"
  date: '2026-10-04'
  author: Amish Chadha
  change: "R7 judged on the bamboo local variant (round-3 decision 2A, SMR-DDR-004); the aluminium prototype's 4.28 kg is recorded, not a failure of R7"
---

# StumpRider requirements

Targets are unchanged from the scaffold. On 2026-10-03 Amish said: "i agree with all the 46 recommendations you provided. please proceed." This decided R1 (10B, a hook head), R3 (11A then C), R7 (12A) and R10 (13C), recorded in SMR-DDR-003. As a result R3 is restated to name the canoes it covers, R7 is restated to apply to the kit carried to and from the canoe, and R10 is verified on the bamboo local variant. Status is on paper at TRL 3, from the calculation note SMR-CAL-001 v0.2; tags in brackets point to its results. On 2026-10-04 Amish decided option 2A on the aluminium prototype's carried mass: "For round 3, I agree with all your proposed recommendations". R7 is judged on the bamboo local variant (3.89 kg, met); the aluminium prototype's 4.28 kg is recorded, not a failure of R7 (SMR-DDR-004). Decisions are in the register SMR-DEC-001.

> **Safety:** R3 is a safety requirement: the shear pin is what keeps the pull from rolling the canoe. Nothing here relaxes the rules that nobody enters the water and that every person on the canoe wears a life jacket.

*Table 1. Requirements and TRL 3 status.*

| ID | Requirement | Target | Verification (TRL 3 or later) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Free a gillnet snagged on a submerged branch without anyone entering the water | At least 8 of 10 staged snags freed from the canoe | Tank or shallow-lake trials with staged branches at TRL 4, the hook head tried beside the ring | At risk: hooked nets need 81 to 126 N, well inside the pin [F1, F2]; a net wrapped once round needs 368 N to 2.3 kN [F3, F4], falling to 162 to 493 N once the hook head has worked it back half a turn [F7, F8] |
| R2 | Reach snags at working depth | Pole reach at least 4 m (13 ft); tether-cord method to 6 m (20 ft) | Measured at trial site | Met on paper: 4.18 m from top hand to ring [R1]; tether to 8 m [R3] |
| R3 | Limit side pull on the canoe | Shear pin breaks at a set load within plus or minus 15 % of its rating, below the tested roll load of the canoe it is used from. Used only from canoes 7 m or longer with at least three crew; a smaller canoe class is served only once heel tests at TRL 4 have set a pin for it (restated 2026-10-03, decision 11A then C) | Pull tests on CalRig; heel tests by canoe size class at TRL 4, with a pin diameter set per class | Met on paper where the tool is allowed: design canoe 3.4 deg kneeling, 4.4 deg standing at the top of the band [H5, H6]. A small dugout would heel 24 deg [K5] and is excluded by the rule. The band holds only if each wire reel is calibrated |
| R4 | Protect the net | No more than 5 broken meshes per release on standard 90 to 150 mm mesh | Mesh count after staged releases | Cannot be shown on paper; the pin caps the pull at 347 N [P3] |
| R5 | Fast to use | Median release time under 5 minutes once the snag is found | Timed trials with fisher crews | Cannot be shown on paper |
| R6 | Fit any common net line | Ring clips onto lines and headropes from 4 to 16 mm diameter | Fit check on sample lines | Met on paper: hinged ring, 100 mm inside [R4] |
| R7 | Stows in a canoe | Packed length under 1.6 m (5.2 ft); mass carried to and from the canoe under 4 kg (8.8 lb), with the gunwale crutch left clamped on the canoe and the jigging weight kept at the landing (restated 2026-10-03, decision 12A) | Measurement | Met, judged on the bamboo local variant, 3.89 kg [V3] (decision 2A, 2026-10-04); the aluminium prototype's 4.28 kg [M11] is recorded, not a failure of R7. Packed length 1.55 m [M9] |
| R8 | Survive wet storage | No functional corrosion or rot after 6 months stored wet in a canoe | Field durability check with partner crews | Met on paper: galvanised steel, 6063 aluminium, stainless pins and rivets, polyester, polyethylene; borax-treated bamboo and zinc-painted ferrules in the local variant, to be watched in the field check |
| R9 | Locally buildable | Built by a village workshop from the drawings using hand tools and a small welder in under one day | Build trial with a local smith | At risk: about 8.1 h for one smith with the hook head [T1], galvanising sent out; inside the accuracy of the estimate |
| R10 | Affordable | Parts cost under USD 40 per kit | Costed bill of materials from local prices, on the bamboo local variant with one crutch and jigging weight shared by five canoes (decision 13C) | Not met: USD 54.90 for the bamboo local variant [V8] and USD 95.50 for the aluminium prototype [V9], at prototype prices |

## Assumptions

- Most snags are on branches or trunks within a few metres of the surface, as described on Volta Lake.
- The crew can hold tension on the net line above the snag while the ring is run down, and slacken it while the operator lifts.
- Canoes under 7 m or with fewer than three crew are outside the scope until per-class pins are set (R3).
- Design canoe: 8 m plank canoe, 1.1 m waterline beam, three crew, 550 kg; hard case: 5.5 m dugout, two crew, 280 kg (SMR-CAL-001, section 3). Both are assumptions until measured.
- Boat owners will use a tool if it is faster than sending someone down.
