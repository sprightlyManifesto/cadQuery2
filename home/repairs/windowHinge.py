from cadquery import *

h,w,l,t = 56,16,23.5,5
pitch,dia,cbore = 25,4.5, 8.8
widthPiston = 10.5

a = Workplane().polyline([(0,0),(-h,0),(-h,l),(-h+16,l),(-h+16,l-t),(-h+t,l-t),
                          (-h+t,l-t-10.5),(-h+16,l-t-10.5),(-h+17,l-t-13.5),(0,l-t-13.5)]).close().extrude(w/2, both=True)

a = a.edges().fillet(1)

pts = [(-8,0),(-8-pitch,0)]

a = a.cut(Workplane("XZ").pushPoints(pts).circle(dia/2).extrude(-t))
a = a.cut(Workplane("XZ").workplane(offset=-t).pushPoints(pts).circle(cbore/2).extrude(2))
a = a.cut(Workplane("XZ").moveTo(-h+ 11.5,0).circle(3.3/2).extrude(-l))

exporters.export(a,"hingeMount.stl")