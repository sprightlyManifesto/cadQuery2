from cadquery import Workplane as WP
import cadquery as cq
#collet tray

N = 7 
pitch = 25
Dia,H,D= 19,19,16
L = pitch * (N) + pitch-D
a = WP().rect(pitch *2+pitch-D,L).extrude(19).edges("|Z").fillet(3)

Ys= [y*pitch-N*pitch/2+pitch/2 for y in range(N)]

for y in Ys:
    a = a.cut(WP().workplane(offset=H).moveTo(pitch/2,y).circle(Dia/2).extrude(-D))
    a = a.cut(WP().workplane(offset=H).moveTo(-pitch/2,y).circle(Dia/2).extrude(-D))

cq.exporters.export(a,"colletTray.stl")