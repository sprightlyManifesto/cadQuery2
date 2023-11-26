from cadquery import Workplane as WP
import cadquery as cq
import os

#return a wire that is on that edge 
def findProfile(wp,faceSelector,edgeSelector):
    edgeToMatch = wp.faces(faceSelector).edges(edgeSelector).val()
    profile = WP()
    whereFound = None
    for n, w in enumerate(wp.faces(faceSelector).wires().vals()):
        print(n,w)
        #note WP.wire().Edges()and WP().edges() return diffrent objects so you have to use is same in loop rather than if e in w.vals()
        for e in w.Edges(): 
            print(f"{e.startPoint()}  |  {e.endPoint()}  | {e.geomType()}")
            if(edgeToMatch.isSame(e)):
                print(f"found: {e} | {edgeToMatch}  |  in wire {n}")
                whereFound = n
                profile = profile.add(w)
                profile = profile.toPending()
    return profile

def remove(profile,cutterD,depth):
    print(len(profile.edges().vals()))
    wp = profile.wires().toPending().offset2D(cutterD/2).extrude(depth)
    try:
        wp = wp.cut(profile.wires().toPending().offset2D(-cutterD/2).extrude(depth))
    except:
        print("no inner loop")
    return wp

intW,intL,H,wall = 124,170,45, 2
extW,extL = intW+wall*2, intL+wall*2
extRad = 10
tool1D= 6
a = WP().rect(extW,extL).extrude(H).edges("|Z").fillet(extRad)
a = a.cut(WP().workplane(offset=wall).rect(intW,intL).extrude(H-wall).edges("|Z").fillet(extRad-wall))
a = a.circle(10).extrude(H) 
billet = WP().rect(extW+2,extL+2).extrude(H)

cutterD = 12
outerProfile = findProfile(a,">Z",">X").offset2D(cutterD/2).toPending()
#innerProfile = findProfile(a,">Z",">X[-1]").offset2D(-cutterD/2).toPending()
OP = remove(outerProfile,cutterD,-H)
#IP = remove(innerProfile,cutterD,-H+wall)
job = billet.cut(OP)#.cut(IP)

#show_object(job)
rest = job.cut(a)

"""
for i in range(11):
    if(len(rest.edges().vals()) >0):
        print(len(rest.edges().vals()))
        cut = remove(findProfile(rest,">Z",">X").toPending(),12,-H+wall)
        rest = rest.cut(cut)
        job = job.cut(cut)
"""
#show_object(rest)
show_object(job)
#show_object(profile)
#show_object(a)
#fshow_object(IP)
#show_object(OP)