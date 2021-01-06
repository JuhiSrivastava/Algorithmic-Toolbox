#Python3
#week -6 - assign2
import numpy as np
def getItem(T,Wei,weight,a):
    i,j = T.shape
    lengW = len(weight)-1
    i = i-1
    j = j-1
    while Wei !=0 and lengW >=0:
        if T[i-1][j] == T[i][j]:
            lengW = lengW -1
            i = i-1
        elif j-weight[lengW] >= 0 and T[i-1][j-weight[lengW]] ==Wei - weight[lengW] :
            i = i-1
            j = j-weight[lengW]
            T = T[:i+1,:j+1]
            Wei = Wei - weight[lengW]
            a.append(weight[lengW])
            lengW = lengW -1
        else:
            lengW = lengW -1
    if len(a)>0:
        return [len(a)] + a 
    else:
        return a  
def Knapsac(W,w,items,T):
    c =[]
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
            if T[i][j] == W:
                b = getItem(T[:i+1][:j+1],W,w[:i],[])
                if len(b) > 0:
                    c.append(b)
    if len(c) >0:
        c = sorted(c,key = lambda x:x[0])
        return c[0][1:]
    else:
        return c
items = int(input())
w = list(map(int,input().split()))
total = sum(w)
if total % 3 != 0:
    print(0)
else:
    W = int(total/3)
    T = np.zeros((items+1,W+1),int)
    a = Knapsac(W,w,items,T)
    summation = 0 
    for k in a:
        summation = summation + k
        w.remove(k)
    if summation != W:
        print(0)
    else:
        items = items - len(a)
        T = np.zeros((items+1,W+1),int)
        b = Knapsac(W,w,items,T)
        summation = 0 
        for k in b:
            summation = summation + k
            w.remove(k)
        if summation != W or sum(w) != W:
            print(0)
        else:
            print(1)
