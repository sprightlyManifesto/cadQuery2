import cadquery as cq
import os
from cadquery import Workplane as WP

part = WP().circle(2).extrude(10).union(WP().moveTo(1,1.5).circle(3).extrude(3))

box = part.val().BoundingBox()
os.system("clear")
print(f"xmin: {box.xmin} xmax: {box.xmax}")
print(f"ymin: {box.ymin} ymax: {box.ymax}")
print(f"zmin: {box.zmin} zmax: {box.zmax}")
print(f"center.x = {box.center.x}")
print(f"center.y = {box.center.y}")
print(f"center.z = {box.center.z}")

part = part.translate((-box.center.x,-box.center.y,-box.center.z))