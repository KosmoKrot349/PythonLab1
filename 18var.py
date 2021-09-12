import math

def fact(n):
        factor=1;
        for i in range(1,n+1):
                factor*=i
        return factor

try:
        a=0
        print('input n')
        n=int(input())
        print('input x')
        x=float(input())

        for i in range(n):
                a+= math.pow((x-1),i)/fact(i)
        print(a)
except ValueError:
        print("some error")


