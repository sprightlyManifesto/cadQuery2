from cadquery import Workplane as WP
from math import ceil, cos, sin, pi
from datetime import datetime

#circular facing Gcode Generator, spirals in from outside of stock
#gemometry
stockOD = 20
stockH = 30
jobH = 27
#5 axis parameters
A,B = 90,0
reorient = True
#machining paramters
ToolNumber = 6
toolD = 3
stepover = 0.5
maxDOC = 0.5
speed = 10000
feed = 100
rapidPlaneAboveStockBy = 2
climb = False
toolChange = True
#end manual parmameters
wps = []
turnWps = []

job = WP().circle(stockOD/2).extrude(jobH,both=True)
job = job.cut(WP().workplane(offset=jobH-5).circle(stockOD).circle(15/2).extrude(-6))
#job = job.cut(WP().workplane(offset=27-22).circle(stockOD/2-2).circle(stockOD/2).extrude(-8))
#job = job.cut(WP().workplane(offset=27-10).polygon(6,6/cos(pi/6)).circle(stockOD/2).extrude(-8))

def stepTurn(d:float,stockOD,l:float,start:float,toolD:float, wps:[WP],job:WP) -> [WP]:
    r = stockOD/2 # Radius of the helix
    p = toolD/2 # Pitch of the helix
    h = l + toolD/2 + 1
    turnStart = start + toolD/2 + 1
    maxDOC = 1
    nPasses = int(ceil(stockOD-d/2)/maxDOC/2)-1
    DOC = (stockOD-d)/nPasses/2
    passes = [r - i*DOC-DOC for i in range(nPasses)]
    #helical turning B rotating A0 starting off the job (step turning)
    for r in passes:
        wire = cq.Wire.makeHelix(pitch=p, height=-h, radius=r)
        wps.append(WP().newObject([wire]).translate((0,0,turnStart)))
        wps.append(WP().workplane(offset=turnStart-h).circle(r))
    return wps

#turn a grove 15 from to 8 wide (allowing for tool diameter)
def groveTurn(d:float,stockOD,w:float,start:float,toolD:float, wps:[WP],job:WP) -> [WP]:
    r = stockOD/2 # Radius of the helix
    p = toolD/2 # Pitch of the helix
    h = w-toolD
    turnStart = start - toolD/2
    maxDOC = 1
    nPasses = int(ceil(stockOD-d/2)/maxDOC/2)-1
    DOC = (stockOD-d)/nPasses/2
    passes = [r - i*DOC-DOC for i in range(nPasses)]
    #helical turning B rotating A0 starting off the job (step turning)
    for r in passes:
        wire = cq.Wire.makeHelix(pitch=p, height=-h, radius=r)
        wps.append(WP().workplane(offset=turnStart).circle(r))
        wps.append(WP().newObject([wire]).translate((0,0,turnStart)))
        wps.append(WP().workplane(offset=turnStart-h).circle(r))
    return wps

def radialHex(AF:float,stockOD,w:float,start:float,toolD:float, wps:[WP],job:WP) -> [WP]:
    d = AF/cos(pi/6)
    wps = groveTurn(d,stockOD,w,start,toolD,wps,job)
    return wps

#def groveTurn(d:float,stockOD,w:float,start:float,toolD:float, wps:[WP],job:WP) -> [WP]:
#turnWps = stepTurn(10,stockOD,5,jobH,6,turnWps,job)
for I in [(10,0),(14,5),(18,10)]:
    d,offset = I
    turnWps = stepTurn(d,stockOD,5,jobH-offset,toolD,turnWps,job)
    job = job.cut(WP().workplane(offset=jobH-offset).circle(stockOD).circle(d/2).extrude(-6))
#turnWps = stepTurn(7,stockOD,8,jobH-16,6,turnWps,job)
d,w = 10, 8
turnWps = groveTurn(d,stockOD,w,10,toolD,turnWps,job)
job = job.cut(WP().workplane(offset=10).circle(stockOD).circle(d/2).extrude(-w))
AF = 8
turnWps = radialHex(AF,stockOD,w,-0,toolD,turnWps,job)
job = job.cut(WP().workplane(offset=-0).circle(stockOD).circle(d/2).extrude(-6))
job = job.cut(WP().workplane(offset=-0).circle(stockOD).polygon(6,AF/cos(pi/6)).extrude(-6))
show_object(job)

show_object(turnWps)
"""
gcode = f";Generated {datetime.now()}"
gcode += f";stock OD:{stockOD} stock Height {stockH}\n"
gcode += f";SET TOOL T{ToolNumber}  ({toolD}mm DIA)\n"
gcode += f";SET STOCK TO TOOL TIP AT A90 B0 X0 Y0 Z{stockH}\n"
gcode += f";job top Z:{jobH}\n"

rapidPlane = stockH + rapidPlaneAboveStockBy
r = (stockOD+toolD/2) + toolD*stepover/2
stock = WP().circle(stockOD).extrude(jobH)
tool = WP().workplane(offset=jobH).moveTo(r,0).circle(toolD/2)
stepMM = toolD*stepover/2
moves = ceil(r / stepMM)
passes = ceil((stockH-jobH)/maxDOC)
DOC = (stockH-jobH)/passes


gcode += f"\nG21 G90 F{feed} S{speed}\n"
if reorient:
    gcode += "G49\nG0 Z0\nA90 B0\n"
if toolChange:
    gcode += f"M6 T{ToolNumber}\n"
gcode += f"G43 H{ToolNumber}\n"
gcode += f"\nG0 Z{rapidPlane}\n"


method = "G3"
if climb: method ="G2"

for iz in range(passes):
    z = stockH - (iz+1)*DOC
    r = (stockOD+toolD/2) + toolD*stepover/2
    x = r
    gcode += f"G0 X{round(x,3)} Y0\nG0 Z{round(z,3)}\n"
    for e,i in enumerate(range(moves)): 
        previousX = x
        arcRad = r-stepMM/2.0
        r -= stepMM
        x = r
        if e%2 == 0: x = -r
        if r < 0:
            gcode += f"G0 Z{round(z +rapidPlaneAboveStockBy,3)}\n"
            break
        I = -arcRad
        if x >0: I = arcRad
        gcode += f"{method} X{round(x,3)} Y0 I{round(I,3)}\n"
        if not(climb):
            arcRad = - arcRad
        wps.append(WP().workplane(offset=z).moveTo(previousX,0).radiusArc((x,0),arcRad)) 
        
gcode += "M5\nG49\n G0 Z0\nG0 X0 Y0\nM30\n"
show_object(wps)
show_object(turnWps)
#show_object(stock)
#show_object(tool)

open(f"OD{stockOD}-toolD{toolD}-stockH{stockH}-jobH{jobH}-circularFacing.nc","w").write(gcode)
"""