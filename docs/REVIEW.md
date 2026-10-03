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
