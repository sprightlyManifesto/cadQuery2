from cadquery import *

r = Workplane().threePointArc((3,4),(6,6)).threePointArc((5,4),(5,0)).lineTo(5,-1)\
    .lineTo(2.5,-7).lineTo(0,-1).close().extrude(.66)
exporters.export(r, "sharkfin.stl")