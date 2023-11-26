#28BYJ-48
import cadquery as cq
from cadquery import Workplane as WP

class stepper28BYJ_48:
    @staticmethod
    def create(): 
        PCD, L  = 35, 17
        a = WP().moveTo(-PCD/2,0).lineTo(PCD/2,0).close().offset2D(3.5).extrude(-1)
        a = a.cut(WP().pushPoints([(-PCD/2,0),(PCD/2,0)]).circle(4.2/2).extrude(-1))
        a = a.union(WP().moveTo(0,L/2).rect(16,L).extrude(-15))
        a = a.union(WP().circle(28/2).extrude(-19))
        a = a.union(WP().moveTo(0,-8).circle(9/2).extrude(1.5))
        a = a.union(WP().moveTo(0,-8).circle(5/2).extrude(10.5))
        a = a.cut(WP().center(0,-8).workplane(offset=4).circle(10).rect(5,3).extrude(10))
        return a
