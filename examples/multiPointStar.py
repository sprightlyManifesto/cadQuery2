from cadquery import Workplane as WP
import cadquery as cq
from math import sin , cos, pi

pts = []
np = 9
n = np*2

for p in range(n):
    if p %2:
        r= 100
    else:
        r=30
    pts.append((r*cos(2*pi/n*p),r*sin(2*pi/n*p)))

a = WP().polyline(pts).close().extrude(5)

for p in range(n):
    f = 10
    if p %2: f = 4
    a = a.edges("|Z").edges(cq.NearestToPointSelector(pts[p])).fillet(f)