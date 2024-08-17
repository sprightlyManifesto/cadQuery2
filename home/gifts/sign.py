from cadquery import Workplane as WP
import cadquery as cq

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

D = 2
L = 300
pts = [(0,50),(L-7.5*5,50),(L,0),(L-7.5*5,-50),(0,-50)]
a = WP().polyline(pts).close().extrude(-10)
a = a.cut(scale(cq.importers.importDXF("Sinnbild_Wanderer.dxf").wires().toPending().extrude(D),0.27,0.27,1)\
          .translate((-220,-40,0)).rotate((0,0,0),(0,1,0),180))
a = a.cut(WP().moveTo(55,0).circle(91/2).extrude(-D))
pts = [(L-60,40),(L-40,40),(L-10,0),(L-40,-40),(L-60,-40),(L-30,0)]
a = a.cut(WP().polyline(pts).close().extrude(-D))

cq.exporters.export(a,"mumAndDad50thSign.stl")
