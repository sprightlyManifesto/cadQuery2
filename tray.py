from cadquery import *

tray = (150,150,40)
wall =2
a = Workplane().rect(tray[0],tray[1]).rect(tray[0]-wall*2,tray[1]-wall*2).extrude(tray[2])
a = a.union(Workplane().rect(tray[0],tray[1]).extrude(-wall-1))
a = a.faces("<Z").edges().chamfer(wall)
a = a.union(Workplane().rect(tray[0]-wall*2-0.5,tray[1]-wall*2-0.5).extrude(-wall*2-1))
a = a.edges("|Z").fillet(wall)
#a = a.faces("<Z").edges().chamfer(wall)




pitch = 100/3
holeCentres = [(-50,20),(-50+pitch,20),(-50+pitch*2,20),(-50+pitch*3,20)]
a = a.cut(Workplane("XZ").pushPoints(holeCentres).circle(30/2).extrude(100,both=True))
a = a.cut(Workplane("YZ").pushPoints(holeCentres).circle(30/2).extrude(100,both=True))

exporters.export(a,"tray.stl")