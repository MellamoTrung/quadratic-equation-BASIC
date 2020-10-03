# put your python code here
from math import sqrt
print("ax^2+bx+c=0")
print("Enter a,b,c:")
a = float(input())
b = float(input())
c = float(input())
d = b*b - 4*a*c

if d == 0:
    print((-b)/(2*a))
elif d > 0:
    x1 = ((-b) -sqrt(d)) / (2*a)
    x2 = ((-b) + sqrt(d)) / (2*a)
    print("%f %f" %(min(x1,x2),max(x1,x2)))
else:
    print("No real roots")
