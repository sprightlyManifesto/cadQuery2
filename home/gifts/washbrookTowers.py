import cadquery as cq
from cadquery import Workplane as WP

H = 30
R = 5
T = 3

a = WP().text("Washbrook",H,T).translate((0,H/2,0))
a = a.union(WP().text("Towers",H,T).translate((0,-H/2,0)))
bb = a.val().BoundingBox()

a = a.union(WP().rect(bb.xmax-bb.xmin+R*2,bb.ymax-bb.ymin+R*2).extrude(-T).edges("|Z").fillet(R))
a = a.cut(WP().pushPoints([(bb.xmax-R*3,-H/2),(bb.xmin+R*3,-H/2)]).circle(5/2).extrude(-T))

cq.exporters.export(a,"washbrookTowers.step")