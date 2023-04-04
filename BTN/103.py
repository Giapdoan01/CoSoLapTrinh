def Ngay_Ky_Dieu():
    for year in range(1901,2000):
        Year=year%100
        for month in range(1,8):
            if year%4==0 and month==2:
                for day in range(1,30):
                    if day*month==Year:
                        print(f'Ngay ky dieu: {day}/{month}/{year}')
            elif month==2:
                for day in range(1,29):
                    if day*month==Year:
                        print(f'Ngay ky dieu: {day}/{month}/{year}')
            elif month!=2 and month%2==0:
                for day in range(1,31):
                    if day*month==Year:
                        print(f'Ngay ky dieu: {day}/{month}/{year}')
            elif month!=2 and month%2!=0 :
                for day in range(1,32):
                    if day*month==Year:
                        print(f'Ngay ky dieu: {day}/{month}/{year}')
        for month in range(8,13):
            if month%2==0:
                for day in range(1,32):
                    if day*month==Year:
                        print(f'Ngay ky dieu: {day}/{month}/{year}')
            if month%2!=0:
                for day in range(1,31):
                    if day*month==Year:
                        print(f'Ngay ky dieu: {day}/{month}/{year}')
Ngay_Ky_Dieu()

