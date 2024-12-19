import cadquery as cq
from cadquery import Workplane as WP
from cadquery.selectors import NearestToPointSelector as NTPS
from math import cos, sin, pi,atan2

a = WP().circle(100/2).extrude(40,both=True)
a = a.union(WP().circle(110/2).extrude(6,both=True).edges().chamfer(5))
a = a.cut(WP().circle(94/2).extrude(40,both=True))

cq.exporters.export(a,"100mmJoint.stl")