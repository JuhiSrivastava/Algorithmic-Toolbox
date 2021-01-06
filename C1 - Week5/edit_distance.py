#Python3
#week -5 - assign3
import numpy as np
def Distance(A,B):
    c= np.zeros((len(A),len(B)),int)
    for i in range(len(A)):
        c[i][0] = i
    for i in range(len(B)):
        c[0][i] = i
    for i in range(1,len(A)):
        for j in range(1,len(B)):
            if A[i] != B[j]:
                c[i][j] = min(c[i-1][j-1],c[i-1][j],c[i][j-1]) + 1
            else:
                c[i][j] = min(c[i-1][j-1],c[i-1][j]+1,c[i][j-1]+1)  
    return c[len(A)-1][len(B)-1]
string1 = " " +input()
string2 = " " +input()
A = [char for char in string1]
B = [char for char in string2]
print(Distance(A,B))