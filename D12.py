#D&D D12 die with 12 pentagonal faces

af = 7
textH = 2
textD = 0.3

faces = {"1":(0,0),  "2":(60,72),     "3":(60,72*2),     "4":(60,72*3),     "5":(60,72*4),     "6":(60,0),
         "C":(180,0),"B":(120,72*3+36),"A":(120,72*4+36),"9":(120,36),"8":(120,72+36),"7":(120,72*2+36)}

a = cq.Workplane("XY").sphere(5)

for k in faces.keys():
    abtY , abtZ = faces[k]
    a = a.cut(cq.Workplane("XY").transformed(rotate=cq.Vector(abtY,0,0))
              .workplane(offset=af/2).rect(10,10).extrude(10).rotate((0,0,0),(0,0,1),abtZ))

a = a.fillet(.5)

for k in faces.keys():
    abtY , abtZ = faces[k]
    a = a.cut(cq.Workplane("XY").transformed(rotate=cq.Vector(abtY,0,0))
              .workplane(offset=af/2-textD).text(k,textH,textD).rotate((0,0,0),(0,0,1),abtZ))

