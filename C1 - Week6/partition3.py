#Python3
#week -6 - assign2
import numpy as np
def Knapsac(w, W, partial,partialind,comb,items):
    outputNum = sum(partial)
    if outputNum == W: 
        comb += [partialind]
    if outputNum >= W:
        return
    for i in range(len(w)):
        n = w[i]
        index = items - len(w) + i
        left = w[i+1:]
        Knapsac(left, W, partial + [n],partialind + [index],comb,items)
    return comb

def CheckComb(c,items):
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            for k in range(j+1,len(c)):
                if len(c[i]) + len(c[j])+ len(c[k]) == items:
                    if len(list(set(c[i]).intersection(c[j]))) == 0 and len(list(set(c[j]).intersection(c[k]))) == 0:
                        return 1
    return 0

items = int(input())
w = list(map(int,input().split()))
total = sum(w)
if total % 3 != 0:
    print(0)
else:
    W = int(total/3)
    T = np.zeros((items+1,W+1),int)
    c = Knapsac(w,W,[],[],[],items)
    print(CheckComb(c,items))