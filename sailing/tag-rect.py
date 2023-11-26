from cadquery import Workplane as WP
import cadquery as cq

tags = ["LASER 4.7", "LASER FULL", "RADIAL", "SAFETY BOATS"]

for text in tags:
    txt =WP().text(text,10,5,valign="center", fontPath="gunplay rg.ttf")
    bb = txt.val().BoundingBox()
    w = bb.xmax - bb.xmin + 5
    t = WP().polyline([(w/2,0),(-w/2,0)]).close().offset2D(10).extrude(3)
    t = t.cut(txt.translate((5,0,0)))
    t = t.cut(WP().pushPoints([(-w/2,0)]).circle(3).extrude(3))
    show_object(t)
    
    cq.exporters.export(t,f"bagTag-{text}.stl")