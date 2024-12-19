from cadquery import Workplane as WP
import cadquery as cq

#user define params
W,L,H = 900,1800,850
d,wall = 40,3
sheetT = 18
casterH = 90

I = d-wall/2
length = 0

blue = cq.Color(0,0,1,1)
brown = cq.Color(0.5,0.5,0,1)

zs = [d/2+casterH,H-sheetT-d/2]
zmid = zs[0]/2+zs[1]/2
topSheet = WP().rect(W,L).extrude(sheetT)
bottomSheet = WP().rect(W,L).extrude(sheetT)
long,short,upright = L,(W-2*d),(zs[1]-zs[0]-d)

longSteel = WP("XZ").rect(I,I).offset2D(wall).rect(I,I).extrude(long/2,both=True)
shortSteel = WP("YZ").rect(I,I).offset2D(wall).rect(I,I).extrude(short/2,both=True)
uprightSteel = WP("XY").rect(I,I).offset2D(wall).rect(I,I).extrude(upright/2,both=True)
assy = cq.Assembly()
assy = assy.add(topSheet.translate((0,0,H-sheetT)),color= brown)
assy = assy.add(bottomSheet.translate((0,0,casterH+d)),color = brown)
Y = L/2-d/2
X = W/2-d/2
l = L-d/2
ys = [l/2,l/6,-l/6,-l/2]
for z in zs:
    for x in [W/2-d/2,-W/2+d/2]:
        assy = assy.add(longSteel.translate((x,0,z)),color = blue)
        length += long
    for y in ys:
        assy = assy.add(shortSteel.translate((0,y,z)),color = blue)
        length += short
for x in [X,-X]:
    for y in ys:
        assy = assy.add(uprightSteel.translate((x,y,zmid)),color = blue)
        length += upright

pricePerM = 11.94

print(f"Steel length: {length} cost: {round(pricePerM*length/1000,2)}")
show_object(assy)