#https://codefights.com/interview/ccHxGiEhZmbyycSNu
def possibleSums(c, q):
    a = set()
    p = max(q)
    l = q.index(p)
    cc = [c[l]*x for x in xrange(p+1)]
    b = set(cc)
    for i in xrange(len(c)):
        if i != l:
            for j in xrange(q[i]):
                d = b.copy()
                for k in b:
                    d.add(k + c[i])
                d.add(c[i])
                b = d
                #print b
    return len(b)-1