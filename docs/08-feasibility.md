---
doc_id: SMR-FEA-001
title: StumpRider feasibility assessment
project: StumpRider
doc_type: Feasibility assessment
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First issue in the kit 1.9.1 upgrade, on the TRL 3 design (option A)
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (SMR-DEC-001 O6 to O9) written in; O10 back with Amish"
---

# StumpRider feasibility assessment

StumpRider is feasible on paper as a village-made hand tool: every part is cut, bent, drilled and stick-welded from common stock, the physics of the pin, the canoe heel and the freeing pull sit within known science (SMR-STM-001), and the kit's parts cost about USD 95.50 (aluminium prototype) or USD 66.90 (bamboo local variant). Two things are not shown on paper and decide whether it is worth making: whether the ring and hook head free real snags (PR-001, at risk) and whether local prices can bring a kit near USD 40 (PR-010, not met). Method: STANDARDS section 23.

> **Safety:** Feasibility here never includes anyone entering the water. The heel limits, the 7 m rule, the calibrated pin and life jackets are conditions of every trial.

Table 1. Feasibility.

| Aspect | Assessment | Rating | Risks and notes | Links |
| --- | --- | --- | --- | --- |
| Design | A hinged ring, a forked pole head on a shear pin and a three-section pole; constructability checks pass (144 of 144 in `cad/src/model.py --check`) and the D3 model passes `cad_check.py` with 77 parts and no interference | High | Hook head fixed to 12 mm bar (F1); dynamic heel limit open (O6) | SMR-STM-001; SMR-CAL-001 s6; `cad/fidelity.json` |
| Materials | Mild steel bar, flat and tube; 6063 aluminium tube or treated bamboo; soft aluminium wire; HDPE, polyester cord, closed-cell foam | High | O-temper pin wire may be hard to find; hard-drawn electrical wire is far stronger and must not be used (PR-011) | SMR-STM-001 S1; `bom/bom.csv` |
| Manufacturing and assembly | Village smith with a stick welder, drill and vice; about 8.1 h a kit; galvanising sent out | Medium | PR-009 at risk by minutes; ring roundness within 2 mm to confirm (S17); galvaniser access | SMR-CAL-001 s9; SMR-BLD-001 |
| Power | None: hand tool | High | None | |
| Controls | None; the shear pin is the only safety device | Medium | The pin works only if every reel is calibrated and no substitute pin is used | PR-011; SMR-BLD-001 safety stop S2 |
| Function | Hooked nets need 81 to 126 N against a 256 N pin floor; wrapped nets need the hook head to work them back | Medium | Friction and how nets lie on real branches unknown; staged-snag trials at TRL 4 decide | PR-001; SMR-CAL-001 s4 |
| Safety | Static heel 3.4 deg in the design canoe; small dugouts excluded; jerk peak 6.5 deg | Medium | Steady-lift rule, 5 deg static limit (O6) and measured displacement x GM (O9), decided 2026-10-25; heel tests by canoe class at TRL 4 | PR-003; SMR-RSK-001 |
| Supply | Steel and hardware are local; aluminium tube and pin wire may come from Accra or Kumasi; bamboo is local | Medium | Local prices to confirm (DEC items to confirm 6) | SMR-MKT-001 |
| Cost | USD 95.50 aluminium prototype, USD 66.90 bamboo local variant against USD 40 | Low | PR-010 not met at prototype prices | SMR-CAL-001 s9, s10 |
| Partner | No co-design partner approached yet | Low | Everything at TRL 4 depends on one | SMR-PRB-001 co-design; SMR-PLN-001 |
