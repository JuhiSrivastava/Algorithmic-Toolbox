#Python3
#Fibonacci- week -3 - assign2
import numpy as np
def greedy(n,vwp,W):
    value = 0
    for i in range(n-1,-1,-1):
        if W==0:
            return value
        a = min(W,vwp[i][0])
        value = value + a*vwp[i][1]
        W = W - a
    return value
n,W = map(int,input().split())
v=[]
w=[]
vwp = np.zeros((n,2))
for i in range(n):
    a,b = map(int,input().split())
    vwp[i] = (b,a/b)
vwp = sorted(vwp, key=lambda x : x[1])
print('{:.4f}'.format(greedy(n,vwp,W)))