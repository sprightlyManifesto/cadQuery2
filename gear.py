from math import atan, asin, acos, tan, sin, cos, pi

class gear:
    @staticmethod
    def herringBone(mod,teeth,bore,width,twist):
        g = gear.spur(mod,teeth,bore,width/2,twist) 
        g = g.union(gear.spur(mod,teeth,bore,width/2,twist).mirror(mirrorPlane="XY"))
        return g
    @staticmethod
    def spur(mod,teeth,bore,width,twist):
        pcd = mod*teeth
        log(f"pcd: {pcd}")
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
        for i in (steps*2,steps,0):
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
mod = 1
teeth = 22
bore = 5
width = 10
for twist in (10,-10):
    g = gear.herringBone(mod,teeth,bore,width,twist)
    cq.exporters.export(g,f'HBGear-M{mod}-T{teeth}-W{width}-B{bore}-T{twist}.stl')
#cq.exporters.export(g,f'SpurGear-M{mod}-T{teeth}-W{width}-B{bore}.step')
