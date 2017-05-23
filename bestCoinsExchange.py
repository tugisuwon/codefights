#https://codefights.com/challenge/vFup7mXP4Sdfpx6TY/solutions/8gx2K2snx4SJPHYJs
def bestCoinsExchange(i, c):
    o = [[0]*(c+1)]
    s = i[0]
    for k in xrange(1,c+1):
        if k%s==0:
            o[-1][k] = k/s
        else:
            o[-1][k] = 1000000
    for j in i[1:]:
        o.append([0]*(c+1))
        for k in xrange(1,c+1):
            if k < j:
                o[-1][k] = o[-2][k]
            else:
                o[-1][k] = min(o[-2][k],o[-1][k-j]+1)
    a = {k:0 for k in i}
    r = c = 1
    s = o[-r][-c]
    while s > 0:
        if r == len(o):
            a[i[0]] += s
            c += i[0]
        elif o[-r-1][-c] == s:
            if c+i[-r] <= len(o[0]):
                if o[-r][-c-i[-r]] < s:
                    a[i[-r]] += 1
                    c += i[-r]
                else:
                    r += 1
            else:
                r += 1
        else:
            a[i[-r]] += 1
            c += i[-r]
        s = o[-r][-c]
        #print a,r,c,s
    an = []
    for j in sorted(i,reverse=True):
        if a[j] != 0:
            an.append([j,a[j]])
    return an