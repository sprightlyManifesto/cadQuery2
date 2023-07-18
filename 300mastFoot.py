from cadquery import Workplane as WP
import cadquery as cq

T,T1,T2 = 35,15,19
D, D1, ID = 77.8, 68.6, 28

a = WP().circle(D/2).extrude(T1)
a = a.union(WP().circle(D1/2).extrude(T))
a = a.faces(">Z or <Z").edges().chamfer(2)
#a = a.faces("<Z").edges().chamfer(2)
a = a.cut(WP().circle(ID/2).extrude(T2).edges(">Z").fillet(8))
a = a.cut(WP().pushPoints([(26,0),(-26,0)]).circle(5/2).extrude(T))