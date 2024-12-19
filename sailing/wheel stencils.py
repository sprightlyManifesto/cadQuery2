from cadquery import Workplane as WP
import cadquery as cq

textD = 275
R = textD/2
OD = 360
dTheta = 15

tags = []
classes = "TOPPER","PICO","LASER", "FEVA"
T = 12
F = 40

for txt in (classes):
    a = WP().circle(27/2).circle(OD/2).extrude(T)
    for e,l in enumerate(txt):
        a = a.cut(WP().text(l,F,T,font="Gunplay").translate((0,R,0)).rotate((0,0,0),(0,0,1),e*-dTheta))
        a = a.cut(WP().text(l,F,T,font="Gunplay").translate((0,R,0)).rotate((0,0,0),(0,0,1),e*-dTheta-180))
    tags.append(a)
    cq.exporters.export(tags[-1],f"Stencil-Round-{txt}_{F}mm.stl")

for t in tags:
    show_object(t)