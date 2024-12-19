from cadquery import Workplane as WP
from forms import forms
import cadquery as cq
from math import sin, cos, pi

N = 11
D = 10
D3 = 2
D2 = 6
Ds = 70

R = Ds/3
N = 6
pts = [(R*sin(2*n/N*pi),R*cos(2*n/N*pi)) for n in range(N)]

sphere = WP().moveTo(Ds/2,0).radiusArc((-Ds/2,0),Ds/2).close().revolve(180,(0,0,0),(1,0,0))
sphere = sphere.cut(WP().pushPoints(pts).circle(D/2).extrude(-D/2))

N = 11
peg = forms.lobedForm(N,D,D3,D2,external=True).close().extrude(D/2.2)

cq.exporters.export(sphere,"sphere.stl")
cq.exporters.export(peg,"peg.stl")