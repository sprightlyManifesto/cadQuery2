from cadquery import Workplane as WP
from cadquery.selectors import NearestToPointSelector as NTPS
from math import sin, cos , pi

H = 10
AF = 13

a = WP()
for r in (0,30):
    a = a.union(WP().polygon(6,AF/cos(pi/6)).extrude(H).rotate((0,0,0),(0,0,1),r))
a = a.cut(WP().circle(10/2).extrude(H))
a = a.edges("|Z").fillet(1)

for r in (0,30):
    a = a.union(WP().polygon(6,AF/cos(pi/6)).extrude(H).rotate((0,0,0),(0,0,1),r))

