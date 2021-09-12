import math


a=0
x=float(input())

for i in range(10):
        a+= math.pow((x-1),i)/math.factorial(i)
print(a)
