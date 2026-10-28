---
doc_id: SMR-DDR-005
title: StumpRider concept selection
project: StumpRider
doc_type: Design decision record
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: Concept selection argued in the kit 1.9.1 upgrade; proposed, awaiting Amish
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Accepted: Amish chose option A on 2026-10-25 (\"i approve of your recommendations\"); concept_chosen set to A"
---

# 0005: Concept selection

- **Date:** 2026-10-24 (proposed); 2026-10-25 (decided)
- **Status:** accepted. Amish Chadha (owner), 2026-10-25 12:43 CT: "i approve of your recommendations". Option A is chosen (SMR-DEC-001 O7); `concept_chosen: A` in `project.yaml`.

> **Safety:** Whichever option is chosen, nobody enters the water, the pull on the canoe is capped or small, and the standing rules apply (life jackets, kneel, slacken, cut rather than capsize, canoes 7 m or longer with three crew).

## Context

Kit 1.8 asks every repo for at least two concept options with different working principles, scored against the user requirements (STANDARDS section 21). StumpRider was designed before kit 1.8, so its TRL 3 design is option A, and it is not redesigned without Amish's go. Two other principles were developed and modelled to D3 (`cad/src/smr_options.py`): option B, a line-riding knocker weight (impact), and option C, a grapnel cross-pull (reverse pull from the far side). SMR-OPT-001 scores them against SMR-URS-001.

## Options considered

Table 1. Options.

| Option | Principle | Weighted score | Strongest point | Weakest point |
| --- | --- | --- | --- | --- |
| A, rider ring on a shear-pin pole | Push a ring down the line and lift the net off; a shear pin caps the pull | 120 | Lifts hooked nets well inside the pin; hook head for wraps; already designed to TRL 3 | Cost (PR-010 not met); a sudden jerk heels the canoe 6.5 deg (O6) |
| B, line-riding knocker weight | Jig a split weight along the line so its knocks shake the net off | 134 | Cheap, simple, under 1 deg of heel | Cannot lift a net draped over a branch (UR-001 scored 1); expected to free only light snags |
| C, grapnel cross-pull | Pull the net from the far side with a grapnel on a rope through a shear link | 109 | Unwinds a wrap | Bites the tree; tears mesh; often needs a second canoe |

## Decision

Decided by Amish on 2026-10-25, as recommended: **option A**, with option B's principle kept in it as the deep-snag jigging mode it already has, and jigging tried first on light snags in the TRL 4 staged-snag trials. Option B's 12 % lead on the weighted sum comes from cost and simplicity; it scores 1 of 5 on freeing the net, the requirement the tool exists for. The alternatives offered beside the recommendation, (a) B as a cheaper tool for light snags alongside A and (b) the scoring rule that an option scoring 1 on a High user requirement is not eligible, were not part of the recommendation and are not adopted.

## Consequences

A is confirmed: nothing in the design changes; `concept_chosen` in `project.yaml` is A. If B is chosen: the drawings, BOM and build plan are redone for B under a new decision record, and A's ring and pole become an option. Options B and C stay in the model at D3 either way.
