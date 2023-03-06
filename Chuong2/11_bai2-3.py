yrs0fService = int(input("yrs0fService="))
salary = int(input("salary="))
bonus = 0
if yrs0fService < 5:
     if salary < 500:
         bonus = 100
     else:
         bonus = 200
else:
    bonus = 700
print ("Bonus amount: ", bonus)
