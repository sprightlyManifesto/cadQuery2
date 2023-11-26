from cadquery import Workplane as WP
import cadquery as cq

a = WP().circle(5.2/2).circle(11/2).extrude(15)

cq.exporters.export(a,"mudguardSpacer.stl")