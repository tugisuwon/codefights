#https://codefights.com/challenge/T9mZQb7SF3jo9Dxhm
def MoreTimesLess(n):
    t = 0
    n = int(n)
    p = n**0.5
    for i in xrange(2+n%2,int(p)+1,2):
        #print n,i,n%i,t
        if n%i==0:
            if (i+n/i)%2==0:
                t += 1
    if p == int(p):
        t -= 1
    return t+n%2

