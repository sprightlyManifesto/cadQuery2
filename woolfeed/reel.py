from cadquery import Workplane as WP
import cadquery as cq

h = 34
D = 30
r = 3
N = 3
flange = 2 
c = 0.5

#thread_profile = cq.Workplane("XZ",origin=(R,0,0)).circle(r)
#path = cq.Workplane("XY", obj=cq.Wire.makeHelix(R,N*R,R))
#res = thread_profile.sweep(path)

a = WP().circle(D/2).extrude(h)
a = a.union(WP().circle(D/2+2).extrude(flange).faces(">Z").edges().chamfer(flange-c))
a = a.union(WP().workplane(offset = h-flange).circle(D/2+2).extrude(flange).faces("<Z").edges().chamfer(flange-c))

b = WP("YZ").center(D/2,h/2).polyline([(2,-4),(2,4),(-3,2.2),(-3,-2.2)]).close().extrude(20,both=True)\
    .edges("|X").fillet(2).rotate((0,0,0),(0,1,0),10)


for n in range(-12,12):
    a = a.cut(b.rotate((0,0,0),(0,0,1),n*30).translate((0,0,n*0.75)))

w = (2.5**2-1.9**2)**0.5 
a = a.cut(WP().moveTo(1.9, -w).threePointArc((-2.5,0),(1.9,w)).close().extrude(h))

show_object(a)

cq.exporters.export(a,"reel.stl")