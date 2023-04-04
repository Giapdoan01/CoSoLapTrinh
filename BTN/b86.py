ngay= ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
qua=['A Partridge in a Pear Tree','Two Turtle Doves','Three French Hens','Four Calling Birds','Five Golden Rings','Six Geese a Laying','Seven Swans a Swimming','Eight Maids a Milking','Nine Ladies Dancing','Ten Lords a Leaping','Eleven Pipers Piping','Twelve Drummers Drumming']
def l(n):
    i=n
    if i==n:
            print(f"On the {ngay[i]} day of christmas, my true love sent to me:")
            i=i+1
            for  j in range (i-1,-1,-1):
                if j==i-1:
                    print(qua[j],sep="",end="")
                if j<=i-3:
                    print(',',qua[j+1],end="")
                if j==0 and j!=i-1:
                    print(", And",qua[0],end="")
            print()
l(0)
l(1)
l(2)
l(3)
l(4)
l(5)
l(6)
l(7)
l(8)
l(9)
l(10)
l(11)