---
doc_id: SMR-PRB-001
title: StumpRider problem statement
project: StumpRider
doc_type: Problem statement
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 update; design canoe and snag cases stated, budget written as a value-engineering target, open questions settled or moved to the design decisions register, first co-design candidates, safety section
---

# StumpRider problem statement

When a gillnet snags on a drowned tree, the crew has three choices: cut the net, pull until something gives, or send someone down. On Lake Volta that someone is often a child. StumpRider is a hand tool that gives the crew a fourth choice from the canoe.

> **Safety:** The tool exists so that nobody enters the water. It must never be presented as a reason to keep children on boats, and it never replaces a life jacket. Pulling on a snag from a narrow canoe can heel it; the shear pin limits that pull, and the crew cuts the net rather than risk a capsize.

## The problem

Child labour studies of Lake Volta list diving to disentangle nets from tree stumps among the tasks children do, alongside paddling, bailing and pulling nets, and name drowning and net entanglement as major dangers ([ILAB](https://www.dol.gov/sites/dolgov/files/ILAB/CHILD%20LABOUR%20IN%20VOLTA%20LAKE%20FISHING%20STUDY%20REPORT%20-%20FINAL%20REPORT.pdf)). Reporting on trafficked children describes boat masters forcing children who cannot swim to dive to the bottom of the lake ([CBS News, 2021](https://www.cbsnews.com/news/ghana-lake-volta-child-slavery/)). The IJM 2024 study found 15 % of working children reported diving to retrieve nets ([IJM, 2024](https://ijmstoragelive.blob.core.windows.net/ijmna/documents/studies/2023-Fishing_Prevalence_Study_Report.pdf)).

Existing tools do not fit this job. Angling lure retrievers slide a weight or ring down a fishing line to knock a lure free, and the basic version was patented in 1967 and has long expired ([US3464138A](https://patents.google.com/patent/US3464138)); retail versions such as the Ott-O-Retriever work the same way ([Bass Pro Shops](https://www.basspro.com/p/knockout-fishing-ott-o-retriever)). They are sized for a monofilament line and a single lure, not a gillnet hooked over a branch. Underwater timber harvesting removes valuable trunks from the Volta Lake and improves navigation ([Wikipedia](https://en.wikipedia.org/wiki/Lake_Volta)), but it is slow and selective and leaves fishers with nothing to use today.

## Users and context

*Table 1. Users.*

| User | Need | Context |
| --- | --- | --- |
| Canoe crews and boat owners | Free a snagged net quickly without cutting it or sending anyone into the water | Dugout or plank canoes, two to five crew, gillnets set among drowned trees |
| Child protection and anti-trafficking NGOs | A tangible tool to distribute with awareness and rescue programmes | Landing sites and fishing villages along the lake |
| Fisheries officers and fisher associations | A safe-practice measure they can promote and help make locally | District fisheries offices, landing-site committees |
| Village blacksmiths and carpenters | Drawings they can follow with hand tools and local stock | Small workshops with a stick welder, a drill and a vice |

## Operating environment

- Warm fresh water, surface temperature typically above 25 °C (77 °F) (estimate), with poor underwater visibility.
- Snags from just below the surface to several metres down; design target 6 m (20 ft) of snag depth.
- Worked from narrow wooden canoes that are easy to roll; the operator kneels near the bow.
- Design canoe for the calculations (SMR-CAL-001): a paddled plank canoe 8 m (26 ft) long, 1.1 m (3.6 ft) wide at the waterline, with three crew. A small dugout of 5.5 m with two crew is checked as the hard case.
- Wind chop, rain and sun; tools left wet in the canoe bottom for months.
- No power, no workshop on the water; repairs happen at the landing site.

## Snag cases

Two cases set the design (SMR-CAL-001, section 4):

- **Hooked:** the net is caught over a branch, about half a turn of contact. Lifting it off takes about 80 to 130 N (18 to 29 lbf) on paper if the crew slackens the line while the operator lifts.
- **Wrapped:** the net has wound once round the branch. Friction grows so fast with each turn that lifting it straight off would need 370 N to more than 2 kN; it has to be worked back round the branch first, or cut.

How often each case occurs is not known; it is the first thing the co-design partner is asked.

## Constraints

- Value-engineering target: USD 2,000 for the prototype work (a hypothetical control target that keeps the design on a value-engineering lens, not a spending limit).
- Unit parts cost target below USD 40 per kit (R10), so that boat owners and NGOs can afford it.
- Buildable with hand tools, a small welder or forge, and locally available steel bar, aluminium or bamboo, and cord.
- Must never require anyone to enter the water.
- The pull transmitted to the canoe must stay below a level that heels it dangerously, which sets the shear-pin rating.
- Open hardware under CERN-OHL-S-2.0; documentation under the lab defaults.

## Out of scope

- Removing or harvesting drowned trees.
- Changing gillnet design or fishing practice beyond snag release.
- Enforcement, rescue or rehabilitation of trafficked children; the tool supports that work but does not replace it.
- Powered winches or capstans on the canoe.

## Prior work

*Table 2. Prior work.*

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| US3464138A, device for releasing a snagged fishing lure (1969, expired) | An openable ring with a weight that is clipped round a fishing line, slid down to the lure and jigged to free the hooks | Sized for a single line and lure; no way to lift a net off a branch or limit the pull on a small canoe | [link](https://patents.google.com/patent/US3464138) |
| Retail lure retrievers (for example Knockout Ott-O-Retriever) | A weight that attaches to the fishing line and slides down to knock a snagged lure free | Works on a light line and a lure, not a gillnet hooked on a trunk | [link](https://www.basspro.com/p/knockout-fishing-ott-o-retriever) |
| Underwater timber harvesting on Volta Lake | Commercial removal of submerged hardwood, which also improves navigation | Slow, selective and far from most fishing grounds; gives fishers nothing to use today | [link](https://commons.wmu.se/cgi/viewcontent.cgi?article=1009&context=all_dissertations) |

## Co-design

A child-protection or anti-trafficking NGO already working with fishing communities on Lake Volta, paired with a fisher association or landing-site committee, so that the tool is tested with crews who actually set nets among stumps and handed out alongside existing protection work. First candidates to approach (none approached yet): Challenging Heights, a Ghanaian NGO working against child trafficking in Volta fishing; a landing-site committee on the Volta Lake through the Fisheries Commission's Volta zone office; and a Ghanaian university fisheries department for the staged-snag trials.

## Questions settled at TRL 2

The open questions of version 0.1 are settled in the design decisions register (SMR-DEC-001) or carried there as items to confirm:

- Safe side pull and shear-pin rating: 300 N nominal (256 to 347 N), set against the design canoe (decision D3); small dugouts are a decision for Amish (SMR-REQ-001, R3).
- Wrapped nets: a ring alone cannot lift a wrapped net within the pin rating (decision for Amish, R1).
- Fork or hook head: kept as an option for the R1 decision; the ring is the prototype head.
- Distribution with child protection work: through the co-design partner, never sold or handed out alone (decision D9).
- Lake Kariba and other reservoirs: to confirm with the partner network; it does not change the prototype.
