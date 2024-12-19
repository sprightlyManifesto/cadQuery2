from cadquery import Workplane as WP
import cadquery as cq

H,W = 100,120

a = WP().rect(W,H).extrude(-10).edges("|Z").fillet(10)
a = a.cut(WP().rect(W-20,H-20,forConstruction=True).vertices().circle(3).extrude(-10))
a = a.cut(WP().text("15",100,-2).translate((-15,0,0)))

a = cq.exporters.export(a,"15.stl")