from cadquery import Workplane as WP
import cadquery as cq

L = 100

alu2020 = WP().rect(20,20).circle(4.2/2).extrude(L).edges("|Z").fillet(0.5)

pts = [(10,5.5),(8,3.5),(8,6),(7,6),(4,3)]
for p in reversed(pts):pts.append((p[0],-p[1]))
p = WP().polyline(pts).close().extrude(L).faces(">X[-2]").edges("|Z").fillet(0.2)