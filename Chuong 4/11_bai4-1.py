def nhap():
    n=int(input("n="))
    return n
def giaithua(n):
    s=1
    if n!=0:
        for i in range (1,n+1):
            s=s*i
    else:
        s=1
    return s
def inkq(s):
    print(n,'!=',s,sep='')

n= nhap()
s= giaithua(n)
inkq(s)