from cadquery import Workplane as WP
import cadquery as cq

text,fontPath,length = "JAMES", "Nintendo_Switch_UI_Font.ttf",150.0

#create at height = 1 and meaure the text length to work out theheight nessary for the desired lenght
a = WP().text(text,1,3,fontPath=fontPath)
fontHeight = length/a.val().BoundingBox().xlen
a = WP().text(text,fontHeight,3,fontPath=fontPath)

bb = a.val().BoundingBox()

cq.exporters.export(a,f"{text}.step") 