def so_thanh_thutu(num):
    if num < 1 or num > 12:
        return ""
    elif num == 1:
        s="first"
        return s
    elif num == 2:
        s="second"
        return s
    elif num == 3:
        s="third"
        return s
    elif num==4:
        s='fourth'
        return s
    elif num==5:
        s='fifth'
        return s
    elif num==6:
        s='sixth'
        return s
    elif num==7:
        s='seventh'
        return s
    elif num==8:
        s='eightth'
        return s
    elif num==9:
        s='ninth'
        return s
    elif num==10:
        s='tenth'
        return s
    elif num==11:
        s='eleventh'
        return s
    elif num==12:
        s='twelfth'
        return s
def inkq(s):
    print(s)
a=so_thanh_thutu(12)
inkq(a)