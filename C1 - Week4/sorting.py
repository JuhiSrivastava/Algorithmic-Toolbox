#Python3
#week -4 - assign3
def Partition3(array,pivot,low,high):
    index1 = low
    index2 = low
    for i in range(low+1,high +1):
        if array[i] < pivot:
            temp = array[i]
            array[i]= array[index2+1]
            array[index2+1] = array[index1]
            array[index1] = temp
            index2 = index2 +1
            index1 = index1 +1
        elif array[i] == pivot:
            temp = array[i]
            array[i]= array[index2 +1]
            array[index2+1] = temp
            index2 = index2 +1
    return index1,index2 
def Sorting(array,low,high):
    pivot = array[low]
    index1,index2 = Partition3(array,pivot,low,high)
    if index1-low > 1:
        Sorting(array,low,index1 - 1)
    if high-index2 >1:
        Sorting(array,index2+1,high)
n = int(input())
array = list(map(int, input().split()))
Sorting(array,0,n-1)
value = ""
for i in range(n):
    if i < n-1:
        value = value + str(array[i]) + " "
    else:
        value = value + str(array[i])
print(value)