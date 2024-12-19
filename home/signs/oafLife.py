import cadquery as cq
import os
from cadquery import Workplane as WP

os.system("clear")

def exportDXFmm(wp,fn,index=-1):
    cq.exporters.export(wp,fn)
    
a = WP().rect(20,10).extrude(1).edges("|Z").fillet(2)
pts = ([(10,0),(-10,0),(5,5),(5,-5),(-5,5),(-5,-5),(0,0)])
a = a.cut(WP().pushPoints(pts).circle(1).extrude(1))
a = a.faces(">Z").circle(1).extrude(1) 

#just show area to mill
#show_object(WP(obj = a.faces(">Z[-2]").vals()[0]))

print(f'a.faces(">Z").wires().vals()[0].endPoint(): {a.faces(">Z").wires().vals()[0].endPoint()}')
print(f'a.faces(">Z").wires().vals()[0].startPoint(): {a.faces(">Z").wires().vals()[0].startPoint()}')


for e,o in enumerate(a.faces(">Z").wires().vals()):
    exportDXFmm(WP(obj = o),f"out_{e}.dxf")


pths = []
offsets = [-o/2-1 for o in range(20)]
for offset in offsets:
    pth = WP(obj=a.faces(">Z[-2]").wires().vals()[0]).edges().toPending().offset2D(offset)
    if len(pth.edges().vals()) > 0:
        pths.append(pth)
        print(offset)
    else: 
        break

pth = WP(obj=a.faces(">Z[-2]").wires().vals()[1]).edges().toPending().offset2D(1)
pths.append(pth)

for pth in pths:
    show_object(pth)

show_object(a)