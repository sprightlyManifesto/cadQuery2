import cadquery as cq
from cadquery import Workplane as WP
from math import sin, cos, atan2,pi
from cadquery.selectors import NearestToPointSelector as NTPS

D1, D2, l , T, wall = 120,50,80.3,20,3
r = (D1-D2)/2
ID, OD, barb = 27, 31.5, 35
H1,H2,H3,H4 = -15,-15.5,-20,-36

theta = atan2(r,l)
x1,y1 = D1/2*sin(theta),D1/2*cos(theta)
x2,y2 = D2/2*sin(theta)+l,D2/2*cos(theta)
a = WP().moveTo(x2,y2).radiusArc((x2,-y2),D2/2).lineTo(x1,-y1).threePointArc((-D1/2,0),(x1,y1)).close().extrude(T,taper=-15)
D1,D2 = 130,60
x1,y1 = D1/2*sin(theta),D1/2*cos(theta)
x2,y2 = D2/2*sin(theta)+l,D2/2*cos(theta)
a = a.union(WP().moveTo(x2,y2).radiusArc((x2,-y2),D2/2).lineTo(x1,-y1).threePointArc((-D1/2,0),(x1,y1)).close().extrude(1))
a = a.union(WP().workplane(offset=1).moveTo(x2,y2).radiusArc((x2,-y2),D2/2).lineTo(x1,-y1).threePointArc((-D1/2,0),(x1,y1)).close().extrude(wall*2,taper=30))

a = a.cut(WP(obj=a.faces(">Z").vals()[0]).wires().toPending().offset2D(-wall).extrude(-T+wall).faces("<Z").edges().fillet(T-wall-1))
pts = [(ID/2,0),(OD/2,0),(OD/2,H1),(barb/2,H1+0.5),(barb/2,H2),(OD/2,H3),(OD/2,H4),(ID/2,H4)]
a = a.union(WP("XZ").polyline(pts).close().revolve(360,(0,0,0),(0,1,0)).translate((l,0,0)))
a = a.union(WP().circle(80/2).circle(86/2).extrude(-30))
a = a.cut(WP().circle(80/2).extrude(T,both=True))
a = a.cut(WP().moveTo(l,0).circle(ID/2).extrude(T,both=True))
a = a.faces(">Z[-4]").edges(NTPS((l,0,0))).fillet(3)
a = a.faces(">Z[-4]").edges(NTPS((0,0,0))).fillet(3)
a = a.union(WP().workplane(offset=-30).pushPoints([(0,46),(0,-46)]).rect(16,12).extrude(20).faces(">Y or <Y").edges(">Z").chamfer(10).faces(">Y or <Y").edges("|X").fillet(5))
a = a.cut(WP("XZ").moveTo(0,-20).rect(3,30).extrude(100,both=True).edges("|Y").fillet(1.4))
a = a.cut(WP("YZ").pushPoints([(47,-24),(-47,-24)]).circle(4.5/2).extrude(10,both=True))
a = a.cut(WP("YZ").workplane(offset=-8).pushPoints([(47,-24),(-47,-24)]).polygon(6,7/cos(pi/6)).extrude(4))
a = a.cut(WP().circle(81.5/2).extrude(T,both=True).edges().fillet(5))

cq.exporters.export(a.rotate((0,1,0),(0,0,0),180).rotate((0,0,1),(0,0,0),45),"dustshoe.stl")