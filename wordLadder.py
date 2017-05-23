#https://codefights.com/interview/EDaACHNYHyH6qQFAL
def wordLadder(b, e, w):
    if e not in w:
        return 0
    s = [b]
    n = 0
    a = 0
    v = set()
    while n < len(w):
        p = []
        for i in s:
            x = [x for x in w if x not in v]
            for j in x:
                #print i,j,sum(1 if i[l] != j[l] else 0 for l in xrange(len(i)))
                if sum(1 if i[l] != j[l] else 0 for l in xrange(len(i))) == 1:
                    v.add(j)
                    if j == e:
                        a = 1
                        break
                    p.append(j)
            if a == 1:
                break
        #print p
        if a == 1:
            n += 2
            break
        if p == []:
            n = 0
            break
        n += 1
        s = p
    return n
        
        
