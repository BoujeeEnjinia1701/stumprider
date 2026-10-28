"""StumpRider concept options B and C at detail level D3 (SMR-OPT-001, STANDARDS sections 21 and 24).

Imported by cad/src/model.py components(); option A, the chosen design, is built in model.py itself. Every
dimension is in model.PARAMS (kb_* for option B, gr_* for option C). Both options share option A's gunwale
crutch, which guides the line or rope over the gunwale. These are concept options: they carry no BOM lines,
drawing or build plan. CONCEPT, NOT FOR FABRICATION.

    B  line-riding knocker weight: a 60 mm steel bar, 120 mm long, split along its axis and bored for the net
       line; the two halves hinge on an M8 bolt through three welded knuckles and close with an 8 mm clevis pin
       through three more; an M10 eye bolt takes the tether; it runs down the net line and is jigged.
    C  grapnel cross-pull: a four-tine grapnel of 14 mm bar on a 16 mm shank with a 10 mm bar eye, a bow
       shackle, and a shear link (fork, tang and the same 2 mm soft aluminium pin as option A) to a 10 mm rope.

Layout for each option: the working piece standing at the origin on the ground (z = 0), the cord or rope
winder beside it on +X and the gunwale crutch beyond.
"""
from __future__ import annotations

import math

from build123d import Box, Cylinder, Pos, Rot, Torus

import model as M
import cad_parts as cp
from cad_parts import part, break_edges
from smr_parts import arc_weld, bent_bar, chamfer_ends, ring_weld, weld_on

P = M.PARAMS
GALV, SS, ALU = "galvanised", "stainless", "aluminium"


def _rod_bead(a, b, r=1.6):
    return M.rod(a, b, r)


# ------------------------------------------------------------------------------------------------ option B
def option_b(p=P):
    od, L, bore, gap = p["kb_od"], p["kb_L"], p["kb_bore"], p["kb_gap"]
    k_od, k_id, k_L = p["kb_knuckle"]
    ar, wt = p["kb_axis_r"], p["kb_web_t"]
    R = od / 2
    g = gap / 2
    body = Pos(0, 0, L / 2) * (Cylinder(R, L) - Cylinder(bore / 2, L + 2))
    eye_x = 20.0
    tap = Pos(eye_x, 0, L - 10) * Cylinder(5.0, 20.0)                  # M10 tapped hole, 20 deep, in the fixed half
    out = []
    for side, nm in ((+1, "fixed"), (-1, "swinging")):
        keep = Pos(side * (g + 100), 0, L / 2) * Box(200, 200, L + 10)
        h = body & keep
        if side > 0:
            h = h - tap
        out.append(part(f"Knocker {nm} half, 60 mm bar split and bored 24 mm", chamfer_ends(h, 1.5), GALV))
    # knuckles: hinge on +Y (fixed half z 10..40 and 80..110, swinging half z 45..75), gate on -Y the same
    spans = {+1: [(10.0, 40.0), (80.0, 110.0)], -1: [(45.0, 75.0)]}
    for sy, axis in ((+1, "hinge"), (-1, "gate")):
        yk = sy * ar
        for side, nm in ((+1, "fixed"), (-1, "swinging")):
            for z0, z1 in spans[side]:
                kn = Pos(0, yk, (z0 + z1) / 2) * (Cylinder(k_od / 2, z1 - z0) - Cylinder(k_id / 2, z1 - z0 + 2))
                out.append(part(f"Knocker {axis} knuckle, {nm} half, z {z0:.0f}", break_edges(kn, 0.5), GALV))
                x0, x1 = sorted((side * g, side * (g + wt)))
                y_in = math.sqrt(R * R - max(abs(x0), abs(x1)) ** 2) - 1.0
                web = Pos((x0 + x1) / 2, sy * (y_in + ar) / 2, (z0 + z1) / 2) * Box(wt, ar - y_in, z1 - z0)
                web = web - Pos(0, 0, L / 2) * Cylinder(R, L + 4) - Pos(0, yk, (z0 + z1) / 2) * Cylinder(k_od / 2, z1 - z0 + 4)
                out.append(part(f"Knocker {axis} web, {nm} half, z {z0:.0f}, 6 mm flat", break_edges(web, 0.5), GALV))
                xf = side * (g + wt) + side * 0.9
                yb = sy * math.sqrt(R * R - (g + wt) ** 2)
                out.append(part(f"Weld, Knocker {axis} web to body, z {z0:.0f}",
                                _rod_bead((xf, yb + sy * 0.6, z0 + 2), (xf, yb + sy * 0.6, z1 - 2)), GALV, kind="weld"))
                yw = sy * (ar - k_od / 2 * math.cos(math.asin(min(1.0, (g + wt) / (k_od / 2)))) if (g + wt) < k_od / 2 else ar)
                out.append(part(f"Weld, Knocker {axis} web to knuckle, z {z0:.0f}",
                                _rod_bead((xf, yw - sy * 0.6, z0 + 2), (xf, yw - sy * 0.6, z1 - 2)), GALV, kind="weld"))
    # hinge: M8 bolt set through the three hinge knuckles (z 10 to 110); gate: 8 mm clevis pin and R-clip
    grip = 100.0
    for nm, sh in cp.hex_bolt_set(8, grip):
        out.append(part(f"Knocker hinge {nm}", Pos(0, ar, 110.0) * sh, SS, kind="fastener"))
    out += M._clevis(8, grip, (0, -ar, 110.0), "z-", "Knocker gate", None)
    # eye bolt M10 in the fixed half's top face, and the tether's bowline through it
    shank = Pos(eye_x, 0, L - 10) * Cylinder(4.95, 20.0)
    collar = Pos(eye_x, 0, L + 3) * Cylinder(10.0, 6.0)
    eye = Pos(eye_x, 0, L + 6 + 14) * Rot(90, 0, 0) * Torus(14 - 4, 4.0)
    eye = Pos(0, 0, -0.5) * eye                                     # the eye sinks 0.5 mm into the collar: one clean solid
    out.append(part("Knocker eye bolt M10, forged", shank + break_edges(collar, 0.6) + eye, GALV, kind="bought"))
    loop = Pos(eye_x, 0, L + 6 + 24) * Rot(0, 0, 90) * Rot(90, 0, 0) * Torus(9.0, 3.0)
    out.append(part("Knocker tether cord, bowline through the eye", loop, "rope", kind="bought"))
    wx, wz = 260.0, 160.0
    out.append(part("Knocker tether cord, wound on the float winder", Pos(wx, 0, wz) * Rot(0, 90, 0) * M.winder_cord(p),
                    "rope", kind="bought"))
    out.append(part("Knocker float winder, closed-cell foam", Pos(wx, 0, wz) * Rot(0, 90, 0) * break_edges(M.float_winder(p), 2.0),
                    "insulated_white", kind="made", color="#F28C28"))
    out += M.crutch_part_list(p, at=(460.0, 0.0, 70.0))
    return out


