import cadquery as cq
from cadquery import Workplane as WP

h = 130
wall = 3

jimBoDeBobsPot = WP().circle(h/2).extrude(h)
jimBoDeBobsPot = jimBoDeBobsPot.cut(WP().workplane(offset =h).circle((h-wall)/2).extrude(-h+wall))
jimBoDeBobsPot = jimBoDeBobsPot.edges().fillet(wall/3)
b = WP().workplane(offset=h).moveTo(40,20).circle(1)

cq.exporters.export(jimBoDeBobsPot,f"{h}x{wall}_pot.stl")
