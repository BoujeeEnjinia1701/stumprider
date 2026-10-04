---
doc_id: SMR-CAL-001
title: StumpRider sizing calculations
project: StumpRider
doc_type: Calculation note
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue at TRL 3, on the constructable design of SMR-DDR-002
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish's requirement decisions of 2026-10-03 carried out (SMR-DDR-003); hook head, carried kit, bamboo local variant and shared crutch and weight; masses of lock pins and rivets corrected; option figures replaced
---

# StumpRider sizing calculations

On paper, a 2.0 mm soft aluminium shear pin (302 N nominal) frees a net hooked over a branch with a margin of at least two, and breaks before the pull can heel the 8 m design canoe more than 4.4 deg. The tool reaches 4.18 m from the top hand to the ring and the tether works snags to 8 m. Amish decided R1, R3, R7 and R10 on 2026-10-03 (SMR-DDR-003): a hook head that pins into the same fork for wrapped nets; the 7 m, three-crew rule kept, with a pin per canoe class from heel tests at TRL 4; the crutch left on the canoe and the jigging weight at the landing; and a bamboo local variant beside the aluminium prototype. With those, the bamboo local variant carries 3.89 kg (R7 met) and costs USD 54.90 a kit (R10 not met); the aluminium prototype carries 4.28 kg (R7 not met) and costs USD 95.50; a smith needs about 8.1 h for a kit (R9 at risk). A net wrapped round a branch still needs more pull than the pin until it has been worked back (R1 at risk).

Every figure comes from `docs/04-calcs/sizing.py`, which imports the parametric model (`cad/src/model.py`), so the sizes here are those of the STEP files, the drawings and the build plan. Tags in square brackets match the script output and `docs/04-calcs/results.csv`. These are screening estimates for a paper proof of concept; they do not replace the pin calibration on CalRig, the canoe heel test or the staged-snag trials, which are TRL 4 work.

> **Safety:** The pin rating is a safety limit. It is valid only for pins cut from a reel whose sample has been broken on CalRig within 256 to 347 N, and only for canoes like the design canoe. Until a heel test says otherwise the tool is not used from canoes under 7 m or with fewer than three crew, the operator kneels, and every person wears a life jacket.

## 1. Assumptions

*Table 1. Assumptions.*

| # | Assumption | Value | Basis |
| --- | --- | --- | --- |
| A1 | Shear strength of the pin wire | 48 MPa | 1050 or 1100 aluminium, O temper: about 0.6 of an 80 MPa tensile strength; to be measured per reel |
| A2 | Design canoe | 8.0 m long, 1.10 m waterline beam, 0.60 m deep, hull 300 kg, three crew of 65 kg, 55 kg of net and gear (550 kg) | A paddled Volta plank canoe; to be replaced by LevelHull or partner measurements |
| A3 | Small dugout (hard case) | 5.5 m, 0.75 m beam, 0.45 m deep, hull 120 kg, two crew, 30 kg load (280 kg) | Smallest canoe likely to carry the tool |
| A4 | Canoe hydrostatics | Waterplane transverse moment 0.05 L B^3; block coefficient 0.45; centre of buoyancy at 0.55 of the draft; hull mass centre 0.22 to 0.25 m up; kneeling crew 0.50 to 0.55 m up | Screening values for narrow round-bilged hulls |
| A5 | Working posture | Pole 20 deg off vertical; operator's hands 0.35 m (0.25 m in the dugout) off the centreline and 0.30 m (kneeling) or 0.85 m (standing) above the gunwale | The crutch is clamped near the bow |
| A6 | Net line forces | Crew holds 100 N while the ring is run down and slackens to 30 N while the operator lifts; the far leg of the net pulls 20 N | Operating rule and the net's own drag |
| A7 | Friction of wet netting on wet bark | 0.3 to 0.5 | Range for nylon on rough wood |
| A8 | Materials | Steel 7,850 kg/m3, S235; 6063-T6 aluminium 2,700 kg/m3, E 69 GPa, bearing 320 MPa; stainless clevis pins 300 MPa in shear; 4.8 mm stainless rivet 2.9 kN; HDPE 950; foam 30 kg/m3; cord 25 g/m | Handbook and catalogue values |
| A9 | Heel limit | 5 deg with the pin at the top of its band | Conservative: well short of the 40 deg at which the design canoe's gunwale goes under, and small enough for kneeling crew to keep their balance |
| A10 | Bamboo culm (local variant) | 36 mm outside, 6 mm wall, 700 kg/m3, E 15 GPa along the culm (10 to 20 GPa range) | Seasoned, treated culm; to be checked culm by culm with the bend test in section 10 |

