#Python3
#week -5 - assign1
n = int(input())
a =[0]
for i in range(1,n+1):
    if i ==1 or i ==3 or i ==4:
        a.append(1)
    elif i-4 > 0:
        a.append(min(a[i-1],a[i-3], a[i-4]) +1)
    else:
        a.append(a[i-1] +1)
print(a[n])