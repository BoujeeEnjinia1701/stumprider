---
doc_id: SMR-REQ-001
title: StumpRider requirements
project: StumpRider
doc_type: Requirements
version: "0.4"
status: Draft
date: '2026-10-03'
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
  change: Status after Amish's round 2 decisions (SMR-DDR-003, D-A1 B, D-A2 A then C at TRL 4, D-A3 A, D-A4 C) from SMR-CAL-001 v0.2; targets unchanged
---

# StumpRider requirements

Targets are unchanged from the scaffold. Status is on paper at TRL 3, from the calculation note SMR-CAL-001 v0.2; tags in brackets point to its results. Amish decided the four TRL 3 requirement decisions on 2026-10-03 (SMR-DDR-003): a hook head for wrapped nets (R1); the interim rule on canoes printed on the pole head now, with a pin per canoe class set after the TRL 4 heel tests (R3); the crutch left on the canoe and the jigging weight at the landing (R7); and a costed local production variant with bamboo sections and a crutch and weight shared by five canoes, built beside the aluminium prototype at TRL 4 (R10). New questions raised while carrying them out are in `docs/REVIEW.md` and SMR-DEC-001.

> **Safety:** R3 is a safety requirement: the shear pin is what keeps the pull from rolling the canoe. Nothing here relaxes the rules that nobody enters the water and that every person on the canoe wears a life jacket.

*Table 1. Requirements and TRL 3 status.*

| ID | Requirement | Target | Verification (TRL 3 or later) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Free a gillnet snagged on a submerged branch without anyone entering the water | At least 8 of 10 staged snags freed from the canoe | Tank or shallow-lake trials with staged branches at TRL 4 | At risk: hooked nets need 81 to 126 N, well inside the pin [F1, F2]; a net wrapped once round needs 368 N to 2.3 kN, above it [F3, F4]. The hook head (SMR-DDR-003) gives a second way to unwind a wrap within the pin [F7]; it is tried beside the ring in the TRL 4 staged-snag trials |
| R2 | Reach snags at working depth | Pole reach at least 4 m (13 ft); tether-cord method to 6 m (20 ft) | Measured at trial site | Met on paper: 4.18 m from top hand to ring [R1]; tether to 8 m [R3] |
| R3 | Limit side pull on the canoe | Shear pin breaks at a set load within plus or minus 15 % of its rating, below the tested roll load of a typical canoe | Pull tests on CalRig and a canoe heel test | Met on paper where the tool is allowed: the design canoe heels 3.4 deg kneeling, 4.4 deg standing at the top of the band [H5, H6]. Canoes under 7 m or with fewer than three crew are not served: the interim rule is printed on the pole head (SMR-DDR-003); a small dugout would heel 24 deg [K5]. Planned TRL 4 step: heel tests by canoe class set a pin per class. The band holds only if each wire reel is calibrated |
| R4 | Protect the net | No more than 5 broken meshes per release on standard 90 to 150 mm mesh | Mesh count after staged releases | Cannot be shown on paper; the pin caps the pull at 347 N [P3] |
| R5 | Fast to use | Median release time under 5 minutes once the snag is found | Timed trials with fisher crews | Cannot be shown on paper |
| R6 | Fit any common net line | Ring clips onto lines and headropes from 4 to 16 mm diameter | Fit check on sample lines | Met on paper: hinged ring, 100 mm inside [R4] |
| R7 | Stows in a canoe | Packed length under 1.6 m (5.2 ft); total mass under 4 kg (8.8 lb) | Measurement | Not met by 0.22 kg: packed length 1.55 m [M9] meets; with the crutch left clamped on the canoe and the jigging weight at the landing (SMR-DDR-003) the carried kit is 4.22 kg with the hook head [M11]. The local production variant carries 3.56 kg [O10] |
| R8 | Survive wet storage | No functional corrosion or rot after 6 months stored wet in a canoe | Field durability check with partner crews | Met on paper: galvanised steel, 6063 aluminium, stainless pins and rivets, polyester, polyethylene |
| R9 | Locally buildable | Built by a village workshop from the drawings using hand tools and a small welder in under one day | Build trial with a local smith | Met on paper, at the limit: about 8.0 h for one smith with the hook head [T1], galvanising sent out |
| R10 | Affordable | Parts cost under USD 40 per kit | Costed bill of materials from local prices | Not met: USD 95.50 at prototype prices with the hook head [C1]; the local production variant, USD 55.90 (`bom/bom-local-variant.csv`) [C8] |

## Assumptions

- Most snags are on branches or trunks within a few metres of the surface, as described on Volta Lake.
- The crew can hold tension on the net line above the snag while the ring is run down, and slacken it while the operator lifts.
- Design canoe: 8 m plank canoe, 1.1 m waterline beam, three crew, 550 kg; hard case: 5.5 m dugout, two crew, 280 kg (SMR-CAL-001, section 3). Both are assumptions until measured. Until the TRL 4 heel tests the tool is used only from canoes of 7 m or more with at least three crew.
- R7 is judged on the kit carried in the canoe: the gunwale crutch is a fitting left clamped on the canoe and the jigging weight is kept at the landing for deep sets.
- Boat owners will use a tool if it is faster than sending someone down.
