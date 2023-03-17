while True:
    n = int(input())
    if n < 0:
         break
    u=1
    i=1    
    while i<=n:
        u=u*i
        i=i+1
    print(u)
# b
n=int(input())
while n>=0:
    i=1
    g=1
    if n>0:
        for i in range (1,n+1):
            g*=i
        print(g)
        n=int(input())
    elif n<0:
        break
    else:
        print('1')
        n=int(input())