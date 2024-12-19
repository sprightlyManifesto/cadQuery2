from cadquery import Workplane as WP
from math import sin,cos,pi

t = 3
N = 8
R1 = 120
a = WP()

for n in range(N):
    x,y = R1*sin(n/N*pi*2),R1*cos(n/N*pi*2)
    a = a.union(WP().lineTo(x,y).close().offset2D(t).extrude(t))
    m = 1 - 0.1*(n%2)
    for p, l in ((0.75,0.2),(0.5,0.35),(0.3,0.15)):
        for b in (1,-1):
            x1,y1 = R1*sin(n/N*pi*2)*p*m,R1*cos(n/N*pi*2)*p*m
            x2,y2 = R1*sin((n+b*m)/N*pi*2)*l/m,R1*cos((n+b*m)/N*pi*2)*l/m
            a = a.union(WP().moveTo(x1,y1).lineTo(x1+x2,y1+y2).close().offset2D(t).extrude(t))

cq.exporters.export(a,"snowflake.stl")