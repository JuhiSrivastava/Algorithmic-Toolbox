#python3
import numpy as np
n = input()
a = np.array(input().split())
maxVal1 = -1
maxVal2 = -1
maxInd = -1
maxInd2 = -1
for i in range(len(a)):
    b = int(a[i])
    if b >= maxVal1:
        maxVal1 = b
        maxInd1 = i
for i in range(len(a)):
    b = int(a[i])
    if i != maxInd1 and b >= maxVal2:
        maxVal2 = b
        maxInd2 = i   
print(maxVal1*maxVal2)