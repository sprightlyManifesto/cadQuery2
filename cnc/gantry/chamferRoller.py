#chamfer bearing
from cadquery import *
bearingOD = 21.8
bearingT = 6.5
thruBore = 19
OD = 42
T = 20
H = 20

a = Workplane().circle(OD/2).extrude(T).faces(">Z").chamfer(4).faces("<Z").chamfer(4)
a = a.cut(Workplane().circle(thruBore/2).extrude(T))
a = a.cut(Workplane().circle(bearingOD/2).extrude(bearingT))
a = a.cut(Workplane().workplane(offset=T).circle(bearingOD/2).extrude(-bearingT))

exporters.export(a,"roller.stl")