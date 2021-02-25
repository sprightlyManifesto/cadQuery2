from cadquery import *
from math import sin,cos,acos,asin,pi,atan2
from pallet import Pallet

p = Pallet()

billet = Workplane().circle(20).extrude(3)

keys = list(p.torx6.keys())
keys.reverse()

for k in keys:
    billet = p.torx(billet.faces(">Z").workplane(),k).extrude(1) 