"""StumpRider parametric model (build123d), TRL 3, constructable design (SMR-DDR-002, SMR-DDR-003).

Run from the repo root:  python cad/src/model.py [--check] [--export]
  --check   run the constructability checks (overlaps, contacts, clearances, pin paths)
  --export  write cad/step/*.step and cad/stl/*.stl

StumpRider is a hand tool for freeing a gillnet snagged on a drowned tree, worked from the canoe.
A hinged steel rider ring closes round the net line and is pushed down onto the snag by a
three-section aluminium pole. The pole head grips a tang on the ring with a forked end and a
2 mm soft aluminium shear pin, so the pole lets go before the pull can heel the canoe too far.
A tether cord on a floating winder brings the ring back; a jigging weight pinned to the tang
works snags beyond pole reach; a clamp-on gunwale crutch with a roller guides the net line.

Coordinates in mm. Working end at the origin: the ring lies in the XY plane, centred on the
net line, which runs along Z. The tang stands up from the ring on the +X side, and the pole
axis runs up the tang centre line at x = 72. The ring is hinged on the +Y side and opens on
the -Y side. The gunwale crutch has its own frame: gunwale along X, roller axis along X,
saddle web top at z = 4.

Kit (BOM line numbers in brackets, see bom/bom.csv):
  [1]  rider ring, two halves of 12 mm steel bar with ears; tang on the fixed half
  [2]  hinge bolt M8 x 30 with nyloc nut
  [3]  gate pin, 8 mm clevis pin with R-clip and lanyard
  [4]  pole head: socket tube, end plate and fork cheeks, welded
  [5]  shear pins, 2 mm soft aluminium wire, 30 mm long (one fitted, spares in [13])
  [6]  pole sections, aluminium tube 32 x 2, three of 1,450 mm
  [7]  joint sleeves, aluminium tube 38 x 2.8, two of 200 mm
  [8]  pop rivets 4.8 mm stainless, four
  [9]  lock pins, 6 mm clevis pins with R-clips, four (two joints, head, weight)
  [10] grip cap, rubber, for 32 mm tube
  [11] tether cord, 6 mm braided polyester, 10 m
  [12] float winder, 40 mm closed-cell polyethylene foam
  [13] spare pin tube with cap
  [14] jigging weight: 50 mm steel bar with fork cheeks
  [15] gunwale crutch frame: saddle and cheeks, 4 mm steel plate, welded
  [16] crutch roller, HDPE, with M12 axle bolt, washers and nyloc nut
  [17] crutch clamp screw: M10 T-handle screw, welded nut and pad
  [21] hook head: 10 mm steel bar hook on a 6 x 28 flat that pins into the same fork (SMR-DDR-003)

Bamboo local variant (SMR-DDR-003, bom/bom-bamboo-variant.csv): three treated bamboo culm sections,
36 mm outside, in place of the aluminium sections [6], sleeves [7], rivets [8] and grip cap [10],
joined by two steel ferrules 40 x 1.5 x 160 fixed with M5 bolts. The bottom 120 mm of the lowest
culm is dressed to slide into the same pole head. Everything else is shared with the prototype kit.
CONCEPT, NOT FOR FABRICATION.
"""
import math
import sys
from pathlib import Path

from build123d import (Box, Compound, Cylinder, Pos, Rot, Torus, Vector, export_step, export_stl)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = {
    # rider ring
    "ring_R": 56.0,          # mean radius of the bar (inside diameter 100)
    "bar_d": 12.0,           # round bar
    "split_gap": 2.0,        # gap between the two halves at each joint
    "ear": (6.0, 30.0, 25.0),   # ear plate: thickness, radial length from bar centre, height
    "ear_hole_r": 18.0,      # bolt hole centre, radially out from the bar centre
    "hinge_d": 8.0,          # hinge bolt and gate pin diameter
    # tang
    "tang": (28.0, 6.0, 84.0),  # width (radial), thickness, height (z from -4 to 80)
    "tang_x0": 58.0,         # inner edge of the tang
    "tether_hole": (10.5, 20.0),   # diameter, height
    "weight_hole": (6.5, 46.0),
    "shear_hole": (2.1, 70.0),
    # pole head
    "cheek": (30.0, 6.0),    # fork cheek width (X), thickness
    "cheek_gap": 8.0,        # inside the fork (tang 6, 1 mm each side)
    "cheek_z": (56.0, 125.0),
    "plate_t": 6.0,          # socket end plate
    "socket": (38.0, 3.0, 120.0),  # OD, wall, length
    "head_pin_up": 60.0,     # lock pin above the end plate
    # shear pin
    "shear_d": 2.0,
    "shear_len": 30.0,
    # pole
    "pole": (32.0, 2.0),     # OD, wall
    "section_L": 1450.0,
    "n_sections": 3,
    "sleeve": (38.0, 2.8, 200.0),   # OD, wall, length (inside 32.4: slide fit on the pole)
    "sleeve_pin_up": 50.0,   # lock pin above the joint line
    "rivet_down": 40.0,      # rivets below the joint line
    "rivet_d": 4.8,
    "lock_d": 6.0,
    "cap": (36.0, 30.0),     # grip cap OD, depth over the tube
    # jigging weight (pinned to the tang at the weight hole instead of the pole head)
    "weight_d": 50.0,
    "weight_L": 60.0,
    "wcheek_z": (34.0, 100.0),
    # tether and float winder
    "cord_d": 6.0,
    "cord_L": 10000.0,
    "winder": (300.0, 120.0, 40.0),  # foam winder length, width, thickness
    "notch": (30.0, 60.0),           # end notch depth, width
    # gunwale crutch
    "saddle": (100.0, 70.0, 70.0, 4.0),   # length along gunwale, inside width, leg depth, plate
    "ccheek": (60.0, 70.0),               # cheek width across the gunwale, height above the web
    "roller": (60.0, 80.0, 13.0),         # OD, length, bore
    "axle_z": 40.0,                        # axle height above the web top
    "clamp_z": -45.0,                      # clamp screw height
    "gunwale": (60.0, 40.0),               # design gunwale thickness range: max 60, min 30 (context 40)
    # hook head (SMR-DDR-003): pins into the pole head's fork in place of the ring's tang
    "hook_flat_z": (20.0, 80.0),           # 6 x 28 flat, same width and thickness as the tang
    "hook_tether_z": 32.0,                 # 10.5 mm tether hole (the tether's bowline is moved across)
    "hook_bar_d": 10.0,
    "hook_R": 30.0,                        # bend radius to the bar centre (throat 50 mm clear)
    "hook_shank_z": -60.0,                 # bend centre height
    "hook_tip_z": -25.0,                   # top of the tip leg
    # bamboo local variant (SMR-DDR-003)
    "culm": (36.0, 6.0),                   # bamboo culm outside diameter, wall (selected culms)
    "spigot": (31.8, 120.0),               # bottom of the lowest culm dressed to this diameter and length
    "ferrule": (40.0, 1.5, 160.0),         # steel tube OD, wall, length (37 inside)
    "ferrule_bolt_down": 40.0,             # M5 bolt below the joint line
    "ferrule_pin_up": 40.0,                # lock pin above the joint line
}

