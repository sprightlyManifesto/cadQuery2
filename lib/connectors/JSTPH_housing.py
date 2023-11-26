from cadquery import Workplane as WP
import cadquery as cq

pins, pitch,sq,h,w = 6,2,1,6,3.3
offset = (pitch*(pins -1))/2
clearance = 0.2

a = WP().rect(pitch*pins+pitch/2-clerance,w).extrude(h-1)
#a = WP().moveTo()

for p in range(pins):
    log(f"{offset + p*pitch} , {p}")
    a = a.cut(WP().moveTo(-offset + p*pitch,0.6).rect(sq,sq).extrude(h))

cq.exporters.export(a,f"JST-PH_housing-{pins}_way.stl")