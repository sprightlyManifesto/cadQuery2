#Holds COLD in pi with brokenSD Slot

import cadquery as cq

holeSpacing= 49
width = 56
inner = 56-6.5*2

r = cq.Workplane().polyline([(0,-6.5),(0,0),(-2,0),(-2,8),(2,8),(2,-6.5)]).close().extrude(width/2,both=True)
r = r.faces(">X").workplane().pushPoints([(-3.5,holeSpacing/2),(-3.5,-holeSpacing/2)]).hole(2.5)

r = r.cut(cq.Workplane("YZ").polyline([(1.5,inner/2),(1.5,-inner/2),(-6.5,-inner/2),(-6.5,inner/2)]).close().extrude(3,both=True))
r = r.faces("<Y").edges("|X").fillet(3.2)
r = r.faces(">Y").edges("|X").fillet(3.2)
r = r.faces(">Z[-2]").edges(">Y").fillet(3)
r = r.faces("<Z[-2]").edges(">Y").fillet(3)

cq.exporters.export(r,"piCardRetainer.stl")