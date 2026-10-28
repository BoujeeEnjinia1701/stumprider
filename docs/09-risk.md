---
doc_id: SMR-RSK-001
title: StumpRider risk register, hazard analysis and design FMEA
project: StumpRider
doc_type: Risk register
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First issue in the kit 1.9.1 upgrade; project risks, preliminary hazard analysis and first-pass design FMEA of option A
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (SMR-DEC-001 O6 to O9) written in; O10 back with Amish"
---

# StumpRider risk register, hazard analysis and design FMEA

The largest hazard is the one the tool exists to remove: a person, often a child, sent into the water to free a net. The design's own hazards are capsize from the pull on the pole, the operator falling back when the pin breaks, and a stronger substitute pin defeating the safety link; each has a control, and two need evidence from TRL 4 (the heel under a jerk, under the steady-lift rule of decision O6, and the pin calibration). The top project risk is that no co-design partner is found, without which nothing can be tested. Scales: likelihood and impact or severity 1 (low) to 5 (high); in the FMEA, detection 1 (sure to be found) to 5 (unlikely to be found) and RPN = severity x occurrence x detection. Method: STANDARDS section 23.

> **Safety:** Every control here assumes the standing rules: nobody enters the water, every person on the canoe wears a life jacket, the operator kneels, the crew slackens the line when the operator lifts and cuts the net rather than risk a capsize, and the tool is used only from canoes 7 m or longer with at least three crew.

## Project risks

Table 1. Project risk register.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | No co-design partner | No NGO or landing committee approached yet | No staged-snag trials, no heel tests, no user validation | 3 | 5 | Project lead | Approach Challenging Heights and the Fisheries Commission's Volta zone office first (SMR-PLN-001) |
| P2 | The tool is read as making children's work on canoes acceptable | Handed out without protection work, or marketed as a safety tool for divers | Harm to children; harm to the partner's work | 2 | 5 | Partner liaison | Distribution only through child-protection partners (D9); wording on every document and the tag (PR-013) |
| P3 | Nets wrap more often than they hook | Snag statistics unknown | PR-001 not met; the hook head carries the load | 3 | 4 | Design lead | Ask partner crews first (DEC item to confirm 4); trial the hook head beside the ring |
| P4 | Kit cost stays above USD 40 | Prototype prices; galvanising minimum lots | PR-010 not met; fewer kits per canoe | 4 | 3 | Design lead | Local prices, batch galvanising, bamboo variant with shared crutch (13C) |
| P5 | O-temper pin wire not available locally | Electrical wire is usually hard-drawn | Pins too strong; safety link defeated | 3 | 5 | Design lead | Specify, calibrate every reel (PR-011); anneal a reel and recalibrate if needed (to assess) |
| P6 | Aluminium tube not available near the fishery | Supply | Aluminium prototype hard to repeat | 3 | 2 | Design lead | Bamboo local variant (SMR-DDR-003) |

## Preliminary hazard analysis

Table 2. Preliminary hazard analysis.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Capsize while working a snag | Pull on the pole heels the canoe; small canoe; standing operator | Drowning | 5 | 2 | Shear pin 302 N nominal; 3.4 deg static heel in the design canoe [H5]; 7 m and three-crew rule; kneel; life jackets; cut the net | Severity 5, likelihood 1 for steady pulls; jerk peak 6.5 deg [H11] ruled out by the steady-lift rule (O6, 2026-10-25) and measured at TRL 4; measured displacement x GM criterion (O9) |
| H2 | Sudden release when the pin breaks | Pin shears at full pull | Operator falls back in the canoe; strikes crew with the pole top | 3 | 3 | Kneel; crew clear of the pole top; pole top painted orange | 2, 3 |
| H3 | Stronger substitute pin | Nail, bolt or steel wire fitted when pins run out | Pull no longer capped; H1 returns | 5 | 3 | Eleven spare pins in the tube; rating marked on the pole head; training; PR-011 | 5, 2 |
| H4 | Someone enters the water anyway | Tool fails; habit | Drowning; the problem the tool exists to stop | 5 | 2 | Cut the net rather than dive; distribution with protection work; tag (PR-013) | 5, 2 |
| H5 | Pinch at the ring gate and hinge | Closing the ring on the line | Finger injury | 2 | 3 | Gate pin on a lanyard; ring closed before it is near the line under tension | 2, 2 |
| H6 | Hook head catches a hand or the operator's clothing | J hook near the canoe | Laceration; pulled toward the water | 3 | 2 | Hook head used kneeling, line slack, with the same pin | 3, 1 |
| H7 | Welding fumes from galvanised steel | Welding after galvanising | Metal fume fever | 3 | 2 | Weld before galvanising, in the open (SMR-BLD-001 S1) | 3, 1 |
| H8 | Crutch clamp slips off the gunwale | Loose clamp; gunwale outside 30 to 60 mm | Line jumps; crutch lost overboard | 2 | 2 | Clamp checked by hand before use (S3) | 2, 1 |

