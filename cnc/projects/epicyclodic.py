#spirograph
from math import sin, cos , pi
from math import atan2
from cadquery import Workplane as WP

feed = 2000
#D1 diameter of outer circle
D1 = 200
#D2 dimmeter of the cirle rolling round the outer circle
D2 = 80
#radius of the point on the inner circle (where the pen goes on spirograph)
r1 = 45
#OD outer diameter of marked shape
OD = D1-D2+r1*2
 
def surfaceZ(x,y):
    D = 1.1*OD
    r = (x**2+y**2)**0.5
    mag = 5
    pz = mag * -cos(17*r/D*pi)
    #*(1-r/D) -mag
    return pz

pts = []
rndpts = []
N = 0
FPerror = 0.0001
OR = D1/2 - D2/2 + r1
Z = OD/8

#calculate number of loops N
for n in range(1,100):
    t = n*2*pi
    cx,cy = (D1-D2)/2*sin(t),(D1-D2)/2*cos(t)
    t2 = -t*(D1/D2)
    px,py = cx + r1*sin(t2),cy + r1*cos(t2)
    #print(f"n:{n} px:{px} py:{py} OR:{OR}")
    if (abs(px) < FPerror) and (abs(py - OR) < FPerror):
        N = n
        break
    
if N == 0:
    print("intersection not found")
    N = 1
else:
    print(f"N:{N}")

#calculate points on curve
for t in range(360*N +1):
    R1 = t/180*pi
    cx,cy = (D1-D2)/2*sin(R1),(D1-D2)/2*cos(R1)    
    R2 = -t*(D1/D2)/180*pi
    px,py = cx + r1*sin(R2), cy + r1*cos(R2)
    pz = surfaceZ(px,py)
    rndpts.append((round(px,3),round(py,3)))#,round(pz,3)))
rndpts = rndpts[0::2]

#calculate surface machining
surfpts  = []
surfSection = [] 
passes = 100
increment = 1.1*OD/2/passes
for p in range(passes):
    px, py = increment*p , surfaceZ(0,p*increment)
    surfSection.append((px,py)) 
    for t in range(360):
        R = t/180*pi
        r = increment*p + t/360*increment
        px,py = r*sin(R), r*cos(R)
        pz = surfaceZ(px,py)
        surfpts.append((round(px,3),round(py,3),round(pz,3)))
surfpts = surfpts[0::2]

gcode = f";Epicyclodic D1:{D1} D2:{D2} r1:{r1} N:{N}\n"
gcode += f"G90 G21 F{feed}\n"
gcode += "G0 Z5\n"
gcode += f"G0 X{surfpts[0][0]} Y{surfpts[0][1]}\n"
for p in surfpts:    
    gcode += f"G1 X{p[0]} Y{p[1]} Z{p[2]}\n"
gcode += "G0 Z5\n"
gcode += f"G0 X{rndpts[0][0]} Y{rndpts[0][1]}\n"
for p in rndpts:    
    gcode += f"G1 X{p[0]} Y{p[1]}\n" #Z{p[2]}\n"
gcode += "G0 z100\n"
distance = 0
#gcode = f";very crap estimates: Distance(mm): {distance} Time(minutes): {round(distance/feed,2)}\n {gcode}"

open(f"Epicyclodic--D1_{D1}_D2_{D2}_r1_{r1}.nc","w").write(gcode)
open(f"latest.nc","w").write(gcode)

t = 50
y = surfSection[-1][1]
surfSection.append((OD*0.6,y))
surfSection.append((OD*0.6,-t))
surfSection.append((0,-t))
#a = WP().polyline(surfpts[::360]).close()
a = WP().polyline(rndpts).close()
#b = WP("YZ").polyline(surfSection).close().revolve(360,(0,0,0),(0,1,0))