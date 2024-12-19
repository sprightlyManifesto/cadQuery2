from cadquery import Workplane as WP
from cadquery.selectors import NearestToPointSelector as NTPS
from math import cos,sin,pi

r = 125/2
pts = [(r*cos(t),r*sin(t)) for t in (0,pi/3,2*pi/3,3*pi/3,4*pi/3,5*pi/3)]
a = WP().circle(94/2).circle(100/2).extrude(40)
a = a.union(WP().circle(94/2).circle(150/2).extrude(4))
a = a.cut(WP().pushPoints(pts).circle(6.5/2).extrude(4))

l1 = 10
r = 70
pth = (WP("YZ")).lineTo(0,l1).radiusArc((r,r+l1),r)
b = WP().circle(100/2).circle(94/2).sweep(pth)
b = b.union(WP().circle(94/2).circle(150/2).extrude(4))
b = b.cut(WP().pushPoints(pts).circle(6.5/2).extrude(4))
b = b.union(WP("XZ").workplane(offset = -48.5).moveTo(0,15).rect(20,30).extrude(-21).faces(">Z").edges("<Y").fillet(18))
b = b.translate((200,0,0))

cq.exporters.export(a,"topFlange.stl")
cq.exporters.export(b,"bottomCurve.stl")