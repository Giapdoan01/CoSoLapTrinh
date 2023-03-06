n=int(input("n="))
S=1
if 0<= n <=100:
    for i in range(1,n+1):
        S=S*i 
print(n,"!=",S,sep="")
