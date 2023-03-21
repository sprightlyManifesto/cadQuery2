import cadquery as cq
from cadquery import Workplane as WP
from cadquery import exporters
import ezdxf
import os
import cv2
import numpy as np
from math import cos, sin, pi

os.system("clear")
scale = 100

#an example moderately horrid shape
pts = []
v = 50
for i in range(32):
    a = i * pi/16
    r = v/((i%8)/8 +1 + (i%3*0.2)+ (i%5*0.4))
    x = r*cos(a)
    y = r*sin(a)
    pts.append((x,y))
    
a = WP().polyline(pts).close().extrude(1).edges("|Z").fillet(0.25)

bb = a.val().BoundingBox()

#get model as STL note this version of CQ gives ascii STL not bin
cq.exporters.export(a.translate((-bb.xmin,-bb.ymin,0)),"out.stl")
stl = open("out.stl").readlines()
triangles = []
pts = []


for l in stl:
    l = l.strip(" ")
    l = l.replace("  "," ")
    l = l.replace("  "," ")
    if "vertex" in l:
        toks = l.split(" ")
        #note neglect Z as only want x,y
        pts.append((int(float(toks[1])*scale), int(float(toks[2])*scale)))
        if len(pts) > 2:
           triangles.append(pts)
           #print(pts)
           pts = []

height, width = int((bb.ymax-bb.ymin)*scale),int((bb.xmax-bb.xmin)*scale)

img = np.zeros((height,width,3), np.uint8)
points = np.array([[320, 130], [321, 130], [250, 300]])
cv2.fillPoly(img, pts=[points], color=(255, 0, 0))

for t in triangles: 
    print(t)
    if t[0]==t[1] or t[0]==t[2] or t[1] == t[2]:
        #skip zero area triangle 
        continue
    else:
        #note points have to be a NP array for cv2.fillPoly
        points = np.array([[t[0][0], t[0][1]], [t[1][0],t[1][1]], [t[2][0],t[2][1]]])
        cv2.fillPoly(img, pts=[points], color=(255, 255, 255))
        
cv2.imwrite("out.png",cv2.bitwise_not(cv2.flip(img, 0)))