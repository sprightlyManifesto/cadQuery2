from cadquery import *
from math import sin,cos,acos,asin,pi,atan2

class Pallet:
    def __init__(self):
        self.torx6 = { 6:(1.75,1.27),  8:(2.4,1.75), 10:(2.8,2.05), 15:(3.35,2.4),  20:(3.95,2.85),
                      25:(4.50,3.25), 30:(5.6,4.05), 40:(6.75,4.85),45:(7.93,5.64), 50:(8.95,6.45),
                      55:(11.35,8.05),60:(13.45,9.6),70:(15.7,11.2),80:(17.75,12.8),90:(20.2,14.4),
                      100:(22.4,16)}
    
    def radialSlot(self,wp,slotRad, cutterRad, a1, a2,offset=(0,0)):
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
    
    def hexAF(self,wp,af):
        R = af/cos(pi/6)/2
        return wp.moveTo(-sin(pi/6)*R,af/2).lineTo(sin(pi/6)*R,af/2).lineTo(R,0)\
            .lineTo(sin(pi/6)*R,-af/2).lineTo(-sin(pi/6)*R,-af/2).lineTo(-R,0).close()
    
    def torx(self,wp,no,AB=None):
        if AB != None:
            A , B = AB 
        else:
            A , B = self.torx6[no]
        re=A*0.1
        ri=A*0.175
        x = ri*(sin(pi/6)*(A/2-re))/(re + ri)
        y1 = B/2 + ri
        y2 = cos(pi/6)*(A/2 - re)
        y = y1 - ri*((y1 -y2))/(re + ri)
        #log(f"x:{x} y1:{y1} y2:{y2}")
        phi = atan2(x,y)
        #log(f"phi:{round(phi,2)}  x:{round(x,2)} y:{round(y,2)} re:{round(re,2)} ri:{round(ri,2)}")
        R = (x**2+y**2)**0.5
        Rm = A/2
        B = B/2
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
        return res

if __name__== "__main__":
    p = Pallet()
    ks = list(p.torx6.keys())
    ks.reverse()
    a = cq.Workplane().circle(12).extrude(-3)
    for k in ks:
        a = a.union(p.torx(a.faces(">Z").workplane(),k).extrude(1))
        
