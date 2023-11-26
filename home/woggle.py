from cadquery import Workplane as WP
import cadquery as cq

a = WP().circle(17/2).circle(24/2).extrude(2,both=True)

a = a.union(WP().circle(20/2).circle(24/2).extrude(25/2,both=True))

a = a.faces(">Z[-2]").edges().fillet(0.45)
a = a.faces("<Z[-2]").edges().fillet(0.45)

cq.exporters.export(a, "woggle.stl")