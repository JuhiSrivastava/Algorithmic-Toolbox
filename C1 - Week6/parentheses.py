#Python3
#week -6 - assign3
import numpy as np
def MinAndMax(i,j,M,m,op):
    mini = 10000000
    maxi = -10000000
    for k in range(i,j):
        if op[k] == '*':
            a = M[i,k] * M[k+1,j]
            b = M[i,k] * m[k+1,j]
            c = m[i,k] * M[k+1,j]
            d = m[i,k] * m[k+1,j]
        if op[k] == '+':
            a = M[i,k] + M[k+1,j]
            b = M[i,k] + m[k+1,j]
            c = m[i,k] + M[k+1,j]
            d = m[i,k] + m[k+1,j]
        if op[k] == '-':
            a = M[i,k] - M[k+1,j]
            b = M[i,k] - m[k+1,j]
            c = m[i,k] - M[k+1,j]
            d = m[i,k] - m[k+1,j]
        mini = min(mini,a,b,c,d)
        maxi = max(maxi,a,b,c,d)
    M[i,j] = maxi
    m[i,j] = mini
    return M,m

exp = input()
size = int(len(exp)/2) +1
M = np.zeros((size,size),int)
m = np.zeros((size,size),int)
op = []
j = 0
for i in range(len(exp)):
    if i%2 == 0:
        M[j,j] = int(exp[i])
        m[j,j] = int(exp[i])
        j = j+1
    else:
        op.append(exp[i])
for s in range(size):
    for i in range(size-s):
        j = i+s
        if i!=j:
            M,m = MinAndMax(i,j,M,m,op)
print(max(M[0][size-1],m[0][size-1]))
        