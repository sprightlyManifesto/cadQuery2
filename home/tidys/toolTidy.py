from cadquery import Workplane as WP
import cadquery as cq

pitch = 30
N= 8
H= 19
a = WP().rect(110,pitch*N+pitch*2).extrude(H).edges("|Z").fillet(5)

for n in range(12):
    y= pitch*n-(N+1)*pitch/2
    a = a.cut(WP().workplane(offset=H).moveTo(40,y).lineTo(-40,y).close().offset2D(13.5/2).extrude(-16))

cq.exporters.export(a, "toolTray.stl")