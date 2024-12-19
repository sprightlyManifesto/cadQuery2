from cadquery import Workplane as WP
from math import pi,cos,sin
D1 = 90
D2 = 65


a = WP().circle(D1/2).extrude(-3)
a = a.cut(WP().circle(D2/2).extrude(-0.5))
r = D1/4+D2/4
a = a.union(WP().center(-18,0).text("5",45,0.5,font="Aroania",kind="bold"))
a = a.cut(WP().center(r,0).text("2024",4.5,-0.5,font="Aroania"))
a = a.cut(WP().center(-r,0).text("1974",4.5,-0.5,font="Aroania"))
a = a.union(WP().center(0,-22).text("YEARS",8,-0.5,font="Aroania"))
a = a.union(WP().center(13,0).circle(15).extrude(-0.5))

txt1 ="NATIONAL TRAIL"

txt2 =" THE PETER & GLYNIS WAY"

theta = 0
engraving = WP()
for e,t in enumerate(txt1):
    if t != " ":
        txt = WP().text(t,8.5,-0.5,font="Aroania")
        if e != 0:
            theta -= txt.val().BoundingBox().xmin* 1 - 1.8
        engraving= engraving.union(txt.translate((0,-r,0)).rotate((0,0,0),(0,0,1),theta))
        theta += txt.val().BoundingBox().xmax*1  + 1.8
    else:
        theta += 4
a = a.cut(engraving.rotate((0,0,0),(0,0,1),-theta/2))

theta = 0
engraving = WP()
for e,t in enumerate(txt2):
    if t != " ":
        txt = WP().text(t,8.5,-0.5,font="Aroania")
        if e != 0:
            theta += (txt.val().BoundingBox().xmin* 1 - 1.8)
        engraving= engraving.union(txt.translate((0,r,0)).rotate((0,0,0),(0,0,1),theta))
        theta -= (txt.val().BoundingBox().xmax*1  + 1.8)
    else:
        theta -= 4

a = a.cut(engraving.rotate((0,0,0),(0,0,1),-theta/2))

acorn = WP().moveTo(-4.5,-4).lineTo(4.5,-4).radiusArc((6.2,6),-40).radiusArc((0,11.5),-30)\
    .radiusArc((-6.2,6),-30).radiusArc((-4.5,-4),-40).close().extrude(-0.5,both=True).edges("|Z").fillet(1)
acorn = acorn.union(WP().moveTo(0,-5).lineTo(9,-5).radiusArc((-9,-5),11).close().extrude(-0.5,both=True).edges("|Z").fillet(1))
acorn = acorn.union(WP().moveTo(0,-9).lineTo(-4,-11).close().offset2D(0.5).extrude(-0.5,both=True))
acorn = acorn.translate((13,0,0))
a = a.cut(acorn)

theta = pi/10
x,y = r*cos(theta), -r*sin(theta)
pts = [(x,y),(-x,y)]
a = a.cut(WP().pushPoints(pts).circle(3/2).extrude(-3))

show_object(a)

cq.exporters.export(a,"mumAndDad50th.stl")