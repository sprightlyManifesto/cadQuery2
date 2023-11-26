import cadquery as cq
from cadquery import Workplane as WP

def scale(workplane: WP, x: float, y: float = None, z: float = None) -> WP:
    if y== None: y = x
    if z== None: z = x
    t = cq.Matrix([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ])
    return workplane.newObject([
        o.transformGeometry(t) if isinstance(o, cq.Shape) else o
        for o in workplane.objects
    ])

a = WP().box(1,1,1)
b = scale(a,1,2,3)
c= scale(a,3)