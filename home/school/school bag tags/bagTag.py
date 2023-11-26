#BagTag
from cadquery import Workplane as WP
from math import sin, cos , pi
import cadquery as cq

tags = dict()

tags["purple"] = ["Ava Kenton","Avani Ghuman","Chloe Raffe","Esme Fuller","Isabelle Homer","Ivy-Mae Peake","Leila Buckley","Bonnie Harper-Angell"]
tags["blue"]  = ["Albert Wadley","Archie Fitzpatrick", "Harry Buckley","Jamie Barella","Lorna Blessing","Riley Bampton"]
tags["yellow"] = ["Albie Pursey","Harry Houghton","Jake French","Zach Gore"]
tags["red"] = ["Oliver Bird", "Tommy Russell","Arthur Toomey"] 
tags["accents"] = ["Jaeylah Charlery"] #blue first e accent
tags["White"] = ["Esme Cornish","Evie Roberts","Isla Swaisland","Mina Ahmad","Thea Alexander-Davies","Zoya Asmari","Imogen Meershoek"]

tags = dict()

tags["missed"]=["Dominic Haddon"]

N = 0

for colour in tags:
    print(colour)
    for name in tags[colour]:
        N += 1
        print(f"\t{name}")
        #name = "Mike Notreal"
        OD = 80
        ID = 50
        R = (OD+ID)/4
        H = 3
        
        name.strip()
        w = WP().circle(OD/2).circle(ID/2).extrude(H)
        
        dA = 360/ (len(name)+3)
        A = 360
        
        for l in name:
            if l in "mMH28B":
                A -= dA * 0.3
            if l != " ":
                w = w.cut(WP().text(l,12,H+2, halign = "center", valign = "center",fontPath="gunplay rg.ttf").translate((0,R,0)).rotate((0,0,0),(0,0,1),A))
            else:
                A -= dA/2
                w = w.cut(WP().circle(10/2).extrude(H).translate((0,R,0)).rotate((0,0,0),(0,0,1),A))
                A -= dA/2
            A -= dA
            if l == "m" or l == "M" or l == "C":
                A -= dA * 0.3
        
        #w = w.cut(WP().circle(10/2).extrude(H).translate((0,40,0)).rotate((0,0,0),(0,0,1),A-dA/2))
        
        cq.exporters.export(w,f"{N}-bagTag-{name}-{colour}.stl")
