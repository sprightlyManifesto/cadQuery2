from cadquery import *

a = Workplane().circle(40/2).extrude(15).cut(Workplane().circle(36/2).extrude(13))
a = a.faces(">Z[-2]").edges().fillet(3)
a = a.faces(">Z").edges().fillet(5)
a = a.rotate((0,0,0),(0,1,0),180)
exporters.export(a,"sofafoot.stl")
