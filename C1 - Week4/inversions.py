#Python3
#week -4 - assign4
def Merge(A,B,count):
    arr =[]
    while len(A)>0 and len(B)>0:
        if A[0]<=B[0]:
            arr.append(A[0])
            A.remove(A[0])
        elif A[0] > B[0]:
            arr.append(B[0])
            count = count +len(A)
            B.remove(B[0])
    if len(A) > 0:
        for i in range(len(A)):
            arr.append(A[i])
    if len(B) > 0:
        for i in range(len(B)):
            arr.append(B[i])
    return arr,count   
            
def MergeSort(array,count):
    if len(array) == 1: 
        return array,count        
    mid = int(len(array)/2)
    A,count = MergeSort(array[:mid],count)
    B,count = MergeSort(array[mid:],count)
    return Merge(A,B,count)
n = int(input())
array = list(map(int, input().split()))
count = 0
array,count = MergeSort(array,count)
print(count)