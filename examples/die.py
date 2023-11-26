#!/usr/bin
#die

import cadquery as cq

dotDia = 1
depth = 0.4

result = (cq.Workplane("front")
          .moveTo(-5,-5)
          .lineTo(5,-5)
          .lineTo(5,5)
          .lineTo(-5,5)
          .close().extrude(10)).translate([0,0,-5]).fillet(1)



#1
result = result.faces(">Z").circle(dotDia/2).cutBlind(-depth)
#2
result = (result.faces("<Y").workplane()
          .moveTo(2,2).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-2,-2).circle(dotDia/2).cutBlind(-depth)
          )
#3
result = (result.faces("<X").workplane()
          .moveTo(-5,0).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-7,2).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-3,-2).circle(dotDia/2).cutBlind(-depth)
          )
#4
result = (result.faces(">X").workplane()
          .moveTo(7,-2).circle(dotDia/2).cutBlind(-depth)
          .moveTo(7,2).circle(dotDia/2).cutBlind(-depth)
          .moveTo(3,-2).circle(dotDia/2).cutBlind(-depth)
          .moveTo(3,2).circle(dotDia/2).cutBlind(-depth)
          )
#5
result = (result.faces(">Y").workplane()
         .moveTo(7,2).circle(dotDia/2).cutBlind(-depth)
         .moveTo(5,0).circle(dotDia/2).cutBlind(-depth)
         .moveTo(3,2).circle(dotDia/2).cutBlind(-depth)
         .moveTo(7,-2).circle(dotDia/2).cutBlind(-depth)
         .moveTo(3,-2).circle(dotDia/2).cutBlind(-depth)
         )

#6 longhand
"""
result = (result.faces("<Z").workplane()
          .moveTo(-7,3).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-3,3).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-3,5).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-7,5).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-3,7).circle(dotDia/2).cutBlind(-depth)
          .moveTo(-7,7).circle(dotDia/2).cutBlind(-depth))
"""
#6 dryer
for x, y in [(-7,3),(-3,3),(-3,5),(-7,5),(-3,7),(-7,7)]:
    result = result.faces("<Z").workplane().moveTo(x,y).circle(dotDia/2).cutBlind(-depth)
