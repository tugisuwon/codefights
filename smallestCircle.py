#https://codefights.com/challenge/9YDBDyHzou7XBWbyR/solutions/fSx7QyR4X4yucGFJa
def smallestCircle(p):
    def check(a,b,c):
        x1,y1 = [a[0]**2,-2*a[0]], [a[1]**2,-2*a[1]]
        x2,y2 = [b[0]**2,-2*b[0]], [b[1]**2,-2*b[1]]
        x3,y3 = [c[0]**2,-2*c[0]], [c[1]**2,-2*c[1]]
        a = [[x2[1]-x1[1],y2[1]-y1[1]],[x3[1]-x1[1],y3[1]-y1[1]]]
        b = [-(x2[0]-x1[0]+y2[0]-y1[0]),-(x3[0]-x1[0]+y3[0]-y1[0])]
        det = float(a[0][0]*a[1][1] - a[0][1]*a[1][0])
        #print det
        if det != 0:
            a_ = [[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]]
            return [sum(x*y for x,y in zip(a_[0],b)),sum(x*y for x,y in zip(a_[1],b))]
        else:
            return []
        
    def cross(o, a, b): 
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    def convex_hull(pp):
        pp = sorted(pp)

        if len(pp) <= 1:
            return pp

        # Build lower hull
        l = []
        for p in pp:
            while len(l) >= 2 and cross(l[-2], l[-1], p) <= 0:
                l.pop()
            l.append(p)

        # Build upper hull
        u = []
        for p in reversed(pp):
            while len(u) >= 2 and cross(u[-2], u[-1], p) <= 0:
                u.pop()
            u.append(p)

        return l[:] + u[:]
    
    con = convex_hull(p)
    ll = [list(x) for x in set(tuple(x) for x in con)]
    #print ll
    o = {}
    from itertools import combinations
    for i in combinations(ll,3):
        tt = check(i[0],i[1],i[2])
        c = 0
        #print i,tt
        if tt != []:
            c = 1
            #print 
            rr = (i[0][0]-tt[0])**2+(i[0][1]-tt[1])**2
            for j in [x for x in ll if x not in i]:
                #print j
                if (j[0]-tt[0])**2+(j[1]-tt[1])**2 > rr:
                    #print j
                    c = 0
                    break
        #print i,tt,c,rr
        if c == 1 and rr not in o:
            o[rr] = [x for x in xrange(len(p)) if p[x] in i]
    #print o,ll
    for i in combinations(ll,2):
        #print i,i[0],i[1]
        tt = [(i[0][0]+i[1][0])/2.,(i[0][1]+i[1][1])/2.]
        c = 1
        rr = (i[0][0]-tt[0])**2+(i[0][1]-tt[1])**2
        for j in [x for x in ll if x not in i]:
            if (j[0]-tt[0])**2+(j[1]-tt[1])**2 > rr:
                c = 0
                break
        #print tt,rr,i,c
        if c == 1 and rr not in o:
            o[rr] = [x for x in xrange(len(p)) if p[x] in i]
    m = 10**9
    an = ''
    #print o
    for i,v in o.items():
        if i < m:
            m = i
            an = v
    return an
        

