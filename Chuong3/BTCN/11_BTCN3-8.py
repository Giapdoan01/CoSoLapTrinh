n=input()
i=int(input())
s=str(" ")
if 1<=i<=20:
    for a in range(1,i+1):
        print(a*(n+s),end=" ",sep="")
        print()
