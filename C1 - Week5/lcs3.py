#Python3
#week -5 - assign5
import numpy as np
def Distance(A,B,C,n,m,p):
    c= np.zeros((n,m,p),int) 
    for i in range(1,n):
        for j in range(1,m):
            for k in range(1,p):
                if A[i] == B[j] and B[j] == C[k]:
                    c[i][j][k] = c[i-1][j-1][k-1] + 1
                else:
                    c[i][j][k] = max(c[i-1][j][k],c[i][j-1][k],c[i-1][j][k-1],c[i][j-1][k-1],c[i][j][k-1])
    return max(c[n-1][m-1][k],c[n-1][m-1][k-1])
n = int(input())
A = list(map(int,input().split()))
A = [" "] + A
m = int(input())
B = list(map(int,input().split()))
B = [" "] + B
p = int(input())
C = list(map(int,input().split()))
C = [" "] + C
n=n+1
m=m+1
p = p+1
print(Distance(A,B,C,n,m,p))