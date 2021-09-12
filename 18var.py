import math


a=0
print('input n')
n=float(input())
print('input x')
x=float(input())

for i in range(n):
        a+= math.pow((x-1),i)/math.factorial(i)
print(a)

