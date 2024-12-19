from cadquery import Workplane as WP
import cadquery as cq

ID,H,H1,H2,OD = 32,20,4,10,60
r =  ID/2 + (OD-ID)/3

pts = [(OD/2,0),(ID/2,0),(ID/2,H1),(r,H2),(r,H),(OD/2,H)]

a = WP("YZ").polyline(pts).close().revolve(360,(0,1,0),(0,0,0))
a = a.union(WP().moveTo(0,OD/4+ID/4).circle(OD/4-ID/4).extrude(H))
a = a.cut(WP().moveTo(0,OD/4+ID/4).circle(5/2).extrude(H*0.9,both=True).rotate((1,0,0),(0,0,0),-10).translate((0,0,H)))
cq.exporters.export(a,"callenderHook.stl")