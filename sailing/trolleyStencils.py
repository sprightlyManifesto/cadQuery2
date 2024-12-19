from cadquery import Workplane as WP
import cadquery as cq

tags = []
classes = "TOPPER","PICO","LASER, FEVA"
T = 3

for F in (15,20,25,30):
    for txt in (classes):
        a = WP().text(txt,F,T,font="Gunplay")
        bb = a.val().BoundingBox()
        tags.append(WP().rect(bb.xlen+50,bb.ylen+10).extrude(T).edges("|Z").fillet(5).cut(a))
        cq.exporters.export(tags[-1],f"Stencil-{txt}_{F}mm.stl")

for e,t in enumerate(tags):
    show_object(t.translate((0,e*(50),0)))