X_POLE = PARAMS["tang_x0"] + PARAMS["tang"][0] / 2      # 72: pole axis


def derived(p=PARAMS):
    d = {}
    s0 = p["cheek_z"][1] + p["plate_t"]                   # pole bottom (on the end plate)
    d["pole_z0"] = s0
    d["joints"] = [s0 + p["section_L"] * (i + 1) for i in range(p["n_sections"] - 1)]
    d["pole_top"] = s0 + p["section_L"] * p["n_sections"]
    d["tool_len"] = d["pole_top"] + p["cap"][1] * 0 + 5 + p["ring_R"] + p["bar_d"] / 2   # ring outer edge to cap top
    d["hand_to_ring"] = d["pole_top"] - 300.0             # top hand 300 mm below the cap
    d["packed_L"] = p["section_L"] + p["sleeve"][2] / 2   # a section with its sleeve
    d["ring_ID"] = 2 * p["ring_R"] - p["bar_d"]
    d["ring_OD"] = 2 * p["ring_R"] + p["bar_d"]
    return d


# ------------------------------------------------------------------ helpers
def rod(a, b, r):
    """Cylinder of radius r from point a to point b."""
    a, b = Vector(*a), Vector(*b)
    v = b - a
    L = v.length
    c = Cylinder(r, L)
    z = Vector(0, 0, 1)
    n = v.normalized()
    ax = z.cross(n)
    if ax.length < 1e-9:
        rot = c if n.Z > 0 else Rot(180, 0, 0) * c
    else:
        ang = math.degrees(math.acos(max(-1.0, min(1.0, z.dot(n)))))
        from build123d import Axis, Location
        rot = c.rotate(Axis((0, 0, 0), (ax.X, ax.Y, ax.Z)), ang)
    m = (a + b) * 0.5
    return Pos(m.X, m.Y, m.Z) * rot


def ycyl(r, y0, y1, x, z):
    """Cylinder along Y from y0 to y1 through (x, z)."""
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(r, abs(y1 - y0))


def xcyl(r, x0, x1, y, z):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(r, abs(x1 - x0))


def zcyl(r, z0, z1, x=0.0, y=0.0):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(r, z1 - z0)


def ztube(ro, ri, z0, z1, x=0.0, y=0.0):
    return zcyl(ro, z0, z1, x, y) - zcyl(ri, z0 - 1, z1 + 1, x, y)


# ------------------------------------------------------------------ rider ring
def ring_half(p=PARAMS, side=+1):
    """side +1: the fixed half (x > 0) with the tang; -1: the swinging half (x < 0).
    Each half carries an ear at each end (hinge at +Y, gate at -Y)."""
    R, rb = p["ring_R"], p["bar_d"] / 2
    g = p["split_gap"] / 2
    big = 4 * R
    keep = Pos(side * (big / 2 + g), 0, 0) * Box(big, big, big)
    half = Torus(R, rb) & keep
    et, el, eh = p["ear"]
    for sy in (+1, -1):
        x0 = side * g
        ear = Pos(x0 + side * et / 2, sy * (R + el / 2 - 6), 0) * Box(et, el + 12, eh)
        hole = xcyl(p["hinge_d"] / 2 + 0.25, -50, 50, sy * (R + p["ear_hole_r"]), 0)
        half = half + (ear - hole)
    if side > 0:
        tw, tt, th = p["tang"]
        tang = Pos(p["tang_x0"] + tw / 2, 0, -4 + th / 2) * Box(tw, tt, th)
        for dia, z in (p["tether_hole"], p["weight_hole"], p["shear_hole"]):
            xh = X_POLE
            tang = tang - ycyl(dia / 2, -10, 10, xh, z)
        half = half + tang
    return half


def hinge_bolt(p=PARAMS):
    R, et = p["ring_R"], p["ear"][0]
    y, r = R + p["ear_hole_r"], p["hinge_d"] / 2
    g = p["split_gap"] / 2
    xo = g + et
    shank = xcyl(r, -xo, xo + 10, y, 0)
    head = xcyl(6.5, -xo - 5.3, -xo, y, 0)
    nut = xcyl(6.5, xo, xo + 8, y, 0) - xcyl(r, xo - 1, xo + 9, y, 0)
    return Compound([shank, head, nut])


