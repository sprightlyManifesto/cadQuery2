from cadquery import Workplane as WP
import cadquery as cq
from math import sin, cos ,pi

x1,y1 = 0, 73/2
x2,y2 = 4.4, -73/2
T = 20
AF = 5.7
r = AF/cos(pi/6)/2
n = 62/2*cos(pi/4)

a = WP().circle(84/2).extrude(T)
a = a.cut(WP().workplane(offset=T).pushPoints([(x1,y1),(x2,y2)]).circle(5/2).extrude(-17))
a = a.union(WP().circle(51.7/2).extrude(-10).faces("<Z").edges().fillet(0.5))

clampHs = [(-1.8,10),(-1.8,-30)]
a = a.cut(WP().pushPoints(clampHs).circle(3.3/2).extrude(T))
pts = [(r*sin(pi/6*p),r*cos(pi/6*p)) for p in (1,3,5,7,9,11)]
for ch in clampHs: a = a.cut(WP().workplane(offset=-10).center(ch[0],ch[1]).polyline(pts).close().extrude(15))
a = a.cut(WP().pushPoints([(n,n),(n,-n),(-n,-n),(-n,n)]).circle(4.5/2).extrude(T))
a = a.cut(WP().workplane(offset=T).pushPoints([(n,n),(n,-n),(-n,-n),(-n,n)]).circle(8/2).extrude(-5))

cq.exporters.export(a,"plate.stl")