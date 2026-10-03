---
doc_id: SMR-DDR-002
title: StumpRider design for construction
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
  change: Design made constructable; changes C1 to C12 and assumptions A1 to A5 decided under Amish's 2026-10-03 pre-approvals
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds".

> **Safety:** C2 and C3 make the shear pin the only link between the pole and the ring, so the safety limit cannot be bypassed by the tang bottoming in the fork. Nothing here changes the safety case of SMR-DDR-001.

## Context

STANDARDS section 18 asks that every part can be made by a stated process and fits and fastens to its neighbours. The TRL 1 concept named a "split rider ring" closed by a "captive pin", a "jointed push pole", a "pole head with shear pin", a "jigging weight" used on the tether cord and a "gunwale roller or crutch", but did not say how the ring opens, what the pin passes through, how the pole joints lock, or how the crutch holds on a canoe. The constructability review of the model (`cad/src/model.py`, 80 checks: overlaps, contacts of every pin and rivet in its holes, fork clearances on the tang, slide fit of the sleeves, the tang's clearance under the end plate, the crutch on 30, 40 and 60 mm gunwales, packed length) led to the changes below. None changes what the product does or its pitch.

## Changes

*Table 1. Changes made for construction.*

| # | The concept had | The constructable design has | Why |
| --- | --- | --- | --- |
| C1 | A split ring with a captive pin | Two half rings of 12 mm bar, 2 mm gaps at the joints; each end carries a 6 x 25 x 42 mm ear; M8 hinge bolt at one joint, 8 mm clevis gate pin with R-clip and lanyard at the other | A one-piece C ring with a pin across its gap cannot open far enough to take a line; hinged halves open fully |
| C2 | "Pole head with shear pin" | A 38 x 3 mm steel socket on a 6 mm end plate, with two 6 x 30 mm fork cheeks 8 mm apart welded under it | Gives the pin two shear planes and a known geometry; the pole bears on the end plate |
| C3 | No connection on the ring | A 6 x 28 x 84 mm tang welded on the outside of the fixed half, with 10.5, 6.5 and 2.1 mm holes (tether, jigging weight, shear pin); its top stops 45 mm below the end plate | The fork straddles the tang; the gap keeps push and pull on the pin; twisting bears on the cheeks |
| C4 | "Two or three sections" | Three 1,450 mm sections of 32 x 2 mm tube; 200 mm sleeves of 38 x 2.8 mm tube riveted (two 4.8 mm rivets) to the lower section of each joint; 6 mm lock pin through sleeve and upper section | Packed length 1.55 m; the joint cannot pull apart or twist |
| C5 | Head fixed on the pole | Head held on the bottom section by a 6 mm lock pin | It comes off for packing and for jigging |
| C6 | Open pole top | Rubber grip cap | Keeps water out and gives a grip |
| C7 | "Tether cord and float" | 10 m of 6 mm cord tied with a bowline through the tang's lowest hole; 300 x 120 x 40 mm foam winder with end notches; spare pin vial tied to it | A defined attachment and a float that holds the ring and cord |
| C8 | Jigging weight "used on the tether cord" | 50 mm steel bar 60 mm long with fork cheeks, pinned to the tang's middle hole with a lock pin, pole head off | A weight loose on the cord would not move the ring |
| C9 | "Gunwale roller or crutch" | 4 mm steel U saddle, 70 mm inside, over the gunwale; two cheeks carrying an 80 mm HDPE roller on an M12 bolt with 2 mm washers; M10 clamp screw with a pad through a nut welded on the inboard leg | Fits gunwales 30 to 60 mm thick without drilling the canoe |
| C10 | Materials open | Mild steel parts hot-dip galvanised after welding; stainless pins and rivets; 6063-T6 aluminium; HDPE; closed-cell polyethylene foam; polyester cord | R8 wet storage |
| C11 | Pin length open | Shear pins 30 mm long, ends bent over by hand after fitting | Holds the pin without a clip that could add strength |
| C12 | No marking | Pin rating painted on the socket; top 300 mm of the pole and the float painted orange | The rating is visible; a dropped part is easy to see |

## Assumptions

*Table 2. Assumptions to confirm when parts are bought (listed in SMR-DEC-001).*

| # | Assumption | Effect if wrong |
| --- | --- | --- |
| A1 | 38 mm tube with a 32.4 mm bore can be bought, or 38 x 3 mm tube opened to a slide fit | Sleeve fit; the lock pin holes must still line up |
| A2 | The pin wire shears at about 48 MPa | The pin diameter is changed to bring ten test pins into the 256 to 347 N band |
| A3 | Gunwales are 30 to 60 mm thick and have 70 mm of clear side below the top | The saddle width or leg depth changes |
| A4 | The design canoe (8 m, three crew, 550 kg) is typical of the first fishery | The heel check is redone with measured data |
| A5 | Bent 12 mm bar holds a 112 mm mean diameter within 2 mm | The joint gaps are trimmed to 2 mm before the ears are welded |

## Consequences

- 80 of 80 constructability checks pass in the model.
- The kit mass rises to 6.5 kg and the cost to USD 92.50 a kit (R7 and R10, decisions for Amish).
- STEP and STL files, the general arrangement (SMR-DWG-001, Rev P2), the making sketches (SMR-DWG-101 to 110), the concept media and the build plan (SMR-BLD-001) all come from the changed model.