def gate_pin(p=PARAMS):
    R, et = p["ring_R"], p["ear"][0]
    y, r = -(R + p["ear_hole_r"]), p["hinge_d"] / 2
    xo = p["split_gap"] / 2 + et
    shank = xcyl(r, -xo, xo + 12, y, 0)
    head = xcyl(6.0, -xo - 3, -xo, y, 0)
    clip = Pos(xo + 7, y, 0) * Rot(0, 90, 0) * Torus(6.0, 0.9)   # R-clip, drawn as a ring
    return Compound([shank, head, clip - xcyl(r + 0.1, xo, xo + 14, y, 0)])


# ------------------------------------------------------------------ pole head and pins
def pole_head(p=PARAMS):
    cw, ct = p["cheek"]
    z0, z1 = p["cheek_z"]
    gi = p["cheek_gap"] / 2
    sd, sh = p["shear_hole"]
    cheeks = []
    for sy in (+1, -1):
        c = Pos(X_POLE, sy * (gi + ct / 2), (z0 + z1) / 2) * Box(cw, ct, z1 - z0)
        cheeks.append(c - ycyl(sd / 2, -20, 20, X_POLE, sh))
    od, wall, L = p["socket"]
    zp = z1 + p["plate_t"]
    plate = zcyl(od / 2, z1, zp, X_POLE)
    sock = ztube(od / 2, od / 2 - wall, zp, zp + L, X_POLE)
    sock = sock - ycyl(p["lock_d"] / 2 + 0.25, -30, 30, X_POLE, zp + p["head_pin_up"])
    s = plate
    for c in cheeks:
        s = s + c
    return s + sock


def shear_pin(p=PARAMS):
    _, z = p["shear_hole"]
    L = p["shear_len"]
    return ycyl(p["shear_d"] / 2, -L / 2, L / 2, X_POLE, z)


def clevis(z, p=PARAMS, x=X_POLE, half=19.0):
    """6 mm clevis pin along Y through a tube of outer radius `half`, head on -Y."""
    r = p["lock_d"] / 2
    shank = ycyl(r, -half, half + 8, x, z)
    head = ycyl(5.0, -half - 2.5, -half, x, z)
    return Compound([shank, head])


# ------------------------------------------------------------------ pole
def pole_sections(p=PARAMS):
    d = derived(p)
    od, wall = p["pole"]
    out = []
    z = d["pole_z0"]
    for i in range(p["n_sections"]):
        s = ztube(od / 2, od / 2 - wall, z, z + p["section_L"], X_POLE)
        holes = []
        if i == 0:
            holes.append(z + p["head_pin_up"])                          # head lock pin
        if i < p["n_sections"] - 1:
            jz = z + p["section_L"]
            holes += [jz - p["rivet_down"]]                              # rivets (sleeve fixed here)
        if i > 0:
            jz = z
            holes.append(jz + p["sleeve_pin_up"])                       # lock pin into this section
        for hz in holes:
            dia = p["rivet_d"] + 0.1 if (i < p["n_sections"] - 1 and abs(hz - (z + p["section_L"] - p["rivet_down"])) < 1e-6) else p["lock_d"] + 0.5
            s = s - ycyl(dia / 2, -30, 30, X_POLE, hz)
        out.append(s)
        z += p["section_L"]
    return out


def sleeves(p=PARAMS):
    d = derived(p)
    od, wall, L = p["sleeve"]
    out = []
    for jz in d["joints"]:
        s = ztube(od / 2, od / 2 - wall, jz - L / 2, jz + L / 2, X_POLE)
        s = s - ycyl(p["rivet_d"] / 2 + 0.05, -30, 30, X_POLE, jz - p["rivet_down"])
        s = s - ycyl(p["lock_d"] / 2 + 0.25, -30, 30, X_POLE, jz + p["sleeve_pin_up"])
        out.append(s)
    return out


def rivets(p=PARAMS):
    d = derived(p)
    od_s = p["sleeve"][0] / 2
    ri = p["pole"][0] / 2 - p["pole"][1]
    r = p["rivet_d"] / 2
    out = []
    for jz in d["joints"]:
        z = jz - p["rivet_down"]
        for sy in (+1, -1):
            a, b = sy * (ri - 1.0), sy * od_s
            shank = ycyl(r, min(a, b), max(a, b), X_POLE, z)
            hy0, hy1 = sorted((sy * od_s, sy * (od_s + 1.5)))
            head = ycyl(4.75, hy0, hy1, X_POLE, z)
            out.append(Compound([shank, head]))
    return out


def lock_pins(p=PARAMS):
    d = derived(p)
    pins = [clevis(d["pole_z0"] + p["head_pin_up"], p)]
    pins += [clevis(jz + p["sleeve_pin_up"], p) for jz in d["joints"]]
    return pins


def grip_cap(p=PARAMS):
    d = derived(p)
    od, depth = p["cap"]
    top = d["pole_top"]
    return ztube(od / 2, p["pole"][0] / 2, top - depth, top, X_POLE) + zcyl(od / 2, top, top + 5, X_POLE)


# ------------------------------------------------------------------ tether, float winder, spare pins
def tether_knot(p=PARAMS, z=None, tail=True):
    """Bowline loop through the tether hole and round the tang's outer edge, and the first 0.4 m of cord."""
    if z is None:
        _, z = p["tether_hole"]
    rc = p["cord_d"] / 2
    xe = p["tang_x0"] + p["tang"][0]                      # outer edge of the tang, 86
    cx = (X_POLE - 2 + xe + rc + 1.5) / 2
    Rl = (xe + rc + 1.5 - (X_POLE - 2)) / 2
    loop = Pos(cx, 0, z) * Torus(Rl, rc)
    if not tail:
        return loop
    tail = rod((xe + 4.5, 0, z + 2), (150, 0, 420), rc)
    return Compound([loop, tail])


