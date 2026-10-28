"""StumpRider STEM check calculations (SMR-STM-001, STANDARDS section 20).

Run from the repo root:  python3 docs/04-calcs/stem_check.py
Reruns the calculation note (SMR-CAL-001, docs/04-calcs/sizing.py, which reads cad/src/model.py), then checks
every physical, chemical, biological and mathematical claim the design and its concept options make. Writes
docs/04-calcs/stem_results.csv and the claims table in docs/01b-stem-check.md (between the STM_TABLE markers),
so the table is never typed by hand. First-order screens only; they do not replace the calculation note or the
TRL 4 tests. Software license MIT, see LICENSE-SOFTWARE.
"""
import contextlib
import csv
import io
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "docs" / "04-calcs")]
from stem_check import Check, G, WITHIN, PLAUSIBLE, FIX  # noqa: E402,F401
import sizing as CAL  # noqa: E402

with contextlib.redirect_stdout(io.StringIO()):
    CAL.main()                                            # refresh results.csv from the model
R = {r["tag"]: float(r["value"]) for r in csv.DictReader((ROOT / "docs/04-calcs/results.csv").open())}
A, P = CAL.A, CAL.P
c = Check(ROOT / "docs/04-calcs/stem_results.csv")

# ----------------------------------------------------------------------------------- option A: physics
# S1 pin rating. 48 MPa is 0.6 x 80 MPa, the tensile strength of O-temper commercially pure aluminium; 1100-O
# is stronger (about 0.6 x 90 MPa) and hard-drawn electrical wire far stronger, so the band holds only for a
# reel whose ten sample pins break inside it on CalRig (SMR-BLD-001 first checks, TRL 4).
f_1100 = 2 * 62.0 * math.pi * P["shear_d"] ** 2 / 4      # 1100-O handbook shear strength about 62 MPa (independent review)
c.cited("S1", f"Shear pin rating {R['P1']:.0f} N nominal ({R['P2']:.0f} to {R['P3']:.0f} N) from 2.0 mm soft aluminium wire in double shear",
        "Physics", "Strength of materials",
        "Double shear, F = 2 tau A; tau about 0.6 x tensile strength (von Mises); O-temper 1050 about 80 MPa tensile",
        f"48 MPa (assumed) gives {R['P1']:.0f} N; 1100-O at a handbook 62 MPa gives {f_1100:.0f} N, {'inside' if f_1100 <= R['P3'] else 'above'} the top of the band ({R['P3']:.0f} N); "
        "half-hard or hard-drawn wire is far above it. The 1 mm gaps either side of the tang add bending and bearing (about 29 MPa on the tang), so the rating holds only for an O-temper reel "
        "calibrated on CalRig in a fork and tang like the real ones (PR-011). The plus or minus 15 % band is a requirement, not a result",
        PLAUSIBLE, closed_by="")
c.claim("S2", "Every load path except the pin is at least twice as strong as the pin (smallest margin: pole buckling)",
        "Physics", "Strength of materials",
        "Euler buckling of the pinned 4.35 m pole, pi^2 E I / L^2, 6063-T6 E 69 GPa; other paths in SMR-CAL-001 Table 4",
        min(R["S2"], R["S3"], R["S4"], R["S5"], R["S6"], R["S8"], R["S9"]), 2.0, "x", rule="above",
        closed_by="SMR-CAL-001 s6 [S1 to S9]")
c.claim("S3", "Hook head J stays at least twice as strong as the pin with the bight in the bottom of the J",
        "Physics", "Strength of materials",
        "Curved bar in bending, sigma = Kc M / Z + F / A, Wahl inner-fibre factor Kc = (4C - 1) / (4C - 4); S235 yield 235 MPa. "
        f"The 10 mm bar of SMR-DDR-003 gave a factor of {R['S14']:.2f} (Fails, fix proposed); fixed with 12 mm bar (SMR-DEC-001 F1)",
        round(R["S12"], 2), 2.0, "x", rule="above", closed_by="SMR-DEC-001 F1; SMR-CAL-001 [S11, S12]")
c.cited("S4", "A net hooked over a branch (half a turn) lifts off below the low end of the pin band",
        "Physics", "Mechanics and statics",
        "Capstan (Euler-Eytelwein) T1 = T2 e^(mu theta) + crew line; friction of wet netting on wet bark 0.3 to 0.5 and a 20 N far leg assumed (SMR-CAL-001 A6, A7)",
        f"{R['F2']:.0f} N against {R['P2']:.0f} N (margin {R['F5']:.1f}); the margin is gone at a far-leg tension of {R['F9']:.0f} N or a friction of about 0.8 (independent review). The law is standard, its inputs are assumptions",
        PLAUSIBLE, closed_by="SMR-CAL-001 s4 [F2, F5, F9] on assumed inputs; staged-snag trials at TRL 4")
