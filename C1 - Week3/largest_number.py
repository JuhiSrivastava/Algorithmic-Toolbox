#Python3
#Fibonacci- week -3 - assign7
import numpy as np
n = int(input())
a = list(map(int,input().split()))
value =""
for i in range(len(a)):
    for j in range(len(a)-1):
        if int(str(a[j])+str(a[j+1])) < int(str(a[j+1])+str(a[j])):
            a[j+1], a[j] = a[j],a[j+1]
for i in range(len(a)):
    value = value + str(a[i])
print(value)