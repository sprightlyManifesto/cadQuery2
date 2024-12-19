#spray can holder
import cadquery as cq
from cadquery import Workplane as WP
from cadquery.selectors import RadiusNthSelector as NthR

a = WP().circle(74/2).extrude(60,both=True).rotate((0,0,0),(1,0,0),15)
a = a.cut(WP().rect(200,200).extrude(-100))
b = WP().circle(68/2).extrude(60,both=True).rotate((0,0,0),(1,0,0),15)
b = b.cut(WP().workplane(offset=5).rect(200,200).extrude(-100))
a = a.cut(b)
a = a.cut(WP().pushPoints([(20,0),(-20,0)]).circle(5/2).extrude(20))
a = a.faces("<Z[-2]").edges(NthR(0)).chamfer(2)

a = a.faces(">Z").edges().fillet(1)

show_object(a)

cq.exporters.export(a,"sprayCanHolder.stl")