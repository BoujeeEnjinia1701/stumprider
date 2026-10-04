# Review note: StumpRider

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (SMR-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (SMR-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (SMR-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate)

Run as the first half of `/to-trl3` under Amish's pre-approvals of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds". Kit 1.7.0 installed.

### What was done

- `docs/01-problem.md` (SMR-PRB-001 v0.2): design canoe and snag cases, budget written as a value-engineering target, open questions settled or moved to the register, first co-design candidates, safety section.
- `docs/02-concept.md` (SMR-PRC-001 v0.2): how it works, components with BOM numbers, key design choices, first-order numbers, design-arounds kept, safety.
- `docs/03-requirements.md` (SMR-REQ-001 v0.2): R1 to R10, targets unchanged, with a concept status.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (1.75 m person for scale), `media/exploded.png` (the working end, BOM callouts), `media/cutaway.png` (cut through the shear pin), `media/concept-blueprint.png`, `.pdf` and `.svg` (SMR-DWG-010), `media/model.glb` (0.9 MB, coarse tessellation) and `media/viewer.html`. No flow diagram: the tool moves no energy or material.
- `bom/bom.csv`: 20 priced lines.

### Results

- A ring on a pole can lift a net hooked over a branch with a modest pull; the pin rating that keeps an 8 m canoe safe is about 300 N. A net wrapped round a branch and a small dugout are the two hard cases.

### Requirements not met

- See the TRL 3 section: R1 and R3 at risk, R7 and R10 not met; R4 and R5 cannot be shown on paper.

### Decisions made under the pre-approval

SMR-DDR-001, items D1 to D10: hinged two-half ring; aluminium prototype pole; one calibrated 2.0 mm aluminium shear pin, 302 N nominal; pin carries push and pull; operating rules including the interim rule on canoes under 7 m; pinned jigging weight; foam float winder; clamp-on roller crutch; distribution only through child-protection partners, first candidates to approach (none approached); requirement targets kept.

### Safety concerns

- The tool must never be read as making child diving or child labour acceptable; it is handed out only with child-protection work.
- Capsize when pulling from a small canoe (see TRL 3).

## Session 2026-10-03: TRL 3 (advance and build plan)

Run as the second half of `/to-trl3` under the same pre-approvals, which count as the TRL 2 approval. Not committed or pushed (batch run).

### What was done

- `cad/src/model.py`: parametric build123d model of the kit; 80 of 80 constructability checks pass (overlaps; every pin and rivet bearing in its holes; fork and weight cheeks clear of the tang; tang 45 mm clear of the end plate; sleeve slide fit; sections butting; tether clear of the head and weight; crutch on 30, 40 and 60 mm gunwales; packed length). Exports `cad/step/stumprider-assembly.step`, `rider-ring.step`, `pole-head.step`, `pole-section.step`, `joint-sleeve.step`, `jigging-weight.step`, `gunwale-crutch.step`, `float-winder.step`, and STL of the ring halves, pole head, roller and float winder.
- `docs/04-calcs/01-sizing.md` (SMR-CAL-001 v0.1) with `docs/04-calcs/sizing.py` and `results.csv`: pin rating, canoe heel for the design canoe and a small dugout, freeing pull, reach, strength, float, mass, build time, cost and the option figures below.
- `cad/src/sheets.py`: general arrangement `cad/drawings/SMR-DWG-001` (SVG, PDF, PNG) at Rev P2: the working end in three views at 1:5 and the whole tool at 1:40.
- `cad/src/build_plan_media.py`: `docs/05-build-plan/overview.png`, 10 making sketches `cad/drawings/SMR-DWG-101` to `110`, 9 joint close-ups and 11 step pictures.
- `docs/05-build-plan.md` (SMR-BLD-001 v0.1), `docs/06-design-decisions.md` (SMR-DEC-001 v0.1), `docs/decisions/0001-trl2-review-decisions.md` (SMR-DDR-001) and `docs/decisions/0002-design-for-construction.md` (SMR-DDR-002). SMR-PRC-001 and SMR-REQ-001 updated to v0.3.
- `cad/src/product_model.py` (appearance model) and render scenes exported with `.kit/export_views.py` to `/home/claude/renders/stumprider` for hero, exploded and detail; photoreal renders and cards are made on Amish's Mac.
- `project.yaml`: trl 3, trl_target 3, `design_state: constructable`, evidence listed; `budget_usd` unchanged. README leads with `media/render-hero.png` and has a "Building the prototype" section.

### Results

- Shear pin: 2.0 mm soft aluminium in double shear, 302 N nominal, 256 to 347 N band (to be calibrated per reel).
- Design canoe (8 m, three crew, 550 kg): 3.4 deg of heel kneeling and 4.4 deg standing when the pin breaks at the top of its band; 523 N would be needed for 5 deg.
- Freeing a hooked net: 81 to 126 N, a margin of 2.0 on the bottom of the pin band.
- Reach: 4.18 m top hand to ring; ring 3.2 m deep at 20 deg; tether to 8 m.
- Strength: pole buckling factor 2.2 is the smallest margin; every other part is at least 6 times the pin.
- Float: holds the ring and cord with a reserve of 2.1, not the jigging weight.
- Mass: working tool 3.73 kg, whole kit 6.5 kg. Build time about 7.7 h for one smith.
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 284 for three prototype kits and calibration wire (USD 1,716 under the target); USD 92.50 for one kit.

### Requirements not met or at risk

- R1 at risk (wrapped nets), R3 at risk (small canoes), R7 not met (kit mass), R10 not met (kit cost). Each is posed below for Amish to decide.
- R4 (mesh damage) and R5 (release time) cannot be shown on paper.

### Decisions for Amish

Each is listed in SMR-DEC-001 under Open decisions as "Proposed, awaiting Amish".

**D-A1. R1, freeing a net wrapped round a branch.**
- State: a net hooked over a branch lifts off at 81 to 126 N, inside the pin; a net wrapped once round needs 368 N (low friction) to 2,260 N (high friction), above the 256 to 347 N pin band. Cause: friction grows exponentially with each turn of net on the branch.
- Option A: no change; the crew is taught to walk the ring back round the branch half a turn at a time before lifting, or to cut. Effect: R1 rests on technique, unproven until trials; cost USD 0, mass 0.
- Option B: add a hook head, a bent 12 mm bar hook on a tang-sized flat that pins into the same fork with a shear pin, to pull the bight back round the branch. Effect: a second way to unwind a wrap; cost about USD 3 a kit, mass about 0.2 kg (R7 worse by that much).
- Option C: a stronger pin for wrapped nets. Effect: frees more wraps but heels the design canoe past 5 deg; rejected on safety grounds unless a heel test allows it; cost USD 0.
- **Recommendation: B**, made and tried beside the ring in the TRL 4 staged-snag trials, with the technique of A taught either way.

**D-A2. R3, small canoes.**
- State: in the 8 m design canoe the pin breaks at 3.4 to 4.4 deg of heel; in a 5.5 m two-crew dugout the same pin allows 23.7 deg kneeling, and 53 N already heels it 5 deg. Cause: a small dugout's righting moment is about a ninth of the design canoe's.
- Option A: keep the interim rule (only canoes of 7 m or more with at least three crew), printed on the pole head. Effect: R3 met where the tool is allowed; small canoes not served; cost USD 0.
- Option B: a light pin, 1.4 mm wire (148 N nominal), for canoes of 5 to 7 m. Effect: still 12.2 deg in the small dugout and barely above the pull a hooked net needs; a second reel to calibrate; cost about USD 3.
- Option C: heel-test real canoes by size class at TRL 4 and set a pin diameter per class. Effect: R3 met with evidence for each class; cost the test time and one reel per class.
- **Recommendation: A now, and C in the TRL 4 heel tests**, so small canoes are served only once a measured pin suits them.

**D-A3. R7, kit mass.**
- State: whole kit 6.5 kg (working tool 3.73 kg); packed length 1.55 m meets. Cause: the jigging weight (1.11 kg) and the steel crutch (1.37 kg).
- Option A: the crutch stays clamped on the canoe as a fitting and the jigging weight is kept at the landing for deep sets. Effect: 4.02 kg carried; cost USD 0.
- Option B: A plus bamboo pole sections with steel ferrules. Effect: 3.37 kg; saves about USD 22; bamboo varies in stiffness and needs rot protection (R8).
- Option C: leave out only the jigging weight. Effect: 5.39 kg; cost USD 0.
- **Recommendation: A** for the prototype; bamboo is judged under D-A4.

**D-A4. R10, kit cost.**
- State: USD 92.50 a kit at prototype prices. Cause: aluminium pole and sleeves (31 %), galvanising (13 %) and the crutch (13 %).
- Option A: bamboo pole sections with steel ferrules. Effect: USD 70.50; mass 0.65 kg less; stiffness to be checked.
- Option B: one crutch and jigging weight shared by five canoes at a landing. Effect: USD 74.90 a kit; no change to the tool.
- Option C: A and B together. Effect: USD 52.90 a kit; with local prices and batch galvanising it may come nearer the target.
- **Recommendation: C** as the local production variant, built alongside the aluminium prototype at TRL 4 so the two can be compared.

### Decisions made under the pre-approval

- SMR-DDR-002: design for construction, changes C1 to C12 and assumptions A1 to A5.
- Safety stops S1 to S5 and first checks, including pin calibration and a moored heel test before any use on a snag.
- Appearance model departures (renders only): a plank deck and a forearm and hand beside the packed kit in the hero; a short net line draped over a branch and the pole cut short in the detail view; the shear pin coloured red so it reads.

### Build plan findings

- Design changes for construction (2026-10-03), all in SMR-DDR-002: hinged two-half ring with ears, bolt hinge and pinned gate; steel socket with end plate and fork; tang with three holes, 45 mm clear of the plate; three 1.45 m sections with riveted sleeves and lock pins; removable head; grip cap; bowline tether and notched foam winder; jigging weight pinned to the tang; clamp-on saddle crutch with roller; galvanised steel and stainless pins; 30 mm pins with bent ends; rating and visibility marks.
- Items to confirm with real parts and canoes (wire strength, sleeve tube, canoe data, snag frequency, friction, prices, ring accuracy, mesh damage) are in SMR-DEC-001.

### Safety concerns

- Nobody enters the water, ever; the tool is handed out only with child-protection work and never presented as making child labour safer.
- Capsize: the pin protects the design canoe only. Until heel tests, no use from canoes under 7 m or with fewer than three crew; the operator kneels and the crew slackens the line when lifting.
- The pin is the safety device: only calibrated pins; a nail or bolt removes the protection.
- Sudden release when the pin breaks: the operator kneels so a fall is into the canoe.
- Welding galvanised steel gives off zinc fumes: all welding is done before galvanising, outdoors.
- Safety stops S1 to S5 in SMR-BLD-001 gate welding, fitting pins, going afloat and the first heel test.

### Recommended next step

Amish decides D-A1 to D-A4. The design is then ready for TRL 4 once Amish chooses to start it: build one aluminium kit (and the bamboo variant if D-A4 C is chosen), calibrate a wire reel on CalRig, and run the bench and moored heel checks of SMR-BLD-001 section 5 with the first co-design candidate.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's requirement decisions carried out

Amish said on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For StumpRider these are decisions 10B (R1), 11A then C (R3), 12A (R7) and 13C (R10), each as recommended under D-A1 to D-A4 above. Recorded in `docs/decisions/0003-requirement-decisions.md` (SMR-DDR-003). Not committed or pushed (batch run).

### Changes

- `cad/src/model.py`: hook head (BOM line 21): 6 x 28 x 60 flat with the tang's 10.5 and 2.1 mm holes and a 10 mm bar J (R30 bend, 50 mm clear throat), pinned into the same fork with the same shear pin; tether bowline moved across to it in use. Bamboo local variant pole: three 36 x 6 culms, bottom 120 mm dressed to 31.8 mm for the pole head, two 40 x 1.5 x 160 steel ferrules with M5 bolts, same lock pins. 144 of 144 constructability checks pass (64 new: hook head in the fork, pin bearing, cheeks clear, flat 45 mm clear of the plate, tether loop clear, throat; bamboo spigot seated, ferrule slide fit, bolts and pins through, culms butting, packed length; hook head clear of every part in the GA and packed layouts). STEP and STL regenerated, with new `hook-head.step`, `bamboo-pole-variant.step` and `hook-head.stl`.
- `bom/bom.csv` line 21 (hook head, USD 3, price basis given) and new `bom/bom-bamboo-variant.csv` (culms USD 1 each, ferrules USD 2 each, price basis given). `budget_usd` unchanged.
- `docs/04-calcs/sizing.py`, `01-sizing.md` v0.2 and `results.csv`: unwinding stages [F7, F8], hook head mass [M10], carried kits [M11, V3], bamboo pole [V1 to V10], new option figures [N1, N2]; old option figures O1 to O10 removed. Correction: lock pins, rivets and the weight pin had been left out of the masses (about 0.07 kg), because parts grouped inside a group read no volume.
- `docs/03-requirements.md` v0.4: R3 restated (used only from canoes 7 m or longer with three crew; smaller classes once heel tests set a pin), R7 restated (mass carried to and from the canoe, crutch on the canoe, weight at the landing), R10 verified on the bamboo local variant; Amish quoted. `docs/02-concept.md` v0.4, README, `project.yaml` evidence.
- `docs/05-build-plan.md` v0.2: Table 1 rows, sections 3.11 (hook head) and 3.12 (bamboo pole), Step 12 (hook head), Steps 10 and 11 (crutch stays on the canoe, weight at the landing), checks 8 and 9, S4 and S5.
- Pictures: general arrangement SMR-DWG-001 Rev P3 (detail B, hook head, and note lines); new making sketches SMR-DWG-111 (hook head) and SMR-DWG-112 (bamboo culms and ferrule joint); overview regenerated with the hook head; new joint-10 (hook head in the fork), joint-11 (ferrule joint) and step-12; concept media regenerated (hero, exploded, cutaway, blueprint key figures, `model.glb`).
- `docs/06-design-decisions.md` v0.2: O1 to O4 moved to Decisions made; new open decision O5; items to confirm 9 to 12; value engineering re-costed.
- `cad/src/product_model.py`: the hook head in the packed kit of the hero view; scenes re-exported to `/home/claude/renders/stumprider`.

### New results

- R1: at risk. A wrap worked back half a turn by the hook head needs 162 to 493 N [F7, F8] (was 368 N to 2.3 kN); low friction comes inside the pin band after one half turn, high friction after two. The staged-snag trials decide.
- R3: met on paper where the tool is allowed (3.4 deg kneeling, 4.4 deg standing in the design canoe); canoes under 7 m or with fewer than three crew excluded by the rule; pins per canoe class at TRL 4.
- R7 (4 kg carried): bamboo local variant 3.89 kg, met; aluminium prototype 4.28 kg, not met (4.08 kg before the hook head; the 4.02 kg quoted in D-A3 was low by 0.07 kg). Packed length 1.55 m, met.
- R9: about 8.1 h for one smith with the hook head (was 7.7 h), at risk by about 5 minutes against one day.
- R10 (USD 40): bamboo local variant USD 54.90 a kit (USD 52.90 decided, plus the USD 3 hook head, less the USD 1 grip cap), aluminium prototype USD 95.50; not met at prototype prices.
- Bamboo pole: buckling factor 1.49 at E 15 GPa, 1.0 at 10 GPa; culms accepted by a bend test (5 kg at the middle of a 1.4 m span sags 2.9 mm or less).
- Mass: hook head 0.21 kg; whole kit 6.78 kg.
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 299.50 for three aluminium kits, one bamboo pole set and calibration wire (USD 1,700.50 under the target).

### For Amish

**O5. R7 on the aluminium prototype (proposed, awaiting Amish).**
- State: the aluminium prototype carries 4.28 kg, 0.28 kg over R7's 4 kg. The 4.02 kg of D-A3 was really 4.08 kg, and the hook head adds 0.21 kg. The bamboo local variant carries 3.89 kg and meets R7.
- Option A: keep the 32 x 2 aluminium pole; judge R7 on the bamboo local variant and weigh the prototype at TRL 4. Cost USD 0.
- Option B: 32 x 1.6 aluminium tube for the prototype pole. Carried 3.86 kg; buckling factor 1.84 instead of 2.2; cost about the same; the thinner wall dents more easily.
- Option C: restate R7 to 4.3 kg.
- **Recommendation: A**, so the prototype trials stay comparable with the calculation note and R7 is judged on the kit fishers would get.
- The photoreal renders (`media/render-*.png`), card and social preview do not show the hook head yet; re-render on the Mac from the re-exported scenes.

### Safety

- The hook head is held by the same calibrated pin as the ring and is used under the same rules (kneel, slacken the line, cut rather than capsize, life jackets); it cannot heel the canoe more than the ring can.
- The 7 m, three-crew rule stands; a smaller canoe class needs its own heel-tested pin first.
- A bamboo culm softer than assumed bows before the pin breaks; this bends the pole but does not raise the load on the canoe. Culms are bend-tested before use.

## 2026-10-04: Amish's requirement decisions carried out (round 3)

Amish on 2026-10-04: "For round 3, I agree with all your proposed recommendations". For StumpRider this decides O5 of SMR-DEC-001 as recommended (2A). Recorded in `docs/decisions/0004-r7-prototype-mass.md` (SMR-DDR-004). Wording and records only; no geometry. Not committed or pushed.

### Changes

- `docs/03-requirements.md` v0.5: R7 judged on the bamboo local variant; Amish quoted.
- `docs/04-calcs/01-sizing.md`: R7 notes and summary row updated.
- `docs/06-design-decisions.md` v0.3: O5 moved to Decisions made; Open decisions now "None."
- No model, BOM, drawing or media change was needed.

### New results

- R7: met on the bamboo local variant, 3.89 kg carried against 4 kg. The aluminium prototype's 4.28 kg is recorded, not a failure of R7; it is weighed at TRL 4.
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 299.50 (USD 1,700.50 under the target). Unchanged.

### For Amish

Nothing new.

## 2026-10-04: photoreal renders redone after the round-2 and round-3 decisions

Views: hero, exploded, detail; cards regenerated; image_qc passes and `render.py --check` has no FAIL.
