from cadquery import Workplane as WP
from math import sin, cos, pi

H = 12.7
proud = 1
SQ = 32.8
D = 11

#billet, bore, mounting holes,cbore,oring grove
a = WP().rect(SQ,SQ).extrude(H)
a = a.faces("<Y").edges("|Z").fillet(2)
a = a.faces(">X").edges("|Z").fillet(2)
a = a.edges("|Z").fillet(3)
a = a.cut(WP().circle(4/2).extrude(H))
a = a.cut(WP().rect(24,24,forConstruction=True).vertices().circle(2.7/2).extrude(H))
a = a.cut(WP().rect(24,24,forConstruction=True).vertices().circle(4.5/2).extrude(H).translate((0,0,H-2)))
a = a.cut(WP().circle(21/2).extrude(proud))
a = a.cut(WP().circle(9/2).circle(16/2).extrude(proud+1.75))

#fan air path
R =26/2
xy = (R**2/2)**0.5
x2,y2 = sin(pi/12)*R,cos(pi/12)*R
a = a.cut(WP().rect(24,24,forConstruction=True).vertices().circle(2.7/2).extrude(H))
a = a.cut(WP().moveTo(-xy,xy).radiusArc((-x2,y2),R).offset2D(2).mirrorX().mirrorY().extrude(H))
a = a.edges("|Z").fillet(1)


#Compressed airpath
a = a.cut(WP("YZ").moveTo(0,H/2).circle(3.3/2).extrude(25))
a = a.cut(WP("YZ").circle(8.8/2).extrude(10).translate((SQ/2-7,0,H/2)))
show_object(a)

cq.exporters.export(a.rotate((0,0,0),(0,1,0),180),"airAssist.stl")