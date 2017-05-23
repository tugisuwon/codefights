#https://codefights.com/challenge/BGtDEzzC5csfZTMzs/solutions/i8nxSw3h9q2gQcgmC
def sumInPerimeter(g, p):
    
    def peri(x,x1,x2,o):
        a = 0
        c = 0
        for i in xrange(x1,len(x)):
            for j in xrange(x2,len(x[0])):
                if x[i][j] == 1:
                    c += 1
                    b = 4
                    if i > 0:
                        if x[i-1][j] == 1:
                            b -= 2
                    if j > 0:
                        if x[i][j-1] == 1:
                            b -= 2
                    a += b
                if c == o:
                    break
            if c == o:
                break
        return a
    
    def score(x,x1,x2,o):
        s = 0
        c = 0
        for i in xrange(x1,len(x)):
            for j in xrange(x2,len(x[0])):
                if x[i][j] == 1:
                    c += 1
                    s += g[i][j]
                if c == o:
                    break
            if c == o:
                break
        return s
    
    m = 0
    a,b = len(g),len(g[0])
    c = [[0]*b]*a
    d = [[1,0],[0,1]]
    for i in xrange(a):
        for j in xrange(b):
            s = [[i,j]]
            t = [[1 if x==j and y==i else c[y][x] for x in xrange(b)] for y in xrange(a)]
            u = [[s,t]]
            m = max(m,score(t,i,j,1))
            o = 2
            v = set()
            while True:
                q = []
                for l in u:
                    ll = l[0]
                    if len(ll) > 3:
                        ll = ll[-3:]
                    for xx in ll:
                        for f in d:
                            ss = [xx[0]+f[0],xx[1]+f[1]]
                            if 0<=ss[0]<a and 0<=ss[1]<b and ss not in l[0]:
                                tt = [[1 if x==ss[1] and y==ss[0] else l[1][y][x] for x in xrange(b)] for y in xrange(a)]
                                ttt = ''.join(''.join(str(tt[x][y]) for y in xrange(b)) for x in xrange(a))
                                if ttt not in v:
                                    v.add(ttt)
                                    pp = peri(tt,i,j,o)
                                    if pp == p:
                                        m = max(m,score(tt,i,j,o))
                                    if pp <= p:
                                        q.append([ll+[ss],tt])
                if q == []:
                    break
                o += 1
                if o == 15:
                    break
                u = q
    return m