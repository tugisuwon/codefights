#https://codefights.com/challenge/HAa3E3KifJqEXotNt/solutions/tR48vueJys9FSGGE9
def maxDiscount(p):
    a = {-1:0}
    j = []
    for i in range(len(p)-2):
        j.append(min(p[i:i+3]))
    for i in range(len(j)):
        b = {}
        for k,l in a.items():
            if k < i:
                t1 = k+3
                t2 = k+1
                if t1 in b:
                    b[t1] = max(b[t1],l+j[i])
                else:
                    b[t1] = l+j[i]
                if t2 in b:
                    b[t2] = max(b[t2],l)
                else:
                    b[t2] = l
                #b.append((k[0]+j[i],k[1]+3))
                #b.append((k[0],k[1]+1))
            else:
                if k in b:
                    b[k] = max(b[k],l)
                else:
                    b[k] = l
        a = b
        #print i,a
    return max(j for i,j in a.items())
