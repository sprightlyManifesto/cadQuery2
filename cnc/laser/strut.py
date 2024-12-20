from cadquery import Workplane as WP
from cadquery.selectors import RadiusNthSelector as NthR 
from math import cos, sin, tan, pi
import cadquery as cq


class bought(object):
    @staticmethod
    def alu2020(L,axis="Z"):
        axis = axis.upper()
        alu2020 = WP().rect(20,20).circle(4.2/2).extrude(L/2,both=True).edges("|Z").fillet(0.5)
        pts = [(10,5.5),(8,3.5),(8,6),(7,6),(4,3)]
        for p in reversed(pts):pts.append((p[0],-p[1]))
        p = WP().polyline(pts).close().extrude(L/2,both=True).faces(">X[-2]").edges("|Z").fillet(0.2)
        for a in (0,90,180,270):
            alu2020 = alu2020.cut(p.rotate((0,0,0),(0,0,1),a))
        if axis == "X":
            alu2020 = alu2020.rotate((0,0,0),(0,1,0),90)
        elif axis == "Y":
            alu2020 = alu2020.rotate((0,0,0),(1,0,0),90)
        return alu2020
    @staticmethod
    def vRoller2020(axis="X"):
        ID,D2,OD,W = 5,19.6, 24.3, 11
        pts = [(-W/2,ID/2),(W/2,ID/2),(W/2,D2/2),(W/4,OD/2),(0,D2/2),(-W/4,OD/2),(-W/2,D2/2)]
        a = WP().polyline(pts).close().revolve(360,(0,0,0),(1,0,0))
        if axis == "Z":
            a = a.rotate((0,0,0),(0,1,0),90)
        if axis == "Y":
            a = a.rotate((0,0,0),(0,0,1),90)
        return a
    @staticmethod
    def pulley():
        a = WP("XZ").circle(16/2).extrude(7.5)
        a = a.union(WP("XZ").circle(12/2).extrude(16))
        a = a.union(WP("XZ").workplane(offset=14.6).circle(16/2).extrude(1.5))
        return a
    
