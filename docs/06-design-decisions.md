---
doc_id: SMR-DEC-001
title: StumpRider design decisions register
project: StumpRider
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's 2026-10-03 pre-approvals; four requirement decisions proposed, awaiting Amish
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: O1 to O4 decided by Amish (10B, 11A then C, 12A, 13C; SMR-DDR-003); one new open decision on the aluminium prototype's carried mass; items to confirm and value engineering updated
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: O5 decided by Amish (round-3 decision 2A, SMR-DDR-004) and moved to Decisions made; no open decisions
---

# StumpRider design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits (the pin rating and its calibration, kneeling, slackening the line, the interim rule on small canoes, life jackets). Each takes the conservative option and names the evidence that would relax it. StumpRider is never a reason to keep children on boats and never replaces a life jacket.

## Open decisions

None. O1 to O4 were decided on 2026-10-03 and O5 (R7 on the aluminium prototype) on 2026-10-04; all are under Decisions made.

## To confirm when parts are bought

These are facts that can only be settled with real parts, a real canoe or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Shear strength of the chosen wire reel (48 MPa assumed): ten pins broken on CalRig | Pin rating and its band (R3) | SMR-CAL-001, A1; SMR-DDR-002, A2 |
| 2 | 38 mm tube with a 32.4 mm bore, or how much opening 38 x 3 tube needs | Sleeve fit | SMR-DDR-002, A1 |
| 3 | Size, mass and crew of the partner's canoes; gunwale thickness and clear side depth | Heel check (R3) and crutch fit | SMR-CAL-001, A2 to A5; SMR-DDR-002, A3 and A4 |
| 4 | How often nets hook and how often they wrap, from partner crews; how hard the hook head must pull to work a wrap back half a turn | R1 and the hook head | SMR-PRB-001; SMR-DDR-003 |
| 5 | Friction of the partner's netting on wet bark (0.3 to 0.5 assumed) | Freeing pull (R1) | SMR-CAL-001, A7 |
| 6 | Local prices for aluminium tube, bamboo, steel tube, galvanising and foam near the first fishery | R10 on the bamboo local variant | `bom/bom.csv`, `bom/bom-bamboo-variant.csv` |
| 7 | Bent ring holds 112 mm mean diameter within 2 mm | Joint gaps and ear alignment | SMR-DDR-002, A5 |
| 8 | Mesh damage at the pin rating on 90 to 150 mm mesh | R4 | SMR-REQ-001 |
| 9 | Stiffness of local bamboo culms: each culm passes the bend test (5 kg at the middle of a 1.4 m span sags 2.9 mm or less); culm diameters 34 to 38 mm slide in the 37 mm ferrule | Bamboo pole buckling (factor 1.49 at E 15 GPa, 1.0 at 10 GPa) | SMR-CAL-001 [V5], [V6], [V10]; SMR-DDR-003 |
| 10 | Borax and boric acid treatment and zinc-painted ferrules hold up for 6 months wet | R8 on the bamboo local variant | SMR-DDR-003 |
| 11 | Canoe size classes at the partner's landings and a measured pin for each class (heel tests at TRL 4) | R3 for canoes under 7 m | SMR-DDR-003 |
| 12 | Workshop time for one kit with the hook head (8.1 h estimated against one day) | R9 | SMR-CAL-001 [T1] |

## Value engineering

Value-engineering target: USD 2,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 299.50 for the prototype run of three aluminium kits, one bamboo pole set and calibration wire (USD 1,700.50 under the target). One aluminium prototype kit is USD 95.50 with the hook head; one bamboo local variant kit with the crutch and weight shared by five canoes is USD 54.90. Main cost drivers and savings worth trying:

- In the aluminium kit the largest lines are the pole, sleeves and rivets (30 %), galvanising (13 %) and the crutch (13 %); the bamboo local variant removes the first and shares the third.
- Savings still worth trying on the local variant: galvanising a batch of kits together, which spreads the galvaniser's minimum lot; zinc-rich paint only where no galvaniser is near (about USD 9, at some risk to R8); local prices for bamboo and steel tube.
- Smith's labour (about 8.1 hours a kit) is not in the parts cost; a partner workshop making kits in batches would cut it.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D10: hinged two-half ring with a pinned gate; three-section aluminium pole for the prototype; one shear pin rating, 2.0 mm soft aluminium, 302 N nominal, calibrated per reel; the pin carries push and pull; operating rules (kneel, slacken, life jackets, tether tied off, cut rather than capsize, interim rule on canoes under 7 m); jigging weight pinned to the tang; foam float winder; clamp-on roller crutch; handed out only through child-protection partners, first candidates to approach (Challenging Heights, a Volta landing-site committee through the Fisheries Commission, a Ghanaian university fisheries department; none approached); requirement targets kept | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | SMR-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C12, and assumptions A1 to A5 | Amish, same pre-approvals | SMR-DDR-002 |
| 2026-10-03 | Safety stops S1 to S5 and the first checks, including pin calibration and a moored heel test before any use on a snag (conservative; a gate, not relaxed) | Amish, same pre-approvals | SMR-BLD-001, sections 5 and 6 |
| 2026-10-03 | O1 (R1, 10B): add a hook head that pins into the same fork (about USD 3), with the unwinding technique taught. O2 (R3, 11A then C): keep the rule (canoes 7 m or longer, three crew) and plan heel tests by canoe size with a pin per class at TRL 4. O3 (R7, 12A): the crutch stays clamped on the canoe and the jigging weight at the landing (4.02 kg carried as proposed; 4.28 kg as built with the hook head and corrected masses). O4 (R10, 13C): a bamboo-pole local variant with a shared crutch and weight (USD 52.90 as proposed; USD 54.90 with the hook head) beside the aluminium prototype | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | SMR-DDR-003 |
| 2026-10-03 | Appearance model departures for the renders: a plank deck and a forearm and hand beside the packed kit; a short net line over a branch and a cut-short pole for the detail view; the shear pin shown red | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
| 2026-10-04 | O5, R7 (2A): keep the 32 x 2 aluminium pole; R7 is judged on the bamboo local variant (3.89 kg, met); the aluminium prototype's 4.28 kg is recorded, not a failure of R7; the prototype is weighed at TRL 4 | Amish: "For round 3, I agree with all your proposed recommendations" | SMR-DDR-004 |