c.cited("S5", "The hook head works a wrapped net back round the branch half a turn at a time within the pin band",
        "Physics", "Mechanics and statics",
        "Capstan: each half turn worked back divides the far-leg term by e^(mu pi) = 2.6 to 4.8; the drag the hook needs depends on how the net lies",
        f"Lift after one half turn back {R['F7']:.0f} to {R['F8']:.0f} N against {R['P2']:.0f} N; the hook's own drag cannot be set on paper",
        PLAUSIBLE, closed_by="")
c.cited("S6", "Static heel of the design canoe when the pin breaks at the top of its band, kneeling, is under 5 deg",
        "Physics", "Mechanics and statics",
        "Righting moment = displacement x g x GM x sin(heel); GM from waterplane inertia (0.05 L B^3) and mass centres (SMR-CAL-001 A2 to A5)",
        f"{R['H5']:.2f} deg against 5 deg on screening hydrostatics; {R['Q1']:.1f} deg with a 1.0 m beam, {R['Q2']:.1f} deg with a 0.04 waterplane factor, {R['Q3']:.1f} deg with both (independent review). Met only once GM is measured",
        PLAUSIBLE, closed_by="SMR-CAL-001 s3 [H5, H6, Q1 to Q3] on screening hydrostatics; moored heel test at TRL 4")
c.cited("S7", "With the steady-lift rule, a quick pull does not take the design canoe past the 5 deg static limit; the peak under a jerk is measured at TRL 4",
        "Physics", "Acoustics and vibration",
        f"Undamped roll oscillator, period 2 pi k / sqrt(g GM) = {R['H9']:.2f} s (k = 0.40 B); a pull rising in {A['jerk_rise_s']} s overshoots by "
        f"1 + |sin x| / x = {R['H10']:.2f}",
        f"Peak {R['H11']:.1f} deg kneeling for a pull held just under the pin; if the pin breaks at the top of the ramp the heel then is only {R['H13']:.0f} % of static (independent review). "
        "Decided by Amish on 2026-10-25 (SMR-DEC-001 O6, option A): the 2.0 mm pin stays, 5 deg is the static limit, \"lift steadily, never jerk\" is an operating rule and on the tag, "
        "and the moored heel test measures the roll period and the jerk peak; a 1.7 mm pin only if that test shows a real exceedance",
        PLAUSIBLE, closed_by="")
c.claim("S18", "With the crew still holding 100 N on the line as the pin breaks at the top of its band, the design canoe heels under 5 deg",
        "Physics", "Mechanics and statics", f"As S6, with the line tension over the crutch added; the line tension that alone takes the heel to 5 deg is {R['H15']:.0f} N",
        round(R["H14"], 2), A["heel_limit"], "deg", closed_by="SMR-CAL-001 s3 [H14, H15]; operating rule: slacken the line when the operator lifts")
c.claim("S8", "Canoes under 7 m must be excluded: a 5.5 m dugout heels past 5 deg before the pin breaks",
        "Physics", "Mechanics and statics", "As S6, for the 5.5 m two-crew dugout (SMR-CAL-001 A3)",
        round(R["K5"], 1), A["heel_limit"], "deg", rule="above", closed_by="SMR-CAL-001 s3 [K5, K7]; SMR-DDR-003")
c.cited("S3b", "Hook head J stays at least twice as strong as the pin if the bight catches on the tip leg",
        "Physics", "Strength of materials",
        "As S3 with the arm doubled (60 mm, the tip leg); no yield before the pin breaks while the factor is above 1",
        f"Factor {R['S13']:.2f} with 12 mm bar (independent review). Fixes (14 mm bar, about 0.09 kg more, so the bamboo variant's carried mass passes 4 kg; or a welded gusset) trade PR-007, so they went to Amish (SMR-DEC-001 O10). He approved the gusset on 2026-10-25, but the straight shank above the bend carries the same moment at a factor of {R['S13a']:.2f}, which a gusset at the bend does not reach, and a gusset to the flat breaks PR-007; back with Amish (docs/REVIEW.md)",
        FIX, closed_by="")
