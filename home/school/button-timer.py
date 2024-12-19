from cadquery import Workplane as WP
from cadquery.selectors import RadiusNthSelector as NthR 
from math import cos, sin, tan, pi
import cadquery as cq

T = 3
OD = 32
D1 = 24
D2 = 20
D3 = 16

a = WP().circle(OD/2).extrude(T)
a = a.cut(WP().circle(D1/2).extrude(-T*0.25).translate((0,0,T)))
a = a.cut(WP().circle(D2/2).extrude(-T*0.5).translate((0,0,T)))
a = a.cut(WP().circle(D3/2).extrude(-T*0.75).translate((0,0,T)))
a = a.edges().chamfer(T/10)

OD += 1
W = OD +8
b = WP()

for i in range(0,5):
    b = b.union(WP().rect(W,W).extrude(T).translate((W*i,0,0)))
    b = b.cut(WP().circle(OD/2).extrude(-T*0.75).translate((W*i,0,T)))
b = b.edges("|Z").fillet(W/2-0.1)

cq.exporters.export(a,"counter.stl")
cq.exporters.export(b,"board.stl")

