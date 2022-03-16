import cadquery as cq
from cadquery import Workplane as WP

C = 0.2 
Dc,Ds,Kw,Kh = 40,24+C,8+C,27+C
p = ((Ds/2)**2 - (Kw/2)**2)**0.5
Hc,Wc,Wp = 35,20,22
D1,D2 = 6,10
Sd = 25+C

keyway = WP().moveTo(-Kw/2,p).threePointArc((0,-Ds/2),(Kw/2,p))\
    .lineTo(Kw/2,Kh-Ds/2).lineTo(-Kw/2,Kh-Ds/2).close().extrude(-40)\
    .translate((0,0,-30))

a = WP().circle(Dc/2).extrude(Hc,both=True)
a = a.cut(WP("YZ").polyline([(Dc,Dc),(Wc/2,Dc),(Wc/2,Wc/2),(Dc,Wc/2)]).close().extrude(Dc,both=True))
a = a.cut(WP("YZ").polyline([(-Dc,Dc),(-Wc/2,Dc),(-Wc/2,Wc/2),(-Dc,Wc/2)]).close().extrude(Dc,both=True))
a = a.cut(WP().workplane(offset=10).rect(Wp,Dc).extrude(Hc))
a = a.faces(">Z[-2]").edges("|X").fillet(6)
a = a.faces(">Z[-2]").edges("|Y").fillet(6)
a = a.faces(">Z").edges("|X").fillet(9)
a = a.cut(WP("YZ").moveTo(0,Hc-Wc/2).circle(D1/2).extrude(Dc,both=True))
a = a.cut(WP("XZ").moveTo(0,-Hc+Wc/2).circle(3).extrude(Dc,both=True))
a = a.translate((0,0,-Hc+Wc/2))
c = a
a = a.cut(keyway)
show_object(a)

b = WP().box(Wp-C,Wp-C,Wp-C).intersect(WP().sphere(28/2))
b = b.cut(WP("YZ").circle(D1/2).extrude(Dc,both=True))
b = b.cut(WP("XZ").circle(D2/2).extrude(Dc))
b = b.cut(WP("XZ").circle(D2/2).extrude(-Wc/2))
b = b.cut(WP("XZ").circle(D1/2).extrude(-Dc))
show_object(b)

c = c.cut(WP("YZ").circle(D2/2).extrude(-Dc))
c = c.cut(WP("YZ").circle(D1/2).extrude(Dc))
c = c.cut(WP().workplane(offset=-30).circle(Sd/2).extrude(-Dc))
c = c.rotate((0,0,0),(0,0,1),90).rotate((0,0,0),(0,1,0),180)
show_object(c)




cq.exporters.export(a,"a.stl")
cq.exporters.export(b,"b.stl")
cq.exporters.export(c.rotate((0,0,0),(0,1,0),180),"c.stl")