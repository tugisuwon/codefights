#https://codefights.com/challenge/2jkS5hmtYhyB8mL76/solutions/jhQFXhkGfaSKYkDA4
def pokerWinner(p1, p2):
    d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
    dd = {j:i for i,j in d.items()}
    suits = {'S':3, 'H':2, 'D':1, 'C':0}
    # 0 = royal flush, 1 = four, 2 = full house, 3 = flush, 4 = straight, 5 = three, 6 = two pair, 7 = one pair, 8 = high
    o = []
    for i in [p1,p2]:
        t = sorted([d[a[0]] for a in i])
        s = list(set([a[1] for a in i]))
        if len(s) == 1:
            if all(t[j+1]-t[j] == 1 for j in xrange(4)):
                o.append((0,suits[s[0]],min(t)))
            else:
                o.append((3,suits[s[0]],min(t)))
        else:
            if all(t[j+1]-t[j] == 1 for j in xrange(4)):
                o.append((4,suits[s[0]],min(t)))
            else:
                temp = {j:t.count(j) for j in set(t)}
                temp_ = {}
                for a,b in temp.items():
                    if b not in temp_:
                        temp_[b] = [a]
                    else:
                        temp_[b].append(a)
                #print temp_
                if 4 in temp_:
                    o.append((1,temp_[4][0]))
                elif 3 in temp_ and 2 in temp_:
                    o.append((2,temp_[3][0],temp_[2][0]))
                elif 3 in temp_:
                    o.append((5,temp_[3][0]))
                elif 2 in temp_:
                    if len(temp_[2]) == 2:
                        o.append((6,max(temp_[2]),min(temp_[2])))
                    else:
                        o.append((7,temp_[2][0]))
                else:
                    o.append((8,max(t)))
    #print o
    if o[0][0] == o[1][0]:
        if o[0][0] in [0,3,4]:
            return 0
        else:
            return [1,2][o[0][1] < o[1][1]]
    else:
        return [1,2][o[0][0] > o[1][0]]
                    
                    
                    