import cadquery as cq

pts = [-30,-15,0,15,30]
dias= [11.8,11.9,12,12.1,12.2]
   
r = cq.Workplane().rect(80,20).extrude(6.5).faces(">X").edges("|Z").fillet(5).faces("<X").edges("|Z").fillet(8)

for i in range(0,len(pts)):
    r = r.cut(cq.Workplane().moveTo(pts[i],0).circle(dias[i]/2).extrude(6.5))

cq.exporters.export(r,"holeTest.stl")