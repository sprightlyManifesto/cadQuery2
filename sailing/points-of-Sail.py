from cadquery import Workplane as WP
import cadquery as cq
from math import sin, cos, pi

L = 30
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
main = main.rotate((0,0,0),(0,0,1),45)

parts = []
names = ["Close Haul", "Close Reach", "Beam Reach", "Broad Reach","Training Run"]

for n,a in enumerate([45,67.5,90,120,160]):
    pt = form.rotate((0,0,0),(0,0,1),a)
    pt = pt.union(main.rotate((0,0,0),(0,0,1),(-45+a)*0.2).translate((-sin(a/180*pi)*(R-L/3),cos(a/180*pi)*(R-L/3))))
    if n ==0:
        pt = pt.union(WP().text(names[n],20,1).rotate((0,0,0),(0,0,1),a))
    parts.append(pt)

part = WP().circle(R+5).circle(R-L-5).extrude(-T)

for p in parts:
    part = part.union(p)
    part = part.union(p.mirror("YZ"))

W = (L-3)/6
arrowPts = [(-W/2,0),(W/2,0),(W/2,-(L-3)/4*3),(W,-(L-3)/4*3),(0,-(L-3)),(-W,-(L-3)/4*3),(-W/2,-(L-3)/4*3)]
part = part.union(WP().polyline(arrowPts).close().offset2D(1).extrude(T).translate((0,R,0)))
show_object(part)

cq.exporters.export(part,"PointsOfSail.step")