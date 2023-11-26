from cadquery import Workplane as WP
import cadquery as cq

S = 8
T = 10
D = T/3
F = 2

a = WP().rect(8*S,9*S).extrude(-T).translate((0,-S*0.5,0)).edges("|Z").fillet(F)
a = a.cut(WP().pushPoints([(2*S,S),(-2*S,S)]).rect(2*S,2*S).extrude(-D).edges("|Z").fillet(F))

pts = [(-S,0),(S,0),(S,-S),(2*S,-S),(2*S,-4*S),(S,-4*S),(S,-3*S),(-S,-3*S),(-S,-4*S),(-S*2,-4*S),(-S*2,-S),(-S,-S)]
a = a.cut(WP().polyline(pts).close().extrude(-D).edges("|Z").fillet(F))

cq.exporters.export(a,"creeper.stl")