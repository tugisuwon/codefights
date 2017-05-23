#https://codefights.com/challenge/W3G9JyaK5wkuvRTRA
def passwordHacking(k, n):
    r = range
    d = {}
    for i in r(10):
        if i % 2:
            d[i] = r(i)
        else:
            d[i] = r(1,10,2)
    t = [0]*n
    for i in k:
        t[i[0]-1] = [i[1]]
        if i[0] < n:
            if i[1] % 2:
                if t[i[0]] == 0:
                    t[i[0]] = r(i[1])
                else:
                    t[i[0]] = list(set(t[i[0]]).intersection(r(i[1])))
            else:
                if t[i[0]] == 0:
                    t[i[0]] = r(1,10,2)  
                else:
                    t[i[0]] = list(set(t[i[0]]).intersection(r(1,10,2)))
        if i[0] - 2 >= 0:
            if i[1] % 2:
                if t[i[0]-2] == 0:
                    t[i[0]-2] = r(0,10,2) + r(i[1],10,2)
                else:
                    t[i[0]-2] = list(set(t[i[0]-2]).intersection(r(0,10,2) + r(i[1],10,2)))
            else:
                if t[i[0]-2] == 0:
                    t[i[0]-2] = r(i[1]+1,10,2)
                else:
                    t[i[0]-2] = list(set(t[i[0]-2]).intersection(r(i[1]+1,10,2)))
    c = {}
    if t[0] == 0:
        for i in r(10):
            c[i] = 1
    else:
        for i in t[0]:
            c[i] = 1
    #print t
    #print c
    for i in r(1,n):
        ne = {}
        if t[i] == 0:
            t[i] = r(10)
        for j,v in c.iteritems():
            temp = set(d[j]).intersection(t[i])
            if len(temp) != 0:
                for k in temp:
                    if k not in ne:
                        ne[k] = v
                    else:
                        ne[k] += v
        #print i,ne
        c = ne
    if len(c) == 0:
        return 0
    else:
        a = 0
        for i,v in c.iteritems():
            a += v
        return a
                    
                
        
        

        
            
