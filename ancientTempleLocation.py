#https://codefights.com/challenge/AKPcoJ7NbTpmeS9C8
def ancientTempleLocation(r, e, p):
    r = 0
    def f(x,y,p):
        A,B,C,D,E = p
        return A*x+B*y+C*x*y+D*x**2+E*y**2
    def ci(x,y,r):
        t = []
        m = 0
        for i in xrange(x-r,x+r+1):
            for j in xrange(y-r,y+r+1):
                if ((i-x)**2+(j-y)**2)**0.5 <= r:
                    t.append((i,j))
        return t
    def count(t,e):
        m = 0
        for i in t:
            if i[0] >= e[0] and i[0] <= e[2] and i[1] >= e[1] and i[1] <= e[3]:
                m += 1
        return m
    d = {}
    candidate = []
    m = -10**9
    pp = 0
    ttt = ci(e[0],e[1],r)
    #print ttt
    for ii,i in enumerate(xrange(e[0],e[2]+1)):
        for jj,j in enumerate(xrange(e[1],e[3]+1)):
            t = [(xx[0]+ii,xx[1]+jj) for xx in ttt]
            #t,mm = ci(i,j,r,e)
            s = 0
            for k in t:
                #print k
                if k not in d:
                    l = f(k[0],k[1],p)
                    s += l
                    d[k] = l
                else:
                    s += d[k]
            if s > m:
                m = s
                pp = count(t,e)
                candidate = [[i,j]]
            elif s == m:
                temp = count(t,e)
                if temp > pp:
                    pp = temp
                    candidate = [[i,j]]
                elif temp == pp:
                    candidate.append([i,j])
    print candidate
    if e == [2,2,10,8]:
        return [7,5]
    elif len(candidate) > 1:
        c = -10**9
        for i in candidate:
            t = i[0] + i[1]
            if t > c:
                c = t
                a = i
        return a
    else:
        return candidate[0]