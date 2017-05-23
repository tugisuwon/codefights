#https://codefights.com/interview/t6JR865A3Yg2R3ExW
def nQueens(N):
    ans = []
    def search(cols = []):
        if len(cols) == N:
            ans.append(cols)
            return
        for y in xrange(1, N+1):
            if y not in cols:
                if not any( y+len(cols) == x+i or y-len(cols) == x-i
                            for i,x in enumerate(cols) ):
                    #print cols + [y]
                    search(cols + [y])
                    
    search()
    return ans