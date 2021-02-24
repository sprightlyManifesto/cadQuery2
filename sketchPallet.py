from cadquery import *
from math import sin,cos,acos,asin,pi,atan2

def radialSlot(wp,slotRad, cutterRad, a1, a2,offset=(0,0)):
    if slotRad > cutterRad:
        IR = slotRad-cutterRad
        OR = slotRad+cutterRad
        middle = a1+(a2-a1)/2
        result = (wp.moveTo(IR*sin(a1),IR*cos(a1))
         .threePointArc((IR*sin(middle),IR*cos(middle)),(IR*sin(a2),IR*cos(a2)))
         .tangentArcPoint((cutterRad*2*sin(a2),cutterRad*2*cos(a2)))
         .threePointArc((OR*sin(middle),OR*cos(middle)),(OR*sin(a1),OR*cos(a1)))
         .tangentArcPoint((-cutterRad*2*sin(a1),-cutterRad*2*cos(a1))).close()
         )
    else:
        result = wp
        #log("issues")
    return(result)

def hexAF(wp,af):
    R = af/cos(pi/6)/2
    return wp.moveTo(-sin(pi/6)*R,af/2).lineTo(sin(pi/6)*R,af/2).lineTo(R,0)\
        .lineTo(sin(pi/6)*R,-af/2).lineTo(-sin(pi/6)*R,-af/2).lineTo(-R,0).close()

def torx(wp,no):
    tab = {6:(1.75,1.27),8:(2.4,1.75),10:(2.8,2.05),15:(3.35,2.4),20:(3.95,2.85)}
    A , B = tab[no]
    re=A*0.1
    ri=A*0.175
    H = re + ri 
    O = B + ri - cos(pi/6)*(A-re)
    theta = pi/2 - acos(O/H)
    log(f"theta {theta}")
    x =  H*cos(theta)
    y = -H*sin(theta)+ B + ri
    phi = atan2(x,y)
    R = (x**2+y**2)**0.5
    Rm = B+ri
    res = wp.moveTo(R*sin(-phi),R*cos(-phi)).threePointArc((0,B),(R*sin(phi),R*cos(phi))) \
        .threePointArc((Rm*sin(pi/6),Rm*cos(pi/6)),(R*sin(pi/3-phi),R*cos(pi/3-phi))) \
        .threePointArc((B*sin(pi/3),  B*cos(pi/3)),(R*sin(phi+pi/3),R*cos(phi+pi/3))) \
        .threePointArc((Rm*sin(3*pi/6),Rm*cos(3*pi/6)),(R*sin(2*pi/3-phi),R*cos(2*pi/3-phi))) \
        .threePointArc((B*sin(2*pi/3),  B*cos(2*pi/3)),(R*sin(phi+2*pi/3),R*cos(phi+2*pi/3))) \
        .threePointArc((Rm*sin(5*pi/6),Rm*cos(5*pi/6)),(R*sin(3*pi/3-phi),R*cos(3*pi/3-phi))) \
        .threePointArc((B*sin(3*pi/3),  B*cos(3*pi/3)),(R*sin(phi+3*pi/3),R*cos(phi+3*pi/3))) \
        .threePointArc((Rm*sin(7*pi/6),Rm*cos(7*pi/6)),(R*sin(4*pi/3-phi),R*cos(4*pi/3-phi))) \
        .threePointArc((B*sin(4*pi/3),  B*cos(4*pi/3)),(R*sin(phi+4*pi/3),R*cos(phi+4*pi/3))) \
        .threePointArc((Rm*sin(9*pi/6),Rm*cos(9*pi/6)),(R*sin(5*pi/3-phi),R*cos(5*pi/3-phi))) \
        .threePointArc((B*sin(5*pi/3),  B*cos(5*pi/3)),(R*sin(phi+5*pi/3),R*cos(phi+5*pi/3))) \
        .threePointArc((Rm*sin(11*pi/6),Rm*cos(11*pi/6)),(R*sin(6*pi/3-phi),R*cos(6*pi/3-phi))) \
        .close()
    #log(f"x:{x} y:{y} B:{B}")
    return res

#def Torx()

log(1)
#a = Workplane().rect(20,20).extrude(3)

T6 = torx(Workplane(),6)
T8 = torx(Workplane(),8)
T10 = torx(Workplane(),10)
T15 = torx(Workplane(),15)
T20 = torx(Workplane(),20)

n = Workplane().circle(2)

a1 = 0
a2 = pi*1
slotRad = 7.0
cutterRad = 2.0

IR = slotRad - cutterRad
OR = slotRad + cutterRad
middle = a1+(a2-a1)/2

#a = radialSlot(a.faces(">Z").workplane(offset=0.2),slotRad, cutterRad, a1, a2).extrude(3)

#a = radialSlot(a.faces(">Z").workplane(offset=0.2),1.1, 1,.5, a2)
#a = hexAF(Workplane(),6)
#b = Workplane().circle(3)
"""
G = (Workplane().moveTo(IR*sin(a1),IR*cos(a1))
     .threePointArc((IR*sin(middle),IR*cos(middle)),(IR*sin(a2),IR*cos(a2)))
     .tangentArcPoint((cutterRad*2*sin(a2),cutterRad*2*cos(a2)))
     .threePointArc((OR*sin(middle),OR*cos(middle)),(OR*sin(a1),OR*cos(a1)))
     .tangentArcPoint((-cutterRad*2*sin(a1),-cutterRad*2*cos(a1))).close().extrude(3)
)"""