def float_winder(p=PARAMS):
    L, W, T = p["winder"]
    nd, nw = p["notch"]
    w = Box(L, W, T)
    for sx in (+1, -1):
        w = w - Pos(sx * (L / 2 - nd / 2 + 0.5), 0, 0) * Box(nd + 1, nw, T + 2)
    return w


def winder_cord(p=PARAMS):
    """The cord wound lengthwise round the winder through the end notches (one block of turns)."""
    L, W, T = p["winder"]
    nd, nw = p["notch"]
    t = 12.0
    inner_L = L - 2 * nd
    band = Box(inner_L + 2 * t, nw - 10, T + 2 * t) - Box(inner_L, nw, T)
    return band


def spare_tube(p=PARAMS):
    return zcyl(7.0, 0, 70) + zcyl(8.0, 70, 82)


# ------------------------------------------------------------------ jigging weight
def jig_weight(p=PARAMS):
    cw, ct = p["cheek"]
    z0, z1 = p["wcheek_z"]
    gi = p["cheek_gap"] / 2
    hd, hz = p["weight_hole"]
    s = zcyl(p["weight_d"] / 2, z1, z1 + p["weight_L"], X_POLE)
    for sy in (+1, -1):
        c = Pos(X_POLE, sy * (gi + ct / 2), (z0 + z1) / 2) * Box(cw, ct, z1 - z0)
        s = s + (c - ycyl(p["lock_d"] / 2 + 0.25, -20, 20, X_POLE, hz))
    return s


def weight_pin(p=PARAMS):
    return clevis(p["weight_hole"][1], p, half=10.0)


# ------------------------------------------------------------------ gunwale crutch (own frame)
def crutch_frame(p=PARAMS):
    L, wi, leg, t = p["saddle"]
    cwid, ch = p["ccheek"]
    web = Pos(0, 0, t / 2) * Box(L, wi + 2 * t, t)
    legs = [Pos(0, sy * (wi / 2 + t / 2), -leg / 2 + t / 2) * Box(L, t, leg + t) for sy in (+1, -1)]
    rl = p["roller"][1]
    xc = rl / 2 + 2.0 + t / 2                                     # 2 mm washer each side
    cheeks = [Pos(sx * xc, 0, t + ch / 2) * Box(t, cwid, ch) for sx in (+1, -1)]
    s = web
    for q in legs + cheeks:
        s = s + q
    s = s - xcyl(6.5, -80, 80, 0, t + p["axle_z"])
    s = s - ycyl(5.5, -wi / 2 - t - 1, -wi / 2 + 1, 0, p["clamp_z"])     # clamp screw hole, inboard leg (-Y)
    return s


def crutch_roller(p=PARAMS):
    od, L, bore = p["roller"]
    t = p["saddle"][3]
    z = t + p["axle_z"]
    r = xcyl(od / 2, -L / 2, L / 2, 0, z) - xcyl(bore / 2, -L, L, 0, z)
    washers = [xcyl(12.0, sx * L / 2, sx * (L / 2 + 2.0), 0, z) - xcyl(6.5, -L, L, 0, z) for sx in (+1, -1)]
    return r, Compound(washers)


def crutch_axle(p=PARAMS):
    t = p["saddle"][3]
    z = t + p["axle_z"]
    xo = p["roller"][1] / 2 + 2.0 + t
    shank = xcyl(6.0, -xo, xo + 12, 0, z)
    head = xcyl(9.5, -xo - 7.5, -xo, 0, z)
    nut = xcyl(9.5, xo, xo + 10, 0, z) - xcyl(6.0, xo - 1, xo + 11, 0, z)
    return Compound([shank, head, nut])


def crutch_clamp(p=PARAMS, gunwale_t=None):
    """M10 screw through a nut welded on the inboard leg, pad on the gunwale face, T-handle outside."""
    L, wi, leg, t = p["saddle"]
    gt = gunwale_t if gunwale_t is not None else p["gunwale"][1]
    z = p["clamp_z"]
    y_leg_in = -wi / 2                                   # inner face of the inboard leg
    y_pad = wi / 2 - gt                                  # gunwale's inboard face (gunwale against the outboard leg)
    nut = ycyl(9.5, y_leg_in - t - 8, y_leg_in - t, 0, z) - ycyl(5.0, -200, 200, 0, z)
    pad = ycyl(15.0, y_pad - 5, y_pad, 0, z)
    screw = ycyl(5.0, y_leg_in - t - 30, y_pad - 5, 0, z)
    handle = Pos(0, y_leg_in - t - 30 - 4, z) * Rot(0, 90, 0) * Cylinder(4.0, 70)
    return Compound([nut]), Compound([screw, pad, handle])


def gunwale_context(p=PARAMS, gunwale_t=None, length=400.0):
    L, wi, leg, t = p["saddle"]
    gt = gunwale_t if gunwale_t is not None else p["gunwale"][1]
    y1 = wi / 2
    top = Pos(0, y1 - gt / 2, -60) * Box(length, gt, 120)
    plank = Pos(0, y1 + 10, -200) * Box(length, 20, 220)
    return top + plank


def net_line(z0=-300.0, z1=1200.0, d=10.0):
    return zcyl(d / 2, z0, z1)


