a=int(input("Nhap hai canh ke cua tam giac vuong:"))
b=int(input())
import math
n=a*a+b*b
x=math.sqrt(n)
print("canh ke thu nhat la: " + str(a) + ", canh ke thu hai: " + str(10) + ", co canh huyen: " + str(round(x,2)))