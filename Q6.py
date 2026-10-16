student={
    "name":"Rahul",
    "course":"MCA",
    "semester":3,
    "marks":85
}

print("Dictionary : ",student)

print("Student Name : ",student["name"])
print("Course : ",student["course"])

print("Semester : ",student.get("semester"))
print("Marks : ",student.get("marks"))

student["marks"]=90
student["semester"]=4

print("Updated Dictionary : ",student)

print("Number of items : ",len(student))