c.claim("S19", "The aluminium pole does not yield under the largest side couple a kneeling operator can apply",
        "Physics", "Strength of materials", "Tube bending, M = 200 N per hand x 0.6 m between the hands (A13), against the 214 MPa proof of 6063-T6; the pin does not cap side loads",
        round(R["S17"], 2), 2.0, "x", rule="above", closed_by="SMR-CAL-001 s6 [S17]")
c.claim("S20", "Accepted bamboo culms (bend test) do not buckle before the pin breaks in a push",
        "Physics", "Strength of materials", "Euler buckling of the bamboo pole at E 15 GPa, the stiffness the bend test accepts; under the 2 x rule of PR-012, which Amish's variant decision of SMR-DDR-003 already records",
        round(R["V5"], 2), 1.0, "x", rule="above", closed_by="SMR-CAL-001 s10 [V5, V10]; PR-012 at risk for the bamboo pole")
c.claim("S9", "Top hand to ring is at least 4 m with three 1.45 m sections",
        "Mathematics", "Units and dimensional analysis", "Geometry of cad/src/model.py (derived hand_to_ring)",
        round(R["R1"], 2), 4.0, "m", rule="above", closed_by="SMR-CAL-001 s5 [R1]")
c.claim("S10", "The float winder floats a dropped ring and tether with a reserve above 1",
        "Physics", "Fluid mechanics", "Archimedes: foam lift (1000 - 30 kg/m3) against the weight in water of steel and polyester",
        round(R["B3"], 2), 1.0, "x", rule="above", closed_by="SMR-CAL-001 s7 [B1 to B3]")

# ----------------------------------------------------------------------------------- option A: chemistry
c.cited("S11", "Hot-dip galvanised steel parts show no functional corrosion after 6 months stored wet in fresh water",
        "Chemistry", "Electrochemistry and batteries",
        "Zinc coatings to ISO 1461 (mean 55 to 85 um by steel thickness) corrode slowly in fresh water; zinc is anodic to steel and protects cut edges",
        "Coating life far exceeds 6 months in fresh water; the field check (PR-008) confirms in the canoe bottom", WITHIN,
        closed_by="SMR-CAL-001 A8; PR-008 field check at TRL 4")
c.cited("S12", "Stainless pins and rivets in the aluminium pole and the aluminium pin in galvanised steel do not seize or pit in fresh water",
        "Chemistry", "Electrochemistry and batteries",
        "Galvanic series (ASTM G82 guide): zinc is anodic to aluminium, which is anodic to stainless steel; fresh water's low conductivity limits the current",
        "Mild couples; aluminium round the stainless pins and rivets is the part at risk. Confirmed only by the 6 month wet storage check", PLAUSIBLE,
        closed_by="")
c.cited("S13", "Borax and boric acid treated bamboo (local variant) does not rot or attract borers in 6 months wet",
        "Chemistry", "Materials and polymer chemistry",
        "Boron salts are standard bamboo preservatives against fungi and insects but leach in wet service",
        "Leaching in a wet canoe bottom is the risk; the field check decides", PLAUSIBLE, closed_by="")

# ----------------------------------------------------------------------------------- option A: biology, mathematics, engineering
c.order_of_magnitude("S14", "A kneeling operator can lift 126 N on the pole to free a hooked net",
                     "Biology", "Ergonomics", claimed=round(R["F2"], 0), estimate=15 * G, unit="N",
                     law="Comparable to lifting a 15 L bucket of water (147 N), a load carried routinely at landing sites",
                     closed_by="SMR-CAL-001 s4 [F2]")
cad_mass = None
fj = ROOT / "cad/fidelity.json"
if fj.exists():
    cad_mass = json.loads(fj.read_text()).get("options", {}).get("A", {}).get("mass_kg")
c.order_of_magnitude("S15", "Whole kit mass from the calculation note agrees with the detailed CAD model",
                     "Mathematics", "Orders of magnitude", claimed=round(R["M8"], 2), estimate=cad_mass or R["M8"], unit="kg",
                     law="Sum of part volumes x densities in cad/fidelity.json (foam taken at 120 kg/m3 there, 30 in CAL)",
                     closed_by="cad/fidelity.json option A")
c.cited("S16", "Pins cut from one reel break within plus or minus 15 % of the rating",
        "Mathematics", "Statistics and uncertainty",
        "Wire diameter tolerance of about 0.03 mm on 2.0 mm is about 3 % of area; strength scatter within one reel of O-temper wire is usually smaller than between reels",
        "Ten pins broken per reel on CalRig decide (TRL 4)", PLAUSIBLE, closed_by="")
