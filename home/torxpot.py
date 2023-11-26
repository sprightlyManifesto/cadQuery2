from cadquery import Workplane as WP
from math import sin, cos, pi

H = 12.6

a = WP().rect(32.8,32,8).circle(6/2).extrude(H).edges("|Z").fillet(1)
a = a.cut(WP().rect(24,24,forConstruction=True).vertices().circle(2.7/2).extrude(H))

R =26/2
xy = (R**2/2)**0.5
x2,y2 = sin(pi/12)*R,cos(pi/12)*R
a = a.cut(WP().rect(24,24,forConstruction=True).vertices().circle(2.7/2).extrude(H))
airPath = WP().moveTo(-xy,xy).radiusArc((-x2,y2),R).offset2D(2).extrude(H)
airPath = airpath.union(airpath.mirrorX())
a = a.cut(airPath)
#a = a.cut(airPath.mirror("XZ"))
#a = a.cut(airPath.mirror("YZ"))
#a = a.cut(airPath.mirror("XZ").mirror("YZ"))

show_object(a)