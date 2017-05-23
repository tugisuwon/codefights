https://codefights.com/challenge/mphk8gHzaN5KQAJij
def sumSquares(k):
    c = 0
    for i in xrange(1,int(1 + k**0.5)):
        if k%i == 0:
            c += (i%4==1)*1 - (i%4==3)*1
            l = k/i
            c += (l%4==1)*1 - (l%4==3)*1 - (l==i)*1
            #print ii,l
    return c