import cadquery as cq
from math import sin, cos, tan, pi

af = 10
r = af*sin(pi/4)

a = cq.Workplane().rect(100,60).extrude(20)