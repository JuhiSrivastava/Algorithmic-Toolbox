#Python3
#Fibonacci- week -3 - assign6
n = int(input())
a = []
summation = 0
i = 1
while summation != n:
    if summation + i == n or (summation + i <= n and n- summation - i > i):
        a.append(i)
        summation = summation +i
    i = i+1
print(len(a))
p=""
for i in range(len(a) -1):
    p = p + str(a[i]) + " "
p = p + str(a[len(a) -1])
print(p)