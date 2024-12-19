from cadquery import Workplane as WP
from math import floor

a = WP().rect(460,460).extrude(25)
a = a.cut(WP().workplane(offset=25).rect(400,400).extrude(-3))
for i in range(64):
    x = 50*(i%8)-175
    y = 50*floor(i/8)-175
    a = a.cut(WP().workplane(offset=25).moveTo(x,y).circle(20).extrude(-5))

cq.exporters.export(a,"board.stl")