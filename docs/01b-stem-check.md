---
doc_id: SMR-STM-001
title: StumpRider STEM check
project: StumpRider
doc_type: STEM check
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First issue in the kit 1.9.1 upgrade, on the TRL 3 design (SMR-DDR-002, SMR-DDR-003) and the concept options of SMR-OPT-001; hook head and option C tines fixed under the standing instruction (SMR-DEC-001 F1, F2); dynamic heel and hook tip-leg case proposed to Amish (O6, O10); independent review recorded and acted on
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (\"i approve of your recommendations\", SMR-DEC-001): S7 restated for O6 (static limit, steady-lift rule) and now plausible; S3b stays failing: the gusset of O10 was stopped when the straight shank above the bend was found at 1.87 [S13a]; 15 within, 11 plausible, 1 failing"
---

# StumpRider STEM check

Verdict: the working principle of the chosen design (a ring pushed down the net line by a pole lifts the net off the branch, and a soft aluminium shear pin caps the pull and the push on the canoe) sits within known physics. Of 27 claims, **15 are within known science, 11 are plausible** (the pin band, the freeing pull, the static heel on screening hydrostatics, the hook head's drag, corrosion couples, bamboo treatment, pin scatter, ring bending accuracy and the B and C working principles; four of them are closed as far as paper allows and need TRL 4 data) and **1 fails with a fix proposed**: S3b, the hook head with the bight caught on its tip leg is 1.58 times as strong as the pin at the bend and 1.87 times in the straight shank above it, under the 2 x rule. S7 (a quick pull held just under the pin can heel the design canoe about 6.5 deg) is plausible since Amish's decision O6 of 2026-10-25 made 5 deg the static limit with a "lift steadily, never jerk" rule, the peak to be measured at TRL 4. Two details failed and were fixed in this session under Amish's standing instruction of 2026-10-23: the hook head's 10 mm J (1.86 times; now 12 mm bar, SMR-DEC-001 F1) and option C's 12 mm grapnel tines (1.91 times; now 14 mm, F2). The fixes for S7 and S3b changed a safety limit or traded another requirement, so they went to Amish (O6, O10); he approved both recommendations on 2026-10-25, and the O10 gusset was stopped while carrying it through (below). `stem_check` is **open**. Method: STANDARDS section 20. Calculations: `docs/04-calcs/stem_check.py`, which reruns the calculation note SMR-CAL-001 (`docs/04-calcs/sizing.py`) and writes the table below.

> **Safety:** The pin rating, the heel limit and the rule on canoes under 7 m are safety limits. Nothing in this check relaxes them: nobody enters the water, every person on the canoe wears a life jacket, the crew slackens the line when the operator lifts, and the crew cuts the net rather than risk a capsize.

## Claims checked

Table 1. Claims, governing science and verdicts (generated from `docs/04-calcs/stem_results.csv`; S rows are option A, the chosen design; B and C rows are the other concept options).

<!-- STM_TABLE -->
| # | Claim | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Shear pin rating 302 N nominal (256 to 347 N) from 2.0 mm soft aluminium wire in double shear | Physics | Strength of materials | Double shear, F = 2 tau A; tau about 0.6 x tensile strength (von Mises); O-temper 1050 about 80 MPa tensile | 48 MPa (assumed) gives 302 N; 1100-O at a handbook 62 MPa gives 390 N, above the top of the band (347 N); half-hard or hard-drawn wire is far above it. The 1 mm gaps either side of the tang add bending and bearing (about 29 MPa on the tang), so the rating holds only for an O-temper reel calibrated on CalRig in a fork and tang like the real ones (PR-011). The plus or minus 15 % band is a requirement, not a result | Plausible, to confirm at TRL 3 | Open |
| S2 | Every load path except the pin is at least twice as strong as the pin (smallest margin: pole buckling) | Physics | Strength of materials | Euler buckling of the pinned 4.35 m pole, pi^2 E I / L^2, 6063-T6 E 69 GPa; other paths in SMR-CAL-001 Table 4 | 2.21 x >= 2 x | Within known science | SMR-CAL-001 s6 [S1 to S9] |
| S3 | Hook head J stays at least twice as strong as the pin with the bight in the bottom of the J | Physics | Strength of materials | Curved bar in bending, sigma = Kc M / Z + F / A, Wahl inner-fibre factor Kc = (4C - 1) / (4C - 4); S235 yield 235 MPa. The 10 mm bar of SMR-DDR-003 gave a factor of 1.86 (Fails, fix proposed); fixed with 12 mm bar (SMR-DEC-001 F1) | 3.1 x >= 2 x | Within known science | SMR-DEC-001 F1; SMR-CAL-001 [S11, S12] |
| S4 | A net hooked over a branch (half a turn) lifts off below the low end of the pin band | Physics | Mechanics and statics | Capstan (Euler-Eytelwein) T1 = T2 e^(mu theta) + crew line; friction of wet netting on wet bark 0.3 to 0.5 and a 20 N far leg assumed (SMR-CAL-001 A6, A7) | 126 N against 256 N (margin 2.0); the margin is gone at a far-leg tension of 47 N or a friction of about 0.8 (independent review). The law is standard, its inputs are assumptions | Plausible, to confirm at TRL 3 | SMR-CAL-001 s4 [F2, F5, F9] on assumed inputs; staged-snag trials at TRL 4 |
| S5 | The hook head works a wrapped net back round the branch half a turn at a time within the pin band | Physics | Mechanics and statics | Capstan: each half turn worked back divides the far-leg term by e^(mu pi) = 2.6 to 4.8; the drag the hook needs depends on how the net lies | Lift after one half turn back 162 to 493 N against 256 N; the hook's own drag cannot be set on paper | Plausible, to confirm at TRL 3 | Open |
| S6 | Static heel of the design canoe when the pin breaks at the top of its band, kneeling, is under 5 deg | Physics | Mechanics and statics | Righting moment = displacement x g x GM x sin(heel); GM from waterplane inertia (0.05 L B^3) and mass centres (SMR-CAL-001 A2 to A5) | 3.41 deg against 5 deg on screening hydrostatics; 5.1 deg with a 1.0 m beam, 4.7 deg with a 0.04 waterplane factor, 7.4 deg with both (independent review). Met only once GM is measured | Plausible, to confirm at TRL 3 | SMR-CAL-001 s3 [H5, H6, Q1 to Q3] on screening hydrostatics; moored heel test at TRL 4 |
| S7 | With the steady-lift rule, a quick pull does not take the design canoe past the 5 deg static limit; the peak under a jerk is measured at TRL 4 | Physics | Acoustics and vibration | Undamped roll oscillator, period 2 pi k / sqrt(g GM) = 1.06 s (k = 0.40 B); a pull rising in 0.25 s overshoots by 1 + |sin x| / x = 1.91 | Peak 6.5 deg kneeling for a pull held just under the pin; if the pin breaks at the top of the ramp the heel then is only 33 % of static (independent review). Decided by Amish on 2026-10-25 (SMR-DEC-001 O6, option A): the 2.0 mm pin stays, 5 deg is the static limit, "lift steadily, never jerk" is an operating rule and on the tag, and the moored heel test measures the roll period and the jerk peak; a 1.7 mm pin only if that test shows a real exceedance | Plausible, to confirm at TRL 3 | Open |
| S18 | With the crew still holding 100 N on the line as the pin breaks at the top of its band, the design canoe heels under 5 deg | Physics | Mechanics and statics | As S6, with the line tension over the crutch added; the line tension that alone takes the heel to 5 deg is 203 N | 4.05 deg <= 5 deg | Within known science | SMR-CAL-001 s3 [H14, H15]; operating rule: slacken the line when the operator lifts |
| S8 | Canoes under 7 m must be excluded: a 5.5 m dugout heels past 5 deg before the pin breaks | Physics | Mechanics and statics | As S6, for the 5.5 m two-crew dugout (SMR-CAL-001 A3) | 23.7 deg >= 5 deg | Within known science | SMR-CAL-001 s3 [K5, K7]; SMR-DDR-003 |
| S3b | Hook head J stays at least twice as strong as the pin if the bight catches on the tip leg | Physics | Strength of materials | As S3 with the arm doubled (60 mm, the tip leg); no yield before the pin breaks while the factor is above 1 | Factor 1.58 with 12 mm bar (independent review). Fixes (14 mm bar, about 0.09 kg more, so the bamboo variant's carried mass passes 4 kg; or a welded gusset) trade PR-007, so they went to Amish (SMR-DEC-001 O10). He approved the gusset on 2026-10-25, but the straight shank above the bend carries the same moment at a factor of 1.87, which a gusset at the bend does not reach, and a gusset to the flat breaks PR-007; back with Amish (docs/REVIEW.md) | Fails, fix proposed | Open |
| S19 | The aluminium pole does not yield under the largest side couple a kneeling operator can apply | Physics | Strength of materials | Tube bending, M = 200 N per hand x 0.6 m between the hands (A13), against the 214 MPa proof of 6063-T6; the pin does not cap side loads | 2.37 x >= 2 x | Within known science | SMR-CAL-001 s6 [S17] |
| S20 | Accepted bamboo culms (bend test) do not buckle before the pin breaks in a push | Physics | Strength of materials | Euler buckling of the bamboo pole at E 15 GPa, the stiffness the bend test accepts; under the 2 x rule of PR-012, which Amish's variant decision of SMR-DDR-003 already records | 1.49 x >= 1 x | Within known science | SMR-CAL-001 s10 [V5, V10]; PR-012 at risk for the bamboo pole |
| S9 | Top hand to ring is at least 4 m with three 1.45 m sections | Mathematics | Units and dimensional analysis | Geometry of cad/src/model.py (derived hand_to_ring) | 4.18 m >= 4 m | Within known science | SMR-CAL-001 s5 [R1] |
| S10 | The float winder floats a dropped ring and tether with a reserve above 1 | Physics | Fluid mechanics | Archimedes: foam lift (1000 - 30 kg/m3) against the weight in water of steel and polyester | 2.08 x >= 1 x | Within known science | SMR-CAL-001 s7 [B1 to B3] |
| S11 | Hot-dip galvanised steel parts show no functional corrosion after 6 months stored wet in fresh water | Chemistry | Electrochemistry and batteries | Zinc coatings to ISO 1461 (mean 55 to 85 um by steel thickness) corrode slowly in fresh water; zinc is anodic to steel and protects cut edges | Coating life far exceeds 6 months in fresh water; the field check (PR-008) confirms in the canoe bottom | Within known science | SMR-CAL-001 A8; PR-008 field check at TRL 4 |
| S12 | Stainless pins and rivets in the aluminium pole and the aluminium pin in galvanised steel do not seize or pit in fresh water | Chemistry | Electrochemistry and batteries | Galvanic series (ASTM G82 guide): zinc is anodic to aluminium, which is anodic to stainless steel; fresh water's low conductivity limits the current | Mild couples; aluminium round the stainless pins and rivets is the part at risk. Confirmed only by the 6 month wet storage check | Plausible, to confirm at TRL 3 | Open |
| S13 | Borax and boric acid treated bamboo (local variant) does not rot or attract borers in 6 months wet | Chemistry | Materials and polymer chemistry | Boron salts are standard bamboo preservatives against fungi and insects but leach in wet service | Leaching in a wet canoe bottom is the risk; the field check decides | Plausible, to confirm at TRL 3 | Open |
| S14 | A kneeling operator can lift 126 N on the pole to free a hooked net | Biology | Ergonomics | Comparable to lifting a 15 L bucket of water (147 N), a load carried routinely at landing sites | claimed 126 N, estimate 147 N (ratio 0.86) | Within known science | SMR-CAL-001 s4 [F2] |
| S15 | Whole kit mass from the calculation note agrees with the detailed CAD model | Mathematics | Orders of magnitude | Sum of part volumes x densities in cad/fidelity.json (foam taken at 120 kg/m3 there, 30 in CAL) | claimed 6.83 kg, estimate 7.2 kg (ratio 0.95) | Within known science | cad/fidelity.json option A |
| S16 | Pins cut from one reel break within plus or minus 15 % of the rating | Mathematics | Statistics and uncertainty | Wire diameter tolerance of about 0.03 mm on 2.0 mm is about 3 % of area; strength scatter within one reel of O-temper wire is usually smaller than between reels | Ten pins broken per reel on CalRig decide (TRL 4) | Plausible, to confirm at TRL 3 | Open |
| S17 | A village smith bends 12 mm bar to a 112 mm mean diameter within 2 mm over a former | Engineering and technology | Manufacturing tolerances | Cold bending of 12 mm mild steel round over a turned former is routine blacksmith work; springback is taken out by overbending | Checked against a full-size template at the build (SMR-BLD-001); the 2 mm joint gap absorbs small errors | Plausible, to confirm at TRL 3 | Open |
| B1 | Option B: a 2.2 kg knocker dropped 0.5 m along the line strikes with about 10 J | Physics | Mechanics and statics | Energy of the weight in water, speed capped at its terminal speed (3.7 m/s, Cd about 1) | claimed 10 J, estimate 9.57 J (ratio 1.04) | Within known science | Open |
| B2 | Option B: knocks along the near leg of the line free a net draped over a branch | Physics | Mechanics and statics | Angling lure retrievers free a hook by knocking the lure back along the line; a net over a branch has no hook point, and a knock along the near leg pushes the bight down onto the branch | Not shown on paper; expected to work only on light snags. Kept as option A's deep-snag mode (jigging weight on the tang) | Plausible, to confirm at TRL 3 | Open |
| B3 | Option B: jigging the knocker heels the design canoe less than 1 deg | Physics | Mechanics and statics | Line tension three times the weight in water at the crutch, 0.6 m arm, against the righting moment of S6 | 0.53 deg <= 1 deg | Within known science | Open |
| C1 | Option C: the shear link caps the rope pull at the same band as option A | Physics | Strength of materials | The same 2.0 mm soft aluminium pin in double shear in a fork and tang link | 347 N <= 523 N | Within known science | SMR-CAL-001 s2, s3 (pull for 5 deg kneeling) |
| C2 | Option C: a grapnel tine loaded at its tip is at least twice as strong as the link | Physics | Strength of materials | Cantilever tine, 14 mm bar, 60 mm arm, sigma = M / Z against S235 yield. With 12 mm tines the factor was 1.91 (Fails, fix proposed; independent review); 14 mm tines (SMR-DEC-001 F2) | 3.04 x >= 2 x | Within known science | SMR-DEC-001 F2 |
| C3 | Option C: pulling the net from the opposite side unwinds a wrap | Physics | Mechanics and statics | Capstan: a pull in the unwinding direction meets the crew-side tension times e^(mu theta) and each half turn undone divides it by 2.6 to 4.8 | Plausible; needs a second canoe or an anchored float, and the grapnel may bite the tree instead of the net | Plausible, to confirm at TRL 3 | Open |
<!-- /STM_TABLE -->

Verdicts: **Within known science**, **Plausible, to confirm at TRL 3**, **Fails, fix proposed**, **Fails**. A Plausible row with "Open" needs TRL 4 data; one with a "Closed by" is closed as far as paper allows, on the inputs it names.

## Fixes made under the standing instruction

Table 2. Fixes.

| Row | What failed | Options weighed | Fix (SMR-DEC-001) | Result |
| --- | --- | --- | --- | --- |
| S3 | The hook head's J of 10 mm bar, with the bight seated in the bottom of the J (30 mm off the shank axis), reaches 126 MPa at the pin's top load with the curved-bar factor, 1.86 times below S235 yield, against the rule that every part but the pin is at least twice as strong (PR-012) | (a) 12 mm bar, the ring's stock; (b) a smaller bend radius (narrows the throat below a doubled 16 mm line with room); (c) a welded gusset | F1: 12 mm bar, same 30 mm bend radius (throat 48 mm), butt welded to the flat's lower edge with a fillet all round in place of the 10 mm lap (a 12 mm bar cannot lap centrally on a 6 mm flat). No extra cost. Mass 0.21 to 0.26 kg | Factor 3.1 [S12]; bamboo variant carried mass 3.95 kg, still under 4 kg (PR-007, now at risk on its margin) |
| C2 | Option C's grapnel tines of 12 mm bar at 1.91 times the link's top load (found by the independent review) | (a) 14 mm tines; (b) shorter tines (less bite) | F2: 14 mm tines in the option C model | Factor 3.0 |

None of the fixes changes the working principle, the pitch or the scope. Both are recorded in SMR-DEC-001 as decided under Amish's standing instruction of 2026-10-23, and he can reverse them.

## Items decided by Amish on 2026-10-25, and the one back with him

- **S7, O6 (heel limit for a quick pull).** The static heel when the pin breaks at the top of its band is 3.4 deg kneeling (S6). A pull that rises to just under the pin in about a quarter of a second and is then held makes the canoe's roll (natural period about 1.1 s) overshoot by a factor of about 1.9, so the peak heel is about 6.5 deg. If the pin breaks at the top of the ramp, the load is gone and the heel is lower than static, as the independent review showed; the bound is the pull that stalls. Recommended: keep the 2.0 mm pin, state 5 deg as the static limit, add "lift steadily, never jerk" to the operating rules and the tag, and measure the peak in the moored heel test at TRL 4; a 1.7 mm pin only if that test shows a real exceedance. **Decided as recommended (O6, option A).**
- **S3b, O10 (hook head tip leg).** With the bight caught on the tip leg the J is 1.58 times as strong as the pin: no yield before the pin breaks, but under the 2 x rule. A 14 mm bar fixes it but adds about 0.09 kg and takes the bamboo variant's carried mass past 4 kg; a small gusset outside the bend was thought to fix it for about 0.02 kg and a little more welding. Recommended: the gusset. **Approved on 2026-10-25, then stopped:** the bight on the tip leg puts the same moment (the load times 60 mm) into the straight shank between the bend and the flat, where the factor is 1.87 (SMR-CAL-001 [S13a]); a gusset at the bend does not reach it, and one that reaches the flat (about 0.06 to 0.10 kg, estimate) takes the bamboo variant past PR-007's 4 kg. Back with Amish (O10).
- **O8 and O9** (crutch sharing against carried mass; canoe eligibility by measured righting moment) came from the review of the calculation note; both decided as recommended on 2026-10-25 (SMR-DEC-001).

## Fields not relevant

None. Physics (statics, strength, fluid mechanics, roll dynamics), chemistry (zinc coatings, galvanic couples, bamboo preservatives), biology (ergonomics of the lift), mathematics (geometry, orders of magnitude, scatter of the pin band) and engineering (manufacturing tolerances) are all touched.

## Concept options

- **Option A, rider ring on a shear-pin pole** (chosen design): rows S1 to S20 and S3b; S3b open with Amish (O10); S7 plausible since decision O6 (2026-10-25).
- **Option B, line-riding knocker weight:** within known science in its physics (B1 impact energy about 10 J, an upper bound; B3 heel under 1 deg, before any dynamic factor), but its working principle (B2) is plausible at best: a knock along the near leg pushes a draped net down onto the branch rather than lifting it, so it is expected to work only on light snags. Not dropped; scored low on freeing (SMR-OPT-001).
- **Option C, grapnel cross-pull:** within known science for the link (C1) and, after F2, the tines (C2); pulling from the opposite side to unwind a wrap (C3) is plausible, but it needs a second canoe or an anchored float, and the grapnel can bite the tree.

## Independent review

A second agent (a separate Claude session run headless, given only this check's claims table and verdicts, the calculation note SMR-CAL-001 v0.3, the product requirements SMR-PRS-001, `docs/04-calcs/sizing.py` and its results, and none of the author's reasoning) was asked on 2026-10-24 to refute the headline results and every "Within known science" verdict. It recomputed the numbers. Its findings and what changed:

Table 3. Independent review findings.

| Row or item | Finding | Change |
| --- | --- | --- |
| S1, pin band | Weakened: arithmetic right, but 1100-O at a handbook 62 MPa gives 390 N, above the band; the 1 mm gaps add bending and bearing; the band is a requirement, not a result | S1 restated with 62 MPa and the bearing; CalRig in a real fork and tang (PR-011); stays plausible |
| S4, F1 to F8 | Weakened: numbers reproduce, but the margin of 2.0 is gone at a 47 N far leg or friction of 0.8; "1.6 to 4.8" should be 2.6 to 4.8 | S4 to plausible, closed on assumed inputs [F9]; the factor corrected in CAL s4, S5 and C3 |
| S6, static heel | Weakened as a margin: 5.1 deg with a 1.0 m beam, 7.4 deg with that and a 0.04 waterplane factor; met only with a measured GM | S6 to plausible with the sensitivity [Q1 to Q3]; PR-003 at risk; O9 proposes a measured righting-moment criterion |
| Line tension on the canoe | Missing: the crew's line adds heel | S18 added: 4.05 deg with the crew holding 100 N [H14]; 203 N alone reaches 5 deg [H15]; the slacken rule stands |
| S7, dynamic heel | Refuted as stated: if the pin breaks at the top of the ramp, the heel then is about a third of static; the 1.9 factor needs a pull held just under the pin | Accepted in part: S7 restated as a quick pull held just under the pin, which is what a stalled pull on a snag does, so it stays "Fails, fix proposed"; the break case added [H13]; O6 recommends the operating rule and a measurement, the lighter pin only on evidence, and drops the immersion-angle argument |
| S8, 7 m rule | Weakened: length is a poor proxy for displacement x GM | O9 (keep the rule as a screen, add a measured criterion) |
| S2, pole buckling | Weakened: the reviewer took the push as uncapped and pole bending as unchecked | Push is capped: the tang stops 45 mm short of the end plate, so push and pull both go through the pin (SMR-DDR-002). Pole bending added: factor 2.4 under the operator's largest side couple [S17] (S19) |
| S3, hook head | Weakened: the tip-leg case (1.58) is a design case; welds unchecked | S3b added as "Fails, fix proposed", to Amish (O10); weld group about 11 MPa (CAL s6 note) |
| Bamboo pole and PR-012 | Missing: buckling 1.49 (1.0 at E 10 GPa) is under the 2 x rule | S20 added (accepted culms do not buckle before the pin breaks: 1.49); PR-012 at risk for the bamboo pole, as Amish's variant decision records |
| Ring and hinge | Weakened: halves pinned at hinge and gate give F R / 2 | Factor 4.1 [S15]; hinge bolt shear factor 44 [S16] |
| S9, reach | Upheld; the working depth of 3.17 m should be stated | Stated in CAL s5 and PRC (unchanged) |
| S10, float | Upheld with caveats (foam density in CAD 120, CAL 30) | Noted in CAL s7: reserve about 1.9 at 120 kg/m3 |
| S11, corrosion | Upheld with gaps (water chemistry, abrasion) | Field check stays the evidence (PR-008) |
| S14, ergonomics | Weakened: the operator must reach 256 to 347 N to break the pin | Kept: freeing needs 126 N, an axial lift on a near-vertical pole; breaking the pin is the limit, not a task. The real pull is measured at TRL 4 |
| S15 and masses | Weakened: 0.05 kg margin on PR-007 is inside the uncertainty; wet bamboo adds about 0.5 kg | PR-007 to at risk |
| V8 and the crutch | Weakened: the crutch is left on the canoe for mass but shared for cost | O8 to Amish |
| B1, B3 | Upheld arithmetically; B1 is a bound, B3 has no dynamic factor | Noted in the option text |
| C1 | Upheld | None |
| C2 | Refuted by the 2 x rule (1.91) | F2: 14 mm tines, factor 3.0 |
| Counts and labels | Upheld | Counts regenerated: 15 within, 10 plausible, 2 fail with a fix proposed |

## Sources

- Capstan (Euler-Eytelwein) and ring bending: W. C. Young and R. G. Budynas, *Roark's Formulas for Stress and Strain*, 7th ed. (New York: McGraw-Hill, 2002).
- Curved-bar inner-fibre factor for round bar: A. M. Wahl, *Mechanical Springs*, 2nd ed. (New York: McGraw-Hill, 1963), the curvature factor (4C - 1) / (4C - 4).
- Response of an undamped single-degree-of-freedom system to a ramped step load: J. M. Biggs, *Introduction to Structural Dynamics* (New York: McGraw-Hill, 1964).
- ISO 1461, *Hot dip galvanized coatings on fabricated iron and steel articles: Specifications and test methods* (coating thickness by steel thickness), as cited for S11.
- ASTM G82, *Standard Guide for Development and Use of a Galvanic Series for Predicting Galvanic Corrosion Performance*, as cited for S12.
- Angling lure retrievers that knock a lure back along the line: US3464138A (expired) and the Knockout Fishing Ott-O-Retriever, cited in SMR-PRB-001 (B2).
- Every design value: SMR-CAL-001 (`docs/04-calcs/01-sizing.md`, `docs/04-calcs/results.csv`), checked 2026-10-24.
