from cadquery import Workplane as WP
import cadquery as cq


for R in range(54,82,2):
    rad = WP().lineTo(R,0).radiusArc((0,R),-R).close().extrude(3)
    rad = rad.cut(WP().circle(R/2).extrude(3))
    rad = rad.cut(WP().workplane(offset=1.5).text(str(R),16,4).translate((R*3/4,0)).rotate((0,0,0),(0,0,1),45))
    cq.exporters.export(rad,f"RadiusGuage{R}.stl")
