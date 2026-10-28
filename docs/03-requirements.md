---
doc_id: SMR-PRS-001
title: StumpRider product requirements and specifications
project: StumpRider
doc_type: Product requirements and specifications
version: "0.7"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold (as SMR-REQ-001)
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
- version: "0.6"
  date: '2026-10-24'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: SMR-REQ-001 becomes SMR-PRS-001 (STANDARDS section 22); R1 to R10 migrated to PR-001 to PR-010 with the old number in Was, tolerance, units and the user requirement each traces to; PR-011 to PR-013 added from the existing design rules (pin calibration, weakest link, marking); status from SMR-CAL-001 v0.3 (hook head of 12 mm bar, SMR-DEC-001 F1; dynamic heel, O6)"
- version: "0.7"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (\"i approve of your recommendations\", SMR-DEC-001): PR-003 restated for O6 (5 deg static limit, steady-lift rule) and O9 (measured displacement x GM criterion at the TRL 4 heel test); PR-010 USD 66.90 for O8; PR-013 tag rule; PR-012 notes O10 stopped"
---

# StumpRider product requirements and specifications

What the design must do, each traced to a user need in SMR-URS-001. Targets are unchanged from SMR-REQ-001 and remain proposals for review with a co-design partner. Status is on paper at TRL 3, from the calculation note SMR-CAL-001 v0.3; tags in brackets point to its results. Amish's decisions are as recorded in SMR-REQ-001 v0.5 and SMR-DEC-001: R1 (10B, a hook head), R3 (11A then C), R7 (12A, then 2A) and R10 (13C) of 2026-10-03 and 2026-10-04. This upgrade changes no target. Method: STANDARDS section 22.

> **Safety:** PR-003, PR-011 and PR-012 are safety requirements: the shear pin is what keeps the pull from rolling the canoe, so it must be calibrated and must be the weakest link. Nothing here relaxes the rules that nobody enters the water and that every person on the canoe wears a life jacket.

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status | Was |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Free a snagged net | The kit shall free a gillnet snagged on a submerged branch without anyone entering the water | 8 of 10 staged snags freed from the canoe | at least | snags | Analysis (SMR-CAL-001 s4), TRL 3; staged-snag trials with the hook head beside the ring, TRL 4 | At risk: hooked 81 to 126 N, inside the pin [F1, F2]; wrapped 368 N to 2.3 kN [F3, F4], 162 to 493 N once worked back half a turn [F7, F8] | R1 |
| PR-002 | UR-002 | Performance | Reach | The pole shall reach from the top hand to the ring, and the tether shall work snags below the surface | Pole 4.0; tether 6.0 | at least | m | Analysis (SMR-CAL-001 s5), TRL 3; measured at the trial site, TRL 4 | Met on paper: 4.18 m [R1]; tether 8 m [R3] | R2 |
| PR-003 | UR-003 | Safety | Limit the side pull | The shear pin shall break at a set load within its band, below the roll load of the canoe it is used from; used only from canoes 7 m or longer with at least three crew until heel tests at TRL 4 set a pin for a smaller class (restated 2026-10-03, 11A then C), and from 2026-10-25 only from canoes whose measured displacement x GM is at least about 260 kg m with the margin set at the heel test (O9); the operator lifts steadily, never with a jerk (O6) | 302 nominal; static heel at the top of the band 5 | plus or minus 15 % (256 to 347 N); heel at most | N; deg | Analysis (SMR-CAL-001 s3), TRL 3; CalRig pull tests and heel tests by canoe class, TRL 4 | At risk: static heel 3.4 deg kneeling, 4.4 deg standing [H5, H6] on screening hydrostatics (5.1 deg with a 1.0 m beam [Q1]); 6.5 deg peak for a quick pull held just under the pin [H11], ruled out by the steady-lift rule and measured at TRL 4 (O6, decided 2026-10-25); measured righting-moment criterion added (O9, decided 2026-10-25) | R3 |
| PR-004 | UR-004 | Performance | Protect the net | Freeing the net shall break no more than a few meshes on standard mesh | 5 on 90 to 150 mm mesh | at most | broken meshes per release | Mesh count after staged releases, TRL 4 | To verify at TRL 4: the pin caps the pull at 347 N [P3] | R4 |
| PR-005 | UR-005 | Usability | Fast to use | Median release time once the snag is found | 5 | at most | min | Timed trials with fisher crews, TRL 4 | To verify at TRL 4 | R5 |
| PR-006 | UR-006 | Usability | Fit any net line | The ring shall clip onto lines and headropes over the whole range | 4 to 16 | range | mm line diameter | Analysis and inspection (SMR-CAL-001 s5), TRL 3; fit check on sample lines, TRL 4 | Met on paper: hinged ring, 100 mm inside [R4] | R6 |
| PR-007 | UR-007 | Packaging and transport | Stows in a canoe | Packed length; mass carried to and from the canoe with the crutch left clamped on and the jigging weight at the landing (restated 2026-10-03, 12A) | Length 1.6; mass 4.0 | at most | m; kg | Analysis (SMR-CAL-001 s8), TRL 3; weighed at TRL 4 | At risk: met on paper on the bamboo local variant, 3.95 kg [V3] (decision 2A, 2026-10-04), but the 0.05 kg margin after F1 is inside the uncertainty (wet bamboo, zinc, paint; independent review); aluminium prototype 4.34 kg [M11] recorded, not a failure. Packed 1.55 m [M9] | R7 |
| PR-008 | UR-008 | Materials | Survive wet storage | No functional corrosion or rot after storage wet in a canoe | 6 | at least | months | Analysis (SMR-STM-001 S11 to S13), TRL 3; field durability check with partner crews, TRL 4 | Met on paper: galvanised steel, 6063 aluminium, stainless pins and rivets, polyester, polyethylene; treated bamboo and zinc-painted ferrules in the local variant to watch | R8 |
| PR-009 | UR-009 | Physical architecture | Locally buildable | A village workshop shall build a kit from the drawings with hand tools and a small welder | 8 | at most | h, one smith | Analysis (SMR-CAL-001 s9), TRL 3; build trial with a local smith, TRL 4 | At risk: about 8.1 h [T1], galvanising sent out | R9 |
| PR-010 | UR-010 | Performance | Affordable | Parts cost of one kit at local prices, on the bamboo local variant with its own crutch and one jigging weight shared by five canoes (13C as changed by O8, 2026-10-25) | 40 | at most | USD | Costed BOM (SMR-CAL-001 s9, s10), TRL 3; local prices, TRL 4 | Not met: USD 66.90 bamboo local variant [V8] (USD 54.90 before O8); USD 95.50 aluminium prototype [V9] | R10 |
| PR-011 | UR-003 | Safety | Calibrated pin wire | Every reel of pin wire shall be O-temper aluminium and its sample pins shall break inside the band before any pin from it is used | 10 pins inside 256 to 347 | all | N | Inspection of the reel and CalRig breaks (SMR-BLD-001 first checks), TRL 4 | To verify at TRL 4 (SMR-STM-001 S1, S16) | |
| PR-012 | UR-003 | Safety | The pin is the weakest link | Every load path between the operator's hands and the snag other than the shear pin shall be at least twice as strong as the top of the pin band | 2 | at least | x | Analysis (SMR-CAL-001 s6), TRL 3 | At risk: aluminium prototype met on paper (smallest factor 2.21, pole buckling [S2]; hook head 3.1 after F1 [S12]; pole side bending 2.4 [S17]); hook head with the bight on the tip leg 1.58 at the bend [S13] and 1.87 in the straight shank [S13a] (O10: the approved gusset was stopped on 2026-10-25 because it does not reach the shank, back with Amish); bamboo pole buckling 1.49 [V5] | |
| PR-013 | UR-011 | Safety | Marked and handed out with protection work | The pole head shall carry the pin rating, and each kit a pictorial tag with the rules (nobody in the water, life jackets, kneel, slacken, lift steadily and never jerk, cut rather than capsize); kits are handed out only through partners | Rating mark and tag on every kit | all | kits | Inspection (BOM line 19; SMR-BLD-001 safety stops), TRL 3; partner distribution plan, TRL 4 | Met by design for the rating mark; tag artwork and distribution plan to do with the partner | |

Categories: physical architecture, performance, materials, usability, packaging and transport, safety, electrical, software. Status: met on paper, met by design, at risk, not met, over target, withdrawn, to verify at TRL 4.

## Assumptions

- Most snags are on branches or trunks within a few metres of the surface, as described on Volta Lake.
- The crew can hold tension on the net line above the snag while the ring is run down, and slacken it while the operator lifts.
- Canoes under 7 m or with fewer than three crew are outside the scope until per-class pins are set (PR-003).
- Design canoe: 8 m plank canoe, 1.1 m waterline beam, three crew, 550 kg; hard case: 5.5 m dugout, two crew, 280 kg (SMR-CAL-001, section 3). Both are assumptions until measured.
- Boat owners will use a tool if it is faster than sending someone down.
