from cadquery import Workplane as WP
import cadquery as cq

D,H,wall = 150,150,2

a = WP().circle(D/2).extrude(H)
a = a.cut(WP().workplane(offset=wall).circle(D/2-wall).extrude(H))
a = a.edges().fillet(wall*0.9)
a = a.cut(WP().workplane(offset=wall/2).text("Reggie",32,1))

cq.exporters.export(a,"reggie-pot.stl")
