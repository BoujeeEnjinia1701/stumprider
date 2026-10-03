---
doc_id: SMR-CAL-001
title: StumpRider sizing calculations
project: StumpRider
doc_type: Calculation note
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue at TRL 3, on the constructable design of SMR-DDR-002
---

# StumpRider sizing calculations

On paper, a 2.0 mm soft aluminium shear pin (302 N nominal) frees a net hooked over a branch with a margin of at least two, and breaks before the pull can heel the 8 m design canoe more than 4.4 deg. The tool reaches 4.18 m from the top hand to the ring and the tether works snags to 8 m. Four results fall short: a net wrapped once round a branch needs more pull than the pin allows (R1); the same pin would heel a small dugout about 24 deg (R3); the whole kit weighs 6.5 kg (R7); and a kit costs USD 92.50 at prototype prices (R10). Each is posed as a decision for Amish in `docs/REVIEW.md`.

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

## 2. Shear pin

The pin passes through both fork cheeks and the tang, so it is cut on two planes. Rating = 2 x shear strength x pin area = 2 x 48 MPa x 3.14 mm2 = 302 N nominal [P1]. R3 allows plus or minus 15 %: 256 N [P2] to 347 N [P3]. Every safety check below uses the top of the band; every freeing check uses the bottom.

## 3. Canoe heel

When the operator pulls up on the pole, the pole pulls down and outboard on the operator's hands, and so on the canoe. The heeling moment is the pull times (cos 20 deg x hands off centreline + sin 20 deg x hands above the water), plus the crew's slack line over the crutch. The righting moment is displacement x g x GM x sin(heel).

*Table 2. Heel when the pin breaks at the top of its band.*

| Canoe | Displacement [H1, K1] | GM [H2, K2] | Freeboard [H3, K3] | Gunwale under at [H4, K4] | Heel, kneeling [H5, K5] | Heel, standing [H6, K6] | Pull for 5 deg, kneeling [H7, K7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Design canoe | 550 kg | 0.69 m | 461 mm | 40 deg | 3.4 deg | 4.4 deg | 523 N |
| Small dugout | 280 kg | 0.15 m | 299 mm | 39 deg | 23.7 deg | 34.1 deg | 53 N |

The pin protects the design canoe with a margin of 1.5 over the top of its band (kneeling). It does not protect the small dugout: 53 N heels it 5 deg, less than half of what a hooked net needs. A lighter 1.4 mm pin (148 N nominal [O11]) still heels the dugout 12.2 deg [L5]. Small canoes are therefore not covered by this design; the interim rule (no use from canoes under 7 m or with fewer than three crew) stands until a heel test, and the long-term answer is a decision for Amish (R3).

## 4. Pull needed to free the net

The net lies over the branch with a contact angle theta. To lift it, the ring must overcome the far leg's tension multiplied by the capstan factor e^(mu theta), plus the crew's line: pull = 20 N x e^(mu theta) + 30 N.

*Table 3. Pull to lift the net off the branch.*

| Snag | Friction 0.3 | Friction 0.5 | Against the pin band (256 to 347 N) |
| --- | --- | --- | --- |
| Hooked, half a turn | 81 N [F1] | 126 N [F2] | Frees, margin 2.0 at the bottom of the band [F5] |
| Wrapped once round, one and a half turns | 368 N [F3] | 2,260 N [F4] | Breaks the pin first |

If the crew keeps full tension while the operator lifts, the hooked case rises to 196 N [F6], still inside the band; slackening the line is the operating rule. A wrapped net cannot be lifted straight off: the ring has to walk it back round the branch half a turn at a time (each half turn divides the pull by 1.6 to 4.8), or the net is cut. R1 is at risk until the staged-snag trials show how often nets wrap and whether the ring can unwind them.

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

Everything except the pin is at least twice as strong as the pin, so the pin is always the part that lets go. The buckling factor of 2.2 is the smallest margin; the sleeves stiffen the joints, which the Euler figure ignores.

## 7. Float

The float winder gives 1.26 kg of net lift [B1]. The ring and the cord weigh 0.60 kg in water [B2], so a dropped ring and cord float with a reserve of 2.1 [B3]. With the jigging weight on, the load is 1.57 kg [B4], more than the float holds: in jigging use the cord's end is tied to a thwart.

## 8. Mass

*Table 5. Masses from the model.*

| Item | Mass |
| --- | --- |
| Rider ring with hinge bolt and gate pin | 0.61 kg [M1] |
| Pole head | 0.56 kg [M2] |
| Pole sections, sleeves, rivets, lock pins, cap | 2.56 kg [M3] |
| Jigging weight | 1.11 kg [M4] |
| Gunwale crutch | 1.37 kg [M5] |
| Tether cord, float winder, spare pins | 0.29 kg [M6] |
| Working tool (ring, head, pole, pins) | 3.73 kg [M7] |
| Whole kit | 6.5 kg [M8] |

The longest packed piece is a section with its sleeve, 1.55 m [M9]; packed length meets R7. The kit mass does not: the jigging weight and the steel crutch are 2.5 kg of it. Options (decision for Amish): crutch left clamped on the canoe and weight kept at the landing, 4.02 kg carried [O9]; the same with bamboo sections, 3.37 kg [O10]; weight left out only, 5.39 kg [O1]; weight out and a hardwood crutch block, 4.9 kg [O4].

## 9. Build time and cost

- Workshop time for one kit, one smith: 7.7 h [T1] (estimate, galvanising sent out). R9 met on paper, with little to spare.
- Parts cost of one kit at prototype prices: USD 92.50 [C1]. R10 not met. The pole, sleeves and rivets are 31 % [C5], galvanising 13 % [C6] and the crutch 13 % [C7].
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 284 for the prototype run of three kits and calibration wire (USD 1,716 under the target) [C2 to C4].
- Options for R10 (decision for Amish): bamboo pole sections with steel ferrules, USD 70.50 [O5]; zinc-rich paint in place of galvanising, USD 83.50 [O6]; crutch and weight shared, one set per five canoes, USD 74.90 [O7]; bamboo and sharing together, USD 52.90 [O8].

## 10. Results against the requirements

*Table 6. Summary.*

| Requirement | Result | Status |
| --- | --- | --- |
| R1 | Hooked nets 81 to 126 N; wrapped nets 368 N to 2.3 kN | At risk |
| R2 | 4.18 m top hand to ring; tether to 8 m | Met on paper |
| R3 | Design canoe 3.4 to 4.4 deg; small dugout 24 deg; band depends on calibration | At risk |
| R4 | Pull capped at 347 N; mesh damage not calculable | Cannot be shown on paper |
| R5 | Release time | Cannot be shown on paper |
| R6 | 100 mm hinged ring | Met on paper |
| R7 | Packed 1.55 m; mass 6.5 kg | Not met (mass) |
| R8 | Galvanised steel, aluminium, stainless, polymers | Met on paper |
| R9 | 7.7 h | Met on paper |
| R10 | USD 92.50 per kit | Not met |
