from cadquery import Workplane as WP
from math import pi, sin, cos ,asin,acos,atan
import os

os.system("clear")

class forms:
    @staticmethod
    def rotateAbtOrigin(pt,theta):
        px,py = pt
        x2 = px*cos(theta) - py*sin(theta)
        y2 = py*cos(theta) + px*sin(theta)
        return x2,y2

    @staticmethod
    def lobedForm(N,D,D1,D2,external=True):
        #opposite and adjacent of triangle of origin to one of small outer circles
        pts = []
        form = WP()
        hypotonuse2 = D1/2 + D2/2
        if external:
            rad = (D-D1)/2
        else:
            rad = (D+D2)/2 
            adjacent = rad * sin(pi/N)
            opposite = rad * cos(pi/N)
            if adjacent > hypotonuse2:
                raise Exception(f"gap between external lobes is to great: {adjacent -hypotonuse2}")
            rad =  opposite - (hypotonuse2**2-adjacent**2)**0.5
        interRad = rad * 2 * pi/N - D1 - D2
        if interRad > 0:
            raise Exception(f"gap between external lobes is to great: {interRad}")
        adjacent = rad * cos(pi/N)
        opposite = rad * sin(pi/N)
        theta = acos(opposite/hypotonuse2)
        x = rad * cos(pi*1/N) + D1/2*sin(theta)
        y = rad * sin(pi*1/N) - D1/2*cos(theta)
        for n in range(N):
            x1,y1 = forms.rotateAbtOrigin((x,y),2*pi*n/N)
            x2,y2 = forms.rotateAbtOrigin((x,-y),2*pi*n/N)
            pts.append((x2,y2))
            pts.append((x1,y1))
        
        if len(pts) != 0:
            for e,p in enumerate(pts):
                x1,y1 = pts[e-1]
                form = form.moveTo(x1,y1)
                if e%2:
                    form = form.radiusArc(p,D2/2)
                else:
                   form = form.radiusArc(p,-D1/2)
        return form


N = 5
D = 8
D1 = 2
D2 = 7

#form = forms.lobedForm(N,D,D1,D2,external=True).close()
form2 = forms.lobedForm(N,D,D1,D2,external=False).close()
circle = WP().circle(D/2)


show_object(circle)
#show_object(form)
show_object(form2)