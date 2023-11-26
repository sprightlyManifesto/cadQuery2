from cadquery import *
from math import pi

D = 7
d1,d2, h =20,52,D+1
d3 = (d2+d1)/2

slots = 10;

a = Workplane().circle(d1/2).circle(d2/2).extrude(h)
a = a.faces(">Z").edges().fillet(0.5)

for i in range(10):

    a = a.cut(Workplane("XZ").center(d3/2,h).
                  polyline([(0,-D),(-D,0),(D,0)]).close().extrude(2/2,both=True).
                  rotate((d3/2,0,0),(d3/2,0,1),-20+i%2*90).
                  rotate((0,0,0),(0,0,1),360/slots * i))

exporters.export(a,"out.stl")