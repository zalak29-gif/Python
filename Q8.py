print("Percentage Calculation")
marks1=int(input("Enter marks of subject 1 : "))
marks2=int(input("Enter marks of subject 2 : "))
marks3=int(input("Enter marks of subject 3 : "))

total_marks=marks1+marks2+marks3
percentage=total_marks/3

if percentage>=90:
    grade="O"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B"
elif percentage>=60:
    grade="C"
elif percentage>=50:
    grade="D"
elif percentage>=40:
    grade="E"
else:
    grade="F"

print("="*25)
print("Subject 1 : ",marks1)
print("Subject 2 : ",marks2)
print("Subject 3 : ",marks3)
print("Total Marks : ",total_marks)
print("Percentage : {:.2f}%".format(percentage))
print("Grade : ",grade)
print("="*25)