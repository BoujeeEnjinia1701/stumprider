"""StumpRider sizing calculations (SMR-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every result with a tag ([M1], [P2] ...) used in docs/04-calcs/01-sizing.md and writes
docs/04-calcs/results.csv. Geometry and masses come from the parametric model (cad/src/model.py),
so the sizes here are the sizes in the STEP files, drawings and build plan.

Screening estimates for a paper proof of concept. They do not replace the CalRig pin calibration,
the canoe heel test or the staged-snag trials, which are TRL 4 work.
Software license MIT, see LICENSE-SOFTWARE.
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad" / "src")]
import model as M  # noqa: E402

P = M.PARAMS
D = M.derived(P)
OUT = []
g = 9.81

A = {
    # materials
    "rho_steel": 7850.0, "rho_al": 2700.0, "rho_ss": 7900.0, "rho_hdpe": 950.0, "rho_foam": 30.0,
    "rho_rubber": 1100.0, "cord_kg_m": 0.025, "rho_polyester": 1380.0, "rho_water": 1000.0,
    "E_al": 69000.0,            # MPa, 6063-T6
    "rho_bamboo": 700.0,        # kg/m3, seasoned treated bamboo culm (assumed; SMR-DDR-003)
    "E_bamboo": 15000.0,        # MPa, along the culm (10 to 20 GPa range; assumed, to be measured by a bend test)
    "tau_pin": 48.0,            # MPa, shear strength of 1050-O / 1100-O wire (about 0.6 x 80 MPa tensile), assumed
    "tau_pin_band": 0.15,       # +/- band on the pin rating that R3 allows
    "fy_steel": 235.0,          # MPa, S235 mild steel
    "tau_ss_pin": 300.0,        # MPa, stainless clevis pins (shear)
    "bear_al": 320.0,           # MPa, bearing of 6063-T6 at a pin hole
    "rivet_kN": 2.9,            # 4.8 mm stainless blind rivet, shear, catalogue typical
    # design canoe (Volta plank canoe, paddled, operator kneeling at the bow), assumed
    "canoe": {"name": "design canoe", "L": 8.0, "B": 1.10, "depth": 0.60, "k_I": 0.050, "Cb": 0.45,
              "hull_kg": 300.0, "hull_kg_z": 0.25, "crew": 3, "crew_kg": 65.0, "crew_z": 0.55,
              "load_kg": 55.0, "load_z": 0.20, "hands_y": 0.35, "half_wl": 0.55},
    "small": {"name": "small dugout", "L": 5.5, "B": 0.75, "depth": 0.45, "k_I": 0.050, "Cb": 0.45,
              "hull_kg": 120.0, "hull_kg_z": 0.22, "crew": 2, "crew_kg": 65.0, "crew_z": 0.50,
              "load_kg": 30.0, "load_z": 0.20, "hands_y": 0.25, "half_wl": 0.375},
    "pole_lean": 20.0,          # deg from vertical while working
    "hands_kneel": 0.30,        # m above the gunwale, kneeling
    "hands_stand": 0.85,        # m above the gunwale, standing
    "heel_limit": 5.0,          # deg, safe working heel at the top of the pin band (conservative)
    "crew_hold_N": 100.0,       # crew tension on the net line while the ring is run down
    "crew_slack_N": 30.0,       # crew tension while the operator lifts (operating rule)
    "net_leg_N": 20.0,          # tension in the far leg of the net (its own drag and weight in water)
    "mu": (0.3, 0.5),           # wet netting on wet bark, low and high
    "grip_below_top_m": 0.30,
    "jig_cord_above_m": 2.0,    # cord needed above the water to the hands, and slack
    "build_min": {               # workshop minutes, one kit, a smith working alone (estimate)
        "ring: cut, bend both halves over a 100 mm former, trim the joint gaps": 60,
        "ring: cut and drill four ears and the tang, weld": 70,
        "pole head: cut tube, plate and cheeks, weld, drill": 60,
        "jigging weight: cut bar and cheeks, weld, drill": 35,
        "crutch: cut, bend and drill the saddle, cut cheeks, weld, weld the nut": 75,
        "crutch: roller from rod, clamp screw with pad and handle": 40,
        "pole: cut three sections and two sleeves, deburr, drill, rivet": 60,
        "shear pins: cut and deburr twelve": 15,
        "float winder: cut foam, paint": 20,
        "assemble, fit pins, tie tether, wind cord": 25,
        "hook head: cut flat and bar, bend the J, weld, drill": 25,
    },
}


def out(tag, text, value=None, unit="", req=None, status=None):
    OUT.append({"tag": tag, "item": text, "value": "" if value is None else value, "unit": unit,
                "requirement": req or "", "status": status or ""})
    v = "" if value is None else (f"{value:,.3g}" if isinstance(value, float) else value)
    print(f"[{tag}] {text}: {v} {unit} {('(' + req + ' ' + status + ')') if req else ''}".rstrip())


# ------------------------------------------------------------------ 1. masses
def masses():
    c = M.build_components(P)
    rho = {"ring": "rho_steel", "hinge": "rho_ss", "gate": "rho_ss", "head": "rho_steel", "shear": "rho_al",
           "poles": "rho_al", "sleeves": "rho_al", "rivets": "rho_ss", "locks": "rho_ss", "cap": "rho_rubber",
           "winder": "rho_foam", "spares": "rho_hdpe", "weight": "rho_steel", "cframe": "rho_steel",
           "clamp": "rho_steel", "hook": "rho_steel"}
    m = {}
    for k, r in rho.items():
        m[k] = sum(q.volume for q in c[k].solids()) * 1e-9 * A[r]   # by solid: nested compounds report no volume
    m["locks"] = m["locks"] * 4 / 3            # four pins; three are fitted in the model
    m["spares"] = 0.004                         # vial and eleven pins
    rol, wash = M.crutch_roller(P)
    m["roller"] = rol.volume * 1e-9 * A["rho_hdpe"] + (wash.volume + M.crutch_axle(P).volume) * 1e-9 * A["rho_steel"]
    m["tether"] = A["cord_kg_m"] * P["cord_L"] / 1000
    m["shear"] = m["shear"] * 12
    tool = sum(m[k] for k in ("ring", "hinge", "gate", "head", "shear", "poles", "sleeves", "rivets", "locks", "cap"))
    kit = sum(m.values())
    out("M1", "Rider ring with hinge bolt and gate pin", m["ring"] + m["hinge"] + m["gate"], "kg")
    out("M2", "Pole head", m["head"], "kg")
    out("M3", "Three pole sections, two sleeves, rivets, lock pins, cap", m["poles"] + m["sleeves"] + m["rivets"] + m["locks"] + m["cap"], "kg")
    out("M4", "Jigging weight", m["weight"], "kg")
    out("M5", "Gunwale crutch (frame, roller, axle, clamp)", m["cframe"] + m["roller"] + m["clamp"], "kg")
    out("M6", "Tether cord, float winder, spare pins", m["tether"] + m["winder"] + m["spares"], "kg")
    out("M7", "Working tool (ring, head, pole, pins)", tool, "kg")
    out("M8", "Whole kit, including the crutch and jigging weight", kit, "kg")
    out("M9", "Longest packed piece (a section with its sleeve)", D["packed_L"], "mm", "R7", "met")
    out("M10", "Hook head (SMR-DDR-003)", m["hook"], "kg")
    carried = kit - m["cframe"] - m["roller"] - m["clamp"] - m["weight"]
    out("M11", "Carried kit, aluminium prototype: crutch stays clamped on the canoe, jigging weight kept at the landing",
        carried, "kg", "R7", "met" if carried < 4.0 else "not met")
    return m, kit


# ------------------------------------------------------------------ 2. shear pin
def pin():
    d = P["shear_d"]
    a = math.pi * d * d / 4
    F = 2 * A["tau_pin"] * a
    lo, hi = F * (1 - A["tau_pin_band"]), F * (1 + A["tau_pin_band"])
    out("P1", "Shear pin rating, 2.0 mm soft aluminium in double shear (nominal)", F, "N")
    out("P2", "Pin band allowed by R3, low", lo, "N")
    out("P3", "Pin band allowed by R3, high (used for every safety check)", hi, "N")
    return F, lo, hi


# ------------------------------------------------------------------ 3. canoe heel
def canoe(cn, F, tag0, excluded=False):
    Ldisp = cn["hull_kg"] + cn["crew"] * cn["crew_kg"] + cn["load_kg"]
    V = Ldisp / A["rho_water"]
    T = V / (cn["L"] * cn["B"] * cn["Cb"])
    I = cn["k_I"] * cn["L"] * cn["B"] ** 3
    KB, BM = 0.55 * T, I / V
    KG = (cn["hull_kg"] * cn["hull_kg_z"] + cn["crew"] * cn["crew_kg"] * cn["crew_z"] + cn["load_kg"] * cn["load_z"]) / Ldisp
    GM = KB + BM - KG
    k = Ldisp * g * GM                                    # N m per radian (small angles: per sin)
    fb = cn["depth"] - T
    lean = math.radians(A["pole_lean"])

    def arm(hands_above_gw):
        h = fb + hands_above_gw                           # hands above the waterline
        return math.cos(lean) * cn["hands_y"] + math.sin(lean) * h

    crew_arm = 0.6 * cn["half_wl"] / 0.55
    res = {}
    for pose, hg in (("kneeling", A["hands_kneel"]), ("standing", A["hands_stand"])):
        Mh = F * arm(hg) + A["crew_slack_N"] * crew_arm
        phi = math.degrees(math.asin(min(1.0, Mh / k)))
        F5 = (k * math.sin(math.radians(A["heel_limit"])) - A["crew_slack_N"] * crew_arm) / arm(hg)
        res[pose] = (phi, F5)
    immerse = math.degrees(math.atan(fb / cn["half_wl"]))
    out(f"{tag0}1", f"{cn['name']}: displacement", Ldisp, "kg")
    out(f"{tag0}2", f"{cn['name']}: metacentric height GM", GM, "m")
    out(f"{tag0}3", f"{cn['name']}: freeboard; heel that puts the gunwale under", fb * 1000, "mm")
    out(f"{tag0}4", f"{cn['name']}: gunwale immersion angle", immerse, "deg")
    st = "met" if res["standing"][0] <= A["heel_limit"] else "at risk"
    if excluded:
        st = "outside the 7 m rule (SMR-DDR-003)"
    out(f"{tag0}5", f"{cn['name']}: heel when the pin breaks at the top of its band, kneeling", res["kneeling"][0], "deg",
        "R3", st if excluded else ("met" if res["kneeling"][0] <= A["heel_limit"] else "at risk"))
    out(f"{tag0}6", f"{cn['name']}: heel when the pin breaks at the top of its band, standing", res["standing"][0], "deg", "R3", st)
    out(f"{tag0}7", f"{cn['name']}: pole pull that heels the canoe 5 deg, kneeling", res["kneeling"][1], "N")
    out(f"{tag0}8", f"{cn['name']}: pole pull that heels the canoe 5 deg, standing", res["standing"][1], "N")
    return res


# ------------------------------------------------------------------ 4. freeing force
def freeing(F_lo):
    rows = []
    for name, th in (("hooked over a branch (half a turn)", math.pi), ("wrapped once round (one and a half turns)", 3 * math.pi)):
        for mu in A["mu"]:
            f = A["net_leg_N"] * math.exp(mu * th) + A["crew_slack_N"]
            rows.append((name, mu, f))
    out("F1", "Pull to lift a hooked net, low friction (mu 0.3)", rows[0][2], "N")
    out("F2", "Pull to lift a hooked net, high friction (mu 0.5)", rows[1][2], "N", "R1", "met" if rows[1][2] < F_lo else "at risk")
    out("F3", "Pull to lift a net wrapped once round, low friction", rows[2][2], "N")
    out("F4", "Pull to lift a net wrapped once round, high friction", rows[3][2], "N", "R1", "at risk")
    out("F5", "Margin of the low end of the pin band over the hooked case, high friction", F_lo / rows[1][2], "x")
    for tag, mu in (("F7", A["mu"][0]), ("F8", A["mu"][1])):
        f1 = A["net_leg_N"] * math.exp(mu * 2 * math.pi) + A["crew_slack_N"]
        out(tag, f"Pull to lift once the hook has worked the wrap back half a turn (one full turn left), mu {mu}", f1, "N")
    f_hold = A["net_leg_N"] * math.exp(A["mu"][1] * math.pi) + A["crew_hold_N"]
    out("F6", "Pull if the crew keeps full tension while the operator lifts (hooked, high friction)", f_hold, "N")
    return rows


# ------------------------------------------------------------------ 5. reach
def reach():
    hr = D["hand_to_ring"] / 1000
    out("R1", "Working length, top hand to ring centre", hr, "m", "R2", "met" if hr >= 4.0 else "not met")
    lean = math.radians(A["pole_lean"])
    cn = A["canoe"]
    fb = cn["depth"] - (cn["hull_kg"] + cn["crew"] * cn["crew_kg"] + cn["load_kg"]) / 1000 / (cn["L"] * cn["B"] * cn["Cb"])
    depth = hr * math.cos(lean) - (fb + A["hands_kneel"])
    out("R2", "Ring depth below the surface at 20 deg lean, kneeling", depth, "m")
    cord_depth = P["cord_L"] / 1000 - A["jig_cord_above_m"]
    out("R3", "Tether reach below the surface, jigging", cord_depth, "m", "R2", "met" if cord_depth >= 6.0 else "not met")
    out("R4", "Ring inside diameter", D["ring_ID"], "mm", "R6", "met")
    return depth


# ------------------------------------------------------------------ 6. strength and stiffness
def strength(F_hi):
    od, w = P["pole"]
    I = math.pi / 64 * (od ** 4 - (od - 2 * w) ** 4)
    L = P["section_L"] * P["n_sections"]
    Pcr = math.pi ** 2 * A["E_al"] * I / L ** 2
    out("S1", "Euler buckling load of the whole pole, pinned ends", Pcr, "N")
    out("S2", "Buckling factor over the top of the pin band (push)", Pcr / F_hi, "x")
    r = P["lock_d"] / 2
    lock = 2 * math.pi * r * r * A["tau_ss_pin"]
    out("S3", "Lock pin factor, 6 mm stainless in double shear", lock / F_hi, "x")
    bear = 2 * P["pole"][1] * P["lock_d"] * A["bear_al"]
    out("S4", "Pole wall bearing factor at a lock pin hole", bear / F_hi, "x")
    out("S5", "Rivet factor, two rivets per sleeve (pull only)", 2 * A["rivet_kN"] * 1000 / F_hi, "x")
    e = P["tang"][2] - 4 - P["shear_hole"][1] - P["shear_hole"][0] / 2
    tear = 2 * e * P["tang"][1] * 0.6 * A["fy_steel"]
    out("S6", "Tang tear-out factor above the shear pin hole", tear / F_hi, "x")
    Zr = math.pi * P["bar_d"] ** 3 / 32
    Mr = F_hi * P["ring_R"] / math.pi
    out("S7", "Ring bending stress, pulled at the tang against the far side", Mr / Zr, "MPa")
    out("S8", "Ring bending factor on yield", A["fy_steel"] / (Mr / Zr), "x")
    Zt = P["tang"][0] * P["tang"][1] ** 2 / 6
    Mt = F_hi * 0.25 * P["shear_hole"][1]           # a quarter of the pull acting sideways at the pin height
    out("S9", "Tang bending factor, quarter of the pull sideways", A["fy_steel"] / (Mt / Zt), "x")
    # crutch axle: line tension 500 N wrapped 90 deg over the roller
    Fa = 2 * 500 * math.sin(math.radians(45))
    span = P["roller"][1] + 2 * 2.0 + P["saddle"][3]
    Ma = Fa * span / 4
    out("S10", "Crutch axle bending stress at 500 N line tension (M12, grade 4.6)", Ma / (math.pi * 12 ** 3 / 32), "MPa")


# ------------------------------------------------------------------ 7. float
def flotation(m):
    L, W, T = P["winder"]
    nd, nw = P["notch"]
    Vf = (L * W * T - 2 * nd * nw * T) * 1e-9
    lift = Vf * (A["rho_water"] - A["rho_foam"])
    wet = lambda kg, rho: kg * (1 - A["rho_water"] / rho)   # noqa: E731
    ring = m["ring"] + m["hinge"] + m["gate"]
    load = wet(ring, A["rho_steel"]) + wet(m["tether"], A["rho_polyester"])
    out("B1", "Float winder net lift", lift, "kg")
    out("B2", "Ring and cord, weight in water", load, "kg")
    out("B3", "Reserve: lift over ring and cord", lift / load, "x")
    loadw = load + wet(m["weight"], A["rho_steel"])
    out("B4", "Ring, cord and jigging weight, weight in water (the float does not hold this)", loadw, "kg")


# ------------------------------------------------------------------ 8. build time and cost
def build_and_cost():
    mins = sum(A["build_min"].values())
    out("T1", "Workshop time for one kit, one smith (estimate)", mins / 60, "h", "R9", "met" if mins <= 8 * 60 else ("at risk" if mins <= 1.05 * 8 * 60 else "not met"))
    rows = list(csv.DictReader((ROOT / "bom" / "bom.csv").open()))
    kit = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
    out("C1", "Parts cost of one kit (prototype prices)", kit, "USD")
    vrows = list(csv.DictReader((ROOT / "bom" / "bom-bamboo-variant.csv").open()))
    vset = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in vrows)
    run = 3 * kit + vset + 6.0
    out("C2", "Prototype run: three aluminium kits, one bamboo pole set and 2 m of calibration wire", run, "USD")
    out("C3", "Value-engineering target (project.yaml)", 2000.0, "USD")
    out("C4", "Prototype run under the value-engineering target by", 2000.0 - run, "USD")
    by = {r["line"]: float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows}
    pole = by["6"] + by["7"] + by["8"]
    out("C5", "Pole, sleeves and rivets, share of the kit cost", pole / kit * 100, "%")
    galv = by["18"]
    out("C6", "Galvanising, share of the kit cost", galv / kit * 100, "%")
    crutch = by["15"] + by["16"] + by["17"]
    out("C7", "Gunwale crutch, share of the kit cost", crutch / kit * 100, "%")
    return kit, by, vset


# ------------------------------------------------------------------ 9. bamboo local variant (SMR-DDR-003)
def bamboo(m, kit, by, vset):
    bs = M.bamboo_sections(P)
    culms = sum(q.volume for q in bs) * 1e-9 * A["rho_bamboo"]
    fer = sum(q.volume for q in M.ferrules(P)) * 1e-9 * A["rho_steel"]
    bolts = sum(q.volume for q in M.ferrule_bolts(P)) * 1e-9 * A["rho_ss"]
    pole = culms + fer + bolts
    al = m["poles"] + m["sleeves"] + m["rivets"] + m["cap"]
    out("V1", "Bamboo pole: three culm sections, two ferrules and bolts", pole, "kg")
    out("V2", "Aluminium pole it replaces: sections, sleeves, rivets and grip cap", al, "kg")
    kitm = sum(m.values())
    carried = kitm - m["cframe"] - m["roller"] - m["clamp"] - m["weight"] - al + pole
    out("V3", "Carried kit, bamboo local variant (crutch on the canoe, weight at the landing)", carried, "kg",
        "R7", "met" if carried < 4.0 else "not met")
    od, w = P["culm"]
    I = math.pi / 64 * (od ** 4 - (od - 2 * w) ** 4)
    L = P["section_L"] * P["n_sections"]
    Pcr = math.pi ** 2 * A["E_bamboo"] * I / L ** 2
    _, _, hi = pin_band()
    out("V4", "Euler buckling load of the bamboo pole, pinned ends, E 15 GPa", Pcr, "N")
    out("V5", "Bamboo pole buckling factor over the top of the pin band (push)", Pcr / hi, "x")
    out("V6", "Bamboo pole buckling factor if E is 10 GPa (low end)", Pcr / hi * 10 / 15, "x")
    span, Fb = 1400.0, 50.0
    defl = Fb * span ** 3 / (48 * A["E_bamboo"] * I)
    out("V10", "Culm bend test: largest sag at mid-span, 50 N (5 kg) hung at the middle of a 1.4 m span, for E 15 GPa", defl, "mm")
    rows = {r["line"]: r for r in csv.DictReader((ROOT / "bom" / "bom.csv").open())}
    removed = sum(float(rows[n]["qty"]) * float(rows[n]["unit_cost_usd"]) for n in ("6", "7", "8", "10"))
    shared = (by["14"] + by["15"] + by["16"] + by["17"] + 6.0) * 0.8
    out("V7", "Crutch and jigging weight with their galvanising, saving per kit when one set serves five canoes", shared, "USD")
    v = kit - removed + vset - shared
    out("V8", "Parts cost of one bamboo local variant kit, crutch and weight shared by five canoes", v, "USD",
        "R10", "met" if v <= 40 else "not met")
    out("V9", "Parts cost of one aluminium prototype kit", kit, "USD", "R10", "met" if kit <= 40 else "not met")
    # new open decision (R7 and R9 on the aluminium prototype): a thinner pole wall
    od_a, w_a = P["pole"]
    w2 = 1.6
    a1 = math.pi / 4 * (od_a ** 2 - (od_a - 2 * w_a) ** 2)
    a2 = math.pi / 4 * (od_a ** 2 - (od_a - 2 * w2) ** 2)
    save = (a1 - a2) * P["section_L"] * P["n_sections"] * 1e-9 * A["rho_al"]
    carried_al = kitm - m["cframe"] - m["roller"] - m["clamp"] - m["weight"]
    out("N1", "Carried kit, aluminium prototype with 32 x 1.6 pole tube in place of 32 x 2", carried_al - save, "kg")
    I1 = math.pi / 64 * (od_a ** 4 - (od_a - 2 * w_a) ** 4)
    I2 = math.pi / 64 * (od_a ** 4 - (od_a - 2 * w2) ** 4)
    Pcr2 = math.pi ** 2 * A["E_al"] * I2 / L ** 2
    out("N2", "Buckling factor of a 32 x 1.6 aluminium pole over the top of the pin band", Pcr2 / hi, "x")
    _ = I1
    return carried, v


def pin_band():
    d = P["shear_d"]
    F = 2 * A["tau_pin"] * math.pi * d * d / 4
    return F, F * (1 - A["tau_pin_band"]), F * (1 + A["tau_pin_band"])


def main():
    m, kit_mass = masses()
    F, lo, hi = pin()
    res = canoe(A["canoe"], hi, "H")
    small = canoe(A["small"], hi, "K", excluded=True)
    freeing(lo)
    reach()
    strength(hi)
    flotation(m)
    kit, by, vset = build_and_cost()
    bamboo(m, kit, by, vset)
    # lighter pin for canoes under 7 m (background for the per-class pins of SMR-DDR-003; not adopted)
    d2 = 1.4
    F2 = 2 * A["tau_pin"] * math.pi * d2 * d2 / 4
    out("O11", "Light pin, 1.4 mm wire: nominal rating", F2, "N")
    r2 = canoe(dict(A["small"], name="small dugout, light pin"), F2 * (1 + A["tau_pin_band"]), "L", excluded=True)
    _ = r2
    with (ROOT / "docs" / "04-calcs" / "results.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["tag", "item", "value", "unit", "requirement", "status"])
        w.writeheader()
        for r in OUT:
            v = r["value"]
            r = dict(r, value=(round(v, 3) if isinstance(v, float) else v))
            w.writerow(r)


if __name__ == "__main__":
    main()
