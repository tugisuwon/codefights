#https://codefights.com/interview/3gY7eyeRMZeARKmyQ
def subsetSum(arr):
    s = sum(arr)
    if s % 2:
        return False
    if s/2 in arr:
        return True
    t = [x for x in arr if x < s/2]
    t = sorted(t)
    dp = [0]*(s/2+1)
    dp[0] = 1
    dp[t[0]] = 1
    for i in t[1:]:
        dp_ = [0]*(s/2+1)
        for j in xrange(i):
            dp_[j] = dp[j]
        for j in xrange(i,s/2+1):
            dp_[j] = dp[j-i] or dp[j]
        if dp_[-1]:
            return True
        dp = dp_
    return False
        
        
                    