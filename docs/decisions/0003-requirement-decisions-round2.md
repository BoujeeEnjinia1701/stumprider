---
doc_id: SMR-DDR-003
title: StumpRider requirement decisions, round 2
project: StumpRider
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish's decisions on R1 (D-A1 B), R3 (D-A2 A now, C at TRL 4), R7 (D-A3 A) and R10 (D-A4 C) carried into the model, calculations, BOM, drawings and build plan
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** Decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For StumpRider these are the four requirement decisions of SMR-DEC-001 (O1 to O4; portfolio decisions 37 to 40), each decided as recommended.

## Context

At TRL 3 (SMR-CAL-001 v0.1) the constructable design (SMR-DDR-002) left four requirements short. R1: a net wrapped once round a branch needs 368 N to 2.3 kN, above the 256 to 347 N pin band. R3: the pin that protects the 8 m design canoe would heel a 5.5 m dugout 23.7 deg. R7: the whole kit weighed 6.5 kg against 4 kg. R10: a kit cost USD 92.50 against USD 40. The four were put to Amish with options and a recommendation in `docs/REVIEW.md` and SMR-DEC-001. Decisions D-A3 and D-A4 interact: D-A4 C includes the bamboo sections and the shared crutch and weight, and D-A3 A leaves bamboo to be judged under D-A4.

## Options considered

*Table 1. The four decisions put to Amish and the option chosen.*

| # | Requirement | Options | Chosen |
| --- | --- | --- | --- |
| D-A1 | R1, wrapped nets | A: teach walking the ring back round the branch, or cutting. B: add a hook head on a shear-pinned flat. C: a stronger pin | **B**, made and tried beside the ring in the TRL 4 staged-snag trials, with A taught either way |
| D-A2 | R3, small canoes (safety) | A: keep the interim rule (only canoes of 7 m or more with three crew) printed on the pole head. B: a light 1.4 mm pin for 5 to 7 m canoes. C: heel-test canoes by size class at TRL 4 and set a pin per class | **A now, and C in the TRL 4 heel tests** |
| D-A3 | R7, kit mass | A: crutch stays clamped on the canoe, jigging weight at the landing. B: A plus bamboo sections. C: leave out only the weight | **A**, with bamboo judged under D-A4 |
| D-A4 | R10, kit cost | A: bamboo sections with steel ferrules. B: one crutch and weight shared by five canoes. C: A and B together | **C**, as the local production variant built alongside the aluminium prototype at TRL 4 |

## Decision

*Table 2. Each decision as carried into the design. Figures from SMR-CAL-001 v0.2 (`docs/04-calcs/sizing.py`).*

| # | Requirement | Option chosen | Effect on the design | Condition |
| --- | --- | --- | --- | --- |
| D-A1 | R1 | B: hook head | A new made part (`hook_head()` in `cad/src/model.py`, BOM line 21, sketch SMR-DWG-111, joint 10, step 12): a 6 x 28 x 50 mm flat, drilled for the same 2.1 mm shear pin at the tang's shear-pin height and for the tether, with a J hook of 12 mm bar below it, 44 mm throat opening upward. It pins into the pole-head fork in place of the ring, so it pulls with at most the top of the pin band, 347 N [F7], and draws the bight back round the branch half a turn at a time. 0.19 kg, USD 3, about 20 min of the smith's time. Model checks: 86 of 86 pass, including the hook head in the fork | R1 stays **at risk** on paper: whether wraps can be unwound is shown only in the TRL 4 staged-snag trials, where the hook head is made and tried beside the ring and the walking-back technique is taught either way |
| D-A2 | R3 (safety) | A now; C at TRL 4 | The interim rule, "only canoes of 7 m or longer with 3 crew", is lettered on the pole head with the pin rating (BOM line 19 now names it; SMR-DWG-001 Rev P3 note; build plan step 5). No change to the pin | R3 is **met on paper where the tool is allowed**; canoes under 7 m or with fewer than three crew are **not served**. Planned TRL 4 step: heel-test real canoes by size class and set a pin diameter per class from the measured righting moment. Small canoes are served only once a measured pin suits them |
| D-A3 | R7 | A: crutch on the canoe, weight at the landing | No part changes. The gunwale crutch is treated as a fitting left clamped on the canoe; the jigging weight is kept at the landing for deep sets. The kit carried in the canoe is 4.02 kg [O9], and 4.22 kg with the hook head of D-A1 [M11]. The aluminium prototype stays the TRL 3 design | R7 stays **not met on paper, by 0.22 kg**, for the aluminium prototype; the local production variant of D-A4 carries 3.56 kg [O10] and meets it. A new question on R7 is in `docs/REVIEW.md` |
| D-A4 | R10 | C: local production variant | Costed line by line in a new `bom/bom-local-variant.csv`: three bamboo sections about 35 mm with node-closed ends, borax-boric treated (USD 1 each), two pinned steel ferrules in place of the aluminium sleeves and rivets (USD 2 each), and one crutch and jigging weight shared by five canoes at a landing (one fifth a kit, with that share of the galvanising). USD 55.90 a kit with the hook head [C8]. The aluminium prototype (`bom/bom.csv`, USD 95.50) is unchanged in the model and drawings | R10 stays **not met** by either: USD 95.50 for the prototype, USD 55.90 for the variant. The variant is built alongside the aluminium prototype at TRL 4 so the two can be compared; bamboo stiffness and rot protection are checked there; local prices and batch galvanising may bring it nearer USD 40 |

## Consequences

- `cad/src/model.py` adds the hook head; STEP (`hook-head.step`, assembly), the GA SMR-DWG-001 (Rev P3), the concept media, `media/model.glb`, the build plan overview, the new sketch SMR-DWG-111, joint 10 and step 12 are regenerated from the model.
- SMR-CAL-001 v0.2 is re-run. R1 at risk; R3 met where allowed, small canoes not served; R7 not met by 0.22 kg (prototype), met by the variant; R9 met at the limit (8.0 h with the hook head); R10 not met (USD 95.50; variant USD 55.90).
- Prototype run of three kits and calibration wire: USD 292.50 (was USD 284), USD 1,707.50 under the USD 2,000 value-engineering target; `budget_usd` unchanged.
- New questions (R7 for the aluminium prototype, R9 at its limit) are recorded in `docs/REVIEW.md` and SMR-DEC-001 as **Proposed, awaiting Amish**.
