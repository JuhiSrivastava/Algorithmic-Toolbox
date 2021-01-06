#Python3
#Fibonacci- week -3 - assign4
import numpy as np
n = int(input())
profit = list(map(int,input().split()))
clicks = list(map(int,input().split()))
profit = np.sort(profit)
clicks = np.sort(clicks)
product = 0
for i in range(n):
    product = product + (profit[i]*clicks[i])
print(product)