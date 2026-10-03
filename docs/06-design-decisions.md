---
doc_id: SMR-DEC-001
title: StumpRider design decisions register
project: StumpRider
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's 2026-10-03 pre-approvals; four requirement decisions proposed, awaiting Amish
---

# StumpRider design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits (the pin rating and its calibration, kneeling, slackening the line, the interim rule on small canoes, life jackets). Each takes the conservative option and names the evidence that would relax it. StumpRider is never a reason to keep children on boats and never replaces a life jacket.

## Open decisions

Requirements that are not met or at risk on paper are Amish's to decide. The state, options and recommendation for each are set out in `docs/REVIEW.md` (TRL 3, Decisions for Amish).

*Table 1. Open decisions, all proposed, awaiting Amish.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O1 | R1: nets wrapped round a branch need 368 N to 2.3 kN, above the pin | A: teach working the ring back round the branch, no change; B: add a pinned hook head that uses the same fork (about USD 3, 0.2 kg); C: a stronger pin for wrapped nets | B, tried beside the ring at TRL 4, with A taught in both cases | One extra made part and sketch | REVIEW.md, D-A1 |
| O2 | R3: the pin would heel a 5.5 m dugout about 24 deg | A: keep the interim rule (canoes 7 m and over, three crew); B: a light 1.4 mm pin for 5 to 7 m canoes (still 12 deg); C: heel-test canoes by class and set a pin per class | A now, and C in the TRL 4 heel tests | Labels and the first checks; a second pin reel if C | REVIEW.md, D-A2 |
| O3 | R7: the kit weighs 6.5 kg | A: crutch stays clamped on the canoe, weight kept at the landing (4.02 kg carried); B: A plus bamboo sections (3.37 kg); C: weight left out only (5.39 kg) | A for the prototype; bamboo is judged under O4 | What is packed; none of the parts change | REVIEW.md, D-A3 |
| O4 | R10: a kit costs USD 92.50 at prototype prices | A: bamboo pole sections with steel ferrules (USD 70.50); B: crutch and weight shared, one set per five canoes (USD 74.90); C: A and B together (USD 52.90) | C as the local production variant, built alongside the aluminium prototype at TRL 4 | A bamboo variant of the pole and its sketch | REVIEW.md, D-A4 |

## To confirm when parts are bought

These are facts that can only be settled with real parts, a real canoe or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Shear strength of the chosen wire reel (48 MPa assumed): ten pins broken on CalRig | Pin rating and its band (R3) | SMR-CAL-001, A1; SMR-DDR-002, A2 |
| 2 | 38 mm tube with a 32.4 mm bore, or how much opening 38 x 3 tube needs | Sleeve fit | SMR-DDR-002, A1 |
| 3 | Size, mass and crew of the partner's canoes; gunwale thickness and clear side depth | Heel check (R3) and crutch fit | SMR-CAL-001, A2 to A5; SMR-DDR-002, A3 and A4 |
| 4 | How often nets hook and how often they wrap, from partner crews | R1 and decision O1 | SMR-PRB-001 |
| 5 | Friction of the partner's netting on wet bark (0.3 to 0.5 assumed) | Freeing pull (R1) | SMR-CAL-001, A7 |
| 6 | Local prices for aluminium tube, bamboo, galvanising and foam near the first fishery | R10 and decision O4 | `bom/bom.csv` |
| 7 | Bent ring holds 112 mm mean diameter within 2 mm | Joint gaps and ear alignment | SMR-DDR-002, A5 |
| 8 | Mesh damage at the pin rating on 90 to 150 mm mesh | R4 | SMR-REQ-001 |

## Value engineering

Value-engineering target: USD 2,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 284 for the prototype run of three kits and calibration wire (USD 1,716 under the target); one kit is USD 92.50. Main cost drivers and savings worth trying:

- The largest lines are the aluminium pole, sleeves and rivets (31 % of a kit), galvanising (13 %) and the crutch (13 %).
- Savings worth trying: bamboo pole sections with steel ferrules (about USD 22 a kit); one crutch and jigging weight shared by five canoes at a landing (about USD 18 a kit); galvanising a batch of kits together, which spreads the galvaniser's minimum lot; zinc-rich paint only where no galvaniser is near (about USD 9, at some risk to R8).
- Smith's labour (about 7.7 hours a kit) is not in the parts cost; a partner workshop making kits in batches would cut it.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D10: hinged two-half ring with a pinned gate; three-section aluminium pole for the prototype; one shear pin rating, 2.0 mm soft aluminium, 302 N nominal, calibrated per reel; the pin carries push and pull; operating rules (kneel, slacken, life jackets, tether tied off, cut rather than capsize, interim rule on canoes under 7 m); jigging weight pinned to the tang; foam float winder; clamp-on roller crutch; handed out only through child-protection partners, first candidates to approach (Challenging Heights, a Volta landing-site committee through the Fisheries Commission, a Ghanaian university fisheries department; none approached); requirement targets kept | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | SMR-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C12, and assumptions A1 to A5 | Amish, same pre-approvals | SMR-DDR-002 |
| 2026-10-03 | Safety stops S1 to S5 and the first checks, including pin calibration and a moored heel test before any use on a snag (conservative; a gate, not relaxed) | Amish, same pre-approvals | SMR-BLD-001, sections 5 and 6 |
| 2026-10-03 | Appearance model departures for the renders: a plank deck and a forearm and hand beside the packed kit; a short net line over a branch and a cut-short pole for the detail view; the shear pin shown red | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
