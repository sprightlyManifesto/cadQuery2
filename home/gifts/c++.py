from cadquery import Workplane as WP
from cadquery.selectors import LengthNthSelector as NthL 
from math import sin, cos, pi
T = 20


white = WP().polygon(6,240).extrude(T).rotate((0,0,0),(0,0,1),30)

pts = white.faces(">Z").wires().val().sample(24)
for p in pts[0]:
    white = white.cut(WP().moveTo(p.x,p.y).circle(10).extrude(T))
white = WP().circle(100/2).circle(50/2).extrude(T)
white = white.cut(WP().lineTo(100,100*sin(pi/6)).lineTo(100,-100*sin(pi/6)).close().extrude(T))
white = white.union(WP().text("++",30,T,kind="bold").translate((50,0,0)))

blue = WP().polygon(6,200).extrude(T).rotate((0,0,0),(0,0,1),30)
blue = blue.edges("|Z").fillet(20)
blue = blue.cut(white)

white = white.union(WP().polygon(6,230).extrude(T).rotate((0,0,0),(0,0,1),30))
white = white.cut(blue)

pts = white.faces(">Z").wires(NthL(0,directionMax=False)).val().sample(9*6)

black = WP().rect(250,250).extrude(T)
black = black.cut(WP().polygon(6,230).extrude(T).rotate((0,0,0),(0,0,1),30))

for e,p in enumerate(pts[0]):
    if e%9!=0:
        white = white.cut(WP().moveTo(p.x,p.y).circle(5.5/2).extrude(T))
        black = black.cut(WP().moveTo(p.x,p.y).circle(5.5/2).extrude(T))

assy = cq.Assembly()

assy.add(black,color=cq.Color(0,0,0))
assy.add(white,color=cq.Color(1,1,1))
assy.add(blue,color=cq.Color(0,0,1))

show_object(assy)

