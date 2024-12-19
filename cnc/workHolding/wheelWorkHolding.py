from cadquery import Workplane as WP
import cadquery as cq
from cadquery.selectors import NearestToPointSelector as NTPS

ID,OD,h = 37,80,35
PCD = ID/2+OD/2
a = WP().circle(OD/2).circle(ID/2).extrude(h)

for t in (0,45,90,135):
    a = a.cut(WP().workplane(offset=10).rect(OD,5).extrude(50).edges("|X").fillet(2.4).rotate((0,0,0),(0,0,1),t+22.5))
    a = a.cut(WP().moveTo(PCD/2,0).circle(5/2).extrude(50).rotate((0,0,0),(0,0,1),t*2))

for p in [(PCD/2,0,h),(-PCD/2,0,h),(0,PCD/2,h),(0,-PCD/2,h)]:
    a = a.edges(NTPS(p)).chamfer(4)

cq.exporters.export(a,"wheelTooling.stl")