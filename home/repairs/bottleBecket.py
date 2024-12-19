import cadquery as cq
W = 27
f = 2
a = cq.Workplane("XY").polyline([(0,0),(5.5,12),(45,12)]).offset2D(2
).extrude(W)
a = a.faces(">Y[-2]").edges("<X").fillet(f)
a = a.union(cq.Workplane("XY").circle(8/2).extrude(W))
a = a.faces("<Y").edges("|Z").fillet(f)

# thining at hinge section
a = a.cut(cq.Workplane("XZ").center(0,W/2).rect(9*2,15)\
          .moveTo(0,11+5).rect(9*2,10)\
          .moveTo(0,-11-5).rect(9*2,10).extrude(20,both=True))

for e in (3,4): a = a.faces("|Z" and f">Z[-{e}]").edges("|Y").fillet(2)

a = a.faces(">Z").edges("<X").chamfer(2.4)
a = a.faces("<Z").edges("<X").chamfer(2.4)
a = a.faces("<Z").edges().fillet(1)
a = a.faces(">Z").edges().fillet(1)

a = a.cut(cq.Workplane("XY").circle(2.8/2).extrude(W))

a = a.cut(cq.Workplane("XZ").moveTo(28,W/2).rect(23,W-10).extrude(-W).edges("|Y").fillet(2))

a = a.faces(">Y").edges(">X[-1]").fillet(1)
a = a.faces(">Y[-2]").edges(">X[-1]").fillet(1)

cq.exporters.export(a,"bottleBecket.stl")