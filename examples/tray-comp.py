import cadquery as cq
from cadquery import Workplane as WP

H =10
W, L = 100,100
wall = 2
nX,nY = 2,2
pX,pY = (W -wall*2)/nX,(W -wall*2)/nY
a = WP().rect(W,L).extrude(H).edges("|Z").fillet(wall*2)
oX, oY = -pX*(nX-1)/2 , -pY*(nY-1)/2

for x in range(nX):
    for y in range(nY):
        cx,cy = x*pX+oX, y*pY+oY
        a = a.cut(WP().workplane(offset=H).moveTo(cx,cy)\
                  .rect(pX-wall,pY-wall).extrude(-H+wall).edges("|Z").fillet(wall))
        a = a.cut(WP().workplane(offset=wall).center(cx,cy)\
                 .text(str(nX*nY-y*nX+ x-nX+1),min(pX,pY)/2,-0.5))

b = WP().rect(W,L).circle(W/3).extrude(-H)

for name,projection in  [("X", (1,0,0)),("-X", (1,0,0)),("Y", (-1,0,0)),("-Y", (0,1,0)),("-Y", (0,-1,0)),("Z", (0,0,1)),("-Z", (0,0,-1))]:
    cq.exporters.export(
                a,
                'op.svg',
                opt={
                    "width": 100,
                    "height": 100,
                    "marginLeft": 0,
                    "marginTop": 0,
                    "showAxes": False,
                    "projectionDir": projection,
                    "strokeWidth": 0.25,
                    "strokeColor": (0, 0, 0),
                    "hiddenColor": (0, 0, 255),
                    "showHidden": False
                },
            )
    
    from xml.dom import minidom
    
    doc = minidom.parse("op.svg")  # parseString also exists
    with open(f"{name}.svg","w") as outFile:
        outFile.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <svg
       xmlns:svg="http://www.w3.org/2000/svg"
       xmlns="http://www.w3.org/2000/svg"
       viewBox="-50 -50 100 100">
        <g transform="scale(1, -1)" stroke-width="0.25"  fill="none">
           <!-- solid lines -->
           <g  stroke="rgb(0,0,0)" fill="none">''')
        
        for path in doc.getElementsByTagName('path'):
            outFile.write(f'<path d="{path.getAttribute("d")}"/>')
        
        outFile.write("</g></g></svg>")
doc.unlink()

