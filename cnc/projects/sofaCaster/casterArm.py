import os
from math import sin, cos , pi
from math import atan2
from cadquery import Workplane as WP

d = 12
dia = 31
h = 14
l = 40
throw  = 27
throat = 16.5
w = 24 
clearance = 20

a = WP().rect(l,w).extrude(h).translate((l/2-7.5,0,0))
a = a.union(WP("XZ").moveTo(-7.5+l-d/2,0).circle(d/2).extrude(w/2,both=True))
a = a.faces(">Z").edges(">X").fillet(13)
a = a.faces("<Z[-1]").edges(">X").fillet(12)
a = a.cut(WP("XZ").moveTo(-7.5+l-d/2,0).circle(4/2).extrude(w/2,both=True))
a = a.cut(WP().rect(l,throat).extrude(h,both=True).edges("|Z").fillet(3.2).rotate((0,0,0),(0,1,0),10).translate((l/2+7.5,0,0)))
a = a.cut(WP().moveTo(-12,23.5).circle(20).extrude(h))
a = a.cut(WP().moveTo(-12,-23.5).circle(20).extrude(h))
a = a.faces("<X").edges("|Z").fillet(5)
a = a.faces(">Y or <Y").edges("<X").fillet(2)
a = a.cut(WP().circle(6.2/2).extrude(h))

b = WP("XZ").moveTo(-7.5+l-d/2,0).circle(31/2).extrude(8,both=True)

cq.exporters.export(a,"caterArm.stl")