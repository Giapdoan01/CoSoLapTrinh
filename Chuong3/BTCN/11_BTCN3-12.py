n=int(input())
m=list(str(n))
if 0<=n<=9999:
    for i in range(0,len(m)):
        p=m[i]
        if p=="0":
            print("A",end="")
        if p=="1":
            print("B",end="")
        if p=="2":
            print("C",end="")
        if p=="3":
            print("D",end="")
        if p=="4":
            print("E",end="")
        if p=="5":
            print("F",end="")
        if p=="6":
            print("G",end="")
        if p=="7":
            print("H",end="")
        if p=="8":
            print("K",end="")
        if p=="9":
            print("L",end="")