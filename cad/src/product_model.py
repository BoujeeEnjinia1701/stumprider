"""StumpRider product appearance model for photoreal renders (STANDARDS sections 12 and 24), TRL 3, kit 1.9.1.

Every product part is components(CHOSEN) from cad/src/model.py as it is: the D3 parts of option A (rider ring
halves, ears, tang, hinge bolt set, gate pin and R-clip, pole head cheeks, end plate and socket, shear pin, lock
pins and R-clips, pole sections, sleeves, rivets, grip cap, tether, float winder, spare pin tube, jigging weight,
gunwale crutch with its roller, axle and clamp, hook head, and every weld bead). Only their placement changes
for the site scene; no dimension changes. Context parts are added:

- hero: a landing site on a lake shore, ground level at model z = 0 (mud with water in the hollows). A beached
  8 m plank canoe (site) with the gunwale crutch clamped on its near gunwale; the tool lies on the mud in front
  of it, the ring resting on its edge; the jigging weight, hook head, float winder and spare pin tube beside it;
  a 1.75 m mannequin standing on the mud for scale.
- studio: the kit in its general arrangement layout (the tool standing on its ring), no context.
- detail: the working end on a snag in the studio: the ring closed round a net line and seated on a drowned
  branch, the pole head forked over the tang with the shear pin through it, the pole cut short.
APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.

Groups: "site" (the hero kit), "context" (canoe, mannequin), "shell" (general arrangement), "detail".

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Pos, Rot  # noqa: E402
import model as M  # noqa: E402
from cad_parts import part, break_edges  # noqa: E402

TITLE = "StumpRider: canoe-worked release tool for gillnets snagged on drowned trees"

_SITE = ["--scene=outdoor", "--ground=mud", "--ground-z=0", "--water=-8", "--sun=38,-80", "--lens=40"]
RENDER_VIEWS = [
    {"name": "hero", "groups": ["site", "context"], "explode": False, "el": 16, "az": -55, "args": _SITE,
     "note": "Site render at a lake landing from the front right, about 16 deg elevation: the kit on the mud in front of a "
             "beached plank canoe, the gunwale crutch clamped on the canoe's near gunwale, the jointed pole lying with the "
             "rider ring on its edge, jigging weight, hook head and orange float winder beside it; 1.75 m person standing on "
             "the mud for scale"},
    {"name": "studio", "groups": ["shell"], "explode": False, "el": 18, "az": -55,
     "note": "Studio render from the front right and above (about 18 deg elevation): the kit in its general arrangement, "
             "the tool standing on its rider ring with the gunwale crutch, float winder, jigging weight and hook head beside it"},
    {"name": "detail", "groups": ["detail"], "explode": False, "el": 14, "az": -35,
     "note": "Detail of the working end on a snag, from the front right and slightly above (about 14 deg elevation): the "
             "rider ring closed round the net line and seated on a drowned branch, the pole head forked over the tang with "
             "the shear pin through it, the hinge bolt and gate pin, the tether bowline in the lowest tang hole"},
]

CANOE = dict(L=8000.0, B=1100.0, D=600.0, wall=40.0, sink=60.0, y_near=150.0, x0=-1500.0)
TOOL_AT = (0.0, -650.0)
TILT = -math.degrees(math.atan(116.0 / 4486.0))       # pole cap end rests on the mud, ring on its edge


def _move(parts, f, grp, suffix=""):
    return [dict(q, shape=f(q["shape"]), group=grp, name=q["name"] + suffix) for q in parts]


def _canoe():
    """A plank canoe beached on the mud (site): a 40 mm shell, pointed at both ends, sunk 60 mm into the mud."""
    c = CANOE
    yc = c["y_near"] + c["B"] / 2
    zc = c["D"] / 2 - c["sink"]
    outer = Pos(c["x0"], yc, zc) * Box(c["L"], c["B"], c["D"])
    inner = Pos(c["x0"], yc, zc + c["wall"]) * Box(c["L"] - 2 * c["wall"], c["B"] - 2 * c["wall"], c["D"])
    hull = outer - inner
    for sx in (+1, -1):
        for sy in (+1, -1):
            cut = Pos(c["x0"] + sx * c["L"] / 2, yc + sy * c["B"] / 2, zc) * Rot(0, 0, sx * sy * 8) * Box(2600, 600, c["D"] + 10)
            hull = hull - cut
    thwarts = [Pos(c["x0"] + dx, yc, c["D"] - c["sink"] - 120) * Box(180, c["B"] - 2 * c["wall"] - 200, 30) for dx in (-1500, 0, 1500)]
    out = [part("Plank canoe hull (site)", break_edges(hull, 4.0), "timber", kind="context", group="context")]
    out += [part(f"Canoe thwart {i + 1} (site)", t, "hardwood", kind="context", group="context") for i, t in enumerate(thwarts)]
    return out


def site():
    a = [q for q in M.components(M.CHOSEN) if q["kind"] != "context"]
    by = lambda g: [q for q in a if q["group"] == g]   # noqa: E731
    out = []
    tx, ty = TOOL_AT
    out += _move(by("tool"), lambda s: Pos(tx, ty, 0) * Rot(0, TILT, 0) * Pos(0, 0, 62.0) * Rot(0, -90, 0) * s, "site")
    out += _move(by("weight"), lambda s: Pos(450.0, -1050.0, -34.0 + 0.5) * Pos(-M.WEIGHT_AT[0], 0, 0) * s, "site")
    out += _move(by("hook"), lambda s: Pos(700.0, -900.0, 1.5) * Pos(-M.HOOK_AT[0], 0, 0) * s, "site")
    wx, wy, wz = M.WINDER_AT
    lay = lambda s: Pos(150.0, -1150.0, 32.0) * Rot(0, -90, 0) * Pos(-wx, -wy, -wz) * s   # noqa: E731
    w = by("winder")
    out += _move([q for q in w if "Spare" not in q["name"]], lay, "site")
    out += _move([q for q in w if "Spare" in q["name"]], lambda s: Pos(-200.0, -1150.0, -(wz - 40)) * Pos(-(wx + 50), -70, 0) * s, "site")
    c = CANOE
    zg = c["D"] - c["sink"]
    cx = M.CRUTCH_AT[0]
    out += _move(by("crutch"), lambda s: Pos(600.0, c["y_near"] + 35.0, zg) * Rot(0, 0, 180) * Pos(-cx, 0, 0) * s, "site")
    out += _canoe()
    try:
        import context_parts
        man = Pos(1300.0, -400.0, 0) * Rot(0, 0, 200) * context_parts.mannequin(1750.0, "stand")
        out.append(part("Person 1.75 m (scale)", man, "skin", kind="context", group="context"))
    except Exception as e:   # the mannequin is for scale only; never block the product parts
        print("mannequin not added:", e)
    return out


def detail():
    """Working end on a snag: parts of the tool within 300 mm of the ring, the pole cut short, a branch and net line."""
    a = [q for q in M.components(M.CHOSEN) if q["group"] == "tool"]
    win = Pos(M.X_POLE, 0, 160) * Box(320, 320, 520)
    out = []
    for q in a:
        bb = q["shape"].bounding_box()
        if bb.min.Z > 400:
            continue
        s = q["shape"] if bb.max.Z < 400 else (q["shape"] & win)
        if s is None or s.volume < 1:
            continue
        out.append(dict(q, shape=s, group="detail", name="Detail: " + q["name"]))
    br = -75.0
    out.append(part("Detail: drowned branch", Pos(-30, 0, br) * Rot(90, 0, 0) * M.zcyl(55, -260, 260), "hardwood",
                    kind="context", group="detail", color="#5B4632"))
    pts = [(0, 0, br + 55), (-50, 0, br + 58), (-95, 0, br + 15), (-102, 0, br - 225)]
    from build123d import Compound
    line = Compound([M.net_line(br + 55, 380, 10)] + [M.rod(p0, p1, 5) for p0, p1 in zip(pts, pts[1:])])
    out.append(part("Detail: net line (headrope)", line, "rope", kind="context", group="detail"))
    return out


def product_parts():
    shell = [dict(q, group="shell") for q in M.components(M.CHOSEN) if q["kind"] != "context"]
    return shell + site() + detail()


if __name__ == "__main__":
    ps = product_parts()
    from collections import Counter
    print(len(ps), "parts;", dict(Counter(p["group"] for p in ps)))
    for g in ("site",):
        zmin = min(p["shape"].bounding_box().min.Z for p in ps if p["group"] == g)
        print(g, "lowest point", round(zmin, 1), "mm")
    for p in ps:
        if p["group"] == "site" and p["shape"].bounding_box().min.Z < -2:
            print("  below ground:", p["name"], round(p["shape"].bounding_box().min.Z, 1))
