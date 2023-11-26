import cadquery as cq
from cadquery import Workplane as WP
from math import pi,cos,sin

W,H,T = 152,170,35
mhp = 35
wheelbase = 130
mountToCw = 22.5
W = wheelbase-mountToCw*2
pts = [(wheelbase/2,0),(-wheelbase/2,0)]
a = WP().workplane(offset=0).rect(W,H).extrude(T/2,both=True)

#motorBody Relifes

ptsM3 = []
for p in pts:
    ptsM3.append((p[0]+mhp/2,p[1]))
    ptsM3.append((p[0]-mhp/2,p[1]))

print(ptsM3)

x,y = 26.4,29.2
for d in (1,-1):
    a = a.union(WP("YZ").workplane(offset=d*W/2).center(0,0).pushPoints(pts).rect(35,35).extrude(W/2*-d))
    #a = a.union(WP("YZ").workplane(offset=d*W/2).pushPoints(ptsM3).circle(T).extrude(10*-d))
    a = a.cut(WP("YZ").workplane(offset=d*W/2).pushPoints(pts).circle(28.5/2).extrude(18.5*-d))
    a = a.cut(WP("YZ").workplane(offset=d*W/2).pushPoints(ptsM3).circle(2.5/2).extrude(10*-d))
    a = a.cut(WP("YZ").workplane(offset=d*W/2).pushPoints(pts).rect(17.5,31).extrude(17.5*-d))
    a = a.cut(WP("YZ").workplane(offset=d*W/2).pushPoints(pts).rect(7,40).extrude(4*-d))
    for c in (W/4,-W/4):
        a = a.cut(WP("XZ").center(c,0).workplane(offset=-H/2*d).rect(x,y,forConstruction=True).vertices().circle(1.6/2).extrude(4.5*d))


pocket = WP().workplane(offset=3-T/2).rect(W-18.5*2,H-10).extrude(T).union(WP().workplane(offset=3-T/2).rect(W-5,90).extrude(T))

a = a.cut(pocket.edges("|Z").fillet(2))
a = a.union(WP().center(0,-12).workplane(offset=-T/2).rect(49,58,forConstruction=True).vertices().circle(5/2).extrude(6))
a = a.cut(WP().center(0,-12).workplane(offset=-T/2).rect(49,58,forConstruction=True).vertices().circle(2.5/2).extrude(T))
a = a.cut(WP().center(0,-12).workplane(offset=-T/2).rect(49,58,forConstruction=True).vertices().polygon(6,4/cos(pi/6)).extrude(2))
a = a.cut(WP().moveTo(0,8).lineTo(0,-8).close().offset2D(4).extrude(H,both=True).rotate((0,0,0),(1,0,0),90))

#a = a.edges("|X").fillet(0.3)

#motor driver posts
#a = a.union(WP().workplane(offset=T/2).moveTo(W/2-32/2).rect(32,10).extrude(35))

driver = WP().workplane(offset=T/2).rect(32,35)
pi = WP().workplane(offset=T/2).rect(56,90)
brick = WP().workplane(offset=T/2).rect(81,170)

show_object(a)

cq.exporters.export(a,"chassis.stl")

#a = a.faces(">Z").shell(2)

