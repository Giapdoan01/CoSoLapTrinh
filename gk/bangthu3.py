a=int(input())
b=int(input())
n=int(input())
if (a and b and n)>=1 and (a and b and n)<10**9:
    if  a+b==n:
        print("+")
    elif a-b==n:
        print("-")
    elif a*b==n:
        print("*")
    elif a/b==n:
        print("/")
    else :
        print("NO")
