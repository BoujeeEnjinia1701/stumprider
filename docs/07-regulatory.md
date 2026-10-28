---
doc_id: SMR-REG-001
title: StumpRider regulatory and standards register
project: StumpRider
doc_type: Regulatory and standards register
version: "0.1"
status: Draft
date: '2026-10-24'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First issue in the kit 1.9.1 upgrade; sources checked 2026-10-25
---

# StumpRider regulatory and standards register

No product standard or certification is known to apply to a hand tool for freeing fishing nets in Ghana; that is **to assess** with a local partner, not assumed. The laws that matter most are the ones the tool exists to serve: Ghana's Children's Act, 1998 (Act 560), which makes "going to sea" hazardous work with a minimum age of eighteen, and the Human Trafficking Act, 2005 (Act 694). The tool must never be presented as making children's work on canoes safe or acceptable (UR-011, PR-013). Fishing itself is governed by the Fisheries and Aquaculture Act, 2025 (Act 1146), which has nothing known to say about release tools; whether the Fisheries Commission would promote StumpRider as a safe practice is to assess. Not legal advice; anything marked "to assess" needs a qualified reviewer before any product claim. Method: STANDARDS section 23.

> **Safety:** Nothing in this register makes StumpRider a substitute for life jackets. The Ghana Maritime Authority says life jacket use is mandatory for all water transport; the tool's own rule is that every person on the canoe wears one while a snag is worked.

Table 1. Regulatory and standards register.

| # | Standard or regulation | Jurisdiction | What it covers | Applicability to this design | Owner (role) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Children's Act, 1998 (Act 560), section 91: minimum age of eighteen for hazardous work, which "includes going to sea" | Ghana | Child labour and hazardous work | The context the tool serves. The tool and every document state that it is never a reason to keep children on boats; distribution only with child-protection partners (UR-011, SMR-DDR-001 D9) | Partner liaison (child-protection NGO) | Applies (to the context; met by design in the wording and the distribution rule) |
| G2 | Human Trafficking Act, 2005 (Act 694) | Ghana | Trafficking and intermediaries; consent is no defence for children | As G1; the README and PRB state the context factually and name no boat owner or community | Partner liaison | Applies (to the context) |
| G3 | ILO Worst Forms of Child Labour Convention, 1999 (No. 182) and Minimum Age Convention, 1973 (No. 138), as reflected in Ghana's law | International | Hazardous work of children | As G1 | Partner liaison | Applies (to the context) |
| G4 | Fisheries and Aquaculture Act, 2025 (Act 1146) | Ghana | Fisheries management, inland management plans, gear and vessel licensing, the Fisheries Commission | A release tool is not fishing gear in the usual sense; whether any gear or safe-practice provision touches it, and whether the Commission can promote it, is not known | Partner liaison with the Fisheries Commission (Volta zone) | To assess |
| G5 | Ghana Maritime Authority safety rules on inland waterways, including mandatory life jackets and its Code of Operation for boat operators | Ghana | Safety of water transport on the Volta Lake | The tool's operating rules (life jackets, kneel, cut rather than capsize, the 7 m rule) sit inside these; no approval of a hand tool is known to be needed | Partner liaison | To assess |
| G6 | ISO 12402 series, personal flotation devices | International | Life jackets and buoyancy aids | The float winder floats the ring and cord only; StumpRider is not a flotation device and must never be presented as one | Design lead | Does not apply |
| G7 | ISO 1461, hot dip galvanized coatings on fabricated iron and steel articles | International | Coating thickness and testing | Called up in the BOM for the steel parts (line 18) as the galvaniser's standard where one is used; zinc-rich paint is the fallback | Design lead | Applies (as specification, to confirm with the galvaniser) |
| G8 | ISO 4017, ISO 4032, ISO 7089 and ISO 2341 fasteners and clevis pins | International | Bolt, nut, washer and clevis pin dimensions | Used for the bought fasteners and in the model (`.kit/cad_parts.py`) | Design lead | Met by design |
| G9 | Patent US3464138A, device for releasing a snagged fishing lure (expired) | United States | Sliding ring and weight on a line | Public prior art; the design keeps to a plain split ring and publishes its own shear pin value (SMR-PRC-001, patent design-arounds). Not legal advice | Design lead | Met by design |
| G10 | Product liability for an open design used on the water | Ghana and wherever it is built | Responsibility if a tool built from the drawings is used and someone is hurt | Published as an open engineering reference, not certified equipment; the warnings travel with every document and kit (PR-013). The legal position is not known | Maintainer, with legal advice | To assess |
| G11 | Open hardware licences: CERN-OHL-S-2.0 (hardware), MIT (software), REUSE | International | Licensing | Applies to the repository | Maintainer | Met by design |

Status: to assess, applies, does not apply, met by design, certification needed later.

## Sources

- Ghana, *Children's Act, 1998* (Act 560), section 91, https://www.ecoi.net/en/file/local/1158191/1504_1217427520_children-s-act.pdf, accessed 2026-10-25.
- US Department of Labor, Bureau of International Labor Affairs, *Ghana's Laws and Regulations on Child Labor, WFCL and Education* (Acts 560, 651, 694 and 778; minimum ages), https://dol.gov/sites/dolgov/files/ILAB/Ghana%27s%20Laws%20and%20Regulations%20on%20Child%20Labor%2C%20WFCL%20and%20Education.pdf, accessed 2026-10-25.
- UNEP Law and Environment Assistance Platform, *Fisheries and Aquaculture Act, 2025 (Act 1146)*, https://leap.unep.org/en/countries/gh/national-legislation/fisheries-and-aquaculture-act-2025-act-1146, accessed 2026-10-25; Ghana News Agency, "President Mahama assents to the Fisheries and Aquaculture Bill, 2025", https://gna.org.gh/2025/08/president-mahama-assents-to-the-fisheries-and-aquaculture-bill-2025/, accessed 2026-10-25.
- *Daily Graphic*, "3 co-wives, 5 children perish in canoe disaster: Maritime Authority insists life jackets use mandatory for all water transport", 11 April 2026, https://www.graphic.com.gh/news/general-news/ghana-news-3-co-wives-5-children-perish-in-canoe-disaster-maritime-authority-insists-life-jackets-use-mandatory-for-all-water-transport.html, accessed 2026-10-25.
- Google Patents, US3464138A, https://patents.google.com/patent/US3464138 (cited in SMR-PRB-001).
- ISO 12402, ISO 1461, ISO 4017, ISO 4032, ISO 7089, ISO 2341: titles as published by ISO; scope as used here, not checked clause by clause.
