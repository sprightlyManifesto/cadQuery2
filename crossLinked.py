from cadquery import Workplane as WP
from math import pi, cos , sin , acos,atan
verbose = False

d1, pcd, pin, pitch,t = 20, 15, 3,30,-3

#calculate link lenght at limit of design travel -45 degrees | (-pi/4) radians
y = pcd/2*cos(-pi/4)
linkLength = ((y*2)**2 + pitch**2)**0.5


log("*"*80)
N = 20
for n in range(N):
    theta = (n-N/2)*pi/(N*2)
    x1,y1 = pcd/2*sin(theta), pcd/2*cos(theta)
    linkLength = ((y1*2)**2 + pitch**2)**0.5
    lv = ((x1-pitch)**2 + (y1)**2)**0.5
    wheel1 = WP().circle(d1/2).moveTo(x1,y1).circle(pin/2).extrude(t)
    #wheel1 = wheel1.cut(WP().moveTo(-d1/2,0).rect(4,d1).extrude(t).rotate())
    
    #rearange Cosine rule to get angle between lv and linklenght CosA = (b² + c² - a²)/2bc
    gamma = atan(y1/abs(x1-pitch)) + acos((linkLength**2 + lv**2 - (pcd/2)**2)/(2*linkLength*lv))
    
    if verbose: log(f"x1:{round(x1,3)} y1:{round(y1,3)} lenght:{abs(x1-pitch)/y1} gamma:{gamma}")
    #log(gamma)
    
    #x2,y2 are relative to wheel 2 center
    x2,y2 = linkLength*cos(gamma)+ x1-pitch, linkLength*-sin(gamma)+ y1 
    wheel2 = WP().circle(d1/2).moveTo(x2,y2).circle(pin/2).extrude(t).translate((pitch,0,0))
    
    f = WP().moveTo(x1,y1).polarLine(linkLength,-gamma/pi*180).close().offset2D(pin).extrude(-t)
    f = f.cut(WP().pushPoints([(x1,y1),(x2+pitch,y2)]).circle(pin/2).extrude(-t))
    
    #double check maths with drawing line of link lenght between calculated points
    if False:
        c = WP().moveTo(x1,y1).circle(linkLength)
        d = WP().moveTo(pitch,0).circle(pcd/2)
        e = WP().moveTo(x1,y1).lineTo(pitch,0)
    
#    log(f"{round(theta,3)} | {round(x1,3)},{round(y1,3)} | {round(x2,3)},{round(y2,3)} ")

    res = wheel1.union(wheel2).union(f)
    cq.exporters.export(res, f'{n}.svg')

log(linkLength)
