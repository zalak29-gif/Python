# gross salary
basic_salary = float(input("Enter salary : "))
if basic_salary <= 10000:
    hra = basic_salary*20/100
    da = basic_salary*80/100
elif basic_salary <= 20000:
    hra = basic_salary*25/100
    da = basic_salary*90/100
else:
    hra = basic_salary*30/100
    da = basic_salary*95/100

    gross_salary = basic_salary+hra+da
    print("Hra : ",hra)
    print("Da : ",da)
    print("Gross salary : ",gross_salary)
