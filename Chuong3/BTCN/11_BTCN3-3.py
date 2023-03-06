x=float(input("x="))
y=float(input("y="))
ch=str(input('Phep toan:'))
if ch=="+" :
    print(x,"+",y,"=",x+y,sep="")
elif ch=="-":
    print(x,"-",y,"=",x-y,sep="")
elif ch=="*":
    print(x,"*",y,"=",x*y,sep="")
elif ch=="/" and y>0:
    c=x/y
    print(x,"/",y,"=",round(c,1),sep="")
else :
    print("khong hop le")
