a=int(input())
b=int(input())
c=int(input())
if (a+b)>c and (b+c)>a and (a+c)>b and a>0 and b>0 and c>0:
    if a==b and a!=c and b!=c:
        print("Tam giac can")
    elif a==b==c:
        print("Tam giac deu")
    elif a*a==b*b+c*c or b*b==c*c+a*a or c*c==b*b+a*a :
        print("Tam giac vuong")
    else :
        print("Tam giac loai khac")
else:
    print("Khong hop le")