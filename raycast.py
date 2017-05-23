#https://codefights.com/challenge/KCdMLuWJyYvARCoEB
def raycast(a, r):
    from itertools import product, islice
    l = xrange
    a = [[float(x) for x in a[j]] for j in l(3)]

    def d(M,prod=1):
        dim = len(M)
        if dim == 1:
            return prod * M.pop().pop()
        it = product(l(1,dim),repeat=2)
        prod *= M[0][0]
        return d([[M[x][y]-M[x][0]*(M[0][y]/M[0][0]) for x,y in islice(it,dim-1)] for i in l(dim-1)],prod)
    
    def cr(a, b):
        return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

    t,u = [[1.,1.,1.,1.]],[[1.,1.,1.,0.]]
    p = [r[0][i]+r[1][i]*100000000 for i in l(3)]
    for i in l(3):
        t.append([a[j][i] for j in l(3)]+[r[0][i]])
        u.append([a[j][i] for j in l(3)]+[p[i]-r[0][i]])
    #print t,u
    b = -d(t)/d(u)
    #b = round(b,6)
    if b < 0:
        return []
    else:
        #print b
        p = [r[0][i]+(p[i]-r[0][i])*b for i in l(3)]
        #print p
        di = sum([(p[i]-r[0][i])**2 for i in l(3)])**0.5
        #print di
        for k in l(3):
            print k,(k+1)%3
            u = [a[(k+1)%3][i]-a[k][i] for i in l(3)]
            v = [a[(k+2)%3][i]-a[k][i] for i in l(3)]
            n = cr(u,v)
            w = [p[i]-a[k][i] for i in l(3)]

            nn = sum([n[i]**2 for i in l(3)])

            g = abs(sum([cr(u,w)[i]*n[i] for i in l(3)]))/nn
            b = abs(sum([cr(w,v)[i]*n[i] for i in l(3)]))/nn
            aa = 1-g-b

            #print g,b,a
            if not (0<=g<=1 and 0<=b<=1 and 0<=aa<=1):
                return []
        return [round(x,2) for x in p+[di]]