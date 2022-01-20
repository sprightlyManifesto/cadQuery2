import cadquery as cq
from pallet import Pallet
from cadquery import exporters
from math import sin, cos, pi

poly = []


for an in (0,60,120,180,240,300):
    poly.append((sin(an/180*pi),cos(an/180*pi)))

a = cq.Workplane().polyline(poly).close().offset2D(.8).extrude(1)



#z = cq.importers.importDXF("/home/r/untitled.dxf")

#b = a.offset2D(-1)
#c = b.offset2D(-1)
#d = c.offset2D(-1)
#p = Pallet()

#line = [(0,0),(1,10),(2,10),(3,0),(4,0),(5,10),(6,10),(7,0)]
#a = cq.Workplane().polyline(line)
#b = a.offset2D(1.5)

#a = p.torx(cq.Workplane(),10)
#b = a.offset2D(0.2)
#c = a.offset2D(0.5)
#d = p.torx(cq.Workplane(),40)
#e = d.offset2D(-0.1)
#exporters.export(a, 'object.dxf')

#a = cq.Workplane().moveTo(1,0).threePointArc((0,5),(-1,0)).threePointArc((0,-5),(1,0)).close()

#raduis arc goes the shortest route flipping each direction as requiredd
#c = cq.Workplane().moveTo(0,2).radiusArc((2,0),2)

#radius arc is relative to origin, only one solution is determined requires a proceeding arc or vector
#d = cq.Workplane().lineTo(0,5).tangentArcPoint((2,0)).close()

#radius arc is relative to origin and will flip direction to meet constraints
#a = cq.Workplane().lineTo(0,5).tangentArcPoint((-2,0)).lineTo(-2,0).close().extrude(1)
#b = a.faces(">Z").edges()
#c = cq.Sketch().pushPoints([(10,10),(0,0)]).circle(2).extrude(2)

#Workplane.sagittaArc(EP,sag) sag is at 270 degrees to vector normal
#e = cq.Workplane().sagittaArc((0,1),-12)
#f = cq.Workplane().sagittaArc((0,1),-11)
#g = cq.Workplane().sagittaArc((0,1),-10)
#h = cq.Workplane().sagittaArc((0,1),-9)
#Workplane.sagittaArc(EP,sag) sag is 
#f = cq.Workplane().sagittaArc((3,3),12)

