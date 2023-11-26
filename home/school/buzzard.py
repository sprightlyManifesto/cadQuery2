from cadquery import Workplane as WP
import cadquery as cq
a = WP().rect(80,30).extrude(3).edges("|Z").fillet(10)
buzzard =cq.importers.importDXF("buzzard.dxf").wires().toPending().extrude(1)
buzzard = buzzard.rotate((0,0,0),(0,0,1),-50).translate((-40,8))

a = a.cut(buzzard)
a = a.cut(WP().text("Buzzards",16,-1).translate((0,7,3)))
a = a.cut(WP().text("2023",16,-1).translate((0,-7,3)))
a = a.cut(WP().moveTo(32.5,-7.5).circle(3).extrude(3))

show_object(a)

cq.exporters.export(a,"buzzards.stl")