class parts(object):
    @staticmethod
    def yAxisEnd(pitch,mirror=False):
        wheelR,T = 11,12
        x,y = 100,pitch+(wheelR-4)*2
        w = 20.1
        a = WP().workplane(offset=11).rect(x,y).extrude(T)
        a = a.cut(WP().moveTo(-x/2,y/2).rect(42*2,78).extrude(40,both=True)).edges("|Z").fillet(2)
        x = x/2 - wheelR -1
        pts = [(x,pitch/2),(x,-pitch/2),(0,pitch/2),(-x,-pitch/2)]
        a = a.cut(WP().pushPoints(pts).circle(5.1/2).extrude(50))
        a = a.cut(WP().workplane(offset=11+T).pushPoints(pts[2:]).circle(10.2/2).extrude(-4.5))
        pts = [(W/2-5,16)]
        a = a.cut(WP("XZ").pushPoints(pts).circle(2.5/2).extrude(y,both=True))
        a = a.cut(WP("YZ").rect(19,30).extrude(100,both=True))
        a = a.union(WP("XZ").workplane(offset=y/2).moveTo(18,28).rect(20,22).extrude(-y))
        pts = [(32,19),(20.5,32.5)]
        a = a.cut(WP("XZ").workplane(offset=y/2).pushPoints(pts).circle(2.5/2).extrude(-y))
        a = a.cut(WP("XY").moveTo(23,0).rect(36,19).extrude(40).edges("|Z").fillet(2))
        a = a.faces(">Z").edges("|Y").fillet(5)
        if mirror:
            a = a.mirror("XY")
        return a
    @staticmethod
    def motorMount(pitch):
        wheelD = 22
        pX,T,H = 50,10,pitch*2+wheelD
        a = WP().rect(72,H).extrude(T)
        a = a.cut(WP().pushPoints([(72/2,0),(-72/2,0)]).rect(wheelD,65).extrude(T))
        a = a.edges("|Z").fillet(5)
        a = a.cut(WP().rect(pX,pitch*2,forConstruction=True).vertices().circle(4.9/2).extrude(T))
        pts = [(-0.7,0),(-0.3,-0.8),(0.3,-0.8),(0.7,0)]
        beltPitch = 2.5
        beltProfile = WP("XZ").center(0,10).polyline(pts).close().extrude(9,both=True)
        for i in range(-10,11):
            a = a.cut(beltProfile.translate((beltPitch*i,0,0)))
        a = a.cut(WP("XZ").moveTo(-8,10).radiusArc((-8,0),5).lineTo(8,0).radiusArc((8,10),5).close().extrude(10,both=True))
        #claming holes
        a = a.cut(WP().rect(30,30,forConstruction=True).vertices().circle(3.3/2).extrude(T))
        a = a.cut(WP().rect(30,30,forConstruction=True).vertices().polygon(6,5.5/cos(pi/6)).extrude(6))
        a = a.cut(WP().moveTo(0,H/2-15).rect(20,20,forConstruction=True).vertices().circle(3.3/2).extrude(T))
        a = a.cut(WP().moveTo(0,H/2-15).rect(20,20,forConstruction=True).vertices().circle(6/2).extrude(T/2))
        return a
    def laserMount(pitch):
        wall, LS, g = 3, 33.2, 3
        wheelD = 22
        T,H = 10,pitch*2+wheelD
        a = WP("XZ").workplane(offset=-H/2).moveTo(0,10+wall*2+LS/2).rect(LS,LS).rect(LS+wall*2,LS+wall*4).extrude(30)
        a = a.cut(WP("XZ").workplane(offset=-H/2).moveTo(0,10+wall*3+LS/2).rect(LS,LS).extrude(30))
        a = a.cut(WP("XZ").workplane(offset=-H/2).moveTo(0,10+wall+LS).rect(g,LS).extrude(30))
        t,w = 5, 10
        x,y = t/2+g/2, w+wall*4+LS+t
        a = a.union(WP("XZ").workplane(offset=-H/2).pushPoints([(x,y),(-x,y)]).rect(5,10).extrude(30))
        a = a.cut(WP("YZ").center(H/2-15,y).pushPoints([(8,0),(-8,0)]).circle(3.3/2).extrude(10,both=True))
        a = a.cut(WP().rect(20,20,forConstruction=True).vertices().circle(3.3/2).extrude(T))
        a = a.cut(WP().workplane(offset=wall*2+T).moveTo(0,H/2-15).rect(20,20,forConstruction=True).vertices().polygon(6,5.5/cos(pi/6)).extrude(-4))
        a = a.cut(WP().moveTo(0,H/2-15).rect(20,20,forConstruction=True).vertices().circle(3.3/2).extrude(T+wall*2))
        return a
    @staticmethod
    def endPulleyMnt(mirror=None):
        a = WP("YZ").rect(26+8,26).extrude(43)
        a = a.faces(">X").edges("|Y").fillet(12.5)
        a = a.translate((-13,-4,10))
        a = a.cut(WP().circle(5/2).extrude(26,both=True))
        a = a.cut(WP().rect(20.1,20.1).extrude(26))
        a = a.cut(WP("XZ").moveTo(19,10).circle(2.5/2).extrude(26,both=True))
        a = a.cut(WP("XZ").moveTo(29,20).rect(35,35).extrude(9.5,both=True).edges("|Y").fillet(8))
        if mirror != None:
            a = a.mirror(mirror)
        return a
    @staticmethod
    def idler():
        ID=2.5
        pts = [(ID/2,-4.5),(ID/2,4.5),(11/2,4.5),(11/2,4.0),(10/2,3.3),(10/2,-3.3),(11/2,-4.0),(11/2,-4.5)]
        a = WP().polyline(pts).close().revolve(360,(0,0,0),(0,1,0))
        return a
    @staticmethod
    def idler13():
        ID=2.5
        pts = [(ID/2,-4.5),(ID/2,4.5),(13/2,4.5),(13/2,-4.5)]
        a = WP().polyline(pts).close().revolve(360,(0,0,0),(0,1,0))
        return a
    @staticmethod
    def stepperBracket(mirror=False):
        s,wall,stpr,offset = 20,5,42,10
        x,y,z = stpr/2+offset+wall+s,s+wall,stpr+wall
        a = WP().rect(x,y).extrude(-stpr-wall).translate((s/2+wall-x/2,wall/2,wall))
        a = a.cut(WP().moveTo(-20,0).rect(60.1,20.1).extrude(-stpr))
        c = (-offset-s/2,s/2,-stpr/2)
        a = a.edges("<Z and <X").chamfer(35)
        a = a.cut(WP("XZ").circle(22/2).extrude(-wall).translate(c))
        a = a.cut(WP("XZ").rect(31,31,forConstruction=True).vertices().circle(3.3/2).extrude(-wall).translate(c))
        a = a.faces(">Y[-2]").edges(NthR(0)).chamfer(1)
        a = a.cut(WP().circle(5.2/2).extrude(wall))
        pts = [(0,-10),(0,-32)]
        a = a.cut(WP("YZ").pushPoints(pts).circle(5.2/2).extrude(s,both=True))
        if mirror:
            a = a.mirror("YZ")
        return a
    @staticmethod
    def brace():
        pts = [(10.5,10),(10.5,3),(11.5,3),(11.5,-3),(10.5,-3),(10.5,-10),(-10.5,-10),(-10.5,-3),(-11.5,-3),(-11.5,3),(-10.5,3),(-10.5,10)]
        a = WP("YZ").polyline(pts).close().extrude(60,both=True)
        a = a.cut(WP().pushPoints([(0,0),(-35,0),(35,0)]).rect(25,15).extrude(10,both=True))
        a = a.cut(WP().workplane(offset=10).rect(120,21).extrude(6,both=True))
        for n in (1,2,3,4,5,6):
            a = a.faces(f">X[{n}]").edges("|Y").chamfer(4)
        a = a.cut(WP("XZ").pushPoints([(6,0),(-6,0),(41,0),(29,0),(-41,0),(-29,0)]).circle(5.2/2).extrude(12,both=True))
        return a
    @staticmethod
    def upstand():
        H,T,W = 80,10,40
        y = H/2-T
        a = WP().moveTo(0,y).rect(W,H).extrude(-T)
        a = a.union(WP().rect(20,6).extrude(2))
        a = a.cut(WP().pushPoints([(-12,0),(12,0)]).circle(5/2).extrude(T,both=True))
        a = a.union(WP().moveTo(0,y+H/2-T/2).rect(W,T).extrude(20))
        a = a.cut(WP("XZ").pushPoints([(-12,10),(12,10)]).circle(5/2).extrude(H,both=True))
        a = a.faces("<Y").edges("|Z").fillet(9.5)
        a = a.faces(">Z").edges("|Y").fillet(9.5)
        a = a.faces("<Z").edges("|Y").fillet(2)
        return a
    
