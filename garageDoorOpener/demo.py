from cadquery import Workplane as WP
h,d = 35,5


a = WP().rect(10,10).circle(d/2).extrude(35).faces(">Z").edges("%CIRCLE").fillet(0.5)
