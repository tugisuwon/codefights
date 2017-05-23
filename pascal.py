#https://codefights.com/challenge/mcmftZWjoRBqHKPWp
def Pascal(n, p):
    r = [0]*(p+1)
    r[0] = 1
    o = 1
    while o < (n+1):
        r[p] = (p*(p+1)/2)*r[p] + p*(p-1)*o*(o-1)/4
        o *= p
    return str(r[p])d