#Python3
#week -4 - assign1
def BinarySearch(n,value, low, high):
    mid = low + int((high - low)/2)
    if high < low:
        return -1
    if n[mid] == value:
        return mid
    elif n[mid] > value:
        return BinarySearch(n,value, low, mid-1)
    else:
        return BinarySearch(n,value, mid+1, high)
n = list(map(int, input().split()))
key = list(map(int, input().split()))
nlen = n[0]
n.remove(n[0])
keylen = key[0]
key.remove(key[0])
value = ""
for i in range(keylen):
    if i < keylen -1:
        value = value + str(BinarySearch(n,key[i], 0, nlen-1)) + " "
    else:
        value = value + str(BinarySearch(n,key[i], 0, nlen-1))
print(value)