# ------------------------------------------------------------------ hook head (SMR-DDR-003)
def hook_head(p=PARAMS):
    """A 6 x 28 flat like the tang, with tether and shear pin holes, and a 10 mm bar bent into a J
    below it. Pins into the pole head's fork in place of the ring; pulls a wrapped bight back round
    the branch. The J opens towards -X (towards the operator's side of the pole)."""
    tw, tt, _ = p["tang"]
    z0, z1 = p["hook_flat_z"]
    flat = Pos(X_POLE, 0, (z0 + z1) / 2) * Box(tw, tt, z1 - z0)
    rb = p["hook_bar_d"] / 2
    R, zc, zt = p["hook_R"], p["hook_shank_z"], p["hook_tip_z"]
    shank = zcyl(rb, zc, z0 + 10, X_POLE)                       # welded 10 mm up the flat's lower edge
    big = 4 * R
    bend = Pos(X_POLE - R, 0, zc) * Rot(90, 0, 0) * Torus(R, rb)
    bend = bend & (Pos(X_POLE - R, 0, zc - big / 2) * Box(big, big, big))
    tip = zcyl(rb, zc, zt, X_POLE - 2 * R)
    h = flat + shank + bend + tip
    h = h - ycyl(p["tether_hole"][0] / 2, -10, 10, X_POLE, p["hook_tether_z"])
    h = h - ycyl(p["shear_hole"][0] / 2, -10, 10, X_POLE, p["shear_hole"][1])
    return h


def hook_knot(p=PARAMS):
    """The tether's bowline moved to the hook head's tether hole (loop only)."""
    return tether_knot(p, z=p["hook_tether_z"], tail=False)


def hook_throat(p=PARAMS):
    """Clear opening of the J between the shank and the tip."""
    return 2 * p["hook_R"] - p["hook_bar_d"]


# ------------------------------------------------------------------ bamboo local variant (SMR-DDR-003)
def bamboo_sections(p=PARAMS):
    d = derived(p)
    od, wall = p["culm"]
    ri = od / 2 - wall
    sd, sl = p["spigot"]
    out = []
    z = d["pole_z0"]
    for i in range(p["n_sections"]):
        if i == 0:
            s = ztube(sd / 2, ri, z, z + sl, X_POLE) + ztube(od / 2, ri, z + sl, z + p["section_L"], X_POLE)
            s = s - ycyl(p["lock_d"] / 2 + 0.25, -30, 30, X_POLE, z + p["head_pin_up"])
        else:
            s = ztube(od / 2, ri, z, z + p["section_L"], X_POLE)
            s = s - ycyl(p["lock_d"] / 2 + 0.25, -30, 30, X_POLE, z + p["ferrule_pin_up"])
        if i < p["n_sections"] - 1:
            s = s - ycyl(2.65, -30, 30, X_POLE, z + p["section_L"] - p["ferrule_bolt_down"])
        out.append(s)
        z += p["section_L"]
    return out


def ferrules(p=PARAMS):
    d = derived(p)
    od, wall, L = p["ferrule"]
    out = []
    for jz in d["joints"]:
        s = ztube(od / 2, od / 2 - wall, jz - L / 2, jz + L / 2, X_POLE)
        s = s - ycyl(2.65, -30, 30, X_POLE, jz - p["ferrule_bolt_down"])
        s = s - ycyl(p["lock_d"] / 2 + 0.25, -30, 30, X_POLE, jz + p["ferrule_pin_up"])
        out.append(s)
    return out


def ferrule_bolts(p=PARAMS):
    """M5 stainless bolt and nyloc nut through ferrule and culm (set in epoxy)."""
    d = derived(p)
    ro = p["ferrule"][0] / 2
    out = []
    for jz in d["joints"]:
        z = jz - p["ferrule_bolt_down"]
        shank = ycyl(2.5, -ro - 0.5, ro + 6, X_POLE, z)
        head = ycyl(4.25, -ro - 4.0, -ro, X_POLE, z)
        nut = ycyl(4.25, ro, ro + 5, X_POLE, z) - ycyl(2.5, ro - 1, ro + 6, X_POLE, z)
        out.append(Compound([shank, head, nut]))
    return out


def bamboo_lock_pins(p=PARAMS):
    d = derived(p)
    half = p["ferrule"][0] / 2 + 0.5
    pins = [clevis(d["pole_z0"] + p["head_pin_up"], p)]
    pins += [clevis(jz + p["ferrule_pin_up"], p, half=half) for jz in d["joints"]]
    return pins


def bamboo_pole(p=PARAMS):
    """The bamboo variant's pole as one compound (sections, ferrules, bolts, lock pins)."""
    return Compound(bamboo_sections(p) + ferrules(p) + ferrule_bolts(p) + bamboo_lock_pins(p))


# ------------------------------------------------------------------ assemblies
BOM = {  # key: (BOM line, name)
    "ring": (1, "Rider ring (two halves, tang)"),
    "hinge": (2, "Hinge bolt M8 with nyloc nut"),
    "gate": (3, "Gate pin 8 mm with R-clip"),
    "head": (4, "Pole head"),
    "shear": (5, "Shear pin, 2 mm soft aluminium"),
    "poles": (6, "Pole sections (3)"),
    "sleeves": (7, "Joint sleeves (2)"),
    "rivets": (8, "Pop rivets (4)"),
    "locks": (9, "Lock pins 6 mm (3 fitted)"),
    "cap": (10, "Grip cap"),
    "tether": (11, "Tether cord"),
    "winder": (12, "Float winder"),
    "spares": (13, "Spare pin tube"),
    "weight": (14, "Jigging weight"),
    "cframe": (15, "Gunwale crutch frame"),
    "roller": (16, "Crutch roller and axle"),
    "clamp": (17, "Crutch clamp screw"),
    "hook": (21, "Hook head"),
}

CRUTCH_AT = (420.0, 0.0, 0.0)       # where the crutch, winder and weight sit beside the tool in the GA
WINDER_AT = (420.0, 0.0, 300.0)
WEIGHT_AT = (300.0, 0.0, 0.0)
HOOK_AT = (190.0, 0.0, 95.0)


