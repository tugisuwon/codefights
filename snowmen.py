#https://codefights.com/challenge/G3NpJorpYBwC3Nviz/solutions/fKttp6jtCXG235WSa
def snowmen(s):
    a = {i:s.count(i) for i in set(s)}
    s = sorted(s)
    p = sum(s)
    n = len(s)/3
    ss = a
    from itertools import combinations as c
    for i in xrange(n,0,-1):
        #print 3*i
        v = set()
        if p < sum(s[:len(s)-3*i]):
            break
        for k in c(s,3*i):
            t = {g:h for g,h in a.items()}
            #k = tuple(sorted(k))
            #print k
            if k not in v:
                b = 1
                v.add(k)
                for j in list(set(k)):
                    if k.count(j) > i:
                        b = 0
                        break
                    t[j] -= k.count(j)
                    if t[j] < 0:
                        b = 0
                        break
            if b == 1:
                temp = sum(g*h for g,h in t.items())
                #print temp
                if temp < p:
                    p = temp
                    ss = t
            if p == 0:
                return 0
        if p == 0:
            return 0
    c = 0
    for i,j in ss.items():
        c += j*i**3
    from math import pi
    return c*4/3.*pi