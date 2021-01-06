#Python3
#Fibonacci- week -2 - assign5
def findPeriod(m):
    b = [0,1]
    i = 0
    while(True):
        g=(b[i] + b[i+1])%m
        if g == 1 and b[-1] == 0:
            break
        b.append(g)
        i = i+1
    return b[0:len(b)-1]
n,m = map(int,input().split())
period = findPeriod(m)
a = len(period)
print(period[n%a])
    