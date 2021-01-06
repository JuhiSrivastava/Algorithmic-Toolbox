#Python3
#Fibonacci- week -3 - assign5

def checkCoverage(n,segments):
    c = []
    while len(segments) > 0:
        c.append(int(segments[0][1]))
        a=[]
        for i in range(len(segments)):
            if segments[0][1] >= segments[i][0] and segments[0][1] <= segments[i][1]:
                a.append(i)
        segments = np.delete(segments,a,0)
    print(len(c))
    p=""
    for i in range(len(c) -1):
        p = p + str(c[i]) + " "
    p = p + str(c[len(c) -1])
    print(p)
import numpy as np
n = int(input())
segments = np.zeros((n,2))
for i in range(n):
    segments[i][0], segments[i][1] = map(int,input().split())
segments = sorted(segments, key=lambda x : x[1])
checkCoverage(n,segments)