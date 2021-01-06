#Python3
#week -6 - assign1
import numpy as np
def Knapsac(W,w,items,T):
    for i in range(items+1):
        T[i][0] = 0
    for i in range(W+1):
        T[0][i] = 0
    for i in range(1,items+1):
        for j in range(1,W+1):
            if T[i-1][j] + w[i-1] <=j and T[i-1][j-w[i-1]] + w[i-1] <=j:
                T[i][j] = max(T[i-1][j] + w[i-1], T[i-1][j-w[i-1]] + w[i-1]) 
            elif T[i-1][j] + w[i-1] <=j:
                T[i][j] = T[i-1][j] + w[i-1]
            elif j-w[i-1] >= 0 and T[i-1][j-w[i-1]] + w[i-1] <=j:
                T[i][j] = T[i-1][j-w[i-1]] + w[i-1]
            T[i][j] = max(T[i][j],T[i][j-1],T[i-1][j])
    return int(T[items][W])
W,items = map(int,input().split())
w = list(map(int,input().split()))
T = np.zeros((items+1,W+1))
print(Knapsac(W,w,items,T))