from cadquery import Workplane as WP
import cadquery as cq

PAREPET =  True

#9700 to garage wall
h,w,d,t  = 2400,15300,9000,100
wh = 1200
dh = 1950 
L2,L3, = 25,-50 

#6140 house to conservatory, 1.84     5.6-3.6-1.9 
#House Outline
pts = [(d,0),(d+3280,0),(d+4200,910),(d+4200,2430),(d+3280,3350),(d,3350),(d,w),(0,w),(0,0)]
H = WP().workplane(offset=-t).polyline(pts).close().extrude(h)
for offset in (0,-300):
    H = H.cut(WP().workplane(offset=L2).polyline(pts[:-3]).close().offset2D(-300)\
              .extrude(h).translate((offset,0,0)))
    H = H.cut(WP().workplane(offset=600).polyline(pts[:-3]).close().extrude(h))
H = H.union(WP().workplane(offset=-t).polyline([(0,w),(d+1840,w),(d+1840,w-5600),(0,w-5600)]).close().extrude(h))

#Lounge
LRO = 210,210
LR = WP().center(LRO[0],LRO[1]).polyline([(0,110),(450,110),(450,-10),
                (1030,-10),(1540,0),(2610,0),(2610,500),(4120,500),
                (4120,0),(5240,0),(5240,3900),(4350,3900),
                (3590,3900),(3440,3900),(3440,3670),(1770,3670),(1770,3560),(0,3560),
                (0,3170),(0,670)]).close().extrude(h)
LRW = WP().workplane(offset=900).center(LRO[0],LRO[1])\
            .polyline([(450,110),(450,-210),(1030,-210),(1030,110)]).close()\
            .polyline([(-LRO[0],3170),(-LRO[0],670),(0,670),(0,3170)]).close()\
                .extrude(1200)
#check heights
LRD = WP().center(LRO[0],LRO[1]).polyline([(4350,3900),(3590,3900),(3590,4200),(4350,4200)])\
    .close().extrude(dh)

#Hall
HLO = LRO[0],3890
HL = WP().center(HLO[0],HLO[1]).polyline([(0,0),(1270,0),(1270,260),(1440,260),(1440,140),
                (3200,140),(3200,360),(5130,360),(5130,1700),(4140,1700),(4140,1940),(3630,1940),(3630,1170),
                (2230,1170),(2230,1950),(1230,1950),(1230,2140),(0,2140)]).close().extrude(h)
HLD = WP().center(HLO[0],HLO[1]).moveTo(0,1050).rect(500,1080).extrude(dh)
#show_object(HL)

#Dining room
DRO = LRO[0], HLO[1]+2140+210
DR = WP().center(DRO[0],DRO[1]).polyline([(0,0),(1470,0),(1470,-320),(4300,-320),(4300,-560),
                (5130,-560),(5130,3040),(1210,3040),(1210,3320),(0,3320)]).close().extrude(h)
DRD = WP().center(DRO[0],DRO[1]).moveTo(4730,-560).rect(750,750).extrude(dh)
DRW = WP().workplane(offset=900).center(DRO[0],DRO[1]).moveTo(0,1760).rect(500,1880).extrude(wh)

KTO = 5660,LRO[1]
KT = WP().workplane(offset=L2).center(KTO[0],KTO[1]).polyline([(0,0),(3000,0),(3000,9000),(0,9000)]).close().extrude(h)
KTW = WP().workplane(offset=900).center(KTO[0],KTO[1]).polyline([(750,0),(750+575,0),(750+575,-LRO[1]),(750,-LRO[1])]).close()\
            .polyline([(2000,0),(2500,0),(2500,-LRO[1]),(2000,-LRO[1])]).close().extrude(wh)
KTD = WP().workplane(offset=L2).center(KTO[0],KTO[1]).moveTo(0,4765).rect(750,750).extrude(dh)
KTA = WP().workplane(offset=L2).center(KTO[0],KTO[1]).moveTo(1430,9000).rect(750,750).extrude(dh)

#Conservatory existing door is 1120 wide
CND = WP().workplane(offset=L2).center(KTO[0],KTO[1]).moveTo(3000,1620).rect(1000,1120).extrude(dh)

#big doors
BBD = WP().workplane(offset=L2).center(KTO[0],KTO[1]).moveTo(3000,6160).rect(1000,2040).extrude(dh)

BBD2 = WP().workplane(offset=L2).center(KTO[0],KTO[1]).moveTo(3000,4500).rect(1000,3000).extrude(dh)
#Penisular
x,y = 1800,1200

if PAREPET:
    PER = WP().workplane(offset=L2).center(KTO[0],KTO[1]).moveTo(3000-x/2,3500).rect(x,y).extrude(900)
    show_object(PER)

SRO = KTO[0], KTO[1] + 9350
SR = WP().workplane(offset=L2).center(SRO[0],SRO[1]).polyline([(0,0),(0,2140),(1660,2140),(1660,1080),(1780,1080),(1780,0)])\
    .close().extrude(h)

#CND,BBD
for f in (LR,LRW,LRD,KT,KTW,KTA,KTD,HL,HLD,DR,DRD,DRW,SR,BBD,CND):H = H.cut(f)
show_object(H)

