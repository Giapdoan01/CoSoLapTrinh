def tim_uoc_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("a="))
b = int(input("b="))

ucln = tim_uoc_chung_lon_nhat(a, b)
m=(a/ucln)
n=(b/ucln)
print(round(m),'/',round(n),sep='')