from cadquery import Workplane as WP
import cadquery as cq

tags = ["LASER 4.7", "LASER FULL", "RADIAL", "SAFETY BOATS","RACE HUT","DISCO","L HARGREAVES","J HARGREAVES"]
T = 4

for e,text in enumerate(tags):
    txt = WP().text(text,10,T,valign="center").translate((0,0,0.5))
    bb = txt.val().BoundingBox()
    w = bb.xmax - bb.xmin + 5
    t = WP().polyline([(w/2,0),(-w/2,0)]).close().offset2D(10).extrude(T/2,both=True)
    t = t.cut(txt.translate((5,0,0)))
    t = t.cut(txt.translate((5,0,0)).rotate((0,0,0),(1,0,0),180))
    t = t.cut(WP().pushPoints([(-w/2,0)]).circle(T).extrude(T/2,both=True))
    show_object(t.translate((0,25*e,0)))
    
    cq.exporters.export(t,f"bagTag-{text}.stl")