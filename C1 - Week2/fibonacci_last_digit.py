#Python3
#Fibonacci- week -2 - assign2
def fib(n):
    fibonacci = [0,1]
    for i in range(int(n)-1):
        fibonacci.append((fibonacci[i] + fibonacci[i+1])%10)
    return fibonacci[int(n)]
n = input()
print(fib(n))

