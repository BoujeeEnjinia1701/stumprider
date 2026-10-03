---
doc_id: SMR-REQ-001
title: StumpRider requirements
project: StumpRider
doc_type: Requirements
version: "0.3"
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
---

# StumpRider requirements

Targets are unchanged from the scaffold. Status is on paper at TRL 3, from the calculation note SMR-CAL-001; tags in brackets point to its results. Where a requirement is not met or at risk, the options and a recommendation are in `docs/REVIEW.md` (TRL 3, Decisions for Amish) and the design decisions register SMR-DEC-001.

> **Safety:** R3 is a safety requirement: the shear pin is what keeps the pull from rolling the canoe. Nothing here relaxes the rules that nobody enters the water and that every person on the canoe wears a life jacket.

*Table 1. Requirements and TRL 3 status.*

| ID | Requirement | Target | Verification (TRL 3 or later) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Free a gillnet snagged on a submerged branch without anyone entering the water | At least 8 of 10 staged snags freed from the canoe | Tank or shallow-lake trials with staged branches at TRL 4 | At risk: hooked nets need 81 to 126 N, well inside the pin [F1, F2]; a net wrapped once round needs 368 N to 2.3 kN, above it [F3, F4] |
| R2 | Reach snags at working depth | Pole reach at least 4 m (13 ft); tether-cord method to 6 m (20 ft) | Measured at trial site | Met on paper: 4.18 m from top hand to ring [R1]; tether to 8 m [R3] |
| R3 | Limit side pull on the canoe | Shear pin breaks at a set load within plus or minus 15 % of its rating, below the tested roll load of a typical canoe | Pull tests on CalRig and a canoe heel test | At risk: met for the design canoe (3.4 deg kneeling, 4.4 deg standing at the top of the band) [H5, H6]; a small dugout would heel 24 deg [K5]. The band holds only if each wire reel is calibrated |
| R4 | Protect the net | No more than 5 broken meshes per release on standard 90 to 150 mm mesh | Mesh count after staged releases | Cannot be shown on paper; the pin caps the pull at 347 N [P3] |
| R5 | Fast to use | Median release time under 5 minutes once the snag is found | Timed trials with fisher crews | Cannot be shown on paper |
| R6 | Fit any common net line | Ring clips onto lines and headropes from 4 to 16 mm diameter | Fit check on sample lines | Met on paper: hinged ring, 100 mm inside [R4] |
| R7 | Stows in a canoe | Packed length under 1.6 m (5.2 ft); total mass under 4 kg (8.8 lb) | Measurement | Not met: packed length 1.55 m [M9] meets; the whole kit is 6.5 kg [M8] |
| R8 | Survive wet storage | No functional corrosion or rot after 6 months stored wet in a canoe | Field durability check with partner crews | Met on paper: galvanised steel, 6063 aluminium, stainless pins and rivets, polyester, polyethylene |
| R9 | Locally buildable | Built by a village workshop from the drawings using hand tools and a small welder in under one day | Build trial with a local smith | Met on paper: about 7.7 h for one smith [T1], galvanising sent out |
| R10 | Affordable | Parts cost under USD 40 per kit | Costed bill of materials from local prices | Not met: USD 92.50 at prototype prices [C1] |

## Assumptions

- Most snags are on branches or trunks within a few metres of the surface, as described on Volta Lake.
- The crew can hold tension on the net line above the snag while the ring is run down, and slacken it while the operator lifts.
- Design canoe: 8 m plank canoe, 1.1 m waterline beam, three crew, 550 kg; hard case: 5.5 m dugout, two crew, 280 kg (SMR-CAL-001, section 3). Both are assumptions until measured.
- Boat owners will use a tool if it is faster than sending someone down.
