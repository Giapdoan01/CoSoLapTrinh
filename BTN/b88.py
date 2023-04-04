a=int(input('số khoảng trắng cần thêm vào='))
b=str(input('chuỗi ban đầu='))
c=' '
def can_chinh():
        d=a//2
        e=a-d
        print('|'+str(d*c)+b+str(e*c)+'|')
ketqua=can_chinh()
