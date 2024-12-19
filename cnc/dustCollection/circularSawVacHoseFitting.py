import cadquery as cq
from cadquery import Workplane as WP
from math import sin, cos, atan2,pi
from cadquery.selectors import NearestToPointSelector as NTPS

#35x18


ID, OD,D2, barb = 27, 31.5,35,35
H1,H2,H3,H4 = -15,-15.5,-20,-36


pts = [(OD/2,0),(OD/2,H1),(barb/2,H1+0.5),(barb/2,H2),(OD/2,H3),(OD/2,H4),(ID/2,H4),(ID/2,0)]
pts.extend([(ID/2,28),(D2/2,28),(D2/2,10)])
a = WP("XZ").polyline(pts).close().revolve(360,(0,0,0),(0,1,0)).translate((0,0,0))

cq.exporters.export(a.rotate((0,1,0),(0,0,0),180).rotate((0,0,1),(0,0,0),45),"circluarSawVacHoseConnector.stl")