ASSY = True
EXPORT = False

strut = 20
laserSquare = 33
table = 750,1090
table = 200,300
pitch = 40.5
W = table[1]-strut
black = cq.Color(0,0,0,1)
orange = cq.Color(1,0.5,0,0.5)
red = cq.Color(1,0,0,0.5)
green = cq.Color(0,1,0,0.5)

"""
bracket = parts.motorMount(pitch)
lm = parts.laserMount(pitch)
show_object(bracket)
show_object(lm)
"""
#upstand = parts.upstand()

if ASSY:
    assy = cq.Assembly()
    for x in (W/2,-W/2):
        assy.add(bought.alu2020(table[0],"Z").translate((x,0,0)))
        z = 100/2 - 12
        assy.add(bought.vRoller2020("X").translate((x,pitch/2, 0)),color= black)
        assy.add(bought.vRoller2020("X").translate((x,-pitch/2,-z)),color=black)
        assy.add(bought.vRoller2020("X").translate((x,-pitch/2,z)), color=black)
    
    for y in (4.5,-4.5):
        assy.add(parts.idler().translate((-W/2+19,y,-table[0]/2+10)))
        assy.add(parts.idler().translate((W/2-19,y,-table[0]/2+10)))
        assy.add(parts.idler().translate((-W/2+19,y,-32)))
        assy.add(parts.idler().translate((W/2-19,y,-32)))
        assy.add(parts.idler().translate((-W/2+32.5,y,-20.5)))
        assy.add(parts.idler().translate((W/2-32.5,y,-20.5)))
        
    for t in [(-25,-pitch,-z),(25,-pitch,-z),(-25,pitch,-z),(25,pitch,-z)]:
        assy.add(bought.vRoller2020("Z").translate(t), color=black)
    
    assy.add(parts.yAxisEnd(pitch).rotate((0,0,0),(0,1,0),90).translate((x,0,0)), color=orange)
    assy.add(parts.yAxisEnd(pitch,mirror=True).rotate((0,0,0),(0,1,0),90).translate((-x,0,0)), color=orange)
    assy.add(parts.motorMount(40.5).translate((0,0,-z+12)),color=orange)
    assy.add(parts.laserMount(pitch).translate((0,0,-z+12)),color=orange)
    #struts:
    assy.add(bought.alu2020(W-46,"X").translate((0,-pitch/2,-z)))
    assy.add(bought.alu2020(W-46,"X").translate((0,pitch/2,-z)))
    assy.add(parts.endPulleyMnt().translate((-W/2,0,-table[0]/2)),color=red)
    assy.add(parts.endPulleyMnt(mirror="YZ").translate((W/2,0,-table[0]/2)),color=red)
    assy.add(parts.stepperBracket().translate((-x,0,table[0]/2)),color=red)
    assy.add(parts.stepperBracket(mirror=True).translate((x,0,table[0]/2)),color=red)
    assy.add(bought.pulley().translate((x+20,0,table[0]/2-20.5)))
    assy.add(bought.pulley().translate((-x-20,0,table[0]/2-20.5)))
    assy.add(parts.brace().translate((0,0,-z)),color=green)
    z = table[0]/2-65
    assy.add(parts.upstand().rotate((0,0,0),(0,1,0),90).translate((-W/2-10,0,z)))
    assy.add(parts.upstand().rotate((0,0,0),(0,1,0),-90).translate((+W/2+10,0,z)))
    assy.add(parts.upstand().rotate((0,0,0),(0,1,0),90).translate((-W/2-10,0,-z)))
    assy.add(parts.upstand().rotate((0,0,0),(0,1,0),-90).translate((+W/2+10,0,-z)))
    #assy = parts.yAxisEnd(40.5)
    #assy = parts.stepperBracket()
    show_object(assy)

if EXPORT:
    cq.exporters.export(parts.brace(),"brace.stl")
    cq.exporters.export(parts.endPulleyMnt(),"endPulleyMnt-L.stl")
    cq.exporters.export(parts.endPulleyMnt(mirror="YZ"),"endPulleyMnt-R.stl")
    cq.exporters.export(parts.yAxisEnd(pitch),"yAxis-L.stl")
    cq.exporters.export(parts.yAxisEnd(pitch,mirror=True).rotate((0,0,0),(0,1,0),-180),"yAxis-R.stl")
    cq.exporters.export(parts.stepperBracket().rotate((0,0,0),(1,0,0),-90),"stepperBracket-L.stl")
    cq.exporters.export(parts.stepperBracket(mirror="True").rotate((0,0,0),(1,0,0),-90),"stepperBracket-R.stl")
    cq.exporters.export(parts.idler().rotate((0,0,0),(1,0,0),90),"idler.stl")
    