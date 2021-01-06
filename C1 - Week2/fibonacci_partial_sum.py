#Python3
#Fibonacci- week -2 - assign7
def findPeriod():
    b = [0,1]
    i = 0
    while(True):
        g=(b[i] + b[i+1])%10
        if g == 1 and b[-1] == 0:
            break
        b.append(g)
        i = i+1
    return b[0:len(b)-1]
def sumOfFib(h,sumOfPeriod,a):
    sumOfNum = (sumOfPeriod*(int(h/a)))
    b = h%a
    for i in range(a):
        if b >=i:
            sumOfNum = sumOfNum + period[i]
    return sumOfNum
m,n = map(int,input().split())
period = findPeriod()
a = len(period)
sumOfPeriod = sum(period)
MaxVal = sumOfFib(n,sumOfPeriod,a)
MinVal = sumOfFib(m-1,sumOfPeriod,a)
print((MaxVal - MinVal)%10)