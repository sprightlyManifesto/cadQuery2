from cadquery import *

t,tw,mh = 50,20,2
l,d,w,h = 30,15,3,15
form = [(l/2,0),(0,0),(-l/2,0)]

a = Workplane().polyline(form).offset2D(d/2+w).extrude(h)
a = a.cut(Workplane().polyline(form).offset2D(d/2).extrude(h))
a = a.union(Workplane("XZ").workplane(h/2).center(0,t/2).rect(tw,t).extrude(w))
a = a.faces().edges("|Y").fillet(tw/2*0.95)
a = a.cut(Workplane("XZ").workplane(offset=h/2).center(0,t-tw/2).circle(mh).extrude(w))
a = a.cut(Workplane("XZ").workplane(offset=h/2).center(0,t-tw/2).circle(8/2).extrude(w-1))

exporters.export("cable_tidy.stl")