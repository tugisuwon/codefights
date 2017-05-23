#https://codefights.com/interview/pGscY3EBKyQq3ro47
def shortestPathWithEdge(start, finish, weight, graph):
    
    d = {i:{} for i in xrange(1,len(graph)+1)}
    for i in xrange(len(graph)):
        for j in xrange(len(graph[0])):
            if graph[i][j] != 0:
                d[i+1][j+1] = graph[i][j]
                d[j+1][i+1] = graph[i][j]
    
    print d
    s = [(start,0)]
    m = 10**9
    v = set()
    v.add(start)
    while True:
        p = []
        for i in s:
            #print i[0], d[i[0]]
            for j,k in d[i[0]].items():
                if j not in v:
                    v.add(j)
                    temp = j
                    score = i[1] + k
                    if finish not in d[j]:
                        m = min(m,score+weight)
                    if j == finish:
                        m = min(m,score)
                    else:
                        p.append((temp,score))
        if p == []:
            break
        s = p
    #print d[finish]
    for i,j in d[finish].items():
        if start not in d[i]:
            m = min(m,j+weight)
    if start not in d[finish]:
        m = min(m,weight)
    return m
        
