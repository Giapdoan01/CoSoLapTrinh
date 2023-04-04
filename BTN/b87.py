def ba_canh_tam_giac():
    a=float(input())
    b=float(input())
    c=float(input())
    return a,b,c
def co_phai_tam_giac(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        s=1
    else:
        s=0
    return s
def inkq(s):
    if s==1:
        print('True')
    if s==0:
        print('False')
k,m,n=ba_canh_tam_giac()
s=co_phai_tam_giac(k,m,n)
inkq(s)