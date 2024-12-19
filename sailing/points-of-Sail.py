from cadquery import Workplane as WP
import cadquery as cq
from math import sin, cos, pi

L = 150
T = 3.5

scale = L/5050
#dinghy outline
form = WP().radiusArc((895*scale,-2100*scale),9340*scale/2)\
    .radiusArc((875*scale,-4100*scale),12110*scale/2)\
    .lineTo(705*scale,-5050*scale)\
    .lineTo(-705*scale,-5050*scale)\
    .radiusArc((-895*scale,-2100*scale),12110*scale/2)\
    .radiusArc((0,0),9340*scale/2).close().extrude(T).edges("|Z").fillet(2)


R = L*2.5
form = form.translate((0,R,0))

main = WP().radiusArc((-300*scale,-600*scale),-800*scale).radiusArc((0*scale,-2500*scale),-4000*scale).offset2D(1).extrude(T+1)
s2 = scale/2
jib = WP().radiusArc((-300*s2,-600*s2),-800*s2).radiusArc((0*s2,-2500*s2),-4000*s2).offset2D(1).extrude(T+1)

parts = []
names = ["Close Hauled", "Close Reach", "Beam Reach", "Broad Reach","Training Run"]

for tack in (1,-1):
    for a,n in zip([45,67.5,90,120,160],names):
        cx,cy = -sin(a/180*pi)*(R-L/3)*tack,cos(a/180*pi)*(R-L/3)
        cx2,cy2 = -sin(a/180*pi)*(R-L/8)*tack,cos(a/180*pi)*(R-L/8)
        pt = form.rotate((0,0,0),(0,0,1),a*tack)
        if tack == 1:
            sail = main
            j = jib
            pt = pt.union(WP().text(n,20,1).translate((cx*1.5,cy*1.5)))
        else:
            sail = main.mirror("YZ")
            j = jib.mirror("YZ")
            
        pt = pt.union(sail.rotate((0,0,0),(0,0,1),(a*0.4+20)*tack).translate((cx,cy)))
        pt = pt.union(j.rotate((0,0,0),(0,0,1),(a*0.4+20)*tack).translate((cx2,cy2)))
        parts.append(pt)

part = WP()

for p in parts:
    part = part.union(p)

W = (L-3)/6
arrowPts = [(-W/2,0),(W/2,0),(W/2,-(L-3)/4*3),(W,-(L-3)/4*3),(0,-(L-3)),(-W,-(L-3)/4*3),(-W/2,-(L-3)/4*3)]
part = part.union(WP().polyline(arrowPts).close().offset2D(1).extrude(T).translate((0,R,0)))
show_object(part)

cq.exporters.export(part,"PointsOfSail.step")