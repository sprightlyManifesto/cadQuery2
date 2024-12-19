import cadquery as cq
from cadquery import Workplane as WP
from math import sin, cos, atan2,pi
from cadquery.selectors import NearestToPointSelector as NTPS

T = 30 
N = 21
pitch = 15
C = N * 10
D = C/pi
OD = D+5
ID = D-5

pts = [(OD/2,T),(ID/2,T),(ID/2,3),(0,3),(0,0),(OD/2,0)]
a = WP("XZ").polyline(pts).close().revolve(360,(0,1,0),(0,0,0))
pts = [(D/2*sin(n/N*2*pi),D/2*cos(n/N*2*pi)) for n in range(N)]
a = a.cut(WP().workplane(offset=T).pushPoints(pts).circle(2.5/2).extrude(-25))

a = cq.exporters.export(a,"dartsCup.stl")