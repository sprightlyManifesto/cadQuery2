from cadquery import Workplane as WP
from math import ceil
from datetime import datetime

#circular facing Gcode Generator, spirals in from outside of stock
#gemometry
toolD = 6
stockOD = 10
stockH = 30
cutH = 27
#5 axis parameters
A,B = 90,0
reorient = True
#machining paramters
ToolNumber = 6
stepover = 0.5
maxDOC = 0.5
speed = 10000
feed = 100
rapidPlaneAboveStockBy = 2
climb = False
toolChange = True
#end manual parmameters

gcode = f";Generated {datetime.now()}"
gcode += f";circular facing stock OD:{stockOD} stock Height {stockH}\n"
gcode += f";SET TOOL T{ToolNumber}  ({toolD}mm DIA)\n"
gcode += f";cutting down to Z:{cutH}\n"

rapidPlane = stockH + rapidPlaneAboveStockBy
r = (stockOD+toolD/2) + toolD*stepover/2
stock = WP().circle(stockOD).extrude(cutH)
tool = WP().workplane(offset=cutH).moveTo(r,0).circle(toolD/2)
stepMM = toolD*stepover/2
moves = ceil(r / stepMM)
passes = ceil((stockH-cutH)/maxDOC)
DOC = (stockH-cutH)/passes


gcode += f"\nG21 G90 F{feed} S{speed}\n"
if reorient:
    gcode += "G49\nG0 Z0\nA90 B0\n"
if toolChange:
    gcode += f"M6 T{ToolNumber}\n"
gcode += f"G43 H{ToolNumber}\n"
gcode += f"\nG0 Z{rapidPlane}\n"
wps = []

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
for wp in wps: show_object(wps)
show_object(stock)
show_object(tool)

open(f"OD{stockOD}-toolD{toolD}-stockH{stockH}-cutH{cutH}-circularFacing.nc","w").write(gcode)