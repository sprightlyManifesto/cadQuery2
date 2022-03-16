#clares watch thingy
from cadquery import Workplane as WP

wD,oD,h,ledD = 40,55, 25,12
knobD = 7
strapW = 30

a = WP().circle(ledD/2).circle(oD/2).extrude(h)
a = a.cut(WP().workplane(offset=h).rect(oD,strapW).extrude(-10))
a = a.cut(WP().workplane(offset=h).moveTo(0,oD/2).rect(knobD,oD).extrude(-10))
a = a.cut(WP().workplane(offset=h).moveTo(12.5,-5.2).lineTo(12.5,5.2).close().offset2D(7.6/2).extrude(-18))
a = a.cut(WP().workplane(offset=h).moveTo(12.5,0).lineTo(12.5,-oD).close().offset2D(6.5/2).extrude(-17))
a = a.cut(WP().workplane(offset=h).lineTo(-oD,12).lineTo(-oD,-12).close().offset2D(ledD/2).extrude(-h))
a = a.cut(WP().workplane(offset=h).circle(40.5/2).extrude(-10))
a = a.edges("|Z").fillet(2)
a = a.faces(">Z").edges().fillet(1)

cq.exporters.export(a,"claresWatchStand.stl")