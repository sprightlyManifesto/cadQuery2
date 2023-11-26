from cadquery import Workplane as WP
import cadquery as cq

length = 150
T = 3.5

scale = length/5050
#505 outline (full size)
a= WP().radiusArc((895*scale,-2100*scale),9340*scale/2)\
    .radiusArc((875*scale,-4100*scale),12110*scale/2)\
    .lineTo(705*scale,-5050*scale)\
    .lineTo(-705*scale,-5050*scale)\
    .radiusArc((-895*scale,-2100*scale),12110*scale/2)\
    .radiusArc((0,0),9340*scale/2).close().extrude(T).edges("|Z").fillet(2)


a = a.cut(WP().workplane(offset=T).pushPoints([(0,-length/3),(0,-2*length/3)]).circle(6.5/2).extrude(-3))


cq.exporters.export(a,"505.stl")
