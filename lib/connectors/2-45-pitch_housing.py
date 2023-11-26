from cadquery import Workplane as WP
import cadquery as cq

pitch,d,h,w,n  = 2.54, 2, 8, 4, 4

#pts = [(3.81,0),(1.27,0),(-1.27.0),(-3.81,0)]
pts = [(pitch*(p- n/2+ 0.5),0) for p in range(n)]
for p in pts: log(p)

a = WP().rect((pitch+0.5)*n,w).extrude(h)
a = a.cut(WP().pushPoints(pts).circle(2/2).extrude(h))

cq.exporters.export(a.rotate((0,0,0),(0,0,1),a),f"housing-{n}-way-{pitch}-pitch.stl")
