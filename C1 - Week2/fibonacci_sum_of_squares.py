#Python3
#Fibonacci- week -2 - assign8
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
            sumOfNum = sumOfNum + (period[i]*period[i])
    return sumOfNum
n = int(input())
if n > 0:
    period = findPeriod()
    a = len(period)
    sumOfPeriod = 0
    for i in range(a):
        sumOfPeriod = sumOfPeriod + (period[i]*period[i])
    sumOfPeriod = sumOfPeriod%10
    print(sumOfFib(n,sumOfPeriod,a)%10)
else:
    print(0)