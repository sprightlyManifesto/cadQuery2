from cadquery import Workplane as WP
import cadquery as cq
from xml.dom import minidom
from collections import namedtuple

class drawing:
    def __init__(self,a,gap = 1):
        individual = False
        viewParameters = namedtuple('viewParameters', ['xmin', 'ymin','W','H','rotation'])
        views = {}
        for name,projection in  [("X", (1,0,0)),("-X", (-1,0,0)),("Y", (0,-1,0)),("-Y", (0,1,0)),("Z", (0,0,1)),("-Z", (0,0,-1))]:
            #get each porjection as svg in doc
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
            doc = minidom.parse("op.svg")
            bb = a.combine().objects[0].BoundingBox()
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
            
            if individual:
                with open(f"{name}.svg","w") as outFile:
                    outFile.write(('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
                    <svg
                   xmlns:svg="http://www.w3.org/2000/svg"
                   xmlns="http://www.w3.org/2000/svg"
                   ''' + viewBox +
                   f'<g transform="scale(1, -1) rotate({rotate})" stroke-width="0.05"  fill="none">' +
                      ' <!-- solid lines --><g  stroke="rgb(0,0,0)" fill="none">'))
                    outFile.write(viewString)
                    outFile.write("</g></g></svg>")
            
            doc.unlink()
            views[name] = (viewString,viewParam)
        # drawinglayout
        #                  [ Z]
        #   [ X] [-Y] [-X] [ Y]
        #                  [-Z]
        H = gap*4 + views["Z"][1].H + views["-X"][1].H + views["-Z"][1].H 
        W = gap*5 + views["X"][1].W + views["-Y"][1].W + views["-X"][1].W + views["Y"][1].W
        col1 = gap - views["X"][1].xmin
        col2 = gap*2 + views["X"][1].W - views["-Y"][1].xmin
        col3 = gap*3 + views["X"][1].W + views["-Y"][1].W - views["-X"][1].xmin
        col4 = gap*4 + views["X"][1].W + views["-Y"][1].W + views["-X"][1].W - views["Y"][1].xmin 
        row1 = gap - views["Z"][1].ymin
        row2 = gap*2 + views["Z"][1].H - views["-X"][1].ymin
        row3 = gap*3 + views["Z"][1].H + views["-X"][1].H - views["-Z"][1].ymin
        
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

