import cadquery as cq
from cadquery import Workplane as WP
from math import sin,cos,tan,pi

ID,OD = 50,65
cw,r = 1, 0.2

ca = 90
W = 8
#R suffix for Radians i prefix for included angle
incAR = (pi - ca/180*pi)/2

log(incAR)
x1,y1  = cw/2 + r*sin(incAR), r- r*cos(incAR)
x2,y2 = W/2, y1 + (W/2-x1) * tan(incAR)
y0 = ID/2
y1 += y0
y2 += y0

a= WP().moveTo(y0,ID/2)\
    .lineTo(cw/2,y0).radiusArc((x1,y1),-r).lineTo(x2,y2)\
    .lineTo(x2,OD/2).lineTo(-x2,OD/2)\
    .lineTo(-x2,y2).lineTo(-x1,y1).radiusArc((-cw/2,y0),-r).close()



x1,y1  = cw/2 + r*sin(incAR), r- r*cos(incAR)
x2,y2 = W/2, y1 + (W/2-x1) * tan(incAR)
y0 = ID/2
y1 += y0
y2 += y0


a = a.revolve(90,(0,0,0),(1,0,0))