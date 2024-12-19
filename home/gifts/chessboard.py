import cadquery as cq
from cadquery import Workplane as WP
from math import floor

a = WP().rect(50,50).extrude(3)
b = a.edges(">X and >Y").fillet(3.18/2)
board = WP().rect(450,450).extrude(25)
board = board.cut(WP().workplane(offset=22).rect(400,400).extrude(3))

cq.exporters.export(a,"square.stl")
cq.exporters.export(b,"squareFillet.stl")

assy = cq.Assembly(board.translate((0,0,-22)))

for i in range (0,64):
    x = (i%8)*50-175
    y = floor(i/8)*50-175
    if (i+floor(i/8))%2:
        colour = cq.Color(1,1,1)
    else:
        colour = cq.Color(0,0,0)
    assy.add(a.translate((x,y,0)),color=colour)

show_object(assy)
cq.exporters.export(a,"board.stl")