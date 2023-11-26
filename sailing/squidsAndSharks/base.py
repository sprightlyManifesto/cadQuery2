import cadquery as cq
from cadquery import Workplane as WP

OD = 136
ID = 58.5
H = 3
W = 50
w = 20
t = 10

b = WP().polyline([(W/2,0),(-W/2,0),(-w/2,t),(w/2,t)]).close().extrude(22,both=True)
b = b.faces(">Y").edges("|X").fillet(5)
b = b.faces(">Y").edges("|Z").fillet(3)
b = b.faces("<Y").edges().fillet(0.3)
b = b.cut(WP().circle(OD/2).extrude(H+0.3).rotate((0,0,0),(1,0,0),15).translate((0,OD/2,0)))

cq.exporters.export(b,"base.stl")