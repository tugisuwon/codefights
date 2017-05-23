#https://codefights.com/challenge/5eqj9PTETb8MS5Xuo/solutions/H5cQet3h8WxRRLKFE
r = range
def validate(p):
    b = {"American Express":{2:[34,37],"l":[15]},"Discover Card":{2:[65],3:r(644,650),4:[6011],6:r(622126,622926),"l":[16,19]},"InterPayment":{3:[636],"l":r(16,20)},"JCB":{4:r(3528,3590),"l":[16]},"Laser":{4:[6304,6706,6771,6709],"l":r(16,20)},"Maestro":{1:[6],2:[50,56,57,58],"l":r(12,20)},"MasterCard":{2:r(51,56),4:r(2221,2721),"l":[16]},"Switch":{4:[4903,4905,4911,4936,6759,6333],6:[564182,633110],"l":[16,18,19]},"Visa":{1:[4],"l":[13,16,19]}}
    z = 0
    w = []
    for l in p:
        jj = False
        if l[0] in b:
            a = b[l[0]]
            d = ''.join(x for x in l[1] if x != ' ' and x != '-')
            #print a["l"]
            if len(d) in a["l"]:
                q = 0
                for i,j in a.items():
                    #print i,j
                    if 0 < i < 9:
                        if int(d[:i]) in j:
                            q = 1
                if l[0] == "Maestro":
                    #print l
                    for c,bb in b.items():
                        for k,v in bb.items():
                            if 0 < k < 9 and c != l[0]:
                                if int(d[:k]) in v:
                                    #print z,c,k,v
                                    q = 0
                if q == 1:
                    s = 0
                    f = 0
                    for i in d[::-1]:
                        if f == 0:
                            s += int(i)
                        else:
                            t = int(i)*2
                            if t > 9:
                                t -= 9
                            s += t
                        f = (f+1) % 2
                    if s % 10 == 0:
                        jj = True
        w.append(jj)
        z += 1
    return w
    
