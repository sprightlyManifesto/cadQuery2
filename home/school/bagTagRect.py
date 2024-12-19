from cadquery import Workplane as WP
import cadquery as cq

first = "James"
last =  "07711131304"
t = WP().rect(62,22).extrude(3).edges("|Z").fillet(5)
t = t.union(WP().text(first,10,5,valign="center").translate((0,5)))
t = t.union(WP().text(last,10,5,valign="center").translate((0,-4)))
t = t.cut(WP().pushPoints([(-25,5)]).circle(3).extrude(3))

cq.exporters.export(t,f"keyTag-{first}-{last}.stl")