def tool_parts(p=PARAMS):
    """The assembled tool (ring, head, pole), working position, as {key: shape}."""
    return {
        "ring": Compound([ring_half(p, +1), ring_half(p, -1)]),
        "hinge": hinge_bolt(p),
        "gate": gate_pin(p),
        "head": pole_head(p),
        "shear": shear_pin(p),
        "poles": Compound(pole_sections(p)),
        "sleeves": Compound(sleeves(p)),
        "rivets": Compound(rivets(p)),
        "locks": Compound(lock_pins(p)),
        "cap": grip_cap(p),
        "tether": tether_knot(p),
    }


def crutch_parts(p=PARAMS, at=(0, 0, 0)):
    r, w = crutch_roller(p)
    nut, screw = crutch_clamp(p)
    x, y, z = at
    return {"cframe": Pos(x, y, z) * Compound([crutch_frame(p), nut]),
            "roller": Pos(x, y, z) * Compound([r, w, crutch_axle(p)]),
            "clamp": Pos(x, y, z) * screw}


def build_components(p=PARAMS):
    """Every kit item as one shape, laid out for the general arrangement: the tool assembled and
    standing on its ring, the crutch, float winder, spare tube and jigging weight beside it."""
    c = tool_parts(p)
    c.update(crutch_parts(p, CRUTCH_AT))
    x, y, z = WINDER_AT
    c["winder"] = Pos(x, y, z) * Rot(0, 90, 0) * float_winder(p)
    c["tether"] = Compound([c["tether"], Pos(x, y, z) * Rot(0, 90, 0) * winder_cord(p)])
    c["spares"] = Pos(x + 50, 70, z - 40) * spare_tube(p)
    wx, wy, wz = WEIGHT_AT
    c["weight"] = Pos(wx - X_POLE, wy, wz) * Compound([jig_weight(p), weight_pin(p)])
    hx, hy, hz = HOOK_AT
    c["hook"] = Pos(hx - X_POLE, hy, hz) * hook_head(p)
    return c


def assembly(p=PARAMS):
    c = build_components(p)
    return Compound([c[k] for k in BOM])


def jigging_parts(p=PARAMS):
    """Deep-snag set-up: the ring with the jigging weight pinned to its tang, no pole."""
    return {"ring": Compound([ring_half(p, +1), ring_half(p, -1)]), "hinge": hinge_bolt(p), "gate": gate_pin(p),
            "weight": jig_weight(p), "wpin": weight_pin(p), "tether": tether_knot(p)}


