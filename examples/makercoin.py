# maker coin
from cadquery import Workplane as WP
from math import asin, sin,cos

R = 20
h1  = 6
D1,D2,D3 = 20,55,14

theta = asin(D1/(R*2))
R2 = R*cos(theta)- D1/2

a = WP().moveTo(0,R).circle(D1/2)
r = 29
b = WP().moveTo(r+6,0).circle(r/2)
pts = []