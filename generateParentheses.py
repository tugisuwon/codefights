def generateParentheses(n):
    s = [('(',1)]
    for i in xrange(2*n-1):
        p = set()
        for j in s:
            for k in '()':
                if k == '(':
                    o = j[1] + 1
                else:
                    o = j[1] - 1
                temp = j[0]+k
                if i == 2*n-2:
                    if o == 0:
                        p.add(temp)
                elif o >= 0:
                    p.add((temp,o))
        s = p
    return sorted(s)