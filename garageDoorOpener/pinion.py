import cadquery as cq
from cadquery import Workplane as WP
from gear import gear

PCD = 146
C = 0.2 

#DiaCoupler, DiaShaft, KeywayWidth, KeywayHeight
Dc,Ds,Kw,Kh = 40,24+C,8+C,27+C
mod,bore,width,helixAngle = 2, Ds,25,0
p = ((Ds/2)**2 - (Kw/2)**2)**0.5
Hc,Wc,Wp = 35,20,22
D1,D2 = 6,10

T1 = 20
T2 = 53
T3 = 16
T4 = T1 + T2 -T3
"""
p = gear.spur(mod,T1,bore,width,helixAngle)
p = p.cut(WP().moveTo(0,Kh/4).rect(Kw,Kh/2).extrude(width))
cq.exporters.export(p,"pinon.stl")

bore = 10
second = gear.spur(mod,T2,bore,width,helixAngle)
teeth = 16
second = second.union(gear.spur(mod,T3,bore,width*2,helixAngle))
second = second.translate((PCD/2,0,0))
cq.exporters.export(second,"second.stl")
"""
#ratio = T2/T1*T4/T3
#log(ratio)

#third = gear.spur(mod,T4,bore,width,helixAngle).translate((0,0,width)
bore = Ds+2*C
a = WP().circle(Dc/2).extrude(Hc,both=False)
a = a.cut(WP("YZ").polyline([(Dc,Dc),(Wc/2,Dc),(Wc/2,Wc/2),(Dc,Wc/2)]).close().extrude(Dc,both=True))
a = a.cut(WP("YZ").polyline([(-Dc,Dc),(-Wc/2,Dc),(-Wc/2,Wc/2),(-Dc,Wc/2)]).close().extrude(Dc,both=True))
a = a.cut(WP().workplane(offset=10).rect(Wp,Dc).extrude(Hc))
a = a.faces(">Z[-2]").edges("|X").fillet(6)
a = a.faces(">Z[-2]").edges("|Y").fillet(6)
a = a.faces(">Z").edges("|X").fillet(9)
a = a.cut(WP("YZ").moveTo(0,Hc-Wc/2).circle(D1/2).extrude(Dc,both=True))
a = a.translate((0,0,0))
a = a.cut(WP().circle((bore+C)/2).extrude(8).faces(">Z").edges().chamfer(7.5))
a = a.union(gear.spur(mod,T4,(bore+C),-width,helixAngle))
#a = WP().circle(mod*teeth/2)

cq.exporters.export(a,"third.stl")