#Python3
#Fibonacci- week -2 - assign1
def fib(n):
    fibonacci = [0,1]
    for i in range(int(n)-1):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return fibonacci[int(n)]
n = input()
print(fib(n))
