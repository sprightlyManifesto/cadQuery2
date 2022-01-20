#compartmentalized tray
from cadquery import Workplane as WP
import cadquery as cq

h,w,d,wall = 30,170,170,2
rows, cols = 3,3
fillet = wall

cw = (w - wall*(cols+1)) / cols
rw = (w - wall*(rows+1)) / rows

cp = w /cols
rp = d /rows

a = WP().rect(w,d).extrude(h)

for y in range(rows):
        Y = -float(rp*rows-rp)/2 + y * rp
        for x in range(cols):
            X = -float(cp*cols-cp)/2 + x*cp
            a = a.cut(WP().workplane(offset=wall).moveTo(X,Y).rect(cw,rw).extrude(h*2))

a = a.edges("|Z").fillet(fillet)
a = a.faces("<Z").edges().chamfer(wall)
a = a.cut(WP().workplane(offset=h-wall/2).rect(w,d).extrude(h).faces("<Z").edges().chamfer(wall))

cq.exporters.export(a,f"tray-({h}x{w}x{d})-rows({rows})-cols({cols})-wall({wall}).stl")