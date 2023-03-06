while True:
 a=int(input("a="))
 b=int(input("b="))
 c=input("toan tu=")
 if c=="+":
        print(a,"+",b,"=",a+b,sep="")
        d=str(input("tiep tuc:"))
 elif c=="-":
        print(a,"-",b,"=",a-b,sep="")
        d=str(input("tiep tuc:"))
 elif c=="/" and b!=0:
        print(a,"/",b,"=",a/b,sep="")
        d=str(input("tiep tuc:"))
 elif c=="*":
        print(a,"*",b,"=",a*b,sep="")
        d=str(input("tiep tuc:"))
 if d=="t" or d=="T":
      continue
 elif d=="x":
            break
