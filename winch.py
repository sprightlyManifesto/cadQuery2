import cadquery as cq
from cadquery import Workplane as WP
#from pallet import Pallet
#from gear import gear

line = [(30,0),(60,0),(60,50),(15,50),(0,15),(10,15)]

a = WP().polyline(line).offset2D(2).extrude(10).faces(">X[-2]").edges("|Z").fillet(3)
