import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
if (a+b)>c and (b+c)>a and (a+c)>b:
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich=",round(s,3),sep="")
else:
    print("Khong hop le")