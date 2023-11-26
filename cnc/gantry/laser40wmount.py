from cadquery import Workplane as WP
from cadquery.selectors import NearestToPointSelector as NTPS
import cadquery as cq



w, h, t = 81, 100, 6.5
oy, hw, hh, d1, d2 = 39.6, 68.2, 57.6,5.2,4.2
lw,wall,slot,f = 33.2, 3,2,5

ptsd1 = [(hw/2,oy),(-hw/2,oy),(hw/2,oy-hh),(-hw/2,oy-hh)]
x = (lw/2+6)
ptsd2 = [(x,-35),(-x,-35)]
ptsd3 = [(lw/2+4,0),(-lw/2-4,0)]

laser = WP().workplane(offset=wall).rect(lw,h).extrude(lw)

a = WP().rect(81,100).pushPoints(ptsd1).circle(d1/2).extrude(t).edges("|Z").fillet(10)
a = a.union(WP().moveTo(0,-35).rect(lw+8*2,30).extrude(lw+wall))
a = a.cut(WP().workplane(offset=lw+wall).center(0,-35).pushPoints(ptsd3).circle(4.3/2).extrude(-15))
a = a.cut(WP().workplane(offset=lw-wall).center(0,-35).rect(w,5.5).extrude(-2.5))
a = a.edges(NTPS((lw/2+8,-35,6))).fillet(4)
a = a.edges(NTPS((-lw/2-8,-35,6))).fillet(4)
a = a.cut(laser)


b = WP().rect(lw+8*2,30).extrude(6)
b = b.cut(WP().pushPoints(ptsd3).circle(4.3/2).extrude(6))
b = b.edges("|Z").fillet(5).translate((lw+wall,0,))

show_object(b)
cq.exporters.export(a,"plate.stl")

"""

#show_object(b)
#cq.exporters.export(b.rotate((0,0,0),(0,1,0),180),"clamp.stl")
"""