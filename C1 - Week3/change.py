#Python3
#Fibonacci- week -3 - assign1
def MoneyChangeCount(n):
    count =0
    if n >= 10:
        count = count + int(n/10)
        n = n%10
    if n >=5:
        count = count + int(n/5)
        n = n%5
    count = count + n
    return count

n = int(input())
print(MoneyChangeCount(n))