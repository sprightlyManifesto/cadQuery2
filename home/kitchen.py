import cadquery as cq
from cadquery import Workplane as WP

wall,W,L,H = 300, 2950,9000,2400

kitchen = WP().rect(W+wall*2,L+wall*2).extrude(H).translate((W/2,L/2,-100))
kitchen = kitchen.cut(WP().rect(W,L).extrude(H).translate((W/2,L/2,0)))
kitchen = kitchen.cut(WP().rect(wall,800).extrude(H).translate((-wall/2,1240,0)))
kitchen = kitchen.cut(WP().rect(800,wall).extrude(H).translate((W/2,-wall/2,0)))
kitchen = kitchen.cut(WP().rect(800,wall).extrude(H).translate((1330,L+wall/2,0)))
kitchen = kitchen.cut(WP().rect(wall,2040).extrude(900).translate((W+wall/2,2700,900)))