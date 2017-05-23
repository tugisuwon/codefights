#https://codefights.com/challenge/nYRdtSE58ChzYbhEN
def HighestScore(game):
    def h(x,c):
        print x,c
        if type(x) is int:
            return x
        [a,b] = x
        v = not c
        if c:
            return max(h(a,v),h(b,v))
        else:
            return min(h(a,v),h(b,v))
    return h(eval(game),True)