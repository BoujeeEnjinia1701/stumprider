---
doc_id: SMR-DDR-001
title: StumpRider TRL 2 review decisions
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
  change: TRL 2 review decisions D1 to D10, decided under Amish's 2026-10-03 pre-approvals
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds". Requirements that are not met or at risk are not decided here; they are posed to Amish in `docs/REVIEW.md` and SMR-DEC-001.

> **Safety:** D3, D5 and D9 set safety limits and rules. Each takes the conservative option and names the evidence that would relax it. The tool never replaces a life jacket and is never a reason to keep children on boats.

## Context

The scaffold (SMR-PRC-001 v0.1) named seven components and left their form, the pin rating, the canoe it is sized for and the way it is handed out open. These had to be settled to write a measurable precis, a massing model and the calculations.

## Options considered and decisions

*Table 1. TRL 2 decisions.*

| # | Question | Options considered | Decision | Why |
| --- | --- | --- | --- | --- |
| D1 | Form of the rider ring | Spring snap clip; open C ring with a pin across the gap; two hinged halves with a pinned gate | Two half rings of 12 mm steel bar, 100 mm inside, hinged on an M8 bolt and closed by an 8 mm clevis pin with a lanyard | Nothing to corrode shut; opens wide for 4 to 16 mm lines; a smith can make it |
| D2 | Pole material for the prototype | Bamboo; aluminium tube; steel tube | Three 1.45 m sections of 6063-T6 aluminium tube 32 x 2 mm, sleeve joints with lock pins | Uniform stiffness, so trials measure the tool; bamboo stays an option in the R7 and R10 decisions |
| D3 | Shear pin and rating | Plastic, brass or soft aluminium pin; one rating or several | One rating: 2.0 mm soft aluminium wire in double shear, 302 N nominal (256 to 347 N); ten pins from every reel broken on CalRig before use | Highest rating that keeps the design canoe under 5 deg of heel at the top of the band. Conservative; relaxed only by a measured heel test on real canoes |
| D4 | Where the pin sits | Pin for pull only, with a push stop; pin for both | The pin carries both push and pull: the tang stops 45 mm short of the end plate; twisting bears on the fork cheeks | One clear limit in both directions |
| D5 | Operating rules | Free use; rules printed on the tool | Operator kneels; crew slackens the line when the operator lifts; every person in a life jacket; tether end tied to a thwart; cut the net rather than risk a capsize; interim rule: not used from canoes under 7 m or with fewer than three crew until a heel test | Conservative; the interim rule is relaxed only by a heel test with the rated pin |
| D6 | Snags beyond pole reach | Second, longer pole; weight on the cord; weight pinned to the ring | A 1.1 kg weight pinned to the tang in place of the pole head, worked on a 10 m tether | A loose weight would not move the ring |
| D7 | Recovery and marking | Plain cord; float on the cord | 6 mm braided polyester cord on a closed-cell foam winder that floats the ring and cord, painted orange | A dropped ring is found and recovered |
| D8 | Net line over the side | Bare gunwale; carved crutch; clamp-on roller | Clamp-on steel saddle with an HDPE roller, for gunwales 30 to 60 mm thick | No drilling of the canoe; no rope cutting into hands or wood |
| D9 | How the tool is handed out | Sale; free handout; with child-protection work | Only through child-protection partners, with the message that nobody dives; first co-design candidates to approach (none approached): Challenging Heights; a Volta landing-site committee through the Fisheries Commission Volta zone; a Ghanaian university fisheries department for trials | The tool must not be read as making child labour safer |
| D10 | Requirements | Change targets; keep | R1 to R10 kept with their targets; design canoe and hard-case dugout defined as assumptions; status given at TRL 3 | Targets are Amish's; the calculations report against them |

## Consequences

- The constructable design (SMR-DDR-002) builds on D1 to D8.
- R1, R3, R7 and R10 come out not met or at risk on paper; they are posed to Amish with options, not decided here.
- Pitch, problem, patent design-arounds and `budget_usd` are unchanged.
