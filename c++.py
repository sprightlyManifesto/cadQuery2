from cadquery import Workplane as WP
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

white = white.union(WP().polygon(6,250).extrude(T).rotate((0,0,0),(0,0,1),30))
white = white.cut(blue)


