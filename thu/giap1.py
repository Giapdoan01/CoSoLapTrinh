# def Nhap ():
#     print("Nhap mot so nguyen:")
#     n=int (input("n="))
#     return n
# def Tinh(n):
#     S= 0
#     for x in range (1,n+1):
#         S=S+x
#     return S
# def InKQ(n,S):
#     print ("Tong cua ",n," so nguyen duong dau tien=" ,S,sep="")

# n=Nhap()
# S=Tinh(n)
# InKQ(n,S)
def nhap():
    n=int(input())
    print('Nhap',n,"so nguyen:")
    return n

def NhapvaDem(n):
    s=0
    i=1
    while i<=n:
        a=int(input())
        i=i+1
        if a%2==0 and a!=0:
            s=s+1
    return s
def inkq(s):
    print('So chu so chan la:',s)

n=nhap()
s=NhapvaDem(n)
inkq(s)


