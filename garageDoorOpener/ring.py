import cadquery as cq
from cadquery import Workplane as WP
from gear import gear

C = 0.2 
#DiaCoupler, DiaShaft, KeywayWidth, KeywayHeight
Dc,Ds,Kw,Kh = 40,24+C,8+C,27+C
PCD = 145.5
D = 175
mod,teeth,bore,width,helixAngle = 2, 80, Ds,25,0

p = gear.ring(mod,teeth,bore,width,helixAngle,D)
#p = p.cut(WP().moveTo(0,Kh/4).rect(Kw,Kh/2).extrude(width))

cq.exporters.export(p,"ring.stl")
a = WP().circle(mod*teeth/2)