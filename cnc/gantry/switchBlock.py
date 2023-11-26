from cadquery import *
h,w,l = 8,10,30
swHoleDia = 2
holeDia = 3
holePitch = 6.5
swH = 5.8
swW = 13
swL = 6.5
mhPitch = (swW+l)/2


a = Workplane().box(w,l,h).translate((0,0,h/2))
a = a.cut(Workplane().box(w,swW,swH).translate((0,0,swH/2)))
a = a.union(Workplane().workplane(offset=4).pushPoints([(0,holePitch/2),(0,-holePitch/2)]).circle(swHoleDia/2).extrude(h-4))
a = a.cut(Workplane().pushPoints([(0,mhPitch/2),(0,-mhPitch/2)]).circle(holeDia/2).extrude(h))
a = a.faces(">Z").edges("%CIRCLE").chamfer(2)
a = a.faces(">Y").edges("|Z").fillet(4.9)
a = a.faces("<Y").edges("|Z").fillet(4.9)
a = a.rotate((0,0,0),(0,1,0),180)

exporters.export(a,"switchMount.step")