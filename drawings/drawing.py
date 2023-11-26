from cadquery import Workplane as WP
import cadquery as cq
from xml.dom import minidom
from collections import namedtuple


class drawing:
    def __init__(self,a,gap = 10):
        self.views = [a]
        self.WP = a
        self.gap = gap

    def projectView(self,parent=-1,direction="U"):
        direction = direction.upper()
        a = self.views[parent]
        bbA = a.val().BoundingBox()
        bbAC = bbA.center
        if direction == "U":
            b = a.rotate((bbAC.x,bbAC.y,0),(bbAC.x + 1,bbAC.y,0),90)
            bbB = b.val().BoundingBox()
            b = b.translate((0,bbA.ymax-bbB.ymin + self.gap,0))
            self.WP = self.WP.union(b)
            self.views.append(b)
        elif direction == "D":
            b = a.rotate((bbAC.x,bbAC.y,0),(bbAC.x + 1,bbAC.y,0),-90)
            bbA, bbB = a.val().BoundingBox() , b.val().BoundingBox()
            b = b.translate((0,+ bbA.ymin - bbB.ymax -self.gap ,0))
            self.WP = self.WP.union(b)
            self.views.append(b)
        elif direction == "L":
            b = a.rotate((bbAC.x,bbAC.y,0),(bbAC.x,bbAC.y+1,0),90)
            bbB = b.val().BoundingBox()
            b = b.translate((bbA.xmin-bbB.xmax - self.gap,0,0))
            self.WP = self.WP.union(b)
            self.views.append(b)
        elif direction == "R":
            b = a.rotate((bbAC.x,bbAC.y,0),(bbAC.x,bbAC.y+1,0),-90)
            bbB = b.val().BoundingBox()
            b = b.translate((bbA.xmax- bbB.xmin + self.gap,0,0))
            self.WP = self.WP.union(b)
            self.views.append(b)
    
    def output(self):
        cq.exporters.export(
                        self.WP,
                        'op.svg',
                        opt={
                            "width": 100,
                            "height": 100,
                            "marginLeft": 0,
                            "marginTop": 0,
                            "showAxes": False,
                            "projectionDir": (0,0,1),
                            "strokeWidth": 0.25,
                            "strokeColor": (0, 0, 0),
                            "hiddenColor": (0, 0, 255),
                            "showHidden": False
                        },
                    )
        
part = WP().box(8,8,8)
part = part.union(WP().text("1",5,5,halign="center",valign="center"))
part = part.union(WP("YZ").text("2",5,5,halign="center",valign="center"))
part = part.union(WP("XZ").text("3",5,5,halign="center",valign="center"))
part = part.union(WP("YZ").text("4",5,5,halign="center",valign="center").rotate((0,0,0),(0,1,0),180))
part = part.union(WP("XZ").text("5",5,5,halign="center",valign="center").rotate((0,0,0),(0,0,1),180))
part = part.union(WP().text("6",5,5,halign="center",valign="center").rotate((0,0,0),(0,1,0),180))

dwg = drawing(part)
dwg.projectView(direction = "U")
dwg.projectView(direction = "R")
dwg.projectView(direction = "R")
dwg.projectView(direction = "D")
dwg.projectView(direction = "D")
dwg.projectView(direction = "L")
dwg.projectView(direction = "L")
dwg.projectView(direction = "U")
show_object(dwg.WP)
dwg.output()
"""
            doc = minidom.parse("op.svg")
            bb = a.val().BoundingBox()
            viewParam = viewParameters(-10,-10, 20, 20,0)
            if name == "X": 
                viewParam = viewParameters(bb.ymin , -bb.zmax, bb.ylen, bb.zlen, 90)
            elif name == "Y": 
                viewParam = viewParameters(bb.xmin , -bb.zmax , bb.xlen , bb.zlen, -90)
            elif name == "Z": 
                viewParam = viewParameters(bb.xmin , -bb.ymax , bb.xlen , bb.ylen, 0)
            elif name == "-X": 
                viewParam = viewParameters(-bb.ymax ,-bb.zmax , bb.ylen , bb.zlen, -90)
            elif name == "-Y": 
                viewParam = viewParameters(-bb.xmax , -bb.zmax , bb.xlen , bb.zlen , 90)
            elif name == "-Z": 
                viewParam = viewParameters(bb.xmin,bb.ymin, bb.xlen, bb.ylen, 180)
            xmin, ymin, W, H,rotate  = viewParam
            viewBox = f'viewBox= "{xmin} {ymin} {W} {H}">'
            # parseString but no method to get the svg out of CQ without file buffer
            #create viewstring containing all SVG as a group
            viewString = "" 
            for path in doc.getElementsByTagName('path'):
                viewString += f'<path d="{path.getAttribute("d")}"/>'
                        
            doc.unlink()
            views[name] = (viewString,viewParam)
        
        self.drawing = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
                    <svg
                    xmlns:svg="http://www.w3.org/2000/svg"
                    xmlns="http://www.w3.org/2000/svg"'''
        self.drawing += f' viewBox="0 0 {W} {H}">'
        self.group(views["X"],col1,row2)
        self.group(views["-Y"],col2,row2)
        self.group(views["-X"],col3,row2)
        self.group(views["Z"],col4,row1)
        self.group(views["-Z"],col4,row3)
        self.group(views["Y"],col4,row2)
        self.drawing += "</svg>"
        
        open("op.svg","w").write(self.drawing)
    
    cq.exporters.export(
                        a,
                        'op.svg',
                        opt={
                            "width": 100,
                            "height": 100,
                            "marginLeft": 0,
                            "marginTop": 0,
                            "showAxes": False,
                            "projectionDir": projection,
                            "strokeWidth": 0.25,
                            "strokeColor": (0, 0, 0),
                            "hiddenColor": (0, 0, 255),
                            "showHidden": False
                        },
                    )
    def group(self,view,x,y):
        xmin, ymin, W, H,rotate  = view[1]
        self.drawing += f'<g transform="translate({x} {y})">'
        self.drawing += f'<g transform="scale(1, -1) rotate({rotate})" stroke-width="0.05" stroke="rgb(0,0,0)" fill="none">'
        self.drawing += view[0] + "</g></g>"

if False:
    a = WP().text("Tx",10,10).translate((5,3,-2))
    a = a.cut(WP("YZ").pushPoints([(0,0),(0,5),(0,3),(3,1)]).circle(0.5).extrude(40,both=True))
    a = a.rotate((0,0,0),(1,0,0),90)
    a = WP()
    drawing(a)

"""