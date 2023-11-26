from cadquery import Workplane as WP
import cadquery as cq
from math import sin, cos ,pi

pts = []
P = 18

R1 = 18

for n in range(0,P):
    R = R1
    if n%2==0:R=22
    pts.append((R*sin(n/P*pi*2),R*0.7*cos(n/P*pi*2)))

a = WP().polyline(pts).close().extrude(3)
a = a.edges("|Z").fillet(2)
a = a.cut(WP().text("Buzzards",10,1,font="Alexander").translate((0,0,2)))
a = a.union(WP().text("2023",16,0.5,font="Alexander").rotate((0,0,0),(0,1,0),180))
a = a.cut(WP().moveTo(0,10).circle(1.5).extrude(3))

cq.exporters.export(a,"buzzards.stl")