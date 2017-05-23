#https://codefights.com/challenge/rdmGB4mPpshQDTv2X/solutions/LwyprpcAmit4SxpAJ
def shortestPathWithManyEdges(s, f, w, e, g):
    r = len(g)
    added = set()
    for i in xrange(r):
        for j in xrange(i+1,r):
            if g[i][j] == 0:
                g[i][j] = w
                added.add((i,j))
                g[j][i] = w
                added.add((j,i))
    #print g
    s = [(str(s-1),0,0)]
    mm, count = 10**9,{}
    
    while True:
        p = []
        for i in s:
            for j in [x for x in range(r) if str(x) not in i[0]]:
                xx,yy = int(i[0][-1]), j
                weight = i[2] + g[xx][yy]
                out = i[1]
                if (xx,yy) in  added:
                    out += 1
                if j == f-1:
                    if out <= e:
                        if weight < mm:
                            mm = weight
                            count = {out:1}
                        elif weight == mm:
                            if out in count:
                                count[out] += 1
                            else:
                                count[out] = 1
                else:
                    path = i[0] + str(j)
                    if out <= e and weight < mm:
                        p.append((path,out,weight))
        #print p
        if p == []:
            break
        s = p

    if mm == 10**9:
        return [0,0]
    else:
        k = min(i for i in count.keys())
        return [mm,count[k]]
                    