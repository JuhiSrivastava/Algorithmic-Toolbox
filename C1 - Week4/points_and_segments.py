#Python3
#week -4 - assign5
s,p = map(int, input().split())
a=[]
dictionary = {}
for i in range(s):
    b,c = map(int,input().split())
    a.append([b,'l'])
    a.append([c,'r'])
points = list(map(int,input().split()))
for i in points:
    a.append([i,'p'])
    dictionary[i] = 0
a.sort(key=lambda x: (x[0],x[1]))
value =""
seg = 0
for i in a:
    if i[1] == 'l':
        seg= seg +1
    if i[1] == 'r':
        seg = seg -1
    if i[1] == 'p':
        if dictionary[i[0]] == 0:
                dictionary[i[0]] += seg
for i in range(len(points)):
    if i != len(points) -1:
        value += str(dictionary[points[i]]) + " "
    else:
        value += str(dictionary[points[i]])
print(value)