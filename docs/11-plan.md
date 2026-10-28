---
doc_id: SMR-PLN-001
title: StumpRider project plan
project: StumpRider
doc_type: Project plan
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First issue in the kit 1.9.1 upgrade; stage P3 reached on paper, P4 on hold under the portfolio cap
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (SMR-DEC-001 O6 to O9) written in; O10 back with Amish"
---

# StumpRider project plan

StumpRider is at TRL 3 and stage P3 (design outputs): model at D3 for three concept options, drawings, priced BOM, build plan, decisions register, design FMEA and traceability for option A. The next gate, P4 (verification at TRL 4), is on hold under the portfolio caps of TRL 3 and P3. Decisions requested from Amish: the concept selection (O7, option A recommended) and the heel limit for a sudden jerk (O6, option A recommended). Method: STANDARDS sections 19 and 23.

> **Safety:** Every planned trial below is from a moored canoe or a bench; nobody enters the water, every person wears a life jacket, and no kit is used on a snag before its pin reel is calibrated and the heel test is passed.

## Workstreams

Table 1. Workstreams.

| Workstream | Owner (role) | Deliverable | Status |
| --- | --- | --- | --- |
| Design and calculations | Design lead | Model (D3), STEP, drawings, SMR-CAL-001, SMR-STM-001 | Done to P3; S7 plausible after O6 (2026-10-25); S3b open with Amish (O10) |
| Concept selection | Amish Chadha | SMR-OPT-001, SMR-DDR-005 | Option A chosen by Amish, 2026-10-25 (O7) |
| Requirements and traceability | Design lead | SMR-URS-001, SMR-PRS-001, SMR-RTM-001 | Done to P3; targets to confirm with a partner |
| Partner | Project lead | A child-protection NGO and a landing-site committee as co-design partners | Not started (risk P1) |
| Regulatory | Partner liaison | Answers to the "to assess" items of SMR-REG-001 | Not started |
| Verification (P4, TRL 4) | Test partner | Pin calibration, bench snags, moored heel tests by canoe class, staged-snag trials, build trial, six-month wet storage | On hold (portfolio cap) |
| Validation (P5) | Partner | Use by crews on the lake with the protection programme | On hold |

## Resources needed

Table 2. Resources (P4 planned work, on hold; costs are estimates from the BOM, not quotes).

| Resource | Deliverable | Effort | Estimated cost (USD) |
| --- | --- | --- | --- |
| Village smith | Three aluminium kits and one bamboo pole from SMR-BLD-001 | About 4 working days | Parts USD 299.50 (SMR-CAL-001 [C2]); labour to assess |
| CalRig or a spring balance rig | Ten pins per reel broken (PR-011) | 1 day | Within the prototype run |
| Moored canoe, three crew in life jackets, inclinometer | Static and jerk heel (PR-003, O6) | 1 day per canoe class | To assess with the partner |
| University fisheries department | Staged-snag trials (PR-001, PR-004, PR-005) | 5 days | To assess |
| Partner crews | Six-month wet storage (PR-008) | 6 months | To assess |

The value-engineering target is USD 2,000 (`project.yaml` budget_usd, unchanged); the prototype run is estimated at USD 299.50.

## Stage gates

Table 3. Stages (P4 to P6 on hold while the stage cap is P3).

| Stage | Gate criteria | Status |
| --- | --- | --- |
| P0 Proposal | PRB with users and stakeholders, STM, OPT, REG, FEA, PLN | Met (2026-10-24) |
| P1 Definition | URS, PRS, RSK with hazard analysis, MKT | Met (2026-10-24) |
| P2 Design inputs | PRS with targets and verification, CAL, RTM, concept selection DDR, STEM check closed on paper | Met on paper; concept selection decided 2026-10-25; S3b (O10) awaiting Amish |
| P3 Design outputs | Model, STEP, drawings, priced BOM, BLD, DEC, design FMEA, traceability complete | Met (2026-10-24) |
| P4 Verification | Test plans and reports, verification report | On hold (cap) |
| P5 Validation | Field trials with a partner | On hold (cap) |
| P6 Commercialization | Only with a named deployment partner; for StumpRider a distribution plan, not a sale | On hold (cap) |

## Next steps and decision requested

