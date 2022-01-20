import cadquery as cq

flange = 1
p = 26
w= 25
m = 18
h = 8
y = w/2-6.5
m12Hole = 12.1
pts = [-30,-15,0,15,30]
dias= [11.8,11.9,12,12.1,12.2]
   
r = cq.Workplane().rect(p*3,w).pushPoints([(0,y),(p,y),(-p,y)]).circle(m12Hole/2)\
    .pushPoints([(p+m/2,y),(p-m/2,y),(-p+m/2,y),(-p-m/2,y),(m/2,y),(-m/2,y)]).circle(1.3/2).extrude(h)
    #.extrude(h).faces(">X").edges("|Z").fillet(1).faces("<X").edges("|Z").fillet(1)

r = r.cut(cq.Workplane().pushPoints([(0,y),(p,y),(-p,y)]).rect(11.5,11.5).extrude(2.5))

r = r.rect(p*3,flange).extrude(-5)

cq.exporters.export(r,"3camMount.stl")