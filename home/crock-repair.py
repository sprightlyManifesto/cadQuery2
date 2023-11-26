import cadquery as cq
from cadquery import Workplane as WP
from math import pi,cos,sin

D1, D2 = 15.5,7
ID = 3.2
CSK = 5.5
T, L = 3, 6.6
AF = 5.5

#OUTER
a = WP("XZ").polyline([(0,0),(D1/2,0),(D1/2,T),(D2/2,T),(D2/2,L),(0,L)]).close()\
    .revolve(axisEnd = (0,0,0), axisStart = (0,1,0))
a = a.faces(">Z[-2]").fillet(1).faces()
a = a.faces("<Z").fillet(1).faces()
#CSK
b = a.cut(WP("XZ").polyline([(0,0),(CSK/2,0),(ID/2,CSK/2-ID/2),(ID/2,L),(0,L)]).close()\
    .revolve(axisEnd = (0,0,0), axisStart = (0,1,0)))

#NUT
a = a.cut(WP().polygon(6,AF/cos(pi/6)).extrude(2.4,both=True))
a = a.cut(WP().circle(ID/2).extrude(L))

show_object(a)
show_object(b.translate((20,0,0)))

cq.exporters.export(a,"side1.stl")
cq.exporters.export(b,"side2.stl")