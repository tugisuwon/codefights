#https://codefights.com/interview/vG6SManzGDZsoqsh7
def swapLexOrder(s, p):
    index = []
    for i in p:
        j = 0
        for k in xrange(len(index)):
            if i[0] in index[k] or i[1] in index[k]:
                index[k].add(i[0])
                index[k].add(i[1])
                j = 1
                break
        if j == 1:
            t = set()
            t.add(i[0])
            t.add(i[1])
            index.append(t)
                                
    print index
        
