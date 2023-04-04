n=int(input('nhap so muong ca phe='))
a=48
b=3
def quy_doi():   
    c=n//a
    d=n-a*c
    f=d//b
    h=d-b*f
    print(c,"cốc")
    print(f,'muỗng canh')
    print(h,'muỗng cà phê')
quy_doi()