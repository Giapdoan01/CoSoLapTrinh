m1=int(input("M1="))
m2=int(input("M2="))
m3=int(input("M3="))
s=int(input("s="))
if 0<=s<=100:
    c=s*m1
    print("Phải tra=",c,sep="")
elif 101<=s<=150:
    c=(100*m1)+(s-100)*m2
    print("Phai tra=",c,sep="")
else:
    c=(100*m1)+(50*m2)+(s-150)*m3
    print("Phai tra=",c,sep="")