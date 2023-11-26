import cadquery as cq
from math import sin, cos ,tan, pi , asin, acos, atan

pts= [(27/2,37.8),(27/2,5.5),(12/2,5.5),(12/2,0),(42/2,0),(42/2,28),
      (76/2,28),(76/2,0),(90/2,0),(117/2,15),(101/2,15),(101/2,12.5),
      (105/2,12.5)]

pts.reverse()
for p in reversed(pts): pts.append((-p[0],p[1]))

a = cq.Workplane().polyline(pts).offset2D(1).extrude(100)
