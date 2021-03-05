from math import atan, asin, acos, tan, sin, cos, pi

class gear:
    @staticmethod
    def spur(mod,teeth,bore,width):
        width = 5
        teeth = 35
        mod = 1
        pcd = mod*teeth
        bore = 3
        log(pcd)
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
            gear = gear.cut(cq.Workplane("XY").spline(sideA,includeCurrent=False) \
                .lineTo(sideA[-1][0]/baseDia * ID,sideA[-1][1]/baseDia *ID) \
                .lineTo(sideB[0][0]/baseDia * ID,sideB[0][1]/baseDia *ID) \
                .lineTo(sideB[0][0],sideB[0][1]) \
                .spline(sideB,includeCurrent=False).close().extrude(width) \
                .rotate([0,0,0],[0,0,1],t/teeth*360))
        
        return gear

mod = 1
teeth = 44
bore = 5
width = 3
g = gear.spur(mod,teeth,bore,width)
cq.exporters.export(g,f'SpurGear-M{mod}-T{teeth}-W{width}-B{bore}.stl')
cq.exporters.export(g,f'SpurGear-M{mod}-T{teeth}-W{width}-B{bore}.step')