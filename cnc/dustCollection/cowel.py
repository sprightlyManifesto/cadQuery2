import cadquery as cq
from cadquery import Workplane as WP
from cadquery.selectors import NearestToPointSelector as NTPS
from math import cos, sin, pi,atan2

sq,SQ,p = 166,177,11
T = 10

a = WP().rect(SQ+6,SQ+6).circle(160/2).extrude(T).edges("|Z").fillet(5.5)
R1,R2,wall = 83,50,3
pts= [(R1,0),(R1,100),(R2,140),(R2,160),(R2-wall,160),(R2-wall,140-wall*0.707),(R1-wall,100-wall*0.707),(R1-wall,0)]
a = a.union(WP("XZ").polyline(pts).close().revolve(360,(0,0,0),(0,1,0)))
a = a.cut(WP().rect(sq,sq,forConstruction=True).vertices().circle(4/2).extrude(T))
a = a.faces("<Z[-2]").edges(NTPS((0,0,0))).fillet(3)

cq.exporters.export(a,"cowel.stl")


"""
a = WP().circle(100/2).circle(100/2).workplane(offset=20).workplane(offset=100).rect(160, 160)).workplane(offset=100).rect(160, 160).loft(combine=True)
#a = a.cut(WP().circle(94/2).workplane(offset=100).rect(154, 154).loft(combine=True))
 
a = a.union(WP().workplane(offset=0.5).circle(100/2).circle(94/2).extrude(-50))
"""