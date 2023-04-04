n=int(input())
a=0
if n>0 and n<=10**6:
    for i in range(1,n+1):
        if i%5==0 and i%3==0:
            a=a+1
    print(a)