from cadquery import Workplane as WP
import cadquery as cq

first = "Lizzie"
last =  "Hargreaves"
t = WP().rect(55,22).extrude(3).edges("|Z").fillet(5)
t = t.union(WP().text(first,10,5,valign="center").translate((0,5)))
t = t.union(WP().text(last,10,5,valign="center").translate((0,-3)))
t = t.cut(WP().pushPoints([(-21,5),(21,5)]).circle(3).extrude(3))

cq.exporters.export(t,f"bagTag-{first}-{last}.stl")