## 2. Shear pin

The pin passes through both fork cheeks and the tang, so it is cut on two planes. Rating = 2 x shear strength x pin area = 2 x 48 MPa x 3.14 mm2 = 302 N nominal [P1]. R3 allows plus or minus 15 %: 256 N [P2] to 347 N [P3]. Every safety check below uses the top of the band; every freeing check uses the bottom.

## 3. Canoe heel

When the operator pulls up on the pole, the pole pulls down and outboard on the operator's hands, and so on the canoe. The heeling moment is the pull times (cos 20 deg x hands off centreline + sin 20 deg x hands above the water), plus the crew's slack line over the crutch. The righting moment is displacement x g x GM x sin(heel).

*Table 2. Heel when the pin breaks at the top of its band.*

| Canoe | Displacement [H1, K1] | GM [H2, K2] | Freeboard [H3, K3] | Gunwale under at [H4, K4] | Heel, kneeling [H5, K5] | Heel, standing [H6, K6] | Pull for 5 deg, kneeling [H7, K7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Design canoe | 550 kg | 0.69 m | 461 mm | 40 deg | 3.4 deg | 4.4 deg | 523 N |
| Small dugout | 280 kg | 0.15 m | 299 mm | 39 deg | 23.7 deg | 34.1 deg | 53 N |

The pin protects the design canoe with a margin of 1.5 over the top of its band (kneeling). It does not protect the small dugout: 53 N heels it 5 deg, less than half of what a hooked net needs. A lighter 1.4 mm pin (148 N nominal [O11]) still heels the dugout 12.2 deg [L5]. Amish decided on 2026-10-03 (SMR-DDR-003) to keep the rule: the tool is used only from canoes 7 m or longer with at least three crew. At TRL 4, real canoes are heel-tested by size class and a pin diameter is set for each class; a smaller class is served only once a measured pin suits it. The dugout figures above are the reason for the rule, not a design case.

## 4. Pull needed to free the net

The net lies over the branch with a contact angle theta. To lift it, the ring must overcome the far leg's tension multiplied by the capstan factor e^(mu theta), plus the crew's line: pull = 20 N x e^(mu theta) + 30 N.

*Table 3. Pull to lift the net off the branch.*

| Snag | Friction 0.3 | Friction 0.5 | Against the pin band (256 to 347 N) |
| --- | --- | --- | --- |
| Hooked, half a turn | 81 N [F1] | 126 N [F2] | Frees, margin 2.0 at the bottom of the band [F5] |
| Wrapped once round, one and a half turns | 368 N [F3] | 2,260 N [F4] | Breaks the pin first |

If the crew keeps full tension while the operator lifts, the hooked case rises to 196 N [F6], still inside the band; slackening the line is the operating rule. A wrapped net cannot be lifted straight off. Amish decided (SMR-DDR-003) to add a hook head: the ring is unpinned and the hook head pinned into the same fork with a calibrated pin, and the hook pulls the bight of net back round the branch half a turn at a time; the unwinding technique is taught with the ring and the hook. Each half turn worked back divides the pull by 1.6 to 4.8:

*Table 3a. Pull to lift as a wrapped net is worked back.*

| Turns of net on the branch | Friction 0.3 | Friction 0.5 |
| --- | --- | --- |
| One and a half (wrapped once round) | 368 N [F3] | 2,260 N [F4] |
| One (worked back half a turn) | 162 N [F7] | 493 N [F8] |
| One half (hooked) | 81 N [F1] | 126 N [F2] |

With low friction, one half turn worked back brings the lift inside the pin band; with high friction it takes two. The pull the hook itself needs to drag a bight round depends on how the net lies and cannot be set on paper; it is still limited by the same pin, so the hook cannot heel the canoe more than the ring can. R1 stays at risk until the TRL 4 staged-snag trials, where the hook is tried beside the ring.

## 5. Reach

- Top hand to ring centre: 4.18 m [R1] (three 1.45 m sections, hands 0.3 m below the cap). R2 met.
- Depth reached at 20 deg lean, kneeling: 3.17 m below the surface [R2].
- Tether cord: 10 m, with 2 m kept above the water to the hands: 8 m below the surface [R3]. R2 met.
- Ring inside diameter 100 mm [R4]; the hinged ring opens fully, so any line from 4 to 16 mm goes in. R6 met.

## 6. Strength and stiffness

*Table 4. Strength checks against the top of the pin band (347 N).*

| Check | Result |
| --- | --- |
| Euler buckling of the whole pole, 4.35 m, pinned ends | 767 N [S1]; factor 2.2 [S2] |
| Lock pins, 6 mm stainless, double shear | factor 49 [S3] |
| Pole wall bearing at a lock pin hole | factor 22 [S4] |
| Sleeve rivets, two per sleeve (pull only; push butts the tubes) | factor 17 [S5] |
| Tang tear-out above the shear pin hole | factor 44 [S6] |
| Ring bending, pulled at the tang against the far side | 36 MPa [S7]; factor 6.5 on yield [S8] |
| Tang bending, a quarter of the pull acting sideways | factor 6.5 [S9] |
| Crutch axle, M12, 500 N line tension over the roller | 92 MPa [S10], below the 240 MPa of grade 4.6 |

Everything except the pin is at least twice as strong as the pin, so the pin is always the part that lets go. The buckling factor of 2.2 is the smallest margin; the sleeves stiffen the joints, which the Euler figure ignores. The hook head's flat is the same 6 x 28 section as the tang, with the shear pin hole 10 mm below its top, so its tear-out factor is the same as the tang's [S6]. The bamboo pole is checked in section 10.

## 7. Float

The float winder gives 1.26 kg of net lift [B1]. The ring and the cord weigh 0.60 kg in water [B2], so a dropped ring and cord float with a reserve of 2.1 [B3]. With the jigging weight on, the load is 1.57 kg [B4], more than the float holds: in jigging use the cord's end is tied to a thwart.

## 8. Mass

*Table 5. Masses from the model.*

| Item | Mass |
| --- | --- |
| Rider ring with hinge bolt and gate pin | 0.61 kg [M1] |
| Pole head | 0.56 kg [M2] |
| Pole sections, sleeves, rivets, lock pins, cap | 2.61 kg [M3] |
| Jigging weight | 1.12 kg [M4] |
| Gunwale crutch | 1.38 kg [M5] |
| Tether cord, float winder, spare pins | 0.29 kg [M6] |
| Hook head | 0.21 kg [M10] |
| Working tool (ring, head, pole, pins) | 3.78 kg [M7] |
| Whole kit, including the crutch and jigging weight | 6.78 kg [M8] |
| Carried kit, aluminium prototype | 4.28 kg [M11] |
| Carried kit, bamboo local variant | 3.89 kg [V3] |

Correction in v0.2: v0.1 left out the mass of the lock pins, rivets and the jigging weight's pin (about 0.07 kg), because the script read no volume from parts grouped inside a group. The carried kit Amish decided on as 4.02 kg was therefore 4.08 kg; with the hook head it is 4.28 kg.

The longest packed piece is a section with its sleeve, 1.55 m [M9]; packed length meets R7. As Amish decided (SMR-DDR-003), the crutch stays clamped on the canoe as a fitting and the jigging weight is kept at the landing for deep sets, so R7 is judged on the carried kit. The aluminium prototype carries 4.28 kg [M11], 0.28 kg over the 4 kg target; the bamboo local variant carries 3.89 kg [V3] and meets it. A 32 x 1.6 aluminium tube in place of 32 x 2 would bring the prototype to 3.86 kg [N1] with a buckling factor of 1.84 [N2]; Amish decided on 2026-10-04 (2A, SMR-DDR-004) to keep the 32 x 2 pole: R7 is judged on the bamboo local variant (3.89 kg, met), and the prototype's 4.28 kg is recorded, not a failure of R7.

## 9. Build time and cost

- Workshop time for one kit, one smith: 8.1 h [T1] (estimate, galvanising sent out), including 25 min for the hook head. R9 asks for under one day (8 h): at risk, about 5 min over, which is inside the accuracy of the estimate. The TRL 4 build trial decides.
- Parts cost of one aluminium prototype kit at prototype prices: USD 95.50 [C1], including the hook head (USD 3). The pole, sleeves and rivets are 30 % [C5], galvanising 13 % [C6] and the crutch 13 % [C7].
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 299.50 for the prototype run of three aluminium kits, one bamboo pole set and calibration wire (USD 1,700.50 under the target) [C2 to C4].

## 10. Bamboo local variant

Amish decided (SMR-DDR-003) that a bamboo local variant is built alongside the aluminium prototype, with one crutch and jigging weight shared by five canoes at a landing. The variant shares the ring, pole head, pins, hook head, tether and float with the prototype; only the pole differs (`bom/bom-bamboo-variant.csv`). Three treated culms 36 mm outside, 1,450 mm long, are joined by two steel ferrules 40 x 1.5 x 160 mm fixed to the lower culm with an M5 bolt and epoxy; the next culm slides in and is held by the same 6 mm lock pin. The bottom 120 mm of the lowest culm is dressed to 31.8 mm to fit the pole head; the top culm is cut above a node, so no grip cap is needed.

*Table 6. Bamboo local variant.*

| Item | Result |
| --- | --- |
| Bamboo pole (culms, ferrules, bolts) | 2.18 kg [V1], against 2.57 kg for the aluminium pole it replaces [V2] |
| Carried kit | 3.89 kg [V3]; R7 met |
| Buckling of the pole, pinned ends, E 15 GPa | 518 N [V4]; factor 1.49 over the top of the pin band [V5] |
| Buckling if E is only 10 GPa | factor 1.0 [V6] |
| Culm bend test (accept a culm) | 50 N (5 kg) hung at the middle of a 1.4 m span sags 2.9 mm or less [V10] |
| Saving from sharing the crutch and weight among five canoes | USD 17.60 a kit [V7] |
| Parts cost of one kit, crutch and weight shared | USD 54.90 [V8]; R10 (USD 40) not met |

The bamboo pole is less stiff than the aluminium one. A culm with E below about 15 GPa could bow before the pin breaks when the operator pushes hard; that bends the pole but does not load the canoe more than the pin allows. Culms are therefore chosen by the bend test above. The variant costs USD 54.90 a kit at prototype prices, USD 2 more than the USD 52.90 Amish decided on: the hook head (USD 3) is now in every kit, and the bamboo top node saves the grip cap (USD 1). Local bamboo, steel and galvanising prices near the first fishery, measured at TRL 4, decide how close it comes to USD 40.

## 10. Results against the requirements

*Table 7. Summary.*

| Requirement | Result | Status |
| --- | --- | --- |
| R1 | Hooked nets 81 to 126 N; wrapped nets 368 N to 2.3 kN, falling to 162 to 493 N once the hook has worked them back half a turn | At risk |
| R2 | 4.18 m top hand to ring; tether to 8 m | Met on paper |
| R3 | Design canoe 3.4 to 4.4 deg; canoes under 7 m or with fewer than three crew excluded by rule until per-class pins are set at TRL 4; band depends on calibration | Met on paper where the tool is allowed |
| R4 | Pull capped at 347 N; mesh damage not calculable | Cannot be shown on paper |
| R5 | Release time | Cannot be shown on paper |
| R6 | 100 mm hinged ring | Met on paper |
| R7 | Packed 1.55 m; carried 4.28 kg (aluminium prototype), 3.89 kg (bamboo local variant) | Met, judged on the local variant; the prototype's 4.28 kg is recorded (decision 2A) |
| R8 | Galvanised steel, aluminium, stainless, polymers; treated bamboo in the local variant | Met on paper |
| R9 | 8.1 h | At risk |
| R10 | USD 95.50 (prototype); USD 54.90 (bamboo local variant, crutch and weight shared) | Not met |
