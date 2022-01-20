import cadquery as cq
buttons = [(-40,10),(-20,10),(0,10),(20,10),(40,10)]
h=20
bd1, bd2,f = 17.5, 12.5,11
r = cq.Workplane("XY").rect(100,40).extrude(h).edges("|Z").fillet(10)
r = r.faces(">Z").workplane().pushPoints(buttons).circle(bd1/2).cutBlind(-5)
x = 11-12.5/2
y = ((bd2/2)**2-x**2)**0.5 

for b in buttons:
    r = r.cut(cq.Workplane().workplane(offset=h).center(b[0],b[1]).moveTo(-x,-y).threePointArc((bd2/2,0),(-x,y)).close().extrude(-h).edges("|Z").fillet(1))
    r = r.cut(cq.Workplane().pushPoints(buttons).circle(bd1/2).extrude(10))
