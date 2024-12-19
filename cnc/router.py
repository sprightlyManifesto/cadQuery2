from cadquery import Workplane as WP
from cadquery.selectors import RadiusNthSelector as NthR 
from math import cos, sin, tan, pi
import cadquery as cq

def bar(sq,L,plane="XY"):
    a = WP(plane).rect(sq,sq).extrude(L/2,both=True)
    return(a)

Y = 100
span = 910
railY = span+40
assy = cq.Assembly()
assy = assy.add(bar(50,1150,"XZ").translate((-railY/2,0,0)))
assy = assy.add(bar(50,1150,"XZ").translate((railY/2,0,0)))
assy = assy.add(bar(50,railY-50,"YZ").translate((0,0,0)))
assy = assy.add(bar(50,railY-50,"YZ").translate((0,1150/2-25,0)))
assy = assy.add(bar(50,railY-50,"YZ").translate((0,-1150/2+25,0)))
#Right Left
h,w,offset,sq = 200,120,25+60,40

for i in (1,-1):
    assy = assy.add(bar(sq,h-sq*2,"XY").translate((i*railY/2,Y-w/2+sq/2, h/2+offset)))
    assy = assy.add(bar(sq,h-sq*2,"XY").translate((i*railY/2,Y+w/2-sq/2, h/2+offset)))
    assy = assy.add(bar(sq,w,"XZ").translate((i*railY/2,Y,offset+sq/2)))
    assy = assy.add(bar(sq,w,"XZ").translate((i*railY/2,Y,offset+h-sq/2)))
    #cross peices:
    top = offset - sq/2 + h
    assy = assy.add(bar(sq,span,"YZ").translate((0,Y+i*(w-sq)/2,top)))
    assy = assy.add(bar(sq,span,"YZ").translate((0,Y+i*(w-sq)/2,top-160)))

show_object(assy)