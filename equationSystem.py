#https://codefights.com/challenge/9o3s9u8gf9f6piHgC
def equationSystem(e):
    def d(a):
        return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2]) -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2]) +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))
    a,b = [],[]
    for i in e:
        i = i.replace('x',' ').replace('y',' ').replace('z',' ').replace('+','').replace('=','').split(' ')
        for j in xrange(len(i)):
            if i[j] == '':
                i[j] = '1'
            elif i[j] == '-':
                i[j] = '-1'
        a.append(map(int,i[:3]))
        b.append(int(i[-1]))
    x,y,z = [],[],[]
    for i in xrange(3):
        x.append([b[i]]+a[i][1:])
        y.append([a[i][0],b[i],a[i][2]])
        z.append(a[i][:-1]+[b[i]])
    print x,y,z,a
    q = d(a)
    return [d(x)/q,d(y)/q,d(z)/q]
