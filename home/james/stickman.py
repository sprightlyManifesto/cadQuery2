from cadquery import Workplane as WP
import cadquery as cq

def scale(workplane: cq.Workplane, x , y = None, z = None) -> cq.Workplane:
    y = y if y is not None else x
    z = z if z is not None else x
    t = cq.Matrix([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ])
    return workplane.newObject([
        o.transformGeometry(t) if isinstance(o, cq.Shape) else o
        for o in workplane.objects
    ])

T = 3
W = 4

a = WP().moveTo(0,67).circle(26/2).extrude(T)
a = a.union(WP().moveTo(20,40).lineTo(-20,40).close().offset2D(W/2).extrude(T))
a = a.union(WP().moveTo(0,24).lineTo(0,67).close().offset2D(W/2).extrude(T))
a = a.union(WP().moveTo(15.5,0).lineTo(0,24).close().offset2D(W/2).extrude(T))
a = a.union(WP().moveTo(-15.5,0).lineTo(0,24).close().offset2D(W/2).extrude(T))
eyes = [(6,70),(-6,70)]
a = a.cut(WP().workplane(offset=T/2).pushPoints(eyes).circle(3).extrude(T))
a = a.edges("|Z").fillet(1)
a = a.cut(WP().workplane(offset=T/2).moveTo(7,62).radiusArc((-7,62),15).threePointArc((0,58),(7,62)).close().offset2D(1).extrude(T))

b = scale(a,2,y = 2,z =1)

wall = 3
frame = 2.5

pts = [(0,15),(50,15)]
c = WP().pushPoints(pts).circle(30/2).circle(30/2-wall).extrude(T).faces(">Z").fillet(wall/2.1).edges()
x,y = pts[0]
for i in range(8):
    c = c.union(WP().moveTo(x,y).circle(8/2-i/2).extrude(T-1+i/4))
x,y = pts[-1]
c = c.union(WP().moveTo(x,y).circle(8/2).circle(6/2).extrude(T/2))
c = c.union(WP().moveTo(x,y).lineTo(x-8,35).close().offset2D(frame/2).extrude(T))
c = c.union(WP().moveTo(18,14).lineTo(x-8,35).close().offset2D(frame/2).extrude(T))
c = c.union(WP().moveTo(16,30).lineTo(x-8,35).close().offset2D(frame/2).extrude(T))
c = c.union(WP().moveTo(18,14).lineTo(15,32).close().offset2D(frame/2).extrude(T))
c = c.union(WP().moveTo(18,13).lineTo(0,15).close().offset2D(frame/4).extrude(T-1))
c = c.union(WP().moveTo(15,30).lineTo(0,15).close().offset2D(frame/4).extrude(T-1))
for i in range(3):
    c = c.union(WP().moveTo(18,14).circle(8/2-i).extrude(T+ 0.5 + i/4))
c = c.union(WP().moveTo(20,20).lineTo(16,8).close().offset2D(frame/4).extrude(T))

show_object(c)

cq.exporters.export(a,"stickman.stl")

