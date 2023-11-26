import cadquery as cq

h=2
f = 50

a = cq.Workplane().text("6:30",f,h*2)
a = a.union(cq.Workplane().rect(f*2.2,f*1.1)
            .extrude(-h).edges("|Z").fillet(3))
a = a.faces(">Z").edges().fillet(1)

cq.exporters.export(a,"sixThirty.stl")