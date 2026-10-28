---
doc_id: SMR-CAL-001
title: StumpRider sizing calculations
project: StumpRider
doc_type: Calculation note
version: "0.4"
status: Draft
date: '2026-10-25'
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
- version: "0.3"
  date: '2026-10-24'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: hook head J of 12 mm bar after the STEM check (SMR-DEC-001 F1, fix rule) with its bending check [S11 to S14]; dynamic heel under a sudden jerk [H9 to H12] (SMR-DEC-001 O6, awaiting Amish); masses after F1; requirement tags now PR numbers of SMR-PRS-001 (R numbers kept in brackets)"
- version: "0.4"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (\"i approve of your recommendations\", SMR-DEC-001): O6 (5 deg is the static limit; lift steadily), O8 (crutch on every canoe, only the jigging weight shared: V7 USD 5.60, V8 USD 66.90), O9 (measured righting-moment criterion at the TRL 4 heel test); S13a added: the hook head's straight shank in the tip-leg case (1.87), which stopped O10"
---

# StumpRider sizing calculations

On paper, a 2.0 mm soft aluminium shear pin (302 N nominal) frees a net hooked over a branch with a margin of at least two, and breaks before the pull can heel the 8 m design canoe more than 4.4 deg. The tool reaches 4.18 m from the top hand to the ring and the tether works snags to 8 m. Amish decided R1, R3, R7 and R10 on 2026-10-03 (SMR-DDR-003): a hook head that pins into the same fork for wrapped nets; the 7 m, three-crew rule kept, with a pin per canoe class from heel tests at TRL 4; the crutch left on the canoe and the jigging weight at the landing; and a bamboo local variant beside the aluminium prototype. With those, the bamboo local variant carries 3.95 kg (PR-007, was R7, met) and costs USD 66.90 a kit with its own crutch since Amish's decision O8 of 2026-10-25 (PR-010, was R10, not met; USD 54.90 when the crutch was shared); the aluminium prototype carries 4.34 kg (recorded, decision 2A) and costs USD 95.50; a smith needs about 8.1 h for a kit (PR-009, was R9, at risk). A net wrapped round a branch still needs more pull than the pin until it has been worked back (PR-001, was R1, at risk). In the kit 1.9.1 upgrade (2026-10-24) the STEM check SMR-STM-001 found two items: the hook head's 10 mm J was less than twice as strong as the pin, so it is now 12 mm bar (SMR-DEC-001 F1, decided under Amish's standing instruction of 2026-10-23; factor 3.1), and a sudden jerk on the pole heels the design canoe about 6.5 deg at its peak, past the 5 deg limit that the static case meets; on 2026-10-25 Amish decided that 5 deg is the static limit, with a "lift steadily, never jerk" rule and the peak measured in the TRL 4 heel test (PR-003; SMR-DEC-001 O6).

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
| A11 | Roll radius of gyration of the loaded canoe | 0.40 of the waterline beam | Screening value for a narrow hull with crew kneeling; to be replaced by the roll period measured in the moored heel test |
| A12 | Sudden jerk on the pole | Pull rises to the pin's top load in 0.25 s | A sharp two-handed jerk; a steady lift takes a second or more |
| A13 | Side couple a kneeling operator can put on the pole | 200 N at each hand, hands 0.6 m apart (120 N m) | Assumed; the pin does not cap side loads, the operator's hands do |

## 2. Shear pin

The pin passes through both fork cheeks and the tang, so it is cut on two planes. Rating = 2 x shear strength x pin area = 2 x 48 MPa x 3.14 mm2 = 302 N nominal [P1]. R3 allows plus or minus 15 %: 256 N [P2] to 347 N [P3]. Every safety check below uses the top of the band; every freeing check uses the bottom.

## 3. Canoe heel

When the operator pulls up on the pole, the pole pulls down and outboard on the operator's hands, and so on the canoe. The heeling moment is the pull times (cos 20 deg x hands off centreline + sin 20 deg x hands above the water), plus the crew's slack line over the crutch. The righting moment is displacement x g x GM x sin(heel).

*Table 2. Heel when the pin breaks at the top of its band.*

| Canoe | Displacement [H1, K1] | GM [H2, K2] | Freeboard [H3, K3] | Gunwale under at [H4, K4] | Heel, kneeling [H5, K5] | Heel, standing [H6, K6] | Pull for 5 deg, kneeling [H7, K7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Design canoe | 550 kg | 0.69 m | 461 mm | 40 deg | 3.4 deg | 4.4 deg | 523 N |
| Small dugout | 280 kg | 0.15 m | 299 mm | 39 deg | 23.7 deg | 34.1 deg | 53 N |

The pin protects the design canoe with a margin of 1.5 over the top of its band (kneeling), for a steady pull. The pin does not protect the small dugout: 53 N heels it 5 deg, less than half of what a hooked net needs. A lighter 1.4 mm pin (148 N nominal [O11]) still heels the dugout 12.2 deg [L5]. Amish decided on 2026-10-03 (SMR-DDR-003) to keep the rule: the tool is used only from canoes 7 m or longer with at least three crew. At TRL 4, real canoes are heel-tested by size class and a pin diameter is set for each class; a smaller class is served only once a measured pin suits it. The dugout figures above are the reason for the rule, not a design case.

**Sensitivity (independent review, 2026-10-24).** The static margin rests on screening hydrostatics (A2 to A4). With a 1.0 m waterline beam in place of 1.1 m the kneeling heel at the top of the band is 5.1 deg [Q1]; with a waterplane factor of 0.04 in place of 0.05 it is 4.7 deg [Q2]; with both it is 7.4 deg [Q3]. PR-003 is therefore met only once the partner's canoes are measured; the moored heel test at TRL 4 is the evidence. If the crew is still holding 100 N on the line when the pin breaks, the heel is 4.05 deg [H14]; a line tension of 203 N over the crutch [H15] would take it to 5 deg, which is why the crew slackens the line while the operator lifts. Amish's decision O9 of 2026-10-25 keeps the 7 m, three-crew rule as a screen and adds a measured criterion at the TRL 4 heel test: displacement times GM of at least about 260 kg m, the value that keeps the static heel at 5 deg, with a margin set from that test.

**Dynamic heel (kit 1.9.1, SMR-STM-001 S7).** The canoe rolls like a spring and mass: with GM 0.69 m and a radius of gyration of 0.40 B (A11) its natural roll period is 1.06 s [H9]. A pull that rises to just under the pin's top load in 0.25 s (A12) and is then held overshoots the static heel by 1 + |sin x| / x with x = pi x 0.25 / 1.06, a factor of 1.91 [H10], so the peak heel is 6.5 deg kneeling [H11]. That is 16 % of the heel that puts the gunwale under [H12], but over the 5 deg working limit of A9, which the static case meets. If instead the pin breaks at the top of the ramp, the load is gone and the heel at that moment is only 33 % of the static heel [H13] (independent review); the bound is the pull that stalls just under the pin. Amish decided this safety trade-off on 2026-10-25 (SMR-DEC-001 O6, option A): the 2.0 mm pin stays, 5 deg is the static limit, the operating rules and the tag say "lift steadily, never jerk", and the moored heel test at TRL 4 measures the roll period and the peak heel under a quick pull. A 1.7 mm pin (band 185 to 251 N, peak about 4.9 deg) is used only if that test shows a real exceedance.

## 4. Pull needed to free the net

The net lies over the branch with a contact angle theta. To lift it, the ring must overcome the far leg's tension multiplied by the capstan factor e^(mu theta), plus the crew's line: pull = 20 N x e^(mu theta) + 30 N.

*Table 3. Pull to lift the net off the branch.*

| Snag | Friction 0.3 | Friction 0.5 | Against the pin band (256 to 347 N) |
| --- | --- | --- | --- |
| Hooked, half a turn | 81 N [F1] | 126 N [F2] | Frees, margin 2.0 at the bottom of the band [F5] |
| Wrapped once round, one and a half turns | 368 N [F3] | 2,260 N [F4] | Breaks the pin first |

If the crew keeps full tension while the operator lifts, the hooked case rises to 196 N [F6], still inside the band; slackening the line is the operating rule. The margin of 2.0 rests on the 20 N far leg and the friction range: it is gone at a far-leg tension of 47 N [F9] or a friction of about 0.8 (independent review), so PR-001 stays at risk until the staged-snag trials. A wrapped net cannot be lifted straight off. Amish decided (SMR-DDR-003) to add a hook head: the ring is unpinned and the hook head pinned into the same fork with a calibrated pin, and the hook pulls the bight of net back round the branch half a turn at a time; the unwinding technique is taught with the ring and the hook. Each half turn worked back divides the far leg's term by e^(mu pi), 2.6 to 4.8 (1.6 in v0.2 was an arithmetic slip, found by the independent review):

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
| Ring bending with the halves pinned at hinge and gate (M = F R / 2, independent review) | factor 4.1 [S15] |
| Hinge bolt M8, single shear, whole pull on one joint | factor 44 [S16] |
| Pole bending under the operator's largest side couple (A13), 6063-T6 proof 214 MPa | factor 2.4 [S17] |
| Tang bending, a quarter of the pull acting sideways | factor 6.5 [S9] |
| Crutch axle, M12, 500 N line tension over the roller | 92 MPa [S10], below the 240 MPa of grade 4.6 |
| Hook head J, 12 mm bar, bight in the bottom of the J (30 mm off the shank axis), Wahl factor 1.19 | 76 MPa [S11]; factor 3.1 on yield [S12] |
| The same if the bight catches on the tip leg (60 mm off the axis) | factor 1.58 [S13] |
| The straight shank between the bend and the flat, bight on the tip leg | factor 1.87 [S13a] |
| The hook head of SMR-DDR-003 in 10 mm bar, for the record | factor 1.86 [S14]: under 2, fixed by F1 |

Everything except the pin is at least twice as strong as the pin, so the pin is always the part that lets go (PR-012). The kit 1.9.1 STEM check found the hook head's 10 mm J at 1.86 times (curved-bar bending with the bight seated in the J, [S14]); under Amish's standing instruction of 2026-10-23 the J is now 12 mm bar, the ring's stock, butt welded to the flat's lower edge (SMR-DEC-001 F1), at 3.1 times [S12]. Its weld to the flat (a 5 mm fillet each side along the 28 mm flat, throat about 3.5 mm) carries the hook's moment of about 10 N m at roughly 11 MPa, far below the weld metal's strength (hand check, not in the script). If the bight catches on the tip leg the factor is 1.58 [S13]: the hook would still not yield before the pin breaks, but it is under the 2 x rule; the independent review takes the tip leg as a design case, and the fixes (14 mm bar or a gusset) cost carried mass, so it went to Amish (SMR-DEC-001 O10). Amish approved the recommended gusset outside the bend on 2026-10-25, but carrying it through found that the bight on the tip leg puts the same moment, the load times 60 mm, into the whole straight shank between the bend and the flat, where the factor is 1.87 [S13a]. A gusset at the bend lifts only the bend; a gusset that reaches the flat would weigh about 0.06 to 0.10 kg (estimate), more than the 0.05 kg left under PR-007. So the gusset was not added, and O10 is back with Amish with this finding (docs/REVIEW.md). The bamboo pole's buckling factor of 1.49 [V5] is also under 2: an accepted culm bows elastically rather than breaking, which caps the push, as recorded when Amish chose the variant (SMR-DDR-003); PR-012 is at risk for it. The buckling factor of 2.2 is the smallest margin; the sleeves stiffen the joints, which the Euler figure ignores. The hook head's flat is the same 6 x 28 section as the tang, with the shear pin hole 10 mm below its top, so its tear-out factor is the same as the tang's [S6]. The bamboo pole is checked in section 10.

## 7. Float

The float winder gives 1.26 kg of net lift [B1] at 30 kg/m3 foam (the CAD model's foam is taken at 120 kg/m3, which would give a reserve of about 1.9). The ring and the cord weigh 0.60 kg in water [B2], so a dropped ring and cord float with a reserve of 2.1 [B3]. With the jigging weight on, the load is 1.57 kg [B4], more than the float holds: in jigging use the cord's end is tied to a thwart.

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
| Hook head (12 mm J, F1) | 0.26 kg [M10] |
| Working tool (ring, head, pole, pins) | 3.78 kg [M7] |
| Whole kit, including the crutch and jigging weight | 6.83 kg [M8] |
| Carried kit, aluminium prototype | 4.34 kg [M11] |
| Carried kit, bamboo local variant | 3.95 kg [V3] |

Correction in v0.2: v0.1 left out the mass of the lock pins, rivets and the jigging weight's pin (about 0.07 kg), because the script read no volume from parts grouped inside a group. The carried kit Amish decided on as 4.02 kg was therefore 4.08 kg; with the hook head it was 4.28 kg, and with the 12 mm hook of F1 (v0.3) it is 4.34 kg.

The longest packed piece is a section with its sleeve, 1.55 m [M9]; packed length meets R7. As Amish decided (SMR-DDR-003), the crutch stays clamped on the canoe as a fitting and the jigging weight is kept at the landing for deep sets, so R7 is judged on the carried kit. The aluminium prototype carries 4.34 kg [M11], 0.34 kg over the 4 kg target; the bamboo local variant carries 3.95 kg [V3] and meets it, with 0.05 kg to spare after F1. A 32 x 1.6 aluminium tube in place of 32 x 2 would bring the prototype to 3.92 kg [N1] with a buckling factor of 1.84 [N2]; Amish decided on 2026-10-04 (2A, SMR-DDR-004) to keep the 32 x 2 pole: R7 (PR-007) is judged on the bamboo local variant (3.95 kg, met), and the prototype's 4.34 kg is recorded, not a failure of R7.

## 9. Build time and cost

- Workshop time for one kit, one smith: 8.1 h [T1] (estimate, galvanising sent out), including 25 min for the hook head. R9 asks for under one day (8 h): at risk, about 5 min over, which is inside the accuracy of the estimate. The TRL 4 build trial decides.
- Parts cost of one aluminium prototype kit at prototype prices: USD 95.50 [C1], including the hook head (USD 3). The pole, sleeves and rivets are 30 % [C5], galvanising 13 % [C6] and the crutch 13 % [C7].
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 299.50 for the prototype run of three aluminium kits, one bamboo pole set and calibration wire (USD 1,700.50 under the target) [C2 to C4].

## 10. Bamboo local variant

Amish decided (SMR-DDR-003) that a bamboo local variant is built alongside the aluminium prototype, with one jigging weight shared by five canoes at a landing; since Amish's decision O8 of 2026-10-25 each canoe keeps its own crutch, so the carried mass (crutch left clamped on) and the cost count the same kit. The variant shares the ring, pole head, pins, hook head, tether and float with the prototype; only the pole differs (`bom/bom-bamboo-variant.csv`). Three treated culms 36 mm outside, 1,450 mm long, are joined by two steel ferrules 40 x 1.5 x 160 mm fixed to the lower culm with an M5 bolt and epoxy; the next culm slides in and is held by the same 6 mm lock pin. The bottom 120 mm of the lowest culm is dressed to 31.8 mm to fit the pole head; the top culm is cut above a node, so no grip cap is needed.

*Table 6. Bamboo local variant.*

| Item | Result |
| --- | --- |
| Bamboo pole (culms, ferrules, bolts) | 2.18 kg [V1], against 2.57 kg for the aluminium pole it replaces [V2] |
| Carried kit | 3.95 kg [V3]; R7 (PR-007) met |
| Buckling of the pole, pinned ends, E 15 GPa | 518 N [V4]; factor 1.49 over the top of the pin band [V5] |
| Buckling if E is only 10 GPa | factor 1.0 [V6] |
| Culm bend test (accept a culm) | 50 N (5 kg) hung at the middle of a 1.4 m span sags 2.9 mm or less [V10] |
| Saving from sharing the jigging weight among five canoes (each canoe keeps its own crutch, decision O8) | USD 5.60 a kit [V7] |
| Parts cost of one kit, its own crutch, weight shared | USD 66.90 [V8]; R10 (USD 40) not met |

The bamboo pole is less stiff than the aluminium one. A culm with E below about 15 GPa could bow before the pin breaks when the operator pushes hard; that bends the pole but does not load the canoe more than the pin allows. Culms are therefore chosen by the bend test above. The variant costs USD 66.90 a kit at prototype prices (estimate): USD 54.90 with the crutch shared (USD 2 more than the USD 52.90 of decision 13C: the hook head, USD 3, is in every kit and the bamboo top node saves the grip cap, USD 1), plus USD 12.00 because each canoe now keeps its own crutch (decision O8). Local bamboo, steel and galvanising prices near the first fishery, measured at TRL 4, decide how close it comes to USD 40.

## 11. Results against the requirements

*Table 7. Summary.*

| Requirement | Result | Status |
| --- | --- | --- |
| R1 | Hooked nets 81 to 126 N; wrapped nets 368 N to 2.3 kN, falling to 162 to 493 N once the hook has worked them back half a turn | At risk |
| R2 | 4.18 m top hand to ring; tether to 8 m | Met on paper |
| R3 | Design canoe 3.4 to 4.4 deg static against the 5 deg static limit (O6); 6.5 deg peak under a sudden jerk, ruled out by "lift steadily" and measured at TRL 4; canoes under 7 m or with fewer than three crew excluded by rule until per-class pins are set, and a measured displacement x GM of at least about 260 kg m added at the heel test (O9); band depends on calibration | Met on paper for a steady pull where the tool is allowed; at risk until the heel test |
| R4 | Pull capped at 347 N; mesh damage not calculable | Cannot be shown on paper |
| R5 | Release time | Cannot be shown on paper |
| R6 | 100 mm hinged ring | Met on paper |
| R7 | Packed 1.55 m; carried 4.34 kg (aluminium prototype), 3.95 kg (bamboo local variant) | Met, judged on the local variant; the prototype's 4.34 kg is recorded (decision 2A) |
| R8 | Galvanised steel, aluminium, stainless, polymers; treated bamboo in the local variant | Met on paper |
| R9 | 8.1 h | At risk |
| R10 | USD 95.50 (prototype); USD 66.90 (bamboo local variant, own crutch, weight shared) | Not met |

R1 to R10 are now PR-001 to PR-010 of SMR-PRS-001, with the same numbers. PR-011 (calibrated pin wire) is the CalRig check of section 2; PR-012 (the pin is the weakest link) is section 6, smallest factor 2.21 [S2], hook head 3.1 [S12]; PR-013 (rating mark and tag) is BOM line 19.
