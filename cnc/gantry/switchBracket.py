import cadquery as cq
from cadquery import Workplane as WP

W = 35
H=30
W1 = 23.2
W2 = 12.5
H2 = 10
L = 30
H1 = 10

W = 30

a = WP().rect(W,L).extrude(H)

pts = [(W1/2,0),(-W1/2,0),(-W1/2,-4.75),(-W2/2,-10),(-W2/2,-13),(-W/2,-13),(-W/2,5)
       ,(W/2,5),(W/2,-13),(W2/2,-13),(W2/2,-10),(W1/2,-4.75)]
a = (WP().polyline(pts).close().extrude(L))
a = a.cut(WP("XZ").moveTo(0,12).rect(22,10.5,forConstruction=True).vertices().circle(2.5/2).extrude(-10))
a = a.cut(WP("XZ").moveTo(0,25).circle(5/2).extrude(-10))

cq.exporters.export(a.rotate((0,0,0),(1,0,0),-90),"lsRailbracket.stl")