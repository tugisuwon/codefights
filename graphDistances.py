def graphDistances(g, s):
    ans = {i:10**9 for i in xrange(len(g))}
    
    import heapq as Q
    ans[s] = 0
    h = [(s,0,set([s]))]
    while h:
        p = Q.heappop(h)
        #print p
        for i in [x for x in xrange(len(g)) if g[p[0]][x] != -1 and x not in p[2]]:
            temp = p[2].copy()
            temp.add(i)
            #print temp
            cost = p[1] + g[p[0]][i]
            new = i
            if ans[i] > cost:
                ans[i] = cost
                Q.heappush(h, (i,cost,temp))
    return ans.values()
