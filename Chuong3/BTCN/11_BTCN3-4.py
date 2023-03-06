t=int(input())
l=int(input())
h=int(input())
tb=((t*2)+(l*3)+h)/6
if tb<3:
    print("Kém")
elif 3<=tb<5:
    print("Yếu")
elif 5<=tb<6:
    print("Trung bình")
elif 6<=tb<7:
    print("Trung bình khá")
elif 7<=tb<8:
    print("Khá")
elif 8<=tb<9:
    print("Giỏi")
else:
    print("Xuất sắc")