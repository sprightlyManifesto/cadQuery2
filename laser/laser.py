from cadquery import Workplane as WP
import cadquery as cq
from math import cos, sin, pi

h,w,l,wall = 40,60,100,3
laserS = 32.2
railP,railD = 50, 6.4
motorBossD, motorBossL,motorMountP = 12.5, 16,35
caridgeH,caridgeL = 30,40
plateT = 8
plateW, plateH = 81,100

motorD = WP().circle(26/2)
motor = WP().pushPoints([(motorMountP/2,0),(-motorMountP/2,0)]).circle(4.3/2)
laser = WP()

caridge = WP().rect(w,caridgeH).extrude(caridgeL)
caridge = caridge.cut(WP().pushPoints([(railP/2,0),(-railP/2,0)]).circle(railD/2).extrude(h))
caridge = caridge.cut(WP().rect(railP-wall*2-railD,caridgeH-wall*2).extrude((caridgeL-5.6)/2).edges("|Z").fillet(wall))
caridge = caridge.cut(WP().workplane(offset=caridgeL).rect(railP-wall*2-railD,caridgeH-wall*2).extrude(-(caridgeL-5.6)/2).edges("|Z").fillet(wall))
caridge = caridge.cut(WP().circle(2.5/2).extrude(caridgeL))
caridge = caridge.union(WP().moveTo(0,laserS/2+ caridgeH/2).rect(laserS,laserS).rect(laserS+wall*2,laserS+wall*2).extrude(caridgeL))
caridge = caridge.faces("<X or >X").edges("|Z").chamfer(8)
caridge = caridge.faces("<X[-2] or >X[-2] or >X or <X").edges("|Z").fillet(wall/2)
caridge = caridge.cut(WP("XZ").workplane(offset=-caridgeH/2).moveTo(0,caridgeL/2).circle(3.5/2).extrude(-wall-laserS))
caridge = caridge.cut(WP("XZ").workplane(offset=-caridgeH/2).moveTo(0,caridgeL/2).polygon(6,5.6/cos(pi/6)).extrude(-wall-laserS+0.5))
caridge = caridge.union(WP().workplane(offset=caridgeL).moveTo(w/2+3,0).rect(6,10).extrude(-3).faces(">X").edges("|Z").fillet(2.5))


offset = caridgeH/2+plateT/2 +1
plate = WP("XZ").workplane(offset= offset).rect(81,100).extrude(plateT/2,both=True).edges("|Y").fillet(4)
a,b = 33.5,26.3
pts = [(a,b),(a,-b),(-a,b),(-a,-b)]
plate = plate.cut(WP("XZ").workplane(offset= offset).center(0,6)\
                  .pushPoints(pts).circle(5.3/2).extrude(plateT,both=True))

plate = plate.union(WP("XZ").workplane(offset=offset).pushPoints([(0,l/2-plateT/2),(0,-l/2+plateT/2)]).rect(w,plateT).extrude(-30))
plate = plate.cut(WP().pushPoints([(railP/2,0),(-railP/2,0)]).circle(railD/2).extrude(l,both=True))
plate = plate.cut(WP().workplane(offset=plateH/2).circle(motorBossD/2).extrude(plateT,both=True))
plate = plate.cut(WP().pushPoints([(motorMountP/2,0),(-motorMountP/2,0)]).circle(3.3/2).extrude(l,both=True))
plate = plate.faces(">Y").edges("|Z").fillet(5)
plate = plate.cut(WP("YZ").workplane(offset=w/2).center(-5,plateH/2-plateT/2).circle(1.6/2).moveTo(-6.6).circle(1.6/2).extrude(-5))