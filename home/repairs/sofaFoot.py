from cadquery import *
H=10
ID = 36
wall = 3
a = Workplane().circle(ID/2+wall).extrude(H).cut(Workplane().circle(ID/2).extrude(13))
a = a.faces(">Z[-2]").edges().fillet(3)
a = a.faces(">Z").edges().fillet(5)
a = a.rotate((0,0,0),(0,1,0),180)
exporters.export(a,"sofafoot.stl")
