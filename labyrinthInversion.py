#https://codefights.com/challenge/GyhEGS9GvtctXhuHh/solutions/fdHNZrPLC9rJ6Ar5Y
def labyrinthInversion(l):
    s = (0,0)
    r,c = len(l), len(l[0])
    if r == 1 and c == 1:
        if l[r][c] == '.':
            return []
        else:
            return [[0,0,1]]
    
    # visited cell
    v = set()
    v.add(s)
    
    # possible direction
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    
    l = [''.join(x) for x in l]
    
    # all possible grid
    ll = [(l,[[0,0,0]])]
    for i in xrange(r):
        for j in xrange(c):
            y = min(r-i,c-j)
            for k in xrange(1,y+1):
                b = []
                for ii in xrange(r):
                    temp = ''
                    for jj in xrange(c):
                        if i <= ii < i+k and j <= jj < j+k:
                            if l[ii][jj] == '.':
                                temp += '#'
                            else:
                                temp += '.'
                        else:
                            temp += l[ii][jj]
                    b.append(temp)
                ll.append((b,[[i,j,k]]))
    lll = [x for x in ll]  
    kk = 0
    while True:
        oo = []
        for l in lll:
            tt = l[0]
            if l[1] != [[0,0,0]]:
                x,y = l[1][kk][0],l[1][kk][1]
                for i in xrange(x,r):
                    for j in xrange(y,c):
                        if i != x or j != y:
                            yy = min(r-i,c-j)
                            #print l,i,j,yy
                            for k in xrange(1,yy+1):
                                b = []
                                for ii in xrange(r):
                                    temp = ''
                                    for jj in xrange(c):
                                        if i <= ii < i+k and j <= jj < j+k:
                                            if tt[ii][jj] == '.':
                                                temp += '#'
                                            else:
                                                temp += '.'
                                        else:
                                            temp += tt[ii][jj]
                                    b.append(temp)
                                if b[0][0] == '.' and b[-1][-1] == '.':
                                    oo.append((b,l[1] + [[i,j,k]]))
        kk += 1
        if oo == [] or kk ==3:
            break
        ll += oo
        lll = oo
    #print ll
    mm,output = r*c,[]
    for lll in ll:
        if lll[0][0][0] == '.':
            s = [((0,0),0)]
            v = set()
            v.add((0,0))
            terminate = 0
            while True:
                p = []
                for i in s:
                    for j in d:
                        po = (i[0][0]+j[0],i[0][1]+j[1])
                        if 0 <= po[0] < r and 0 <= po[1] < c:
                            if po not in v:
                                if po == (r-1,c-1) and lll[0][po[0]][po[1]] == '.':
                                    if i[1]+1 < mm:
                                        #print lll, i[1]+1
                                        mm = i[1]+1
                                        output = [lll[1]]
                                    elif i[1]+1 == mm:
                                        #print lll,i
                                        output.append(lll[1])
                                    terminate= 1
                                v.add(po)
                                if lll[0][po[0]][po[1]] != '#':
                                    p.append((po,i[1]+1))
                        if terminate == 1:
                            break
                    if terminate == 1:
                        break
                if terminate == 1 or p == []:
                    break
                s = p
    #print output
    if output == []:
        return []
    ans = min(len(x) for x in output)
    output = [x for x in output if len(x) == ans]
    #print 'o',output
    temp = sorted(output)[0]
    if temp[0].count(0) == len(temp[0]):
        return []
    else:
        return temp
        
