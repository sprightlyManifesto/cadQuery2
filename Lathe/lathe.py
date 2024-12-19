from cadquery import Workplane as WP
import cadquery as cq

sqr1 = WP().rect(40,600).extrude(40).translate((70,0,0)) 
sqr2 = WP().rect(40,600).extrude(40).translate((-70,0,0)) 
a = WP().rect(100,600).extrude(40)
volume = round(a.val().Volume())
print(f"{volume}mm3")
print(f"{volume/1000**2}L")
