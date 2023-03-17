#  a
n=int(input("n="))
for i in range (1,n+1):
    print(i)
print()
#b
n=int(input("n="))
i=1
while i<=n:
        print(i,end=" ")
        i=i+1
        j=i
        while j%5==1:
            print() 
            j=j+1     
#c
n=int(input("n="))
if n>=1:
    j=1
    while j<=n:
        for i in range (1,n+1):
            print(i,end=" ")
        print()
        j=j+1