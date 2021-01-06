#Python3
#week -5 - assign4
import numpy as np
def Distance(A,B,n,m):
    c= np.zeros((n,m),int)
    for i in range(1,n):
        for j in range(1,m):
            if A[i] == B[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    return c[n-1][m-1]
n = int(input())
A = list(map(int,input().split()))
A = [" "] + A
m = int(input())
B = list(map(int,input().split()))
B = [" "] + B
n=n+1
m=m+1
print(Distance(A,B,n,m))