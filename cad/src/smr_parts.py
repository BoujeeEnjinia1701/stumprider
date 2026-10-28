"""StumpRider repo-specific CAD helpers beside .kit/cad_parts.py (kit 1.9, STANDARDS section 24).

    weld_on()       a cad_parts.weld_fillet bead along any axis with its legs on any two faces
    ring_weld()     a round fillet bead where a bar or tube meets a face (revolved triangle)
    arc_weld()      a bead following part of a circle (round bar to flat plate, curved joints)
    bent_bar()      a round bar bent through a polyline with a given bend radius (swept circle)
    chamfer_ends()  chamfer only the edges of the planar faces (sawn ends of bar, cut ends of a ring half)
    tube_with_holes() a round tube along Z with cross holes along Y

All sizes in millimetres. CONCEPT, NOT FOR FABRICATION. Software license: see REUSE.toml (cad/** is
CERN-OHL-S-2.0).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".kit"))
from build123d import (Axis, Circle, FilletPolyline, Location, Plane, Polygon, Pos, Rot, Torus, Box,  # noqa: E402
                       chamfer, revolve, sweep, Cylinder, Vector)
from cad_parts import weld_fillet  # noqa: E402


def _loc(origin, u, n):
    return Location(Plane(origin=tuple(origin), x_dir=tuple(u), z_dir=tuple(n)))


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def weld_on(start, axis, length, leg, d1, d2):
    """Fillet weld bead from start along the unit vector axis for length, its legs along the unit vectors
    d1 and d2 (pointing away from the corner along the two faces it joins)."""
    bead = weld_fillet(length, leg)
    for a, b in ((d1, d2), (d2, d1)):
        if all(abs(x - y) < 1e-6 for x, y in zip(_cross(b, axis), a)):
            return _loc(start, axis, b) * bead
    raise ValueError("weld_on: axis, d1 and d2 must be mutually perpendicular unit vectors")


def ring_weld(r, leg, origin=(0, 0, 0), n=(0, 0, 1)):
    """Round fillet bead at radius r (a bar or tube's outside) on a face through origin with normal n;
    one leg along the face (outward), the other along n (up the bar)."""
    ring = revolve(Plane.XZ * Polygon((r, 0), (r + leg, 0), (r, leg), align=None), Axis.Z, 360)
    u = (1, 0, 0) if abs(n[0]) < 0.9 else (0, 1, 0)
    return _loc(origin, u, n) * ring


def arc_weld(R, r_bead, centre, n, keep_box=None):
    """A bead of radius r_bead following a circle of radius R about centre, in the plane normal to n,
    optionally clipped to keep_box (a build123d solid)."""
    u = (1, 0, 0) if abs(n[0]) < 0.9 else (0, 1, 0)
    bead = _loc(centre, u, n) * Torus(R, r_bead)
    return bead & keep_box if keep_box is not None else bead


def bent_bar(points, d, bend_r):
    """Round bar of diameter d bent through the 3D polyline points with inside bend radius bend_r - d/2
    (bend_r is the radius to the bar centre line). Ends are square."""
    path = FilletPolyline(*[Vector(*p) for p in points], radius=bend_r)
    a, b = Vector(*points[0]), Vector(*points[1])
    t = (b - a).normalized()
    u = Vector(1, 0, 0) if abs(t.X) < 0.9 else Vector(0, 1, 0)
    prof = Plane(origin=a, x_dir=u - t * u.dot(t), z_dir=t) * Circle(d / 2)
    return sweep(prof, path)


def chamfer_ends(shape, c=0.5):
    """Chamfer the edges of the planar faces only (sawn bar ends, the cut faces of a ring half)."""
    try:
        edges = [e for f in shape.faces() if f.geom_type.name == "PLANE" for e in f.edges()]
        if not edges:
            return shape
        out = chamfer(edges, c)
        return out if out.is_valid else shape
    except Exception:
        return shape


def tube_with_holes(od, wall, z0, z1, x=0.0, y=0.0, holes=()):
    """Round tube along Z from z0 to z1 centred on (x, y), with cross holes along Y [(z, d), ...]."""
    t = Pos(x, y, (z0 + z1) / 2) * (Cylinder(od / 2, z1 - z0) - Cylinder(od / 2 - wall, z1 - z0 + 2))
    for z, dia in holes:
        t = t - Pos(x, 0, z) * Rot(90, 0, 0) * Cylinder(dia / 2, 4 * od)
    return t


def half_space(axis, sign, offset=0.0, big=4000.0):
    """A large box occupying sign * axis > offset (axis 'x', 'y' or 'z')."""
    c = sign * (offset + big / 2)
    pos = {"x": (c, 0, 0), "y": (0, c, 0), "z": (0, 0, c)}[axis]
    return Pos(*pos) * Box(big, big, big)
