#Python3
#week -5 - assign2
n = int(input())
a =[0,0,1,1]
b = [0,0,1,1]
for i in range(4,n+1):
    operations = 0
    value =i
    while value%2 != 0 and value%3 != 0:
        operations = operations +1
        value = value -1
    if value%2 == 0 and value%3 == 0:
        if a[int(value/2)] < a[int(value/3)]:
            a.append(a[int(value/2)] + operations + 1)
            b.append(int(value/2))
        else:
            a.append(a[int(value/3)] + operations + 1)
            b.append(int(value/3))
    elif value%2 == 0:
        if a[int(value/2)] <= a[value -1] :
            a.append(a[int(value/2)] + operations + 1)
            b.append(int(value/2))
        else:
            a.append(a[value-1] + operations + 1)
            b.append(value-1)
    else:
        if a[int(value/3)] <= a[value -1] :
             a.append(a[int(value/3)] + operations + 1)  
             b.append(int(value/3))
        else:
            a.append(a[value-1] + operations + 1)
            b.append(value-1)
       
value = ""
j = len(b)-1
i = len(a)-1
while j !=0:
    if j == 1:
        value = str(i) + " " + value
        break
    else:
        for k in range(a[i] - a[b[j]]):
            if value == "":
                value = str(i)
            else:
                value = str(i) + " " + value
            i = i-1
        i = b[j]
        j = i
print(a[n])
print(value)