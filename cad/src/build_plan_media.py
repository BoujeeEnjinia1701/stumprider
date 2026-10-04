"""StumpRider prototype build plan pictures (SMR-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything. Every picture is drawn from cad/src/model.py, so the
pictures and the model never disagree:
    docs/05-build-plan/overview.png    every component, laid out as packed, numbered in build order
    cad/drawings/SMR-DWG-101 to 112    making sketches for the made components (111 hook head,
                                       112 bamboo local variant pole, SMR-DDR-003)
    docs/05-build-plan/joint-NN.png    close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png     one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Box, Compound, Pos, Rot  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
D = M.derived(P)
OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
XP = M.X_POLE
Z0 = D["pole_z0"]
J1 = D["joints"][0]

COL = {"ring": "#B45309", "ring2": "#D97706", "hinge": "#6B7280", "gate": "#9CA3AF", "head": "#0F766E",
       "shear": "#DC2626", "pole": "#94A3B8", "sleeve": "#475569", "rivet": "#374151", "lock": "#6B7280",
       "cap": "#111827", "tether": "#EA580C", "winder": "#F97316", "spares": "#A3A3A3", "weight": "#78350F",
       "cframe": "#1D4ED8", "roller": "#A8A29E", "clamp": "#4B5563", "line": "#D6D3D1", "gunwale": "#D6D3D1",
       "hook": "#9A3412", "bamboo": "#CA8A04", "ferrule": "#57534E"}


def win(xc, yc, zc, sx, sy, sz):
    return Pos(xc, yc, zc) * Box(sx, sy, sz)


def A():
    return M.ring_half(P, +1)


def B():
    return M.ring_half(P, -1)


def crutch():
    r, w = M.crutch_roller(P)
    nut, scr = M.crutch_clamp(P)
    return {"frame": Compound([M.crutch_frame(P), nut]), "roller": r, "washers": w, "axle": M.crutch_axle(P),
            "clamp": scr, "gunwale": M.gunwale_context(P)}


# ------------------------------------------------------------------ overview
def overview():
    L = M.packed_layout(P)
    ring = Pos(220, -200, P["ear"][2] / 2)
    cr = crutch()
    cpos = Pos(1000, -200, P["saddle"][2] - P["saddle"][3])
    wpos = Pos(1330, -200, P["winder"][2] / 2 + 12)
    lk = M.lock_pins(P)
    parts = [
        Part("Rider ring, two halves with tang", ring * Compound([A(), B()]), COL["ring"], 1, (0, -150, 0)),
        Part("Hinge bolt M8 and nyloc nut", ring * M.hinge_bolt(P), COL["hinge"], 2, (-110, 0, 0)),
        Part("Gate pin 8 mm with R-clip", ring * M.gate_pin(P), COL["gate"], 3, (0, -100, 0)),
        Part("Pole head", L["head"], COL["head"], 4, (0, -120, 0)),
        Part("Shear pins, 2 mm aluminium wire (12)", L["spares"], COL["shear"], 5, (0, -60, 0)),
        Part("Pole sections (3)", L["poles"], COL["pole"], 6, (0, 0, 0)),
        Part("Joint sleeves (2)", L["sleeves"], COL["sleeve"], 7, (0, 0, 60)),
        Part("Pop rivets (4)", L["rivets"], COL["rivet"], 8, (0, 0, 100)),
        Part("Lock pins 6 mm (4)", L["locks"], COL["lock"], 9, (0, 0, 140)),
        Part("Grip cap", L["cap"], COL["cap"], 10, (120, 0, 0)),
        Part("Tether cord, 10 m", wpos * M.winder_cord(P), COL["tether"], 11, (0, 0, 70)),
        Part("Float winder", wpos * M.float_winder(P), COL["winder"], 12, (0, 0, 0)),
        Part("Spare pin tube", Pos(0, -40, 0) * L["spares"], COL["spares"], 13, (0, -60, 0)),
        Part("Jigging weight", L["weight"], COL["weight"], 14, (0, -120, 0)),
        Part("Gunwale crutch frame", cpos * cr["frame"], COL["cframe"], 15, (0, -150, 0)),
        Part("Crutch roller, washers and axle", cpos * Compound([cr["roller"], cr["washers"], cr["axle"]]), COL["roller"], 16, (0, -130, 90)),
        Part("Crutch clamp screw with pad", cpos * cr["clamp"], COL["clamp"], 17, (0, -300, 0)),
        Part("Hook head", L["hook"], COL["hook"], 21, (0, -120, 0)),
    ]
    _ = lk
    bv.overview(parts, OUT / "overview.png", "StumpRider: the kit, in build order",
                subtitle="Everything laid out as packed; small parts pulled clear. Plan, not yet built",
                elev=34, azim=-62, size=(11, 7.5), key=True)


# ------------------------------------------------------------------ making sketches
def sheets():
    t = M.tool_parts(P)
    ring = Compound([A(), B()])
    end_nb = [Part("Pole head and pins", Compound([t["head"], t["shear"], t["hinge"], t["gate"]]), "#D1D5DB")]
    bv.component_sheet(Part("Rider ring", ring, COL["ring"]), end_nb, "StumpRider", "SMR-DWG-101",
                       "Rider ring, two halves with ears and tang", "12 mm mild steel round bar; 6 mm flat bar",
                       ["Bend 12 bar round a 100 mm former into a full ring,",
                        "  112 mean diameter; saw across it to make two halves",
                        "  with a 2 mm gap at each joint.",
                        "Ears: four 6 x 25 x 42 flat bar, 8.5 hole 18 out from",
                        "  the bar centre; weld one to each end, holes in line.",
                        "Tang: 6 x 28 x 84 flat bar, welded on the outside of the",
                        "  fixed half midway between the joints, 4 below its top.",
                        "Tang holes 10.5, 6.5 and 2.1 at 20, 46 and 70 up,",
                        "  14 from the inner edge. Galvanise after welding.",
                        "Check: halves meet with 2 mm gaps, both holes line up."],
                       DATE, inset_view=(24, -50))
    bv.component_sheet(Part("Pole head", t["head"], COL["head"]),
                       [Part("Ring and pole", Compound([ring, M.pole_sections(P)[0] & win(XP, 0, 400, 200, 200, 600)]), "#D1D5DB")],
                       "StumpRider", "SMR-DWG-102", "Pole head (socket, end plate and fork)", "38 x 3 steel tube; 6 mm plate and flat bar",
                       ["Socket: 38 x 3 steel tube, 120 long, ends square.",
                        "End plate: 38 disc of 6 plate, welded across one end.",
                        "Cheeks: two 6 x 30 x 69 flat bar, welded under the plate,",
                        "  centred, 8 apart inside (use an 8 spacer while welding).",
                        "Drill the 2.1 shear pin hole through both cheeks",
                        "  together, 55 below the plate.",
                        "Drill 6.5 across the socket 60 above the plate.",
                        "Galvanise; paint the pin rating on the socket.",
                        "Check: the tang slides between the cheeks freely."],
                       DATE, inset_view=(20, -50))
    bv.component_sheet(Part("Shear pin", Rot(90, 0, 0) * Pos(-XP, 0, -P["shear_hole"][1]) * t["shear"], COL["shear"]),
                       [], "StumpRider", "SMR-DWG-103", "Shear pin (12, one fitted)", "2.0 mm soft aluminium wire, 1050 or 1100, O temper",
                       ["Cut 30 long from one reel of 2.0 soft aluminium wire;",
                        "  file the ends square, no burr.",
                        "Never use steel wire, a nail or a bolt: the pin is",
                        "  the safety device that limits the pull.",
                        "Before use, break ten pins from the reel on CalRig",
                        "  in a test fork: all must break 256 to 347 N.",
                        "Fit: push through cheek, tang and cheek; bend both",
                        "  ends over by hand to about 45 deg.",
                        "Keep eleven spares in the spare pin tube."],
                       DATE, inset_view=(24, -50),
                       view_shape=Rot(90, 0, 0) * Pos(-XP, 0, -P["shear_hole"][1]) * t["shear"])
    sec = M.pole_sections(P)[0]
    lay = Rot(0, 90, 0) * Pos(-XP, 0, -Z0)
    bv.component_sheet(Part("Pole section", lay * sec, COL["pole"]),
                       [Part("Sleeve", lay * M.sleeves(P)[0], "#D1D5DB")],
                       "StumpRider", "SMR-DWG-104", "Pole section (3)", "6063-T6 aluminium tube 32 x 2",
                       ["Cut three 1,450 lengths from one 6 m tube; deburr.",
                        "Bottom section: 6.5 hole across, 60 from the bottom",
                        "  (head lock pin); 4.9 hole across, 40 from the top.",
                        "Middle section: 6.5 hole 50 from the bottom (joint",
                        "  lock pin); 4.9 hole 40 from the top.",
                        "Top section: 6.5 hole 50 from the bottom; grip cap",
                        "  on the top end; paint the top 300 orange.",
                        "Drill each hole square through both walls.",
                        "Check: sections butt end to end in a sleeve."],
                       DATE, inset_view=(24, -50))
    slv = M.sleeves(P)[0]
    lays = Rot(0, 90, 0) * Pos(-XP, 0, -(J1 - 100))
    bv.component_sheet(Part("Joint sleeve", lays * slv, COL["sleeve"]),
                       [Part("Pole sections", lays * Compound([M.pole_sections(P)[0], M.pole_sections(P)[1]]) & win(100, 0, 0, 600, 100, 100), "#D1D5DB")],
                       "StumpRider", "SMR-DWG-105", "Joint sleeve (2)", "Aluminium tube 38 x 2.8 (32.4 inside)",
                       ["Cut two 200 lengths; deburr inside and out.",
                        "Inside must slide on the 32 pole by hand: if the tube",
                        "  is 38 x 3, open the bore with emery on a stick.",
                        "4.9 hole across, 60 from one end (rivets).",
                        "6.5 hole across, 150 from the same end (lock pin).",
                        "Fit: rivet end over the top of the section below,",
                        "  pushed on 100 so the hole meets its 4.9 hole;",
                        "  one rivet each side.",
                        "Check: next section slides in and the 6.5 holes meet."],
                       DATE, inset_view=(24, -50))
    bv.component_sheet(Part("Float winder", M.float_winder(P), COL["winder"]),
                       [Part("Cord", M.winder_cord(P), "#D1D5DB")],
                       "StumpRider", "SMR-DWG-106", "Float winder", "40 mm closed-cell polyethylene foam",
                       ["Cut 300 x 120 from 40 closed-cell foam (net float",
                        "  or packaging foam; not polystyrene).",
                        "Cut a 30 deep, 60 wide notch in each end.",
                        "Round the corners; paint orange.",
                        "Tie the cord's free end through a 6 hole near one",
                        "  notch and wind the 10 m lengthwise in the notches.",
                        "Floats the ring and cord with 2 times reserve;",
                        "  not the jigging weight.",
                        "Check: floats with the ring hung on it."],
                       DATE, inset_view=(30, -50))
    wt = Pos(-XP, 0, 0) * M.jig_weight(P)
    bv.component_sheet(Part("Jigging weight", wt, COL["weight"]),
                       [Part("Ring", Pos(-XP, 0, 0) * ring, "#D1D5DB")],
                       "StumpRider", "SMR-DWG-107", "Jigging weight", "50 mm mild steel round bar; 6 mm flat bar",
                       ["Saw 60 from 50 round bar; face both ends.",
                        "Cheeks: two 6 x 30 x 66 flat bar welded to one end",
                        "  face, centred, 8 apart inside (8 spacer).",
                        "Drill 6.5 through both cheeks together, 12 from",
                        "  their free ends.",
                        "Galvanise. Mass about 1.1 kg with its pin.",
                        "Fit: cheeks over the tang, 6 mm lock pin through",
                        "  the middle tang hole; only with the pole head off.",
                        "Check: the weight swings freely on its pin."],
                       DATE, inset_view=(20, -50))
    cr = crutch()
    nb = [Part("Roller, axle and gunwale", Compound([cr["roller"], cr["axle"], cr["gunwale"]]), "#D1D5DB")]
    bv.component_sheet(Part("Crutch frame", cr["frame"], COL["cframe"]), nb, "StumpRider", "SMR-DWG-108",
                       "Gunwale crutch frame (saddle and cheeks)", "4 mm steel plate; M10 nut",
                       ["Saddle: 4 plate 100 wide, bent to a U, 70 inside,",
                        "  legs 70 deep below the web.",
                        "Cheeks: two 60 x 70 of 4 plate, 13 hole 40 above the",
                        "  web; weld upright on the web, 84 apart inside.",
                        "Drill 11 in the inboard leg, 45 below the web, and",
                        "  weld an M10 nut over it outside.",
                        "Galvanise. Mark the inboard leg.",
                        "Check: slides over a 60 mm board; the axle bolt",
                        "  passes both cheek holes."],
                       DATE, inset_view=(24, -50))
    bv.component_sheet(Part("Roller", cr["roller"], COL["roller"]),
                       [Part("Frame", cr["frame"], "#D1D5DB")], "StumpRider", "SMR-DWG-109",
                       "Crutch roller", "HDPE rod 60 mm",
                       ["Saw 80 from 60 HDPE rod; face the ends square.",
                        "Bore 13 on the axis (drill 6 pilot, then 13).",
                        "Break the outer edges with a knife.",
                        "Fit: on an M12 x 110 bolt between the cheeks, a",
                        "  2 mm washer each side; nyloc nut snug, not tight.",
                        "Check: spins freely by hand with the nut done up."],
                       DATE, inset_view=(24, -50))
    bv.component_sheet(Part("Clamp screw", cr["clamp"], COL["clamp"]),
                       [Part("Frame and gunwale", Compound([cr["frame"], cr["gunwale"]]), "#D1D5DB")],
                       "StumpRider", "SMR-DWG-110", "Crutch clamp screw", "M10 threaded rod; 5 mm plate; 8 mm bar",
                       ["Cut 100 of M10 galvanised threaded rod.",
                        "Pad: 30 disc of 5 plate, welded square on one end.",
                        "Handle: 70 of 8 bar, welded across the other end.",
                        "Run the rod through the welded nut from outside,",
                        "  pad end first, before the crutch goes on the boat.",
                        "Fits gunwales 30 to 60 thick: tighten by hand only.",
                        "Check: pad bears flat on the gunwale side."],
                       DATE, inset_view=(24, -40))
    bv.component_sheet(Part("Hook head", M.hook_head(P), COL["hook"]),
                       [Part("Pole head and shear pin", Compound([t["head"], t["shear"]]), "#D1D5DB")],
                       "StumpRider", "SMR-DWG-111", "Hook head (for nets wrapped round a branch)",
                       "6 mm flat bar; 10 mm mild steel round bar",
                       ["Flat: 6 x 28 flat bar, 60 long. Drill 10.5 at 12",
                        "  and 2.1 at 50 from the bottom end, on the centre",
                        "  line (the same holes as the ring's tang).",
                        "Bar: about 220 of 10 round bar. Bend a J round a",
                        "  50 pipe in the vice: 30 bend radius to the bar",
                        "  centre, legs 60 apart, tip leg 35 long.",
                        "Weld the long leg 10 up the flat's bottom edge,",
                        "  both sides, in line with the flat. Galvanise.",
                        "Check: the fork slides over the flat freely and a",
                        "  2 rod passes cheek, flat and cheek."],
                       DATE, inset_view=(20, -50))
    bs = M.bamboo_sections(P)
    layb = Rot(0, 90, 0) * Pos(-XP, 0, -(J1 - 120))
    jw = win(XP, 0, J1, 80, 80, 260)
    bv.component_sheet(Part("Ferrule on the lower culm", layb * Compound([M.ferrules(P)[0], M.ferrule_bolts(P)[0], bs[0] & jw]), COL["ferrule"]),
                       [Part("Upper culm and lock pin", layb * Compound([bs[1] & jw, M.bamboo_lock_pins(P)[1]]), "#D1D5DB")],
                       "StumpRider", "SMR-DWG-112", "Bamboo local variant: culms and ferrule joint",
                       "Treated bamboo culm 36 mm; steel tube 40 x 1.5",
                       ["Culms: three straight 1,450 lengths, 34 to 38",
                        "  outside; top one cut just above a node. Soak in",
                        "  borax and boric acid; whip each end with wire.",
                        "Accept a culm only if 5 kg hung at the middle of",
                        "  a 1.4 m span sags 2.9 or less.",
                        "Bottom culm: dress the bottom 120 to 31.8 for the",
                        "  pole head; 6.5 hole 60 up. Ferrules: 160 of",
                        "  40 x 1.5 tube; 5.3 hole 40 and 6.5 hole 120 from",
                        "  one end. Set on the lower culm in epoxy with an",
                        "  M5 bolt; next culm slides in, 6 mm lock pin."],
                       DATE, inset_view=(24, -50))


# ------------------------------------------------------------------ joints
def joints():
    t = M.tool_parts(P)
    yh = P["ring_R"] + P["ear_hole_r"]
    w = win(0, yh - 10, 0, 70, 70, 50)
    bv.joint([Part("Fixed half (ear)", A() & w, COL["ring"]), Part("Swinging half (ear)", B() & w, COL["ring2"]),
              Part("Hinge bolt, nut and washer", M.hinge_bolt(P), COL["hinge"])],
             OUT / "joint-01.png", "Joint 1: the ring hinge",
             "Two ears face to face, 2 mm apart; M8 bolt through both, nyloc nut snug so the half still swings",
             elev=24, azim=-30)
    w = win(0, -yh + 10, 0, 70, 70, 50)
    bv.joint([Part("Fixed half (ear)", A() & w, COL["ring"]), Part("Swinging half (ear)", B() & w, COL["ring2"]),
              Part("Gate pin and R-clip", M.gate_pin(P), COL["gate"])],
             OUT / "joint-02.png", "Joint 2: the ring gate",
             "Clevis pin from the swinging side, R-clip on the fixed side; the lanyard keeps both on the ring",
             elev=24, azim=-150)
    w = win(XP, 0, 40, 80, 80, 110)
    bv.joint([Part("Fixed half of the ring", A() & w, COL["ring"]), Part("Tether bowline", t["tether"] & w, COL["tether"])],
             OUT / "joint-03.png", "Joint 3: tang welded to the ring; tether tied through the lowest hole",
             "Tang on the outside of the bar, welded both sides; bowline through the 10.5 mm hole, round the outer edge",
             elev=18, azim=-40)
    w = win(XP, 0, 100, 60, 60, 120)
    bv.joint([Part("Tang (cut)", A() & w, COL["ring"]), Part("Fork cheeks and end plate (cut)", t["head"] & w, COL["head"]),
              Part("Shear pin, ends bent", t["shear"], COL["shear"])],
             OUT / "joint-04.png", "Joint 4: fork on the tang, cut through the shear pin",
             "1 mm each side of the tang; 45 mm from the tang top to the plate, so push and pull both go through the pin",
             cut="+X", elev=12, azim=-160)
    zp = Z0 + P["head_pin_up"]
    w = win(XP, 0, zp - 20, 60, 60, 140)
    bv.joint([Part("Socket and end plate (cut)", t["head"] & w, COL["head"]),
              Part("Bottom pole section (cut)", M.pole_sections(P)[0] & w, COL["pole"]),
              Part("Lock pin 6 mm", M.lock_pins(P)[0], COL["lock"])],
             OUT / "joint-05.png", "Joint 5: pole in the head socket, cut",
             "Pole pushed in to the end plate; lock pin through socket and pole, R-clip on the far side",
             cut="+X", elev=12, azim=-160)
    w = win(XP, 0, J1, 60, 60, 220)
    bv.joint([Part("Bottom section (cut)", M.pole_sections(P)[0] & w, COL["pole"]),
              Part("Middle section (cut)", M.pole_sections(P)[1] & w, "#CBD5E1"),
              Part("Joint sleeve (cut)", M.sleeves(P)[0] & w, COL["sleeve"]),
              Part("Pop rivets", Compound(M.rivets(P)[:2]), COL["rivet"]),
              Part("Lock pin 6 mm", M.lock_pins(P)[1], COL["lock"])],
             OUT / "joint-06.png", "Joint 6: pole joint, cut",
             "Sleeve riveted to the section below; the section above butts on it and is held by the lock pin",
             cut="+X", elev=12, azim=-160)
    w = win(XP, 0, 70, 90, 90, 140)
    bv.joint([Part("Fixed half of the ring", A() & w, COL["ring"]), Part("Jigging weight", M.jig_weight(P), COL["weight"]),
              Part("Lock pin 6 mm", M.weight_pin(P), COL["lock"])],
             OUT / "joint-07.png", "Joint 7: jigging weight on the tang",
             "Pole head off; weight cheeks over the tang, lock pin through the middle hole",
             elev=18, azim=-40)
    cr = crutch()
    bv.joint([Part("Crutch frame (cut)", cr["frame"], COL["cframe"]), Part("Clamp screw and pad (cut)", cr["clamp"], COL["clamp"]),
              Part("Gunwale, 40 mm (cut)", cr["gunwale"] & win(0, 0, -60, 400, 400, 200), COL["gunwale"]),
              Part("Roller (cut)", cr["roller"], COL["roller"])],
             OUT / "joint-08.png", "Joint 8: crutch on the gunwale, cut across",
             "Web on the gunwale top, outboard leg against the outside; the pad clamps the inboard face",
             cut="+X", elev=10, azim=-170)
    bv.joint([Part("Cheeks (cut)", cr["frame"] & win(0, 0, 44, 120, 80, 80), COL["cframe"]),
              Part("Roller (cut)", cr["roller"], COL["roller"]), Part("Washers", cr["washers"], COL["hinge"]),
              Part("Axle bolt and nyloc nut", cr["axle"], COL["clamp"])],
             OUT / "joint-09.png", "Joint 9: roller on its axle, cut",
             "2 mm washer each side; nyloc nut snug so the roller spins and the cheeks are not pulled in",
             cut="+Y", elev=14, azim=-80)
    w = win(XP, 0, 60, 70, 70, 140)
    bv.joint([Part("Hook head flat (cut)", M.hook_head(P) & w, COL["hook"]),
              Part("Fork cheeks and end plate (cut)", t["head"] & w, COL["head"]),
              Part("Shear pin, ends bent", t["shear"], COL["shear"])],
             OUT / "joint-10.png", "Joint 10: fork on the hook head, cut through the shear pin",
             "Same fork, same calibrated pin as on the ring; the flat's top stops 45 mm short of the plate",
             cut="+X", elev=12, azim=-160)
    bs = M.bamboo_sections(P)
    w = win(XP, 0, J1, 70, 70, 220)
    bv.joint([Part("Lower culm (cut)", bs[0] & w, COL["bamboo"]),
              Part("Upper culm (cut)", bs[1] & w, "#FDE68A"),
              Part("Ferrule (cut)", M.ferrules(P)[0] & w, COL["ferrule"]),
              Part("M5 bolt and nyloc nut", M.ferrule_bolts(P)[0], COL["rivet"]),
              Part("Lock pin 6 mm", M.bamboo_lock_pins(P)[1], COL["lock"])],
             OUT / "joint-11.png", "Joint 11: bamboo local variant, ferrule joint, cut",
             "Ferrule set on the lower culm with epoxy and an M5 bolt; the upper culm butts on it and is held by the lock pin",
             cut="+X", elev=12, azim=-160)


# ------------------------------------------------------------------ steps
def steps():
    t = M.tool_parts(P)
    a = Part("Fixed half", A(), COL["ring"])
    b = Part("Swinging half", B(), COL["ring2"], None, (-70, 0, 0))
    hb = Part("Hinge bolt and nut", M.hinge_bolt(P), COL["hinge"], None, (-80, 0, 0))
    gp = Part("Gate pin and R-clip", M.gate_pin(P), COL["gate"], None, (-80, 0, 0))
    seq = []
    bv.step([a], [b, hb], OUT / "step-01.png", "Step 1: hinge the two ring halves",
            "Ears face to face at the +Y joint; M8 bolt through both, nyloc nut snug", elev=26, azim=-60)
    b0 = Part("Swinging half", B(), "#D1D5DB")
    hb0 = Part("Hinge bolt", M.hinge_bolt(P), "#D1D5DB")
    bv.step([a, b0, hb0], [gp], OUT / "step-02.png", "Step 2: close the gate with the gate pin",
            "Pin in from the swinging side, R-clip on; tie the lanyard through the clip and the ear", elev=26, azim=-130)
    ring_done = [Part("Rider ring", Compound([A(), B(), M.hinge_bolt(P), M.gate_pin(P)]), "#D1D5DB")]
    knot = Part("Tether cord, bowline", t["tether"], COL["tether"], None, (80, 0, 60))
    bv.step(ring_done, [knot], OUT / "step-03.png", "Step 3: tie the tether to the tang",
            "Bowline through the lowest tang hole; wind the rest on the float winder; tie its end to a thwart in use",
            elev=20, azim=-40)
    w1 = win(XP, 0, J1 - 60, 80, 80, 260)
    s1 = Part("Bottom section", M.pole_sections(P)[0] & w1, COL["pole"])
    sl = Part("Joint sleeve", M.sleeves(P)[0], COL["sleeve"], None, (0, 0, 160))
    rvt = Part("Pop rivets", Compound(M.rivets(P)[:2]), COL["rivet"], None, (0, 0, 160))
    bv.step([s1], [sl, rvt], OUT / "step-04.png", "Step 4: rivet a sleeve on the top of the bottom and middle sections",
            "Push the sleeve on 100 mm until the holes meet; one rivet each side", elev=18, azim=-50)
    w0 = win(XP, 0, Z0 + 150, 80, 80, 300)
    hd = Part("Pole head", t["head"], COL["head"], None, (0, 0, -150))
    pin0 = Part("Lock pin", M.lock_pins(P)[0], COL["lock"], None, (0, -90, 0))
    bv.step([Part("Bottom section", M.pole_sections(P)[0] & w0, COL["pole"])], [hd, pin0], OUT / "step-05.png",
            "Step 5: fit the pole head to the bottom section",
            "Head on until the pole meets the end plate; lock pin through, R-clip on", elev=18, azim=-50)
    s2 = Part("Middle section", M.pole_sections(P)[1] & w1, "#CBD5E1", None, (0, 0, 160))
    pin1 = Part("Lock pin", M.lock_pins(P)[1], COL["lock"], None, (0, -90, 0))
    bv.step([Part("Bottom section and sleeve", Compound([M.pole_sections(P)[0] & w1, M.sleeves(P)[0], *M.rivets(P)[:2]]), COL["pole"])],
            [s2, pin1], OUT / "step-06.png", "Step 6: join the sections",
            "Middle section into the sleeve until it butts; lock pin through; the same for the top section, then the grip cap",
            elev=18, azim=-50)
    end = Compound([t["head"], M.pole_sections(P)[0] & w0, M.lock_pins(P)[0]])
    pole_end = Part("Pole with head", end, COL["head"], None, (0, 0, 120))
    sh = Part("Shear pin", t["shear"], COL["shear"], None, (0, -60, 0))
    bv.step(ring_done, [pole_end, sh], OUT / "step-07.png", "Step 7: put the fork on the tang and fit the shear pin",
            "Line up the 2.1 mm holes, push the pin through, bend both ends over by hand", elev=18, azim=-50)
    cr = crutch()
    fr = Part("Crutch frame", cr["frame"], "#D1D5DB")
    ro = Part("Roller and washers", Compound([cr["roller"], cr["washers"]]), COL["roller"], None, (0, 0, 90))
    ax = Part("Axle bolt and nut", cr["axle"], COL["clamp"], None, (-140, 0, 0))
    bv.step([fr], [ro, ax], OUT / "step-08.png", "Step 8: fit the roller between the cheeks",
            "Washer each side, bolt through, nyloc nut snug; the roller must spin", elev=22, azim=-55)
    cl = Part("Clamp screw with pad", cr["clamp"], COL["clamp"], None, (0, -120, 0))
    rdone = Part("Roller and axle", Compound([cr["roller"], cr["washers"], cr["axle"]]), "#D1D5DB")
    bv.step([fr, rdone], [cl], OUT / "step-09.png", "Step 9: run the clamp screw into the welded nut",
            "From outside the inboard leg, pad end first", elev=22, azim=-130)
    cdone = Part("Crutch", Compound([cr["frame"], cr["roller"], cr["washers"], cr["axle"], cr["clamp"]]), COL["cframe"], None, (0, 0, 160))
    bv.step([], [cdone], OUT / "step-10.png", "Step 10: clamp the crutch on the gunwale",
            "Near the bow, where the operator kneels; outboard leg on the outside, tighten the screw by hand",
            context=[Part("Gunwale and top plank (context)", cr["gunwale"], COL["gunwale"])], elev=22, azim=-130)
    wt = Part("Jigging weight", M.jig_weight(P), COL["weight"], None, (0, 0, 120))
    wp = Part("Lock pin", M.weight_pin(P), COL["lock"], None, (0, -80, 0))
    bv.step(ring_done + [Part("Tether", t["tether"] & win(100, 0, 60, 200, 200, 200), "#D1D5DB")], [wt, wp], OUT / "step-11.png",
            "Step 11: for deep snags, pin the jigging weight to the tang",
            "Pole head off first; weight cheeks over the tang, lock pin through the middle hole", elev=18, azim=-50)
    hk = Part("Hook head", M.hook_head(P), COL["hook"], None, (0, 0, -150))
    sh2 = Part("Shear pin", t["shear"], COL["shear"], None, (0, -60, 0))
    kn = Part("Tether bowline, moved across", M.hook_knot(P), COL["tether"], None, (80, 0, 0))
    bv.step([Part("Pole head", Compound([t["head"], M.pole_sections(P)[0] & w0, M.lock_pins(P)[0]]), "#D1D5DB")],
            [hk, sh2, kn], OUT / "step-12.png", "Step 12: for a net wrapped round a branch, pin on the hook head",
            "Draw the pin, lift the fork off the ring, put it over the hook head, fit a calibrated pin; move the tether across",
            elev=18, azim=-50)
    _ = seq


if __name__ == "__main__":
    what = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    for w in what:
        globals()[w]()
        print("done", w)