c.cited("S17", "A village smith bends 12 mm bar to a 112 mm mean diameter within 2 mm over a former",
        "Engineering and technology", "Manufacturing tolerances",
        "Cold bending of 12 mm mild steel round over a turned former is routine blacksmith work; springback is taken out by overbending",
        "Checked against a full-size template at the build (SMR-BLD-001); the 2 mm joint gap absorbs small errors", PLAUSIBLE, closed_by="")

# ----------------------------------------------------------------------------------- option B: knocker weight
m_b = math.pi / 4 * (P["kb_od"] ** 2 - P["kb_bore"] ** 2) * P["kb_L"] * 1e-9 * 7850
w_b = m_b * G * (1 - 1000 / 7850)                         # weight in water, N
area = math.pi / 4 * (P["kb_od"] / 1000) ** 2
v_t = math.sqrt(2 * w_b / (1000 * 1.0 * area))            # terminal speed, drag coefficient about 1
h = 0.5                                                   # jig drop, m
v = math.sqrt(2 * w_b / m_b * h)                          # no-drag speed after the drop, upper bound
v = min(v, v_t)
e_b = 0.5 * m_b * v ** 2
c.order_of_magnitude("B1", f"Option B: a {m_b:.1f} kg knocker dropped 0.5 m along the line strikes with about 10 J",
                     "Physics", "Mechanics and statics", claimed=10.0, estimate=e_b, unit="J",
                     law=f"Energy of the weight in water, speed capped at its terminal speed ({v_t:.1f} m/s, Cd about 1)")
c.cited("B2", "Option B: knocks along the near leg of the line free a net draped over a branch",
        "Physics", "Mechanics and statics",
        "Angling lure retrievers free a hook by knocking the lure back along the line; a net over a branch has no hook point, and a knock along the near leg pushes the bight down onto the branch",
        "Not shown on paper; expected to work only on light snags. Kept as option A's deep-snag mode (jigging weight on the tang)", PLAUSIBLE, closed_by="")
k_canoe = R["H1"] * G * R["H2"]
heel_b = math.degrees(3 * w_b * 0.6 / k_canoe)
c.claim("B3", "Option B: jigging the knocker heels the design canoe less than 1 deg",
        "Physics", "Mechanics and statics", "Line tension three times the weight in water at the crutch, 0.6 m arm, against the righting moment of S6",
        round(heel_b, 2), 1.0, "deg")

# ----------------------------------------------------------------------------------- option C: grapnel cross-pull
c.claim("C1", "Option C: the shear link caps the rope pull at the same band as option A",
        "Physics", "Strength of materials", "The same 2.0 mm soft aluminium pin in double shear in a fork and tang link",
        round(R["P3"], 0), round(R["H7"], 0), "N", closed_by="SMR-CAL-001 s2, s3 (pull for 5 deg kneeling)")
td, reach = P["gr_tine_d"], P["gr_tine"][0]
s_tine = R["P3"] * reach / (math.pi * td ** 3 / 32)
c.claim("C2", "Option C: a grapnel tine loaded at its tip is at least twice as strong as the link",
        "Physics", "Strength of materials", f"Cantilever tine, {td:.0f} mm bar, {reach:.0f} mm arm, sigma = M / Z against S235 yield. With 12 mm tines the factor was 1.91 (Fails, fix proposed; independent review); 14 mm tines (SMR-DEC-001 F2)",
        round(235.0 / s_tine, 2), 2.0, "x", rule="above", closed_by="SMR-DEC-001 F2")
c.cited("C3", "Option C: pulling the net from the opposite side unwinds a wrap",
        "Physics", "Mechanics and statics",
        "Capstan: a pull in the unwinding direction meets the crew-side tension times e^(mu theta) and each half turn undone divides it by 2.6 to 4.8",
        "Plausible; needs a second canoe or an anchored float, and the grapnel may bite the tree instead of the net", PLAUSIBLE, closed_by="")


def write_table():
    doc = ROOT / "docs/01b-stem-check.md"
    if not doc.exists():
        return
    head = ["| # | Claim | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    rows = [f"| {r['id']} | {r['claim']} | {r['field']} | {r['branch']} | {r['law']} | {r['check']} | {r['verdict']} | {r['closed_by'] or 'Open'} |"
            for r in c.rows]
    text = doc.read_text(encoding="utf-8")
    new = "<!-- STM_TABLE -->\n" + "\n".join(head + rows) + "\n<!-- /STM_TABLE -->"
    text = re.sub(r"<!-- STM_TABLE -->.*?<!-- /STM_TABLE -->", lambda m: new, text, flags=re.S)
    doc.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    c.write()
    write_table()
