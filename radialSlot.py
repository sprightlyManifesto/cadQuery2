from cadquery import *
from math import *

def radialSlot(wp,slotRad, cutterRad, a1, a2,offset=(0,0)):
    IR = slotRad-cutterRad
    OR = slotRad+cutterRad
    middle = a1+(a2-a1)/2
    return(wp.moveTo(IR*sin(a1),IR*cos(a1))
     .threePointArc((IR*sin(middle),IR*cos(middle)),(IR*sin(a2),IR*cos(a2)))
     .tangentArcPoint((cutterRad*2*sin(a2),cutterRad*2*cos(a2)))
     .threePointArc((OR*sin(middle),OR*cos(middle)),(OR*sin(a1),OR*cos(a1)))
     .tangentArcPoint((-cutterRad*2*sin(a1),-cutterRad*2*cos(a1))).close()
     )


log(1)
a = Workplane().rect(20,20).extrude(3)

a1 = 0
a2 = pi*1.5
slotRad = 7.0
cutterRad =2.0

IR = slotRad - cutterRad
OR = slotRad + cutterRad
middle = a1+(a2-a1)/2

a = radialSlot(a.faces(">Z").workplane(offset=0.2),slotRad, cutterRad, a1, a2).cutBlind(-2)
a = radialSlot(a.faces(">Z").workplane(offset=0.2),10, .5,.5, a2).cutBlind(-1)
"""
G = (Workplane().moveTo(IR*sin(a1),IR*cos(a1))
     .threePointArc((IR*sin(middle),IR*cos(middle)),(IR*sin(a2),IR*cos(a2)))
     .tangentArcPoint((cutterRad*2*sin(a2),cutterRad*2*cos(a2)))
     .threePointArc((OR*sin(middle),OR*cos(middle)),(OR*sin(a1),OR*cos(a1)))
     .tangentArcPoint((-cutterRad*2*sin(a1),-cutterRad*2*cos(a1))).close().extrude(3)
)"""