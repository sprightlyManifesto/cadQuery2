from cadquery import *
from math import sin,cos,pi

cutAngle = 100
cutBase = 1
cutWidth = 8
cutRad = 0.2

x1,y1 = -cutBase/2 , 0
theta = pi*(cutAngle/2)/180

rtheta = (pi/2 - theta)

log(rtheta*180/pi)
x2,y2 = (-cutRad * sin(rtheta) + x1 ,  cutRad - cutRad * cos(rtheta))
x3,y3 = -cutWidth/2, (cutWidth/2- y2)*sin(rtheta)
log(f"x2:{round(x2,2)} y2:{round(y2,2)} y3:{round(y3,2)}")

a = Workplane().lineTo(x1,y1).radiusArc((x2,y2),cutRad).lineTo(-cutWidth/2,y3).lineTo(-cutWidth/2,10)\
   .lineTo(cutWidth/2,10).lineTo(cutWidth/2,y3).lineTo(-x2,y2).radiusArc((-x1,y1),cutRad).close()
