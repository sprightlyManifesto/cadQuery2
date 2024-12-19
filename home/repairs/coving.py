from cadquery import Workplane as WP
import cadquery as cq

T = 9
W = 150

for n in (1,2,3,4,5):
    a = WP().rect(W,W/2).extrude(T).edges("|Z").fillet(10)
    a = a.cut(WP().workplane(offset=T/2).text("3",W/2,T,font="Chandas").translate((-W/4,0,0)))
    a = a.cut(WP().workplane(offset=T/2).rect(W/2-10,W/2-10).extrude(T).edges("|Z").fillet(5).translate((W/4,0,0)))
    exporters(a,f"board-{n}.stl")