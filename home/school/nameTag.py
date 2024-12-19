from cadquery import Workplane as WP
import cadquery as cq

tag = WP().moveTo(0,6).text("LIZZIE",10,1)
tag = WP().moveTo(0,6).text("HARGREAVES",10,1)
tag = tag.union(WP().polygon(5,50).extrude(-2))


#cq.exporters.export(a.rotate((0,0,0),(0,0,1),a),f"housing-{n}-way-{pitch}-pitch.stl")
