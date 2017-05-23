#https://codefights.com/interview/Gh37HrvDBrqfLi2iA
def longestCommonSubstring(s, t):
    if not set(s).intersection(set(t)):
        return 0
    from collections import defaultdict as d
    a = d(list)
    for i in xrange(len(t)):
        a[t[i]].append(i)
    m = 0
    i = 0
    while i < len(s):
        #print 'a'
        if s[i] in a:
            j = i+1
            x = a[s[i]]
            k = 1
            while x and j < len(s):
                t = s[j]
                #print x,j,k,t,a[t]
                if t in a:
                    x = [y+1 for y in x if y+1 in a[t]]
                    if not x:
                        break
                    else:
                        m = max(m,k)
                else:
                    #i = j
                    break
                j += 1
                k += 1
        i += 1
    return m+1