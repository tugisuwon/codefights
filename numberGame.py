#https://codefights.com/challenge/9nTbqicisfHXHMjHn
def numberGame(n, d):
    p = 0
    c = [n]
    while True:
        ne = []
        #print c
        for cc in c:
            if len(cc) > 1:
                for i in xrange(len(cc)):
                    t = int(cc[:i]+cc[i+1::])
                    if t % d == 0 and t != 0:
                        if str(t) not in ne:
                            ne.append(str(t))
        if ne != []:
            p += 1
        d -= 1
        if ne == [] or d == 1:
            break
        c = ne
    ne = [int(x) for x in ne]
    if d == 1 and ne != [] and max(ne)>9:
        #print ne
        p += 1
    return p
