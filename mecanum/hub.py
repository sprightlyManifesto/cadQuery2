from math import sin,cos,pi
from cadquery import Workplane as WP
import cadquery as cq

AF = 12.2
r = 12.2/cos(pi/6)/2
pts = [(r*cos(p*pi/3),r*sin(p*pi/3)) for p in range(6)]
part = WP().polyline(pts).close().extrude(-4)

pts = [(0,0),(8,0),(11.5,11),(11.5,22),(0,22)]
part = part.union(WP("XZ").polyline(pts).close().revolve(360,(0,0,0),(0,1,0)))

r,af = 5.1/2, 4.8 
y = af-r
x = (r**2 - y**2)**0.5

shaft = WP().workplane(offset=22).circle(4.9/2).extrude(-9)
shaft = shaft.cut(WP().workplane(offset=20).rect(2.9,10).rect(10,10).extrude(-9))
part = part.cut(shaft)
#part = part.cut(WP().workplane(offset=22).extrude(-15))
part = part.cut(WP().workplane(offset=-4).circle(3.3/2).extrude(12))
part = part.cut(WP("YZ").polyline([(AF/2,-4),(AF/2+4,-4),(AF/2+4,0)]).close().revolve(360,(0,0,0),(0,1,0)))

show_object(part)

cq.exporters.export(part,"hub.stl")