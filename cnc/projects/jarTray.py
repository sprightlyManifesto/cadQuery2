from cadquery import Workplane as WP
import cadquery as cq


i,j = 2,5
D,depth,T,L,W = 90,20,25,580,290
pitch = min(L/j,W/i) 

a = WP().rect(W,L).extrude(T)

for nx in range(i):
    x = -(i-1)*pitch/2 + pitch * nx
    for ny in range(j):
        y = -(j-1)*pitch/2 + pitch * ny
        a = a.cut(WP().workplane(offset=T).moveTo(x,y).circle(D/2).extrude(-depth))

cq.exporters.export(a,"jarTray.stl")