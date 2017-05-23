#https://codefights.com/interview/roN2QLRJnPnfMqDaD
def regexMatching(pattern, test):
    if '^' in pattern:
        p = pattern.replace('^','')
        return p == test[:len(p)]
    elif '$' in pattern:
        p = pattern.replace('$','')
        return p == test[-len(p):]
    else:
        return pattern in test
