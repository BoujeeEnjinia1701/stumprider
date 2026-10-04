"""StumpRider concept media (TRL 3, constructable design of SMR-DDR-002), generated from the model.

Run from the repo root:  python cad/src/concept_media.py
Takes the kit from cad/src/model.py and renders the media set with .kit/concept.py:
media/hero.png (the tool standing beside a 1.75 m person, with the crutch, float winder and
jigging weight), media/exploded.png (the working end pulled apart, numbers match bom/bom.csv),
media/cutaway.png (the working end cut through the shear pin), media/concept-blueprint.png, .pdf
and .svg (SMR-DWG-010), media/model.glb and media/viewer.html. No flow diagram: the tool moves no
energy or material. Figures on the sheet come from docs/04-calcs/results.csv (SMR-CAL-001).
CONCEPT, NOT FOR FABRICATION.
"""
import csv
import functools
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import concept as K  # noqa: E402
from concept import Part, render_all  # noqa: E402
from build123d import Box, Compound, Pos  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
D = M.derived(P)
PROJECT = "StumpRider"
TITLE = "Canoe-worked release tool for gillnets snagged on drowned trees"

COLORS = {"ring": "#B45309", "hinge": "#6B7280", "gate": "#9CA3AF", "head": "#0F766E", "shear": "#DC2626",
          "poles": "#94A3B8", "sleeves": "#475569", "rivets": "#374151", "locks": "#6B7280", "cap": "#111827",
          "tether": "#EA580C", "winder": "#F97316", "spares": "#E5E7EB", "weight": "#78350F",
          "cframe": "#1D4ED8", "roller": "#F5F5F4", "clamp": "#4B5563",
          "hook": "#9A3412"}
LINE = "#A8A29E"


def R():
    rows = {r["tag"]: r for r in csv.DictReader((ROOT / "docs" / "04-calcs" / "results.csv").open())}
    return lambda t: float(rows[t]["value"])


def kit_parts():
    c = M.build_components(P)
    return [Part(name, c[key], COLORS[key], num) for key, (num, name) in M.BOM.items()]


def working_end(explode=True):
    """Ring, head, bottom of the pole and pins, pulled apart along the way each comes off."""
    t = M.tool_parts(P)
    win = Pos(M.X_POLE, 0, 205) * Box(200, 200, 150)
    pole = M.pole_sections(P)[0] & win
    e = (lambda v: v) if explode else (lambda v: (0, 0, 0))
    return [
        Part("Net line (context)", M.net_line(-120, 200), LINE, None, e((0, 0, 0))),
        Part("Rider ring, fixed half with tang", M.ring_half(P, +1), COLORS["ring"], 1, e((0, 0, 0))),
        Part("Rider ring, swinging half", M.ring_half(P, -1), "#D97706", 1, e((-110, 0, 0))),
        Part("Hinge bolt M8", M.hinge_bolt(P), COLORS["hinge"], 2, e((-60, 90, 0))),
        Part("Gate pin 8 mm", M.gate_pin(P), COLORS["gate"], 3, e((-60, -110, 0))),
        Part("Shear pin, 2 mm", M.shear_pin(P), COLORS["shear"], 5, e((0, -120, 0))),
        Part("Pole head", M.pole_head(P), COLORS["head"], 4, e((0, 0, 110))),
        Part("Lock pin 6 mm", M.lock_pins(P)[0], COLORS["locks"], 9, e((0, -90, 190))),
        Part("Pole section, bottom", pole, COLORS["poles"], 6, e((0, 0, 200))),
        Part("Tether cord", t["tether"] & Pos(100, 0, 60) * Box(200, 200, 140), COLORS["tether"], 11, e((90, 0, 0))),
    ]


def cutaway():
    """The working end cut on the plane through the pole axis along the shear pin (keeps the -X half)."""
    cut = Pos(M.X_POLE - 1000, 0, 0) * Box(2000, 2000, 2000)
    out = []
    for q in working_end(explode=False):
        if q.bom is None:
            continue
        s = q.shape & cut
        if s is not None and s.volume > 1e-3:
            out.append(Part(q.name, s, q.color, q.bom))
    return out


def web():
    """Coarse glTF tessellation (1 mm chord, 0.35 rad) keeps media/model.glb a few MB."""
    import build123d as bd
    orig = bd.export_gltf
    bd.export_gltf = functools.partial(orig, linear_deflection=1.0, angular_deflection=0.35)
    try:
        return K.export_web_model(kit_parts(), "media", title=f"{PROJECT}: {TITLE}")
    finally:
        bd.export_gltf = orig


def main():
    if "exploded" in sys.argv:
        return exploded_only()
    r = R()
    web()
    render_all(
        kit_parts(), project=PROJECT, title=f"{TITLE} concept", dwg_no="SMR-DWG-010",
        key_figures=[
            f"Rider ring 12 mm steel bar, {D['ring_ID']:.0f} mm inside, hinged; opens for lines 4 to 16 mm",
            f"Pole three 1.45 m aluminium sections; {r('R1'):.2f} m from top hand to ring",
            f"Shear pin 2 mm soft aluminium, {r('P1'):.0f} N nominal ({r('P2'):.0f} to {r('P3'):.0f} N)",
            f"Design canoe heels {r('H5'):.1f} deg (kneeling) when the pin breaks",
            f"Jigging weight {r('M4'):.1f} kg and {P['cord_L'] / 1000:.0f} m tether for snags to {r('R3'):.0f} m",
            f"Hook head pins into the same fork for nets wrapped round a branch",
            f"Carried {r('M11'):.2f} kg (bamboo variant {r('V3'):.2f} kg); about USD {r('C1'):.0f} a kit; nobody enters the water",
        ],
        scale_figure=True, web_model=False, cut=False,
    )
    exploded_only()


def exploded_only():
    """The exploded view and the cutaway of the working end (run alone with: concept_media.py exploded)."""
    K._render(working_end(), ROOT / "media" / "exploded.png", offsets=True, labels=True, elev=20, azim=-50,
              size=(10, 7.5), title=f"{PROJECT}: exploded view of the working end",
              note="Ring, pins, pole head and the bottom of the pole pulled apart along the way each comes off; "
                   "seen from the front right and above, 20 deg elevation; numbers match bom/bom.csv; grey is the net line")
    K._render(cutaway(), ROOT / "media" / "cutaway.png", elev=10, azim=-20, size=(10, 7.5),
              title=f"{PROJECT}: cutaway of the working end",
              note="Cut on the plane through the pole axis and along the shear pin, the outer half removed; seen from outside "
                   "the ring (from +X, a little to the front), 10 deg elevation. The 2 mm pin is the only link between the fork and the tang, so a push or a pull "
                   "above its rating breaks it and the pole comes away")
    for d in ("_views", "_views_fig"):
        shutil.rmtree(ROOT / "media" / d, ignore_errors=True)


if __name__ == "__main__":
    main()
