import cadquery as cq
from cadquery import Workplane as WP
from pallet import Pallet
from gear import gear

GEARS = False

P = Pallet()

od,id,l,fw,v = 30,3,20,4,5
d1,d2 = 5, 5
mod,teeth,bore,width,helixAngle = 2,15,2,l,0
n = 31/2

outline = [(-21,-21),(-21,21),(42,21),(42,-21)]

box = WP("YZ").polyline(outline).close().extrude(6)

box = box.cut(WP("YZ").circle(22.3/2).pushPoints([(n,n),(-n,n),(n,-n),(-n,-n)])\
              .circle(3.5/2).extrude(6)).faces(">X").edges("%circle").chamfer(2.5)

box = box.union(WP("YZ").moveTo(od,0).circle(9.8/2).extrude(16).faces(">X").edges().chamfer(1))

box = box.faces(">Y").edges("|X").fillet(5)
box = box.faces("<Y").edges("|X").fillet(5)

cq.exporters.export(box.rotate((0,0,0),(0,1,0),-90),"box.stl")
cq.exporters.export(box.rotate((0,0,0),(0,1,0),-90),"box.step")

show_object(box)

if GEARS:
    g = gear.spur(mod,teeth,bore,width,helixAngle)\
        .rotate((0,0,0),(0,1,0),90).translate((-l/2,0,0))
    
    vpts = [(-l/2,od/2+d2),(0,od/2-d2),(l/2,od/2+d2)]
    apts = [(-l/2,od/2-d2),(0,od/2+d2),(l/2,od/2-d2)]
    
    a = WP().polyline(vpts).close()
    b = WP().polyline(apts).close()
    a = a.revolve(360,(0,0,0),(1,0,0)).edges("%circle")\
        .edges(cq.NearestToPointSelector((0,od/2,0))).fillet(2)\
    
    w = (2.5**2-1.9**2)**0.5 
                    
    b = b.revolve(360,(0,0,0),(1,0,0)).edges("%circle")\
        .edges(cq.NearestToPointSelector((0,od/2,0))).fillet(3)
    
    a = g.cut(a)
    b = g.union(b)
    
    b = b.cut(WP("YZ").circle(10/2).extrude(l,both=True))
    a = a.cut(WP("YZ").moveTo(1.9, -w).threePointArc((-2.5,0),(1.9,w)).close().extrude(l,both=True))
    
    b = b.translate((0,od,0))
    
    cq.exporters.export(a.rotate((0,0,0),(0,1,0),90),"a.stl")
    cq.exporters.export(a.rotate((0,0,0),(0,1,0),90),"a.step")
    cq.exporters.export(b.rotate((0,0,0),(0,1,0),90),"b.stl")
    cq.exporters.export(a.rotate((0,0,0),(0,1,0),90),"b.step")
    show_object(a)
    show_object(b)