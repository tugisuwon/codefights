#https://codefights.com/challenge/g97soCpb4sGnMAsTc
def isNumberlinkWellDesigned(g):
    p = {i:[] for i in xrange(1,50)}
    r,c = len(g),len(g[0])
    a = set()
    dot = 0
    for i in xrange(r):
        for j in xrange(c):
            if g[i][j].isdigit():
                p[int(g[i][j])].append((i,j))
                a.add(int(g[i][j]))
            else:
                dot += 1
    import heapq as H
    #print p
    if dot == 0:
        return True
    
    d = [[-1,0],[1,0],[0,1],[0,-1]]
    l = [set('0')]
    #a = sorted(list(a))
    for i in a:
        s = p[i][0]
        ww = [str(s[0])+str(s[1])]
        po = []
        
        #Q = [ww]
        for kk in l:
            v = kk
            o = {}
            Q = [ww]
            cu = set()
            while Q:
                j = H.heappop(Q)
                for k in d:
                    pp = (int(j[-1][0])+k[0],int(j[-1][1])+k[1])
                    te = str(pp[0])+str(pp[1])
                    if 0 <= pp[0] < r and 0 <= pp[1] < c and te not in j and te not in v:
                        if te in o:
                            o[te] += 1
                        else:
                            o[te] = 1
                        if o[te] < 150:
                            np = j+[te]
                            if g[pp[0]][pp[1]].isdigit() and i == int(g[pp[0]][pp[1]]):
                                tt = ''.join(sorted(np))
                                temp = set(np)
                                #print i,v,np
                                if tt not in cu:
                                    cu.add(tt)
                                    #print i, tt, cu, v, temp
                                    po.append(v.union(temp))
                            #elif pp not in v:
                            elif not g[pp[0]][pp[1]].isdigit():
                                #v.add(pp)
                                H.heappush(Q,np)
        if po == []:
            l = []
            break
        l = po
        #print i,l

    return sum(len(x)-1 == r*c for x in l) == 1

                            
                            