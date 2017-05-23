#https://codefights.com/challenge/Bsmyb86TtXuL9DyE3
def NewYearCodeFightsHacking(n, m):
    x = range
    o = 'codefights'*n
    g,h = len(m),len(o)
    if g > h:
        return -1
    else:
        a = [[0]*(g+1)]
        for i in x(h):
            t = [y for y in a[-1]]
            for j in x(g):
                if o[i] == m[j]:
                    t[j+1] = a[-1][j]+1
                else:
                    t[j+1] = max(a[-1][j],a[-1][j+1])
                j += 1
                if j > i:
                    break
                
            a = [t]
        #print 2*len(m),a[-1],len(m),len(o)
        return 2*g-a[-1][-1]
        

