---
doc_id: SMR-OPT-001
title: StumpRider concept options
project: StumpRider
doc_type: Concept options
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First issue in the kit 1.9.1 upgrade; the TRL 3 design is option A; options B and C added with different working principles, each modelled to D3; scored against SMR-URS-001; selection proposed, awaiting Amish
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish chose option A on 2026-10-25 (SMR-DEC-001 O7); S7 plausible after O6; bamboo variant USD 66.90 after O8 (scores unchanged)"
---

# StumpRider concept options

Recommendation: keep **option A, the rider ring on a shear-pin pole** (weighted score 120). Option B, the line-riding knocker weight, scores highest on the weighted sum (134, 12 % above A) because it is cheap, simple and harmless to the canoe, but it scores 1 of 5 on the one requirement the tool exists for (UR-001, freeing the net): a knock along the line cannot lift a net draped over a branch (SMR-STM-001 B2). Option C, the grapnel cross-pull, scores 109. Amish chose option A on 2026-10-25 ("i approve of your recommendations"; SMR-DEC-001 O7, SMR-DDR-005). Method: STANDARDS section 21.

![Concept options side by side at one scale](../media/options.png)

*Figure 1. The three options from the D3 model (`cad/src/model.py` components(); Cycles render by the coordinator with `python .kit/options.py`; until then the file is a labelled placeholder).*

> **Safety:** Every option is worked from the canoe and none puts anyone in the water. Each caps or limits the pull on the canoe in a different way, and each is used only under the standing rules: life jackets, kneel, slacken, cut rather than capsize, canoes 7 m or longer with three crew.

## The options

### Option A: rider ring on a shear-pin pole

A hinged ring of 12 mm steel bar, 100 mm inside, is closed round the net line and pushed down it onto the snag by a three-section aluminium pole (4.18 m from the top hand). The crew slackens the line and the operator lifts, twists and pushes the ring along the branch until the mesh lifts clear. The pole head forks over the ring's tang and is held only by a 2.0 mm soft aluminium shear pin (302 N nominal), so a hard pull breaks the pin before it heels the canoe more than 3.4 deg (steady pull). A hook head pins into the same fork for nets wrapped round a branch, and a jigging weight pins onto the tang for snags beyond the pole. This is the design carried since TRL 2 (SMR-PRC-001, SMR-DDR-002, SMR-DDR-003). Key risks: wrapped nets (PR-001 at risk), a sudden jerk (S7, O6), pin wire calibration. From a partner: snag statistics, canoe sizes, staged-snag trials.

### Option B: line-riding knocker weight

A 60 mm steel bar 120 mm long, split along its axis and bored 24 mm, is hinged on an M8 bolt through three welded knuckles and closed round the net line by an 8 mm clevis pin through three more. It runs down the line on a 10 m tether tied to an M10 eye bolt and is jigged: each 0.5 m drop strikes with about 10 J (B1). There is no pole and the pull on the canoe is only the weight's (heel under 1 deg, B3). This is the angling lure retriever scaled up to a net line. Key risk: a knock along the near leg pushes a draped net down onto the branch rather than lifting it, so it is expected to free only light snags (B2). From a partner: whether light snags are common.

### Option C: grapnel cross-pull

A four-tine grapnel of 14 mm bar (F2) on a 16 mm shank is swept on a 15 m rope under the net beyond the snag, from a second canoe or after paddling round, and pulled from the opposite side, so the net is drawn back the way it hooked or wrapped. A shear link (a fork and tang with the same 2.0 mm pin) between the rope and the grapnel's shackle caps the pull at the same band as option A. Key risks: the grapnel bites the tree as readily as the net, the tines tear mesh, and it needs a second canoe or an anchored float (C3). From a partner: whether a second canoe is usually at hand.

## First-order numbers

Table 1. Options compared (masses and part counts from `cad/fidelity.json`, D3).

