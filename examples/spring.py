from cadquery import *
from math import sin,cos,acos,asin,pi,atan2
from pallet import Pallet

p = Pallet()
#billet = Workplane().circle(20).extrude(3)
"""
keys = list(p.torx6.keys())
keys.reverse()

for k in keys:
    billet = p.torx(billet.faces(">Z").workplane(),k).extrude(1)

exporters.export(billet, '/home/r/torx.svg')
exporters.export(billet, '/home/r/torx.stl')
"""

#billet = p.torx(billet.faces(">Z").workplane(),10).twistExtrude(10, 720)
r=10


A = cq.Workplane("XY").newObject([Wire.makeHelix(6, 20, r)])
B = cq.Workplane("XY").newObject([Wire.makeHelix(2, -4, r)])
#B = cq.Workplane("XY").newObject([Wire.makeHelix(3, -9, r)])
c = cq.Workplane("XZ").moveTo(10,0).circle(1).sweep(A)
c = c.add(cq.Workplane("XZ").moveTo(10,0).circle(1).sweep(B))
#c = c.cutThruAll(cq.Workplane("XY").workplane(offset=-2).circle(12).extrude(10))
D = cq.Workplane("XY").workplane(offset=-2).circle(12).extrude(10)