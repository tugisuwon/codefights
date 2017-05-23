#https://codefights.com/interview/jAkQe9roSfJme2XRt
def nearestGreater(a):
    ans = [-1]*len(a)
    m = max(a)
    p = 0
    for i in xrange(len(a)):
        if p != 0 and p == a[i]:
            k = max(1,k-2)
        else:
            k = 1
        #print i,k
        if a[i] == m:
            pass
        else:
            while True:
                if i-k >= 0 and a[i-k] > a[i]:
                    ans[i] = i-k
                    break
                if i+k < len(a) and a[i+k] > a[i]:
                    ans[i] = i+k
                    break
                if i-k < 0 and i+k >= len(a):
                    break
                k += 1
        #print k
        p = a[i]
    return ans
