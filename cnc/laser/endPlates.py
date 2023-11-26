from cadquery import Workplane as WP
T,D1,D2,H = 6, 5, 8,70
M5cboreDia,M5cboreDepth  = 9,5

a = WP().polyline([(-10,10),(30,10),(110,-H+10),(110,-H),(-10,-H)]).close().extrude(T).edges("|Z").fillet(2)
pts = [(0,0),(20,0)]
a = a.cut(WP().pushPoints(pts).circle(D1/2).extrude(T))
a = a.cut(WP().workplane(offset=T).pushPoints(pts).circle(M5cboreDia/2).extrude(-M5cboreDepth))