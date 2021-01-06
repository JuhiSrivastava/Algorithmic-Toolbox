#Python3
#week -4 - assign2
def Partition3(array,pivot,low,high):
    index1 = low
    index2 = low
    for i in range(low+1,len(array)):
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
def FindMajor(array,low,high,n):
    pivot = array[low]
    index1,index2 = Partition3(array,pivot,low,high)
    if (index2 - index1 + 1) > int(n/2):
        return 1
    elif index1 - low > int(n/2):
        return FindMajor(array[low : index1],0,index1 - low,n)
    elif high - index2 > int(n/2):
        return FindMajor(array[index2+1 : high+1],0,high - index2,n)
    else:
        return 0
n = int(input())
array = list(map(int, input().split()))
print(FindMajor(array,0,n-1,n))
