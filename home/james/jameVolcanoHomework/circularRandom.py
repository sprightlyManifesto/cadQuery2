from math import pi,cos,sin
from random import random


def circularRandom(lenght):
    values = []
    sum = 0
    for f in range(lenght):
        values.append(sum)
        sum += random()*2-1
    delta = -values[-1]/(lenght-1)
    for f in range(lenght):
        values[f] += (f-lenght/2 + 2)*delta
    return values 

def calPt(r,angle):
    return r*cos(angle),r*sin(angle)

def smooth(pts,no):
    smoothPts = []
    smoothWindow = range(-no,no)
    for i in range(len(pts)):
        x,y = 0,0
        for j in smoothWindow:
            address = i+j
            if address >= noPts: address -= noPts
            x += pts[address][0]
            y += pts[address][1]
        smoothPts.append((x/len(smoothWindow),y/len(smoothWindow)))
    return smoothPts


noPts = 1000
pitch = 2*pi/noPts
rands = circularRandom(noPts)
rad = 100
layers = 20
noiseAmplitude = 1
layerH = 3

viewboxSize = (rad+max(rands))*2.2

html = "<html><head><style>svg {height: 90%;}</style></head><body>"
html += f'<svg viewBox="{-viewboxSize/2} {-viewboxSize/2} {viewboxSize} {viewboxSize}">'
x,y = calPt(rad+rands[0]*noiseAmplitude,0)
pts = []
for i in range(noPts):
    pts.append(calPt(rad+rands[i]*noiseAmplitude,i/noPts*2*pi))

smoothRad = 2
pts = smooth(pts,smoothRad)

for l in range(layers):
    smoothRad += 1
    x,y = pts[0]
    html += f'<path fill="none" stroke="#111111" d="M{x} {y} '
    newPts = []
    for i in range(noPts):
        x,y = pts[i] 
        html += f"L{x} {y}"
        mag = (x**2+y**2)**0.5
        delta = layerH * (0.5+random()*1.5)
        newPts.append(calPt(mag-delta,i/noPts*2*pi))
        #*(0.5+random()/2) 
    html += 'Z" />'
    pts = smooth(newPts,smoothRad)

html += '</svg>'
 

html += "</body></html>"
open("svg.html","w").write(html)