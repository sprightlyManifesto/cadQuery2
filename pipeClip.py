from cadquery import *
h,w,l = 30,14,57
holeDia = 4.5
holePitch = 6.5
swH = 25.5
swW = 26
swL = 6.5
mhPitch = (swW+l)/2+3


a = Workplane().box(w,l,h).translate((0,0,h/2))
a = a.cut(Workplane().box(w,swW,swH).translate((0,0,swH/2)))
a = a.cut(Workplane().pushPoints([(0,mhPitch/2),(0,-mhPitch/2)]).circle(holeDia/2).extrude(h))
a = a.cut(Workplane().box(w,swW,swH).translate((0,0,swH/2)))
a = a.cut(Workplane().box(w,20,h).translate((0,27,h/2+5)))
a = a.cut(Workplane().box(w,20,h).translate((0,-27,h/2+5)))
a = a.faces("<Z[-3]").edges("|X").fillet(12)
a = a.faces(">Z").edges("|X").fillet(15)
a = a.faces(">Y").edges("|Z").fillet(4)
a = a.faces("<Y").edges("|Z").fillet(4)
a = a.faces("<Z[-2]").edges("%CIRCLE").chamfer(1.75)

exporters.export(a,"pipeClip.stl")