import cadquery as cq

a = cq.Workplane("XY").box(50,20,3).faces().edges("|Z").fillet(3).faces(">Z").edges().chamfer(1)
a = a.moveTo(-10,0).circle(1.4).moveTo(17.5,0).circle(1.4).extrude(6).faces(">Z").edges().chamfer(0.2)

cq.exporters.export(a,"plate.stl")