# ------------------------------------------------------------------------------------------------ option C
def option_c(p=P):
    sd, sl = p["gr_shank"]
    td = p["gr_tine_d"]
    reach, bend, rise = p["gr_tine"]
    er, eb = p["gr_eye"]
    out = []
    zt = td / 2                                                   # tine centre line height (tines stand on the ground)
    shank = Pos(0, 0, 0) * cp.round_bar(sd, sl, 1.0)
    out.append(part("Grapnel shank, 16 mm bar", shank, GALV))
    for k in range(4):
        a = 45.0 + 90.0 * k
        tine = bent_bar([(sd / 2, 0, zt), (reach, 0, zt), (reach, 0, zt + rise)], td, bend)
        tine = chamfer_ends(tine, 3.0)
        out.append(part(f"Grapnel tine {k + 1}, {td:.0f} mm bar bent R{bend:.0f}", Rot(0, 0, a) * tine, GALV))
        out.append(part(f"Weld, Grapnel tine {k + 1} to shank", Rot(0, 0, a) * ring_weld(td / 2, 3.0, (sd / 2, 0, zt), (1, 0, 0)),
                        GALV, kind="weld"))
    ze = sl + er + eb
    out.append(part("Grapnel eye, 10 mm bar ring", Pos(0, 0, ze) * Rot(90, 0, 0) * Torus(er, eb), GALV))
    out.append(part("Weld, Grapnel eye to shank", arc_weld(sd / 2 - 1.5, 2.5, (0, 0, sl), (0, 0, 1)), GALV, kind="weld"))
    # bow shackle through the eye, its pin through the link tang
    zb = ze + er                                                 # bow centre: the bow's bottom passes inside the eye
    rb, bw = 4.0, 14.0
    bow = Pos(0, 0, zb) * Rot(0, 90, 0) * Torus(bw, rb)
    bow = bow & (Pos(0, 0, zb - 50) * Box(100, 100, 100))
    zp = zb + 30.0
    legs = [Pos(0, sy * bw, (zb + zp + 8) / 2) * Cylinder(rb, zp + 8 - zb) for sy in (+1, -1)]
    pin_hole = Pos(0, 0, zp) * Rot(90, 0, 0) * Cylinder(rb + 0.2, 60)
    bow = bow + legs[0] + legs[1] - pin_hole
    out.append(part("Link bow shackle, 8 mm", bow, GALV, kind="bought"))
    spin = Pos(0, 0, zp) * Rot(90, 0, 0) * (Cylinder(rb, 2 * bw + 2 * rb + 4) + Pos(0, 0, bw + rb + 2) * Cylinder(6.5, 4.0))
    out.append(part("Link shackle pin, 8 mm with head", break_edges(spin, 0.4), GALV, kind="fastener"))
    # shear link: tang (6 x 28 flat) in a fork (two 6 x 30 cheeks on a spacer), 2 mm soft aluminium pin
    tw, tt = 28.0, 6.0
    zt0, zt1 = zp - 10.0, zp + 60.0
    tang = Pos(0, 0, (zt0 + zt1) / 2) * Box(tw, tt, zt1 - zt0)
    zs = zp + 50.0                                               # shear pin height
    tang = tang - Pos(0, 0, zp) * Rot(90, 0, 0) * Cylinder(rb + 0.25, 20) - Pos(0, 0, zs) * Rot(90, 0, 0) * Cylinder(1.05, 20)
    out.append(part("Link tang, 6 x 28 flat", break_edges(tang, 0.5), GALV))
    zc0, zc1 = zp + 30.0, zt1 + 35.0
    for sy in (+1, -1):
        ch = Pos(0, sy * 7.0, (zc0 + zc1) / 2) * Box(30.0, 6.0, zc1 - zc0) - Pos(0, 0, zs) * Rot(90, 0, 0) * Cylinder(1.05, 40)
        out.append(part(f"Link fork cheek {'+' if sy > 0 else '-'}Y, 6 x 30 flat", break_edges(ch, 0.5), GALV))
        out.append(part(f"Weld, Link fork cheek {'+' if sy > 0 else '-'}Y to spacer",
                        weld_on((-12.0, sy * 10.0, zc1), (1, 0, 0), 24.0, 3.0, (0, sy, 0), (0, 0, -1)), GALV, kind="weld"))
    sp = Pos(0, 0, zc1 + 10.0) * Box(30.0, 28.0, 20.0) - Pos(0, 0, zc1 + 10.0) * Rot(90, 0, 0) * Cylinder(6.0, 40)
    out.append(part("Link spacer with rope eye, 30 x 28 x 20", break_edges(sp, 1.0), GALV))
    out.append(part("Link shear pin, 2 mm soft aluminium", chamfer_ends(Pos(0, 0, zs) * Rot(90, 0, 0) * Cylinder(1.0, 30.0), 0.2),
                    ALU, kind="made"))
    rr = p["gr_rope_d"] / 2
    loop = Pos(0, 0, zc1 + 10.0 + 14.0) * Rot(0, 90, 0) * Torus(14.0, rr)    # through the eye along Y, over the top
    loop = loop - (Pos(0, 0, zc1 + 10.0) * Box(30.4, 28.4, 20.4) - Pos(0, 0, zc1 + 10.0) * Rot(90, 0, 0) * Cylinder(rr + 0.2, 40))
    out.append(part("Grapnel rope, bowline through the link", loop, "rope", kind="bought"))
    # rope wound on a plywood winder board beside the grapnel
    bx, bz = 300.0, 200.0
    board = Box(300.0, 150.0, 12.0)
    for sx in (+1, -1):
        board = board - Pos(sx * (150 - 20), 0, 0) * Box(41.0, 70.0, 14.0)
    out.append(part("Grapnel rope winder, 12 mm plywood", Pos(bx, 0, bz) * Rot(0, 90, 0) * break_edges(board, 1.5), "plywood"))
    band = Box(260.0 - 2 * 20 + 2 * 14, 60.0, 12.0 + 2 * 14) - Box(260.0 - 2 * 20, 72.0, 12.0)
    out.append(part("Grapnel rope, 15 m wound on the winder", Pos(bx, 0, bz) * Rot(0, 90, 0) * band, "rope", kind="bought"))
    out += M.crutch_part_list(p, at=(520.0, 0.0, 70.0))
    return out
