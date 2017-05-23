#https://codefights.com/interview/kEgA4DXcfXuriqGru
def sumSubsets(arr, num):

    output = []
    arr = sorted(arr)
    for i in xrange(len(arr)):
        if arr[i] == num:
            output.append([arr[i]])
            break
            
        s = [[arr[i]]]
        for j in xrange(i+1,len(arr)):
            if arr[i] + arr[j] == num:
                if [arr[i],arr[j]] not in output:
                    output.append([arr[i],arr[j]])
                break
            p = []
            for k in s:
                if sum(k) + arr[j] == num:
                    if k+[arr[j]] not in output:
                        #print k
                        output.append(k+[arr[j]])
                elif sum(k) + arr[j] < num:
                    p.append(k+[arr[j]])
            s = p + s
    if output == []:
        return [[]]
    else:
        return sorted(output)
                
        
