https://codefights.com/interview/Q8td3XApSWuobjEaJ
def setsOfFactors(n):
    f = set()
    for i in xrange(1,int(round(n**0.5))+1):
        if n%i == 0:
            f.add(tuple(sorted([i,n/i])[::-1]))
    #print f
    a = f.copy()
    while True:
        change = 0
        ff = set()
        for i in a:
            #print i
            if 1 not in i:
                i = list(i)
                for j in xrange(len(i)):
                    for k in xrange(2,int(round(i[j]**0.5))+1):
                        if i[j]%k == 0:
                            temp = i[:j] + i[j+1:] + [i[j]/k,k]
                            #print i,temp
                            ff.add(tuple(sorted(temp)[::-1]))
                            change = 1
        if change == 0:
            break
        for i in ff:
            f.add(i)
        a = ff
    return sorted([list(x) for x in f], reverse=True)
                        
