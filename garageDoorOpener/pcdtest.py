import cadquery as cq
from cadquery import Workplane as WP
from math import pi, sin , cos , tan

MH = 6
PCD = 145.5
h = 1

a = WP().circle(50/2).extrude(h) 

for n in (0,2*pi/3, 4*pi/3):
    a=  a.union(WP().lineTo(PCD/2*sin(n),PCD/2*cos(n)).close().offset2D(MH).extrude(h))
    a = a.cut(WP().moveTo(PCD/2*sin(n),PCD/2*cos(n)).circle(MH/2).extrude(h))

a = a.cut(WP().circle(25/2).extrude(h))

cq.exporters.export(a,"out.stl")