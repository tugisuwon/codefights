#https://codefights.com/challenge/mATNcCZX4f5MEzQug/solutions/AbuzLJ3uM7BP76fMt
def safeSystem(p, l, t):
    d = {}
    e = {}
    n = len(p)
    a = [x for x in range(2,n+2) if x not in p]
    for i in range(n):
        if p[i] in d:
            d[p[i]].append(i+2)
        else:
            d[p[i]] = [i+2]
        if p[i] != 1:
            if p[i] not in e:
                e[p[i]] = {0:t[p[i]-2]}
    # visited node        
    v = set() 
    for i in a:
        e[i] = {0:10**9}
        #v.add(i)

    #print e
    while 1 not in e or len(e) > 1:
        ff = []
        for i in e.keys():
            q = 0
            # only need to process the node where all child(ren) are visited previously; otherwise, we add new element if arrival time is different or modify if arrival time is already present in that node
            if i in d and i != 1:
                if all(x in v for x in d[i]):
                    q = 1
            elif i in a:
                q = 1
            if q == 1:
                v.add(i)
                y = p[i-2]
                for j in e[i].keys():
                    m = min(e[i][j], t[i-2]) 
                    # pipe area is limited, so we use min
                    o = j + l[i-2] 
                    # new arrival time
                    if y in e:
                        if o in e[y]:
                            e[y][o] += m
                        else:
                            e[y][o] = m
                    else:
                        e[y] = {o:m}
                ff.append(i)
        for f in ff:
            del e[f]
        #print e,v
    #print e
    return sum(e[1][x] for x in e[1].keys())
