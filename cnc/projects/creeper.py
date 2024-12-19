from cadquery import Workplane as WP
import cadquery as cq

T=  6
D = = T/2
S = 15
F = 4

a = WP().rect(8*S,8*S).extrude(-T).edges("|Z").fillet(4)
a = a.cut(WP().pushPoints([(2*S,S),(-2*S,S)]).rect(2*S,2*S).extrude(-D).edges("|Z").fillet(4))
a = a.cut(WP().moveTo(0,-1.5*S).rect(2*S,3*S).extrude(-D))
a = a.cut(WP().pushPoints([(1.5*S,-2.5*S),(-1.5*S,-2.5*S)]).rect(1*S,-3*S).extrude(-D))
a = a.edges("|Z").fillet(4)