#Python3
#week -5 - assign5
import numpy as np
def Distance(A,B,n,m):
    c= np.zeros((n,m),int) 
    for i in range(1,n):
        for j in range(1,m):
            if A[i] == B[j]:
                c[i][j] = max(c[i-1][j-1],c[i-1][j],c[i][j-1]) + 1
            else:
                c[i][j] = max(c[i-1][j-1],c[i-1][j],c[i][j-1])
    a = '''  value = c[n-1][m-1]
    i=n-1
    j=m-1
    lis = []
    while value!=0:
        if max(c[i-1][j-1],c[i-1][j],c[i][j-1]) == value-1:
            lis = [A[i]] + lis
            value = value -1
        if c[i-1][j-1] >= c[i-1][j] and c[i-1][j-1] >=c[i][j-1]:
            i = i-1
            j=j-1
        elif c[i-1][j]>=c[i][j-1]:
            i = i-1
        else:
            j=j-1
    print(lis)'''
    return c[n-1][m-1]
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
print(min(Distance(A,B,n,m),Distance(B,C,m,p),Distance(C,A,p,n)))


#fsffvfdsbbdfvvdavavavavavav
#565535462245334131313131313 27
#fvdaabavvvvvadvdvavavadfsfsdafvvav
#5341121333331434313131456564153313 34
#f vdb vvd vavavavav
#f vdb vvd vavavavav
#16
#a b v d f s
#1 2 3 4 5 6
