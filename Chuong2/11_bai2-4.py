a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
S=(a+b+c)/2
import math
S1=math.sqrt(S*(S-a)*(S-b)*(S-c))
print("dien tich=",S1)