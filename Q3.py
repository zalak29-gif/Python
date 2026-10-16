basic_salary=float(input("Enter salary : "))
years=int(input("Enter years of service : "))
if years<=2:
    bonus=basic_salary*5/100
elif years<=5:
    bonus=basic_salary*10/100
elif years<=10:
    bonus=basic_salary*15/100
else:
    bonus=basic_salary*20/100
gross_salary=basic_salary+bonus
print("Basic Salary : ",basic_salary)
print("Bonus : ",bonus)
print("Gross Salary : ",gross_salary)