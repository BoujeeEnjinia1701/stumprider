"""StumpRider general arrangement sheet SMR-DWG-001, Rev P2 (TRL 3; SMR-DDR-002 applied).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/SMR-DWG-001.svg, .pdf and .png from the parametric model in cad/src/model.py
with .kit/drawing.py: the working end of the tool (ring, pins, pole head and the bottom of the pole)
in three views, the whole tool as a side elevation at 1:40, and the main sizes. Dimensions come from
PARAMS and derived(), so they follow any parameter change. The concept blueprint in media/ is
SMR-DWG-010; the making sketches are SMR-DWG-101 onward (cad/src/build_plan_media.py).
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Box, Compound, Pos, Rot  # noqa: E402
from drawing import Sheet, _t, project_views, INK, MUTED, _viewbox  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
DATE = "2026-10-03"
FULL_K = 1 / 40


def main():
    D = M.derived(P)
    work = ROOT / "cad" / "drawings" / "_ga_views"
    t = M.tool_parts(P)
    win = Pos(M.X_POLE, 0, 200) * Box(300, 300, 520)
    end = Compound([t["ring"], t["hinge"], t["gate"], t["head"], t["shear"], t["locks"] & win,
                    M.pole_sections(P)[0] & win, t["tether"] & Pos(0, 0, 100) * Box(400, 400, 260)])
    views = project_views(end, work)
    full = Rot(0, 90, 0) * Compound([t[k] for k in ("ring", "hinge", "gate", "head", "shear", "poles", "sleeves",
                                                     "rivets", "locks", "cap")])
    fv = project_views(full, work / "full")
    s = Sheet(project="StumpRider", title="Canoe-worked gillnet release tool: general arrangement",
              dwg_no="SMR-DWG-001", rev="P2", author="Amish Chadha", date=DATE, scale=None,
              material="Kit per bom/bom.csv. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Preliminary GA for TRL 3 (from cad/src/model.py)", DATE, "AC"),
                         ("P2", "SMR-DDR-002: design for construction", DATE, "AC")])
    s.add_ortho(views)
    vb = _viewbox(Path(fv["front"]).read_text())
    vw, vh = vb[2] * FULL_K, vb[3] * FULL_K
    x0, y0 = 279.0, 36.0
    s.add_svg(fv["front"], x0, y0, vw, vh, scale=FULL_K)
    s._layers += [
        _t(x0 + vw / 2, y0 + vh + 6, "WHOLE TOOL, ASSEMBLED", 2.8, 600, INK, "middle"),
        _t(x0 + vw / 2, y0 + vh + 10, "Scale 1:40; side elevation looking along +Y, ring on the left", 2.2, 400, MUTED, "middle"),
    ]
    s._dim(x0, y0 + vh, x0 + vw, y0 + vh, f"{vb[2] - 0.35:.0f}", "below", off=14)
    s.add_notes("Main sizes (mm unless stated)", [
        f"Rider ring: 12 bar, {D['ring_ID']:.0f} inside, {D['ring_OD']:.0f} outside",
        "Two halves, 2 gap at each joint; hinge M8 (+Y), gate pin 8 (-Y)",
        "Tang 6 x 28 x 84 on the fixed half; holes 10.5 (tether),",
        "  6.5 (jigging weight) and 2.1 (shear pin), 20, 46, 70 up",
        "Pole head: tube 38 x 3 x 120 on a 6 end plate; fork",
        "  cheeks 6 x 30, 8 apart; tang top 45 below the plate",
        "Shear pin: 2.0 soft aluminium wire, 30 long, ends bent",
        "Pole: three 1,450 sections, 32 x 2 aluminium; sleeves",
        "  38 x 2.8 x 200, two rivets below and a 6 pin above",
        f"Top hand to ring {D['hand_to_ring']:,.0f}; packed {D['packed_L']:,.0f}",
        "Pin rating 302 N nominal, 256 to 347 N band",
        "Third-angle; ring centre at the origin, pole on +X",
    ], x=276, y=118, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "SMR-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
