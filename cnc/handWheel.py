import cadquery as cq
from cadquery import Workplane as WP
from math import sin, cos, atan2,pi
from cadquery.selectors import NearestToPointSelector as NTPS

OD,D2,D3 = 90,70,30
DISH = 17
ID = 17.9
T = 40

pts = [(OD/2,T-12),(OD/2,T),(D2/2,T),(D3/2,T-DISH),(ID/2,T-DISH),(ID/2,0),(D3/2,0),(D3/2,14)]
a = WP().polyline(pts).close().revolve(360,(0,0,0),(0,1,0)).edges("not <Y").fillet(1)
a = a.cut(WP("XZ").moveTo((OD+D2)/4,0).circle(5/2).extrude(-T))
a = a.cut(WP().moveTo(0,9).circle(6/2).extrude(-T))

cq.exporters.export(a.rotate((0,0,0),(1,0,0),-90),"handwheel.stl")