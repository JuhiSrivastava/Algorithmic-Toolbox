#Python3
#Fibonacci- week -2 - assign3
def euclidGCD(a,b):
    if b == 0:
        return a
    remainder = a%b
    return euclidGCD(b,remainder)

a,b = map(int,input().split())
if a>=b:
   print(euclidGCD(a,b))
else:
   print(euclidGCD(b,a))