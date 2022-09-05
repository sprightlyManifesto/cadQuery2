import cadquery as cq
from cadquery import Workplane as WP
from math import sin, cos, tan, pi

mountingHoleD = 4.2
D1, D2, PCD = 51.75, 76.75, 63.4
L1, L2  = 13, 34.5

#Turned form
a = WP().circle(D1/2).extrude(-L1)
a = a.union(WP().circle(D2/2).extrude(L2-L1))

for f in (">Z", "<Z"): 
    a = a.faces(f).edges().fillet(0.5)

#mounting holes
PCDholes = []
slotDepth = 8.2
a = a.cut(WP().polygon(8,PCD,forConstruction=True).vertices().circle(mountingHoleD/2).extrude(L2))

#woodruff slto to hold vice

offset = 21.4/2 - 3/cos(pi/6)
a = a.cut(WP("YZ").center(0,L2-L1).rect(21.8,slotDepth*2).extrude(PCD,both=True))
a = a.cut(WP("YZ").rect(6,24).extrude(PCD,both=True).rotate((0,0,0),(1,0,0),30).translate((0,offset,L2-L1)))
a = a.cut(WP("YZ").rect(6,24).extrude(PCD,both=True).rotate((0,0,0),(1,0,0),-30).translate((0,-offset,L2-L1)))

#end stop M4 hole
a = a.cut(WP().workplane(offset=L2-slotDepth-L1).moveTo(-36.5/2,0).circle(3.3/2).extrude(-10))

#M4 cross hole
a = a.cut(WP("XZ").moveTo( 10,L2-slotDepth/2-L1).circle(3.3/2).extrude(-PCD))
a = a.cut(WP("XZ").moveTo(-10,L2-slotDepth/2-L1).circle(3.3/2).extrude(-PCD))

pocketNCoffset = 0.836 * 25.4
cq.exporters.export(a.rotate((0,0,0),(1,0,0),-90).translate((0,-pocketNCoffset,0)), "viceMount.stl")

