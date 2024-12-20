#friday afternoon gear/thread extestanisum;
# when does a high helix gear stop being a gear and become a thread
import cadquery as cq
from math import atan, asin, acos, tan, sin, cos, pi

class gear:
    @staticmethod
    def herringBone(mod,teeth,bore,width,helixAngle):
        g = gear.spur(mod,teeth,bore,width/2,helixAngle) 
        g = g.union(gear.spur(mod,teeth,bore,width/2,helixAngle).mirror(mirrorPlane="XY"))
        return g
    @staticmethod
    def ring(mod,teeth,bore,width,helixAngle,D):
        pcd = mod*teeth
        CP = pcd*pi/teeth
        OD = mod*(teeth+2)
        ID = OD - (OD-pcd)*2
        r = cq.Workplane().circle(D/2).circle(ID/2).extrude(width)
        PA = 20/180*pi
        ID -= mod/5
        
        for t in range(0,teeth):
            r = r.cut(cq.Workplane().polyline([(CP*0.2,OD/2),(-CP*0.2,OD/2),(-CP*0.4,ID/2),(CP*0.4,ID/2)]).close().extrude(width).rotate((0,0,0),(0,0,1),t/teeth*360))
            
        return r
    @staticmethod
    def spur(mod,teeth,bore,width,helixAngle):
        pcd = mod*teeth
        if helixAngle != 0:
            twist = width * tan(helixAngle*pi/180) / (pi*pcd) * 360
        else:
            twist = 0
        OD = mod*(teeth+2)
        if mod >1.25:
            ID = OD - (OD-pcd)*2.25
        else:
            ID = OD - (OD-pcd)*2.4
        PA = 20/180*pi
        baseDia = cos(PA)*pcd
        steps = 20
        dT = PA/steps
        Aoffset = PA-atan(PA)
        sideA = []
        sideB = []
        for i in (steps*3,steps*2,steps,0):
            T = i*dT
            L = baseDia/2*dT*i
            H = (L**2 + (baseDia/2)**2)**0.5
            A =    T - atan(L/(baseDia/2)) - Aoffset  + pi/teeth/2 #+ pi*2*t/teeth
            B =  -(T - atan(L/(baseDia/2)) - Aoffset) - pi/teeth/2 #+ pi*2*t/teeth
            sideA.append((H*sin(A),H*cos(A)))
            sideB.append((H*sin(B),H*cos(B)))
        sideB.reverse()
        
        gear =  cq.Workplane("XY").circle(bore/2).circle(OD/2).extrude(width)
        
        for t in range(0,teeth):
            a = cq.Workplane("XY").spline(sideA,includeCurrent=False) \
                .lineTo(sideA[-1][0]/baseDia * ID,sideA[-1][1]/baseDia *ID) \
                .lineTo(sideB[0][0]/baseDia * ID,sideB[0][1]/baseDia *ID) \
                .lineTo(sideB[0][0],sideB[0][1]) \
                .spline(sideB,includeCurrent=False).close()
            if twist != 0:
                gear = gear.cut(a.twistExtrude(width,angleDegrees=twist)\
                                .rotate([0,0,0],[0,0,1],t/teeth*360))
            else:
                gear = gear.cut(a.extrude(width).rotate([0,0,0],[0,0,1],t/teeth*360))
        return gear


#takes a few seconds to run on an 2019 i7
mod =1
teeth = 24
bore = 5
width = 5
helixAngle = 0
D = 90

r = gear.ring(mod,teeth*3,bore,width-1,helixAngle,D)

#b = gear.spur(mod,teeth,bore,width,helixAngle).translate((teeth*mod,0,0))
a = gear.spur(mod,teeth,bore,width,helixAngle).rotate((0,0,0),(0,0,1),180/teeth)\
    .translate((0,mod*teeth,0))
b = gear.spur(mod,teeth,bore,width-1,helixAngle).rotate((0,0,0),(0,0,1),180/teeth)\
    .translate((0,mod*teeth,0)).rotate((0,0,0),(0,0,1),120)
c = gear.spur(mod,teeth,bore,width-1,helixAngle).rotate((0,0,0),(0,0,1),180/teeth)\
    .translate((0,mod*teeth,0)).rotate((0,0,0),(0,0,1),240)
d = gear.spur(mod,teeth,bore,width-1,helixAngle)
#for teeth, helixAngle in ((20,45),(40,-45)):
#    g = gear.spur(mod,teeth,bore,width,helixAngle)
#   cq.exporters.export(g,f'TWGear-M{mod}-T{teeth}-W{width}-B{bore}-HA{helixAngle}.stl')
#cq.exporters.export(g,f'SpurGear-M{mod}-T{teeth}-W{width}-B{bore}.step')
