from cadquery import Workplane as WP
import cadquery as cq

H,W,T = 63.5,25.4,7
h,w = 47.2, 17.5

pts = [(W/2+T/2,0),(W/2+ 2,T+1),(W/2,T+1),(W/2,T),(-W/2,T),(-W/2,T+1),(-W/2-2,T+1),(-W/2-T/2,0)]

a = WP().polyline(pts).close().extrude(H/2,both=True)
a = a.cut(WP("XZ").rect(w,h, forConstruction=True).vertices().circle(3.2/2).extrude(-T))
a = a.faces(">Y").edges(">X or <X").fillet(1)

cq.exporters.export(a, "doorBoltBlock.step")