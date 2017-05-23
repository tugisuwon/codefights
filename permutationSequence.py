#https://codefights.com/interview/Ruzueihek5i5cHJRD
def permutationSequence(n, k):
    f = [1]
    for i in xrange(1, n+1):
        f.append(f[-1] * i)
    
    p = range(1, n+1)
    ans = []
    k -= 1
    while k:
        q, r = k/f[n-1], k%f[n-1]
        ans.append(p.pop(q))
        k = r
        n -= 1
    ans.extend(p)
    return "".join(map(str, ans))