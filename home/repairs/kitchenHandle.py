import cadquery as cq
from cadquery import Workplane as WP

H,W,HD,offset,T = 91,40, 76, 14.5,20
D = 97
a = WP().moveTo(0,40-D/2).circle(D/2).extrude(T)
a = a.cut(WP().moveTo(0,40-D/2).circle((D-9*2)/2).extrude(T-3))
a = a.cut(WP().moveTo(0,-D/2).rect(D,D).extrude(T))
a = a.cut(WP().pushPoints([(HD/2,offset),(-HD/2,offset)]).circle(6/2).extrude(T))
a = a.intersect(WP().rect(92,D).extrude(T))
a = a.faces(">X").edges(">Y").fillet(20)
a = a.faces(">X").edges("<Y").fillet(1)
a = a.faces("<X").edges(">Y").fillet(20)
a = a.faces("<X").edges("<Y").fillet(1)

cq.exporters.export(a,"/home/r/kitchenHandleTemplate.stl")