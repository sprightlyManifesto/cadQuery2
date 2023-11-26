from cadquery import Workplane as WP
import cadquery as cq
L,H,T,D = 150,25,3,6

a = WP().rect(L,H).extrude(-T).edges("|Z").fillet(5)
a = a.cut(WP().center(L/2-D*0.75,H/2-D*0.75).circle(D/2).extrude(-T))
i = 0
tags = []
for t  in ("DORY","ROSIE","JAFFA","GREY","COMMITEE","RACE HUT","SCHOOL", "BOX 1", "BOX 2", "BOX 3", "BOX 4", "BOX 5","GARAGE 1", "GARAGE 2"): 
    tags.append(a.union(WP().text(t, 24,1)).translate((0,(H+T)*i,0)))
    i += 1
    cq.exporters.export(tags[-1],f"{t}.stl")

for t in tags: show_object(t)