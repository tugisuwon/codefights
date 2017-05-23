#https://codefights.com/challenge/pA34fzHCHE9fJMi4F
def fillByPowers(s, b, e):
    a = []
    c = 1
    while c**e <= b:
        a += [c**e]
        c += 1
    d = a
    for _ in xrange(s-1):
        n = set()
        for i in d:
            for j in a:
                if i + j <= b:
                    n.add(i + j)
        d = n
    #print d
    return len(d)