## Design FMEA (first pass, option A)

Table 3. Design FMEA.

| Item | Function | Failure mode | Effect | Cause | Severity | Occurrence | Detection | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shear pin (5) | Break at 256 to 347 N | Breaks high | Canoe heels further; H1 | Wrong temper or alloy; thick wire | 5 | 3 | 3 | 45 | CalRig per reel (PR-011); O-temper specified; rating mark |
| Shear pin (5) | Break at 256 to 347 N | Breaks low | Pin breaks on hooked nets; slow use | Thin wire; nicked pin | 2 | 3 | 3 | 18 | Calibration; deburr; spares |
| Pole and pole head (4, 6, 7) | Carry push and pull to the ring | Pole buckles before the pin breaks | Pole bent; pull not capped cleanly | Factor 2.21 [S2]; damaged section | 3 | 2 | 2 | 12 | Replace bent sections; sleeves stiffen joints |
| Hook head (21) | Drag a wrapped bight back | J opens | Hook lost; bight not freed | 10 mm bar at factor 1.86 | 3 | 1 | 2 | 6 | Fixed by F1: 12 mm bar, factor 3.1 [S12] |
| Rider ring (1) | Close round the line and slide | Ring out of round; gate pin will not go in | Ring cannot be closed | Bending error over 2 mm | 2 | 3 | 1 | 6 | Bend over a former; check against a template (S17) |
| Gate pin (3) | Keep the ring closed | R-clip lost; pin falls out | Ring opens; ring lost if the tether fails | Lanyard cut | 3 | 2 | 2 | 12 | Lanyard; tether holds the ring |
| Tether and float (11, 12) | Recover the ring; float it if dropped | Bowline slips; foam waterlogged | Ring lost | Poor knot; damaged foam | 2 | 2 | 2 | 8 | Bowline checked; closed-cell foam; reserve 2.1 [B3] |
| Lock pins and rivets (8, 9) | Hold the pole joints | Corrosion of aluminium round stainless | Joint loose; pole separates | Galvanic couple in wet storage (S12) | 3 | 2 | 3 | 18 | Six month wet storage check (PR-008) |
| Galvanised steel parts | Resist wet storage | Coating damaged at cuts after galvanising | Rust | Drilling or grinding after galvanising | 2 | 2 | 2 | 8 | All cutting before galvanising; zinc paint on damage |
| Bamboo pole (V1, V2) | Same as the aluminium pole | Culm splits or rots; buckles at 1.0 factor at low E | Pole fails; pull not capped cleanly | Untreated or weak culm | 3 | 3 | 2 | 18 | Bend test per culm [V10]; borax treatment; field check |
| Gunwale crutch (15 to 17) | Guide the line over the gunwale | Roller seizes | Line chafes | Grit in the bore | 1 | 3 | 1 | 3 | Rinse; HDPE on a bolt |
| Operator on the canoe | Lift steadily | Jerks the pole | Peak heel 6.5 deg [H11] | Snag lets go, frustration | 4 | 3 | 3 | 36 | Steady-lift rule in the operating rules and on the tag (O6, decided 2026-10-25); measured at TRL 4; 1.7 mm pin only if the test shows a real exceedance |
