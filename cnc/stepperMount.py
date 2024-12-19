#nema23
from cadquery import Workplane as WP
import cadquery as cq
from math import cos, pi
H = 30.5
W = 79
W1 = 57.3

a = WP().moveTo(0,H/2+W1/4).rect(W,H+W1/2).extrude(20)
a = a.faces(">Y").edges("|Z").fillet(5)
a = a.cut(WP().moveTo(0,H).circle(38.4/2).extrude(20))
a = a.cut(WP().center(0,H).rect(47.14,47.14,forConstruction=True).vertices().circle(5.2/2).extrude(20))
a = a.cut(WP("XZ").moveTo(0,30).circle(20).extrude(-H*2))
a = a.translate((0,0,-10))

pts = [(33,0),(-33,0)]
a = a.cut(WP("XZ").pushPoints(pts).circle(6.3/2).extrude(-80))
for x,y in pts:
    a = a.cut(WP().moveTo(x,y).lineTo(x*2,y-x).lineTo(x*2,y+x).close().offset2D(6).extrude(H*2).rotate((0,0,0),(1,0,0),-90).translate((0,35,0)))

a= a.edges("|Y").fillet(1)
cq.exporters.export(a,"stepperBracket.stl")

9.9
collar = WP().circle(30/2).circle(6.35/2).extrude(35/2,both=True)
collar = collar.cut(WP().lineTo(50,0).close().offset2D(0.5).extrude(50,both=True).rotate((0,0,0),(0,1,0),90).translate((0,0,5)))
collar = collar.cut(WP().lineTo(0,-50).close().offset2D(0.5).extrude(50,both=True).rotate((0,0,0),(1,0,0),-90).translate((0,0,-5)))
pts = [(9,11),(-9,11)]
collar = collar.cut(WP("YZ").pushPoints(pts).circle(4.3/2).extrude(30,both=True))

for x,y in pts:
    collar = collar.cut(WP("YZ").polygon(6,6.8/cos(pi/6)).extrude(30).rotate((0,0,0),(1,0,0),90).translate((4,x,y)))
collar = collar.cut(WP("YZ").workplane(offset=-4).pushPoints(pts).circle(8/2).extrude(-30))

pts = [(9,-11),(-9,-11)]
collar = collar.cut(WP("XZ").pushPoints(pts).circle(4.3/2).extrude(30,both=True))
for x,y in pts:
    collar = collar.cut(WP("XZ").polygon(6,6.8/cos(pi/6)).extrude(30).rotate((0,0,0),(0,1,0),90).translate((x,-4,y)))
collar = collar.cut(WP("XZ").workplane(offset=-4).pushPoints(pts).circle(8/2).extrude(-30))

collar = collar.translate((0,H,0))
show_object(collar)

cq.exporters.export(collar,"collar.stl")