1. Amish: decide O10 again (hook head tip leg: accept the case, 14 mm bar, or a gusset to the flat, each trading PR-012 against PR-007). O6 to O9 were decided on 2026-10-25.
2. Approach the first co-design candidates (Challenging Heights; a Volta landing-site committee through the Fisheries Commission; a university fisheries department) once Amish agrees.
3. When the portfolio cap lifts: build to SMR-BLD-001 and run the first checks.

## References

- Bass Pro Shops. "Knockout Fishing Ott-O-Retriever." https://www.basspro.com/p/knockout-fishing-ott-o-retriever.
- Biggs, John M. *Introduction to Structural Dynamics*. New York: McGraw-Hill, 1964.
- CBS News. "Ghana's Lake Volta Child Slavery." 2021. https://www.cbsnews.com/news/ghana-lake-volta-child-slavery/.
- *Daily Graphic*. "3 Co-wives, 5 Children Perish in Canoe Disaster: Maritime Authority Insists Life Jackets Use Mandatory for All Water Transport." April 11, 2026. https://www.graphic.com.gh/news/general-news/ghana-news-3-co-wives-5-children-perish-in-canoe-disaster-maritime-authority-insists-life-jackets-use-mandatory-for-all-water-transport.html. Accessed October 25, 2026.
- FAO. "Lake Kariba Fisheries." https://www.fao.org/4/y5056e/y5056e03.pdf.
- Ghana. *Children's Act, 1998* (Act 560). https://www.ecoi.net/en/file/local/1158191/1504_1217427520_children-s-act.pdf. Accessed October 25, 2026.
- Ghana News Agency. "President Mahama Assents to the Fisheries and Aquaculture Bill, 2025." August 2025. https://gna.org.gh/2025/08/president-mahama-assents-to-the-fisheries-and-aquaculture-bill-2025/. Accessed October 25, 2026.
- Google Patents. US3464138A, Device for Releasing a Snagged Fishing Lure. https://patents.google.com/patent/US3464138.
- GS Products. "1.5kg Galvanised Steel Folding Boat Anchor." https://gsproducts.co.uk/1-5kg-galvanised-steel-folding-boat-anchor. Accessed October 25, 2026.
- IJM. *Fishing Prevalence Study Report*. 2024. https://ijmstoragelive.blob.core.windows.net/ijmna/documents/studies/2023-Fishing_Prevalence_Study_Report.pdf.
- IJM. "Foli." https://www.ijm.org/stories/foli.
- ILAB (US Department of Labor). *Analytical Study on Child Labour in Lake Volta Fishing in Ghana*. https://www.dol.gov/sites/dolgov/files/ILAB/CHILD%20LABOUR%20IN%20VOLTA%20LAKE%20FISHING%20STUDY%20REPORT%20-%20FINAL%20REPORT.pdf.
- ILAB (US Department of Labor). *Ghana's Laws and Regulations on Child Labor, WFCL and Education*. https://dol.gov/sites/dolgov/files/ILAB/Ghana%27s%20Laws%20and%20Regulations%20on%20Child%20Labor%2C%20WFCL%20and%20Education.pdf. Accessed October 25, 2026.
- Nature. "Small-Scale Fisheries." https://www.nature.com/articles/s41586-024-08448-z.
- Tackle Warehouse. "Knockout Fishing Ott-O Lure Retriever." https://www.tacklewarehouse.com/Knockout_Fishing_Ott-O-Lure_Retriever/descpage-OTTO.html. Accessed October 25, 2026.
- UNEP Law and Environment Assistance Platform. "Fisheries and Aquaculture Act, 2025 (Act 1146)." https://leap.unep.org/en/countries/gh/national-legislation/fisheries-and-aquaculture-act-2025-act-1146. Accessed October 25, 2026.
- Wahl, A. M. *Mechanical Springs*. 2nd ed. New York: McGraw-Hill, 1963.
- Wikipedia. "Lake Volta." https://en.wikipedia.org/wiki/Lake_Volta.
- World Maritime University. *Underwater Timber Harvesting on the Volta Lake*. https://commons.wmu.se/cgi/viewcontent.cgi?article=1009&context=all_dissertations.
- Young, Warren C., and Richard G. Budynas. *Roark's Formulas for Stress and Strain*. 7th ed. New York: McGraw-Hill, 2002.
- ISO 1461, ISO 2341, ISO 4017, ISO 4032, ISO 7089, ISO 12402; ASTM G82 (titles as cited in SMR-STM-001 and SMR-REG-001).
