import cadquery as cq
from cadquery import Workplane as WP

T1 = 50

a = (
    WP().sketch()
    .arc((0, 0), 126/2, 0.0, 360.0)
    .arc((0, 100), 96/2, 0.0, 360.0)
    .hull().finalize().extrude(100)
)

a = a.cut(WP("YZ").moveTo(-70,50).lineTo(0,50).lineTo(200,150).lineTo(-70,150).close().extrude(100,both=True))
a = a.union(WP().moveTo(0,100).circle(96/2).extrude(120))
a = a.cut(WP("YZ").lineTo(50,0).lineTo(200,100).lineTo(150,0).close().extrude(100,both=True))

show_object(a)
