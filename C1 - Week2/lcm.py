#Python3
#Fibonacci- week -2 - assign4
def euclidGCD(a,b):
    if b == 0:
        return a
    remainder = a%b
    return euclidGCD(b,remainder)

a,b = map(int,input().split())
gcd = 0
if a>=b:
   gcd = euclidGCD(a,b)
else:
   gcd = euclidGCD(b,a)
lcm = int((a*b)/gcd) 
print(lcm)