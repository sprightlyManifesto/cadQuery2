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

a,b = 225,185

pkt = WP().workplane(offset=-5).rect(a,b).extrude(T)
pkt = pkt.union(WP().workplane(offset=-5).rect(b,a).extrude(T)).edges("|Z").fillet(5)
black = black.cut(pkt)
black = black.cut(WP().workplane(offset=T).rect(234,234).extrude(3))

x,y = 165/2,205/2
mntpts = [(x,y),(x,-y),(-x,y),(-x,-y)]
black = black.cut(WP().workplane(offset=-1).pushPoints(mntpts).circle(2/2).extrude(T))

pcb = WP().rect(a-1,b-1).extrude(1.6)
pcb = pcb.union(WP().rect(b-1,a-1).extrude(1.6)).edges("|Z").fillet(5)
pcb = pcb.cut(WP().pushPoints(mntpts).circle(3/2).extrude(1.6))

for e,p in enumerate(pts[0]):
    if e%9!=0:
        white = white.cut(WP().moveTo(p.x,p.y).circle(5.5/2).extrude(T))
        black = black.cut(WP().moveTo(p.x,p.y).circle(5.5/2).extrude(T))
        pcb = pcb.cut(WP().moveTo(p.x+1,p.y).circle(1/2).extrude(1.6))
        pcb = pcb.cut(WP().moveTo(p.x-1,p.y).circle(1/2).extrude(1.6))

R  = 110
switchx,switchy = R*cos(pi/3),-R*sin(pi/3)
pcb = pcb.cut(WP().moveTo(switchx,switchy).circle(1/2).extrude(1.6))
pcb = pcb.cut(WP().moveTo(-switchx,switchy).circle(1/2).extrude(1.6))
black = black.cut(WP().moveTo(-switchx,switchy).circle(3/2).extrude(T))
black = black.cut(WP().moveTo(switchx,switchy).circle(3/2).extrude(T))
assy = cq.Assembly()

assy.add(black,color=cq.Color(0,0,0))
assy.add(white,color=cq.Color(1,1,1))
assy.add(blue,color=cq.Color(0,0,1))
assy.add(pcb.translate((0,0,-6.6)),color=cq.Color(0,1,0))
show_object(assy)

cq.exporters.export(pcb.faces("<Z").edges(),"c++pcb.dxf")