| Quantity | Option A | Option B | Option C |
| --- | --- | --- | --- |
| Estimated parts cost (USD) | 95.50 aluminium prototype; 66.90 bamboo local variant (BOM, own crutch since O8) | About 52 before the eye bolt (estimate from BOM line prices; eye bolt to assess) | About 45 before the shackle and rope (estimate; shackle and rope to assess) |
| Mass of the modelled kit (kg) | 7.2 (whole kit with crutch and weight; carried 4.34, bamboo 3.95) | 4.5 (knocker, tether, winder, crutch) | 3.8 (grapnel, link, rope winder, crutch) |
| Output | Lifts a hooked net at 81 to 126 N; wrapped nets worked back with the hook head | Knocks of about 10 J along the line | Pull from the far side up to the link's 347 N |
| Effort and pull on the canoe | Pin caps the pull at 256 to 347 N; static heel 3.4 deg, jerk peak 6.5 deg | Heel under 1 deg | Same cap as A |
| Parts count (D3 model) | 77 (36 made or bought, 22 fasteners, 19 welds) | 55 (26, 10, 19) | 42 (23, 5, 14) |
| STEM check | Within known science; S7 plausible after decision O6; S3b fails with a fix proposed (O10) | B2 plausible at best | C3 plausible |

## Scoring

Table 2. Weighted scoring (weights: High UR 3, Medium 2, Low 1; scores 1 to 5). Cost and buildability are UR-010 and UR-009, so they are not counted twice.

| Criterion | Source | Weight | A | B | C | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Free the net from the canoe | UR-001 | 3 | 4 | 1 | 3 | A lifts hooked nets well inside the pin and has the hook head for wraps; B cannot lift a draped net; C can unwind a wrap but must first catch the net, not the tree |
| Reach the snag | UR-002 | 3 | 5 | 5 | 4 | A: 4.18 m pole and 8 m tether; B: any depth on its tether; C: any depth, but aiming a grapnel blind is hard |
| Never risk the canoe | UR-003 | 3 | 4 | 5 | 3 | A: pin cap, jerk peak open; B: under 1 deg; C: same cap as A, but a grapnel fast in a tree loads the canoe until the link breaks |
| Keep the net whole | UR-004 | 2 | 4 | 4 | 2 | A and B work on the line; C's tines tear mesh |
| Quick | UR-005 | 2 | 3 | 4 | 2 | A: assemble pole, place ring; B: clip on and jig; C: sweep, often from a second canoe |
| Any net | UR-006 | 2 | 5 | 4 | 5 | A: hinged 100 mm ring; B: 24 mm bore takes 16 mm with little room for knots; C: needs no fit |
| Stows in a canoe | UR-007 | 2 | 3 | 4 | 4 | A: 4.34 kg carried (3.95 bamboo), 1.55 m; B and C: short and compact |
| Survives the canoe bottom | UR-008 | 2 | 4 | 5 | 5 | A has aluminium round stainless and a bamboo option; B and C are galvanised steel and rope |
| Made and mended locally | UR-009 | 3 | 3 | 5 | 4 | A: 8.1 h, ring bending, pole drilling; B: cut, drill and weld a bar; C: bend four tines and a link |
| Affordable | UR-010 | 3 | 2 | 5 | 4 | A: USD 66.90 to 95.50 (54.90 when scored, before O8); B about 52 before the eye bolt but no pole; C about 45 before rope |
| Handed out with protection work | UR-011 | 3 | 4 | 4 | 3 | A and B are one-canoe tools; C often needs a second canoe on the water |
| Safety | STANDARDS s21 | 3 | 4 | 4 | 2 | A: sudden release when the pin breaks; B: a jerked weight near the hands; C: a grapnel and rope under load |
| Maintenance | STANDARDS s21 | 1 | 4 | 5 | 4 | Spare pins for A and C; B has no consumables |
| **Weighted total** | | | **120** | **134** | **109** | |

## Recommendation

**Decided by Amish on 2026-10-25 (SMR-DEC-001 O7, argued in SMR-DDR-005):** keep option A. Option B leads the weighted sum by 12 %, more than the 10 % band in which both would go to Amish without a pick, so the rule for an existing design applies: when another option outscores option A, that goes to Amish as a decision. The recommendation departs from the totals because B's lead comes from cost and simplicity while it scores 1 on UR-001, the reason the tool exists; a weighted sum should not let price outvote the function. A suggested rule, an option that scores 1 on a High user requirement is not eligible, was not part of the recommendation and is not adopted.

**The runner-up's best idea:** option B's principle is already in option A as the deep-snag mode (the jigging weight pinned to the ring's tang and jigged on the tether), so nothing needs grafting; the suggestion is to try jigging first on light snags in the TRL 4 staged-snag trials, since it is the cheapest move. Option C's best idea, pulling a wrap back from the opposite side, is what the hook head does from the same canoe; it can be taught as a technique when a second canoe is at hand.