def packed_layout(p=PARAMS):
    """The kit laid out on the ground (z = 0) as it is packed: the three pole sections side by side
    along X, the small parts in front of them (-Y). Used for the overview picture and the hero render."""
    d = derived(p)
    r = p["pole"][0] / 2
    secs = pole_sections(p)
    slv = sleeves(p)
    rv = rivets(p)

    def lay(shape, z_start, y):
        return Pos(0, y, r) * Rot(0, 90, 0) * Pos(-X_POLE, 0, -z_start) * shape

    out = {}
    z0 = d["pole_z0"]
    ys = (0.0, 60.0, 120.0)
    out["poles"] = Compound([lay(s, z0 + i * p["section_L"], ys[i]) for i, s in enumerate(secs)])
    out["sleeves"] = Compound([lay(s, z0 + i * p["section_L"], ys[i]) for i, s in enumerate(slv)])
    out["rivets"] = Compound([lay(q, z0 + (i // 2) * p["section_L"], ys[i // 2]) for i, q in enumerate(rv)])
    out["cap"] = lay(grip_cap(p), z0 + 2 * p["section_L"], ys[2])
    lk = lock_pins(p)
    out["locks"] = Compound([lay(lk[i], z0 + (i - 1) * p["section_L"], ys[i - 1]) for i in range(1, len(lk))]
                            + [Pos(400, -330, 5) * Pos(-X_POLE, 0, -(z0 + p["head_pin_up"])) * lk[0]])
    ring = Compound([ring_half(p, +1), ring_half(p, -1), hinge_bolt(p), gate_pin(p)])
    out["ring"] = Pos(220, -200, p["ear"][2] / 2) * ring
    out["head"] = Pos(470, -170, p["socket"][0] / 2) * Rot(0, 90, 0) * Pos(-X_POLE, 0, -150) * pole_head(p)
    out["weight"] = Pos(760, -190, 0) * Pos(-X_POLE, 0, -p["wcheek_z"][0]) * Compound([jig_weight(p), weight_pin(p)])
    cr = crutch_parts(p)
    out["crutch"] = Pos(1000, -200, p["saddle"][2] - p["saddle"][3]) * Compound(list(cr.values()))
    w = float_winder(p)
    out["winder"] = Pos(1330, -200, p["winder"][2] / 2 + 12) * Compound([w, winder_cord(p)])
    out["spares"] = Pos(1180, -330, 7) * Rot(0, 90, 0) * spare_tube(p)
    out["hook"] = Pos(620, -330, p["tang"][1] / 2) * Rot(90, 0, 0) * Pos(-X_POLE, 0, 0) * hook_head(p)
    return out


# ------------------------------------------------------------------ checks
def _vol(a, b):
    try:
        s = a & b
        return s.volume if s is not None else 0.0
    except Exception:
        return 0.0


def _dist(a, b):
    return a.distance_to(b)


def checks(p=PARAMS):
    """Constructability checks. Returns [(name, ok, detail)]."""
    r = []
    A, B = ring_half(p, +1), ring_half(p, -1)
    hb, gp = hinge_bolt(p), gate_pin(p)
    head, sp = pole_head(p), shear_pin(p)
    poles, slv, rv, lk = pole_sections(p), sleeves(p), rivets(p), lock_pins(p)
    cap = grip_cap(p)
    knot = tether_knot(p)
    wt, wp = jig_weight(p), weight_pin(p)
    fr = crutch_frame(p)
    rol, wash = crutch_roller(p)
    ax = crutch_axle(p)
    nut, scr = crutch_clamp(p)
    gun = gunwale_context(p)
    tol = 1.0   # mm3

    def no_overlap(n, a, b):
        v = _vol(a, b)
        r.append((f"no overlap: {n}", v < tol, f"{v:.2f} mm3"))

    def touches(n, a, b, gap=0.3):
        d = _dist(a, b)
        r.append((f"contact: {n}", d <= gap, f"gap {d:.2f} mm"))

    def clear(n, a, b, need):
        d = _dist(a, b)
        r.append((f"clearance: {n}", d >= need, f"{d:.1f} mm (need {need})"))

    # ring
    no_overlap("ring halves", A, B)
    clear("ring halves at the joints (split gap)", A, B, p["split_gap"] - 0.01)
    for n, s in (("hinge bolt / fixed half", A), ("hinge bolt / swinging half", B)):
        no_overlap(n, hb, s)
        touches(n, hb, s, 0.6)
    for n, s in (("gate pin / fixed half", A), ("gate pin / swinging half", B)):
        no_overlap(n, gp, s)
        touches(n, gp, s, 0.6)
    r.append(("ring inside diameter takes the largest line (16 mm) with room to slide",
              derived(p)["ring_ID"] >= 16 * 4, f"{derived(p)['ring_ID']:.0f} mm"))
    # head on tang
    no_overlap("pole head / ring", head, Compound([A, B]))
    clear("fork cheeks clear the tang faces (free to swing)", head, A, 0.9)
    no_overlap("shear pin / tang", sp, A)
    no_overlap("shear pin / head", sp, head)
    touches("shear pin bears in the tang hole", sp, A, 0.1)
    touches("shear pin bears in the cheek holes", sp, head, 0.1)
    gap_top = p["cheek_z"][1] - (p["tang"][2] - 4)
    r.append(("tang top stays clear of the end plate, so push and pull both go through the pin",
              gap_top >= 20, f"{gap_top:.0f} mm"))
    # pole
    no_overlap("pole bottom / head socket", poles[0], head)
    touches("pole bottom seats on the end plate", poles[0], head, 0.05)
    for i, s in enumerate(slv):
        no_overlap(f"sleeve {i + 1} / lower section", s, poles[i])
        no_overlap(f"sleeve {i + 1} / upper section", s, poles[i + 1])
        clear(f"sleeve {i + 1} slide fit on the upper section", s, poles[i + 1], 0.15)
    for i in range(len(poles) - 1):
        d = _dist(poles[i], poles[i + 1])
        r.append((f"sections {i + 1} and {i + 2} butt inside the sleeve", d < 0.05, f"gap {d:.2f} mm"))
    for i, q in enumerate(rv):
        j = i // 2
        no_overlap(f"rivet {i + 1} / sleeve", q, slv[j])
        no_overlap(f"rivet {i + 1} / lower section", q, poles[j])
        touches(f"rivet {i + 1} through sleeve", q, slv[j], 0.1)
        touches(f"rivet {i + 1} through section", q, poles[j], 0.1)
    no_overlap("head lock pin / socket", lk[0], head)
    no_overlap("head lock pin / pole", lk[0], poles[0])
    touches("head lock pin through socket", lk[0], head, 0.3)
    for i in range(1, len(lk)):
        no_overlap(f"joint lock pin {i} / sleeve", lk[i], slv[i - 1])
        no_overlap(f"joint lock pin {i} / upper section", lk[i], poles[i])
        touches(f"joint lock pin {i} through upper section", lk[i], poles[i], 0.6)
    no_overlap("grip cap / top section", cap, poles[-1])
    touches("grip cap on top section", cap, poles[-1], 0.05)
    # tether
    no_overlap("tether loop / tang", knot, A)
    no_overlap("tether / head", knot, head)
    no_overlap("tether / swinging half", knot, B)
    # weight
    no_overlap("jigging weight / ring", wt, Compound([A, B]))
    clear("weight cheeks clear the tang faces", wt, A, 0.9)
    no_overlap("weight pin / tang", wp, A)
    no_overlap("weight pin / weight", wp, wt)
    no_overlap("weight / tether loop", wt, knot)
    touches("weight pin bears in the tang hole", wp, A, 0.3)
    # hook head in the fork (SMR-DDR-003)
    hk = hook_head(p)
    hkn = hook_knot(p)
    no_overlap("hook head / pole head", hk, head)
    clear("fork cheeks clear the hook head's flat faces (free to swing)", head, hk, 0.9)
    no_overlap("shear pin / hook head", sp, hk)
    touches("shear pin bears in the hook head's hole", sp, hk, 0.1)
    hgap = p["cheek_z"][1] - p["hook_flat_z"][1]
    r.append(("hook head's flat stops clear of the end plate, so push and pull go through the pin",
              hgap >= 20, f"{hgap:.0f} mm"))
    no_overlap("tether loop / hook head", hkn, hk)
    clear("tether loop on the hook head clears the fork cheeks", hkn, head, 2.0)
    r.append(("hook throat takes a doubled 16 mm line with room to spare",
              hook_throat(p) >= 40, f"{hook_throat(p):.0f} mm clear"))
    clear("hook tip clears the pole head (bight can enter the J)", Pos(0, 0, 0) * zcyl(p["hook_bar_d"] / 2, p["hook_shank_z"], p["hook_tip_z"], X_POLE - 2 * p["hook_R"]), head, 50.0)
    # bamboo local variant (SMR-DDR-003)
    bs, fe, fb, bl = bamboo_sections(p), ferrules(p), ferrule_bolts(p), bamboo_lock_pins(p)
    no_overlap("bamboo spigot / head socket", bs[0], head)
    touches("bamboo spigot seats on the end plate", bs[0], head, 0.05)
    no_overlap("head lock pin / bamboo spigot", bl[0], bs[0])
    touches("head lock pin through the bamboo spigot", bl[0], bs[0], 0.3)
    for i, s in enumerate(fe):
        no_overlap(f"ferrule {i + 1} / lower culm", s, bs[i])
        no_overlap(f"ferrule {i + 1} / upper culm", s, bs[i + 1])
        clear(f"ferrule {i + 1} slide fit on the upper culm", s, bs[i + 1], 0.15)
        no_overlap(f"ferrule bolt {i + 1} / ferrule", fb[i], s)
        no_overlap(f"ferrule bolt {i + 1} / lower culm", fb[i], bs[i])
        touches(f"ferrule bolt {i + 1} through the ferrule", fb[i], s, 0.3)
        touches(f"ferrule bolt {i + 1} through the lower culm", fb[i], bs[i], 0.3)
        no_overlap(f"bamboo lock pin {i + 1} / ferrule", bl[i + 1], s)
        no_overlap(f"bamboo lock pin {i + 1} / upper culm", bl[i + 1], bs[i + 1])
        touches(f"bamboo lock pin {i + 1} through the upper culm", bl[i + 1], bs[i + 1], 0.6)
    for i in range(len(bs) - 1):
        d_ = _dist(bs[i], bs[i + 1])
        r.append((f"culms {i + 1} and {i + 2} butt inside the ferrule", d_ < 0.05, f"gap {d_:.2f} mm"))
    bpl = p["section_L"] + p["ferrule"][2] / 2
    r.append(("longest packed bamboo piece (a culm with its ferrule)", bpl <= 1600, f"{bpl:.0f} mm"))
    # crutch
    no_overlap("roller / frame", rol, fr)
    no_overlap("washers / frame", wash, fr)
    no_overlap("axle / frame", ax, fr)
    no_overlap("axle / roller", ax, rol)
    touches("washers between roller and cheeks", wash, fr, 0.05)
    clear("roller clears the saddle web", rol, fr, 1.5)
    no_overlap("clamp nut / frame", nut, fr)
    touches("clamp nut welded to the inboard leg", nut, fr, 0.05)
    no_overlap("clamp screw / frame", scr, fr)
    no_overlap("saddle / gunwale (40 mm)", fr, gun)
    touches("saddle web sits on the gunwale", fr, gun, 0.05)
    no_overlap("clamp pad / gunwale", scr, gun)
    touches("clamp pad on the gunwale face", scr, gun, 0.05)
    for gt in (30.0, 60.0):
        _, s2 = crutch_clamp(p, gt)
        g2 = gunwale_context(p, gt)
        ok = _vol(s2, fr) < tol and _vol(s2, g2) < tol and _vol(fr, g2) < tol
        r.append((f"crutch fits a {gt:.0f} mm gunwale", ok, "screw reaches without clash"))
    # packing
    d = derived(p)
    r.append(("longest packed piece (a section with its sleeve)", d["packed_L"] <= 1600, f"{d['packed_L']:.0f} mm"))
    # kit in its GA and packed layouts
    c = build_components(p)
    for k in BOM:
        if k != "hook":
            no_overlap(f"GA layout: hook head / {BOM[k][1].lower()}", c["hook"], c[k])
    L = packed_layout(p)
    for k, v in L.items():
        if k != "hook":
            no_overlap(f"packed: hook head / {k}", L["hook"], v)
    return r


# ------------------------------------------------------------------ exports
def export(p=PARAMS):
    step = ROOT / "cad" / "step"
    stl = ROOT / "cad" / "stl"
    step.mkdir(parents=True, exist_ok=True)
    stl.mkdir(parents=True, exist_ok=True)
    c = build_components(p)
    export_step(Compound([c[k] for k in BOM]), str(step / "stumprider-assembly.step"))
    export_step(Compound([ring_half(p, +1), ring_half(p, -1), hinge_bolt(p), gate_pin(p)]), str(step / "rider-ring.step"))
    export_step(pole_head(p), str(step / "pole-head.step"))
    export_step(Compound([jig_weight(p), weight_pin(p)]), str(step / "jigging-weight.step"))
    cr = crutch_parts(p)
    export_step(Compound(list(cr.values())), str(step / "gunwale-crutch.step"))
    export_step(float_winder(p), str(step / "float-winder.step"))
    export_step(pole_sections(p)[0], str(step / "pole-section.step"))
    export_step(sleeves(p)[0], str(step / "joint-sleeve.step"))
    export_step(hook_head(p), str(step / "hook-head.step"))
    export_step(bamboo_pole(p), str(step / "bamboo-pole-variant.step"))
    kw = dict(tolerance=0.2, angular_tolerance=0.3)
    export_stl(crutch_roller(p)[0], str(stl / "crutch-roller.stl"), **kw)
    export_stl(float_winder(p), str(stl / "float-winder.stl"), **kw)
    export_stl(ring_half(p, +1), str(stl / "ring-fixed-half.stl"), **kw)
    export_stl(ring_half(p, -1), str(stl / "ring-swinging-half.stl"), **kw)
    export_stl(pole_head(p), str(stl / "pole-head.stl"), **kw)
    export_stl(hook_head(p), str(stl / "hook-head.stl"), **kw)


if __name__ == "__main__":
    d = derived()
    print({k: (round(v, 1) if isinstance(v, float) else v) for k, v in d.items()})
    if "--check" in sys.argv:
        res = checks()
        for name, ok, det in res:
            print(("ok  " if ok else "FAIL"), name, det)
        print(f"{sum(ok for _, ok, _ in res)} of {len(res)} constructability checks pass")
    if "--export" in sys.argv:
        export()
        print("exported STEP and STL")
