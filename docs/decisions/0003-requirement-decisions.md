---
doc_id: SMR-DDR-003
title: StumpRider requirement decisions on wrapped nets, small canoes, kit mass and kit cost (R1, R3, R7, R10)
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
  change: Amish's requirement decisions 10B, 11A then C, 12A and 13C carried out
---

# 0003: Hook head, small-canoe rule, carried kit and bamboo local variant (R1, R3, R7, R10)

- **Date:** 2026-10-03
- **Status:** accepted
- **Decided by:** Amish Chadha, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For StumpRider these are decisions 10B (R1), 11A then C (R3), 12A (R7) and 13C (R10), each as recommended in `docs/REVIEW.md` (TRL 3, D-A1 to D-A4).

> **Safety:** The hook head is held by the same calibrated shear pin as the ring, so it cannot pull the canoe over any further than the ring can. The rule that the tool is used only from canoes 7 m or longer with at least three crew is kept; smaller canoes are served only after heel tests set a pin for their class. The bamboo pole changes nothing in the pin, the head or the canoe loads. Nobody enters the water; every person wears a life jacket; the operator kneels.

## Context

At TRL 3 (SMR-CAL-001 v0.1) four requirements fell short: a net wrapped once round a branch needs 368 N to 2.3 kN, above the 256 to 347 N pin band (R1); the same pin would heel a 5.5 m dugout about 24 deg (R3); the whole kit weighed 6.5 kg against 4 kg (R7); and a kit cost USD 92.50 against USD 40 (R10).

## Options considered

- **R1 (D-A1):** A, technique only; **B (chosen), a hook head that pins into the same fork, with the unwinding technique taught**; C, a stronger pin (rejected on heel).
- **R3 (D-A2):** **A (chosen now), keep the rule: canoes 7 m or longer, three crew**; B, a 1.4 mm light pin (still 12 deg in the dugout); **C (chosen for TRL 4), heel tests by canoe size class with a pin per class**.
- **R7 (D-A3):** **A (chosen), the crutch stays clamped on the canoe and the jigging weight stays at the landing**; B, A with bamboo; C, weight left out only.
- **R10 (D-A4):** A, bamboo only; B, sharing only; **C (chosen), a bamboo-pole local variant with a crutch and weight shared by five canoes, beside the aluminium prototype**.

## Decision

1. **Hook head (R1), BOM line 21, making sketch SMR-DWG-111.** A 6 x 28 flat, 60 mm long, with the tang's 10.5 mm tether hole and 2.1 mm shear pin hole, and a 10 mm steel bar bent into a J below it (30 mm bend radius, 50 mm clear throat), welded and galvanised; 0.21 kg, USD 3. In use the shear pin is drawn, the fork is lifted off the ring's tang and put over the hook head's flat, and a calibrated pin is fitted; the tether's bowline is moved to the hook head so it comes back if the pin breaks. The hook pulls the bight of net back round the branch half a turn at a time, then the ring lifts it off. The unwinding technique is taught with both the ring and the hook.
2. **Small canoes (R3).** The rule stands and is printed on the pole head: only canoes 7 m or longer with at least three crew. At TRL 4 the partner's canoes are heel-tested by size class, and a pin diameter is set for each class from its heel test; a class is served only once a measured pin suits it. R3 is restated to say so.
3. **Carried kit (R7).** The gunwale crutch stays clamped on the canoe as a fitting and the jigging weight is kept at the landing for deep sets. R7's mass target applies to the kit carried to and from the canoe and is restated to say so.
4. **Bamboo local variant (R10), `bom/bom-bamboo-variant.csv`, making sketch SMR-DWG-112.** Three treated bamboo culms 36 mm outside and 1,450 mm long in place of the aluminium sections, sleeves, rivets and grip cap; two steel ferrules 40 x 1.5 x 160 mm fixed to the lower culm with an M5 bolt and epoxy; the bottom 120 mm of the lowest culm dressed to 31.8 mm for the same pole head; the top culm cut above a node. One crutch and jigging weight serve five canoes at a landing. One bamboo pole set is built alongside the three aluminium prototype kits for TRL 4 so the two can be compared.

## Consequences

- R1: still at risk on paper. Once the hook has worked a wrap back half a turn the lift falls to 162 to 493 N [F7, F8], inside the pin band for low friction; high friction needs two half turns. The TRL 4 staged-snag trials decide.
- R3: met on paper where the tool is allowed (3.4 deg kneeling, 4.4 deg standing in the design canoe); small canoes excluded by rule.
- R7: the bamboo local variant carries 3.89 kg [V3], met. The aluminium prototype carries 4.28 kg [M11], not met. Correction: the 4.02 kg quoted in D-A3 left out the lock pins, rivets and weight pin (about 0.07 kg); the true figure was 4.08 kg, and the hook head adds 0.21 kg. A thinner prototype pole wall is posed to Amish as a new open decision.
- R9: about 8.1 h for one smith with the hook head [T1], at risk by about 5 minutes; the TRL 4 build trial decides.
- R10: USD 54.90 a kit for the bamboo local variant [V8] (USD 52.90 decided, plus the USD 3 hook head, less the USD 1 grip cap the top node replaces); USD 95.50 for the aluminium prototype. Not met at prototype prices; local prices at TRL 4 decide.
- Bamboo stiffness: buckling factor 1.49 with E 15 GPa [V5], 1.0 if E is only 10 GPa [V6]. Culms are accepted by a bend test: 5 kg hung at the middle of a 1.4 m span sags 2.9 mm or less [V10].
- Cost: Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 299.50 for three aluminium kits, one bamboo pole set and calibration wire (USD 1,700.50 under the target).
- Constructability: 144 of 144 model checks pass, including the hook head in the fork (pin bearing in its hole, cheeks clear, flat 45 mm clear of the end plate, tether loop clear) and the bamboo pole (spigot seated in the head, ferrule slide fit 0.5 mm, bolts and lock pins through, culms butting, packed length 1.53 m).
