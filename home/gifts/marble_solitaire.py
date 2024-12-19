from cadquery import Workplane as WP
from forms import forms
import cadquery as cq

D1 = 20
pitch = D1*1.3
offset = pitch * 3
T = 12.7
D = pitch*10

board = WP().circle(D/2).extrude(T).faces(">Z").edges().fillet(3)
b = WP("XZ").moveTo(pitch*8.5/2,T+D1/4).circle(D1/2).revolve(360,(0,0,0),(0,1,0))
board = board.cut(b)

sphere = WP().moveTo(D1/2,0).radiusArc((-D1/2,0),D1/2).close().revolve(180,(0,0,0),(1,0,0))

for x in range(7):
    for y in range(7):
        if (y > 1 and y <5) or (x >1 and x <5):
            board = board.cut(sphere.translate((x*pitch-offset, y*pitch-offset,T+D1/6)))

sphere = sphere.cut(WP().circle(D1/4).extrude(-D1/4))

#show_object(board)
#show_object(sphere)

N = 11
D = 10
D3 = 2
D2 = 6

peg = forms.lobedForm(N,D,D3,D2,external=True).close().extrude(D1/2.2)
show_object(peg)

cq.exporters.export(board,"board.stl")
cq.exporters.export(sphere,"marble.stl")
cq.exporters.export(peg,"peg.stl")