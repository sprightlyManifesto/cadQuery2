from cadquery import *
h,w,d =  36,36,20

outline = [(0,0),(0,w),(d,w),(d,w/2+4),(12,w/2+4),(12,w/2-4) ,(d,w/2-4),(d,0)]

a = Workplane().polyline(outline).close().extrude(h)
a = a.union(Workplane().polyline([(0,0),(0,w),(d,w),(d,0)]).close().extrude(3))
a = a.cut(Workplane().moveTo(16,w/2).circle(2).extrude(10))
a = a.cut(Workplane("XZ").moveTo(-39,0).circle(100).circle(60).extrude(100,both=True))
a = a.faces(">Z").edges("|X").fillet(4)
a = a.faces(">X[-2]").edges("|Z").fillet(3.5)
a = a.faces(">X").edges(">Z").fillet(30)
a = a.faces(">Z").edges(">X").fillet(3)
a = a.cut(Workplane("YZ").center(1,1).polyline([(0,0),(0,w-2),(h-2,w-2),(h-2,0)]).close().extrude(4).faces(">Z").edges("|X").fillet(4))
a = a.cut(Workplane("YZ").polyline([(0,0),(0,w-4),(h-1,w-4),(h-1,0)]).close().extrude(4))
a = a.union(Workplane("YZ").moveTo(11,5.5).rect(5,1).extrude(4))
a = a.union(Workplane("YZ").moveTo(11,8.5).rect(5,1).extrude(4))
a = a.union(Workplane("YZ").moveTo(20.5,2.5).rect(1,5).extrude(4))
a = a.cut(Workplane("YZ").moveTo(32.5,19.5).circle(1.6).extrude(h))
a = a.cut(Workplane("YZ").workplane(offset=7).moveTo(32.5,19.5).circle(4).extrude(h))
a = a.cut(Workplane("YZ").workplane(offset=7).moveTo(36.5,19.5).rect(8,8).extrude(h))

a = a.cut(Workplane("YZ").moveTo(26.3,11).rect(4.5,6).extrude(20))
a = a.cut(Workplane("YZ").workplane(offset=20).moveTo(26.3,8).rect(4.5,10).extrude(-2))
a = a.faces(">X[-2]").edges(">Z").fillet(2)
