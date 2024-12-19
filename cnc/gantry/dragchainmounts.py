import cadquery as cq
from cadquery import Workplane as WP

T = 16
L = 60
a = WP().moveTo(L/2,0).rect(L,26).extrude(T/2,both=True)
a = a.union(WP().moveTo(5,0).rect(10,50).extrude(T/2,both=True))
a = a.faces(">Y[-2] or <Y[-2]").edges("<X").fillet(4)
a = a.cut(WP("YZ").pushPoints([(20,0),(-20,0)]).circle(7/2).extrude(L))
a = a.cut(WP("YZ").workplane(offset=10).pushPoints([(20,0),(-20,0)]).circle(13.7/2).extrude(L))
a = a.faces(">X").edges(">Z").chamfer(T-2)
l = L-13
a = a.cut(WP().pushPoints([(l-3.5,5.5),(l+3.5,-5.5)]).circle(3.3/2).extrude(L,both=True))

T = 20
L = 25
b = WP().moveTo(L/2,0).rect(L,26).extrude(T/2,both=True)
b = b.union(WP().moveTo(5,0).rect(10,80).extrude(T/2,both=True))
b = b.faces(">Y[-2] or <Y[-2]").edges("<X").fillet(10)
b = b.cut(WP("YZ").pushPoints([(30,0),(-30,0)]).circle(5/2).extrude(L))
b = b.faces(">X").edges(">Z").chamfer(T-2)
l = L-13
b = b.cut(WP().pushPoints([(l-5.5,3.5),(l+5.5,-3.5)]).circle(3.3/2).extrude(L,both=True))
b = b.translate((0,80,0))

T = 16
L = 60
c = WP().moveTo(L/2,0).rect(L,26).extrude(T/2,both=True)
c = c.union(WP().moveTo(5,0).rect(10,56).extrude(T/2,both=True))
c = c.faces(">Y[-2] or <Y[-2]").edges("<X").fillet(4)
c = c.cut(WP("YZ").pushPoints([(23,0),(-23,0)]).circle(7/2).extrude(L))
c = c.faces(">X").edges(">Z").chamfer(T-2)
l = L-13
c = c.cut(WP().pushPoints([(l-3.5,5.5),(l+3.5,-5.5)]).circle(3.3/2).extrude(L,both=True))
c = c.translate((0,-80,0))