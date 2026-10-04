"""StumpRider product appearance model (build123d), TRL 3, constructable design (SMR-DDR-002).

Finished-product look for photoreal renders, built from the constructable model: every kit piece
of cad/src/model.py is used as it is (rider ring with hinge bolt and gate pin, pole head, shear pin,
pole sections, sleeves, rivets, lock pins, grip cap, tether, float winder, spare pin tube, jigging
weight, gunwale crutch, and the hook head of SMR-DDR-003). Only the look is added, as recorded in docs/REVIEW.md: a plank deck under the
packed kit with a forearm and hand beside the ring for scale (hero), and a short net line draped over
a branch for the detail view, with the pole cut short.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py. Groups: "shell" (the packed kit, hero), "context" (deck and forearm), "end" (the
working end, exploded view), "detail" (the working end on a branch).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Compound, Pos, Rot  # noqa: E402
import model as M  # noqa: E402

TITLE = "StumpRider: canoe-worked release tool for gillnets snagged on drowned trees"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 38, "az": -62,
     "note": "Product render from the front right and above (about 38 deg elevation): the kit laid out as packed on a "
             "plank deck, three aluminium pole sections with their sleeves, the hinged rider ring, pole head, jigging "
             "weight, clamp-on gunwale crutch with its roller, the orange float winder with the tether, and the J-shaped hook head; a forearm "
             "and hand beside the ring for scale"},
    {"name": "exploded", "groups": ["end"], "explode": True, "el": 20, "az": -50,
     "note": "Exploded view of the working end from the front right and above (about 20 deg elevation): the two ring "
             "halves, hinge bolt and gate pin, the red 2 mm shear pin, the pole head and its lock pin, and the bottom "
             "of the pole pulled apart along the way each comes off"},
    {"name": "detail", "groups": ["detail"], "explode": False, "el": 14, "az": -35,
     "note": "Detail of the working end on a snag, from the front right and slightly above (about 14 deg elevation): "
             "the rider ring closed round the net line and seated on the branch, the pole head forked over the tang "
             "with the shear pin through it, and the tether tied through the lowest tang hole"},
]

C_ALU = "#B8BEC6"
C_STEEL = "#9AA1A9"        # hot-dip galvanised
C_SS = "#C9CED4"
C_HEAD = "#8E969E"
C_PIN = "#C81E1E"          # the shear pin is shown red so it reads
C_CORD = "#E2621B"
C_FLOAT = "#F28C28"
C_RUBBER = "#1F2328"
C_HDPE = "#ECEBE6"
C_DECK = "#8A6A47"
C_CLAY = "#B9B4AC"
C_BARK = "#5B4632"
C_LINE = "#D9CBA3"
C_MARK = "#E8590C"


def product_parts(p=M.PARAMS):
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material, "bom": bom,
                    "group": group, "explode": tuple(explode)})

    # hero: the packed kit
    L = M.packed_layout(p)
    add("Pole sections, aluminium", L["poles"], C_ALU, "metal", 6, "shell")
    add("Joint sleeves, aluminium", L["sleeves"], C_ALU, "metal", 7, "shell")
    add("Pop rivets, stainless", L["rivets"], C_SS, "metal", 8, "shell")
    add("Lock pins, stainless", L["locks"], C_SS, "metal", 9, "shell")
    add("Grip cap, rubber", L["cap"], C_RUBBER, "rubber", 10, "shell")
    add("Rider ring, galvanised steel", L["ring"], C_STEEL, "metal", 1, "shell")
    add("Pole head, galvanised steel", L["head"], C_HEAD, "metal", 4, "shell")
    add("Jigging weight, galvanised steel", L["weight"], C_STEEL, "metal", 14, "shell")
    add("Gunwale crutch, galvanised steel with HDPE roller", L["crutch"], C_STEEL, "metal", 15, "shell")
    add("Float winder, orange foam, with tether cord", L["winder"], C_FLOAT, "painted", 12, "shell")
    add("Spare pin tube", L["spares"], C_HDPE, "painted", 13, "shell")
    add("Hook head, galvanised steel", L["hook"], C_STEEL, "metal", 21, "shell")
    add("Plank deck", Pos(720, -260, -15) * Box(1900, 1100, 30), C_DECK, "wood", None, "context")
    from context_parts import forearm_hand
    arm = Pos(240, -560, 22) * Rot(0, 0, 90) * forearm_hand(side="right", pose="flat")
    add("Forearm and hand (scale)", arm, C_CLAY, "clay", None, "context")

    # the working end (exploded and detail views)
    t = M.tool_parts(p)
    stub = Pos(M.X_POLE, 0, 330) * Box(200, 200, 400)
    pole = M.pole_sections(p)[0] & stub
    end = [
        ("Rider ring, fixed half with tang", M.ring_half(p, +1), C_STEEL, 1, (0, 0, 0)),
        ("Rider ring, swinging half", M.ring_half(p, -1), C_STEEL, 1, (-110, 0, 0)),
        ("Hinge bolt and nut, stainless", M.hinge_bolt(p), C_SS, 2, (-60, 90, 0)),
        ("Gate pin and R-clip, stainless", M.gate_pin(p), C_SS, 3, (-60, -110, 0)),
        ("Shear pin, 2 mm aluminium", M.shear_pin(p), C_PIN, 5, (0, -120, 0)),
        ("Pole head, galvanised steel", t["head"], C_HEAD, 4, (0, 0, 110)),
        ("Lock pin, stainless", M.lock_pins(p)[0], C_SS, 9, (0, -90, 190)),
        ("Pole section, aluminium", pole, C_ALU, 6, (0, 0, 220)),
    ]
    for name, shape, color, bom, ex in end:
        mat = "rubber" if "Shear" in name else "metal"
        add(f"End: {name}", shape, color, mat, bom, "end", ex)
    knot = t["tether"] & Pos(100, 0, 140) * Box(200, 200, 300)
    add("End: tether cord", knot, C_CORD, "fabric", 11, "end", (90, 0, 0))
    for name, shape, color, bom, _ in end:
        mat = "rubber" if "Shear" in name else "metal"
        add(f"Detail: {name}", shape, color, mat, bom, "detail")
    add("Detail: tether cord", knot, C_CORD, "fabric", 11, "detail")
    # context for the detail: net line coming down through the ring and over a drowned branch
    br_z = -P_BRANCH_DROP
    add("Detail: drowned branch", Pos(-30, 0, br_z) * Rot(90, 0, 0) * M.zcyl(55, -260, 260), C_BARK, "wood", None, "detail")
    pts = [(0, 0, br_z + 55), (-50, 0, br_z + 58), (-95, 0, br_z + 15), (-102, 0, br_z - 225)]
    line = Compound([M.net_line(br_z + 55, 560, 10)] + [M.rod(a, b, 5) for a, b in zip(pts, pts[1:])])
    add("Detail: net line (headrope)", line, C_LINE, "fabric", None, "detail")
    return out


P_BRANCH_DROP = 75.0      # branch top 20 mm below the ring


if __name__ == "__main__":
    for q in product_parts():
        s = q["shape"]
        print(f"{q['name']:60s} {q['group']:8s} {q['material']:8s} vol={s.volume / 1000:10.1f} cm3")
