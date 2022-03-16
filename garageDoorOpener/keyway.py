import cadquery as cq
from cadquery import Workplane as WP

Dc,Ds,Kw,Kh = 40,24.2,8.2,27.2
p = ((Ds/2)**2 - (Kw/2)**2)**0.5

keyway = WP().moveTo(-Kw/2,p).threePointArc((0,-Ds/2),(Kw/2,p))\
    .lineTo(Kw/2,Kh-Ds/2).lineTo(-Kw/2,Kh-Ds/2).close().extrude(40)\
    .translate((0,0,-30))

c = WP().circle(Dc/2).extrude(5).cut(keyway)

r = -120
txt = WP()
for t in f"{Kw}x{Kh}x{Ds}":
    txt = txt.union(WP().text(t,8,5.5).translate((0,-Dc/2 +(Dc-Ds)/4,0)).rotate((0,0,0),(0,0,1),r))
    r += 20

c = c.union(txt)

show_object(c)

cq.exporters.export(c,"0point2.stl")