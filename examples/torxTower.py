from cadquery import Workplane as WP
from pallet import Pallet
import cadquery as cq

p = Pallet()

A = 145
B = A*16/22.4
wall = 2

i = 3
a = WP().circle(25.4/2).extrude(i)
ns = list(p.torx6.keys())
ns.reverse()
for t in ns[:7]:
    i += 0.5
    a = a.union(p.torx(WP(),t).extrude(i))

cq.exporters.export(a,"torxTower.stl")