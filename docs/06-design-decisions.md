---
doc_id: SMR-DEC-001
title: StumpRider design decisions register
project: StumpRider
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
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
  change: Round 2. Amish decided O1 to O4 as recommended (SMR-DDR-003); two new questions proposed, awaiting Amish
---

# StumpRider design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits (the pin rating and its calibration, kneeling, slackening the line, the interim rule on small canoes, life jackets). Each takes the conservative option and names the evidence that would relax it. StumpRider is never a reason to keep children on boats and never replaces a life jacket.

## Open decisions

Amish decided O1 to O4 on 2026-10-03 (SMR-DDR-003); they are listed under Decisions made. The questions below were raised while carrying them out; the state, options and recommendation for each are in `docs/REVIEW.md` (session 2026-10-03, round 2).

*Table 1. Open decisions, all proposed, awaiting Amish.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O5 | R7 for the aluminium prototype: the carried kit is 4.22 kg with the hook head, 0.22 kg over 4 kg (4.02 kg without it); the local production variant carries 3.56 kg | A: judge R7 on the local production variant and accept 4.22 kg for the aluminium prototype, which exists to measure the tool; B: lighten the prototype: pole head socket of 38 x 2 tube 80 long (about 0.17 kg less) and the hook head carried only when wrapped nets are expected (3.85 kg carried, 4.05 kg with the hook head); C: restate R7 to 4.5 kg | A: no change to the prototype; R7 is shown by the variant at TRL 4 | None | SMR-CAL-001, M11 and O10 |
| O6 | R9 at its limit: with the hook head one smith needs about 8.0 h for a kit, the whole of a working day | A: accept and time it in the TRL 4 build trial; B: have the HDPE roller turned and the clamp screw made by a supplier, saving about 30 min of the smith's time (estimate) | A | None | SMR-CAL-001, T1 |

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

Value-engineering target: USD 2,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 292.50 for the prototype run of three kits and calibration wire (USD 1,707.50 under the target); one kit is USD 95.50 with the hook head. The local production variant (SMR-DDR-003, `bom/bom-local-variant.csv`) is USD 55.90 a kit. Main cost drivers and savings worth trying:

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
| 2026-10-03 | O1, R1: option B, a hook head pinned into the same fork with the same shear pin, made and tried beside the ring in the TRL 4 staged-snag trials, with walking the ring back taught either way | Amish: "i approve all of the 47 recommendations provided by you. Execute them." | SMR-DDR-003, D-A1 |
| 2026-10-03 | O2, R3 (safety): option A now, the interim rule (only canoes of 7 m or more with three crew) lettered on the pole head; option C as the planned TRL 4 step, heel tests by canoe class setting a pin per class | Amish, as above | SMR-DDR-003, D-A2 |
| 2026-10-03 | O3, R7: option A, crutch left clamped on the canoe and jigging weight kept at the landing; aluminium prototype stays the TRL 3 design; bamboo judged under O4 | Amish, as above | SMR-DDR-003, D-A3 |
| 2026-10-03 | O4, R10: option C, the local production variant (bamboo sections, crutch and weight shared by five canoes), costed and built alongside the aluminium prototype at TRL 4 | Amish, as above | SMR-DDR-003, D-A4 |

## Change log

- 2026-10-03, v0.2: O1 to O4 decided as recommended and carried into the design (SMR-DDR-003); O5 and O6 opened.
