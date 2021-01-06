#Python3
#week -4 - assign6
import math
def CheckStrip(a,mindis):
    b=[]
    mid = int(len(a)/2)
    for i in range(len(a)):
        if a[i][0] - a[mid][0] < mindis or a[mid][0] - a[i][0] < mindis:
            b.append(a[i])
    b = sorted(b,key = lambda x:x[1])
    minDis2 = mindis
    for i in range(len(b)):
        if i <=7:
            for j in range(i+7+1):
                if j < len(b) and j!=i:
                    if minDis2 > Dist(b[i],b[j]):
                        minDis2 = Dist(b[i],b[j])
                else:
                    break  
        if i >=7:
            for j in range(i-7,i+7+1):
                if j < len(b) and j!=i:
                    if minDis2 > Dist(b[i],b[j]):
                        minDis2 = Dist(b[i],b[j])
                else:
                    break
    print("{:4f}".format(minDis2))
def Dist(point1,point2):
    return math.sqrt(((point1[0] - point2[0])*(point1[0] - point2[0])) + ((point1[1] - point2[1])*(point1[1] - point2[1])))
def CalDistance(a):
    if len(a) == 3:
        return min(Dist(a[0], a[1]),Dist(a[1], a[2]),Dist(a[0], a[2]))
    if len(a) == 2:
        return Dist(a[0], a[1])
    mid = int(len(a)/2)
    return min(CalDistance(a[:mid]),CalDistance(a[mid:]))
n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a = sorted(a,key = lambda x:x[0])
minDis = CalDistance(a)
if minDis == 0.0:
    print("{:4f}".format(minDis))
else:
    CheckStrip(a,minDis)