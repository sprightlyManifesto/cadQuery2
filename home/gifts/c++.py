from cadquery import Workplane as WP
from cadquery.selectors import LengthNthSelector as NthL 
from math import sin, cos, pi
T = -20
pocket = 15

white = WP().polygon(6,240).extrude(T+pocket).rotate((0,0,0),(0,0,1),30)

pts = white.faces(">Z").wires().val().sample(24)
for p in pts[0]:
    white = white.cut(WP().moveTo(p.x,p.y).circle(10).extrude(T+pocket))
white = WP().circle(100/2).circle(50/2).extrude(T+pocket)
white = white.cut(WP().lineTo(100,100*sin(pi/6)).lineTo(100,-100*sin(pi/6)).close().extrude(T+pocket))
white = white.union(WP().text("++",30,T+pocket,kind="bold").translate((50,0,0)))

blue = WP().polygon(6,190).extrude(T+pocket).rotate((0,0,0),(0,0,1),30)
blue = blue.edges("|Z").fillet(20)
blue = blue.cut(white)

white = white.union(WP().polygon(6,220).extrude(T+pocket).rotate((0,0,0),(0,0,1),30))
white = white.cut(blue)

pts = white.faces(">Z").wires(NthL(0,directionMax=False)).val().sample(9*6)

black = WP().rect(240,240).extrude(T).edges("|Z").fillet(10)
black = black.cut(WP().polygon(6,220).extrude(T).rotate((0,0,0),(0,0,1),30))

pkt = pkt =WP().workplane(offset=T+pocket).polygon(6,240).extrude(T).rotate((0,0,0),(0,0,1),30).edges("|Z").fillet(50)
x,y = 110*sin(pi/6),110*cos(pi/6)
pkt = pkt.union(WP().workplane(offset=T+pocket).moveTo(x,y).lineTo(-x,-y).close().offset2D(10).extrude(T))
pkt = pkt.union(WP().workplane(offset=T+pocket).moveTo(-x,y).lineTo(x,-y).close().offset2D(10).extrude(T))
pkt = pkt.edges("|Z").fillet(10)
black = black.cut(pkt)
mntpts = [(x,y),(x,-y),(-x,y),(-x,-y)]
black = black.cut(WP().workplane(offset=T+pocket).pushPoints(mntpts).circle(2/2).extrude(4))


for e,p in enumerate(pts[0]):
    if e%9!=0:
        white = white.cut(WP().moveTo(p.x,p.y).circle(5.5/2).extrude(T))
        black = black.cut(WP().moveTo(p.x,p.y).circle(5.5/2).extrude(T))

assy = cq.Assembly()

assy.add(black,color=cq.Color(0,0,0))
assy.add(white,color=cq.Color(1,1,1))
assy.add(blue,color=cq.Color(0,0,1))

show_object(assy)

