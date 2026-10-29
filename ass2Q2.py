# Create list1 containing names of five students
list1 = ["Rahul","Anjli","Anvita","Rohit","Priya"]

# Create list2 containing student names and marks
list2 = [
    ["Rahul", 98],
    ["Anjili", 87],
    ["Anvita", 84],
    ["Rohit", 71],
    ["Priya", 78]
]

print("Original Student List:", list1)

name = input("Enter student name to search: ")

if name in list1:
    print("Student found at index:", list1.index(name))
else:
    print("Student name not found in the list.")

# (b) Sort names in ascending and descending order
list1.sort()
print("Ascending Order using sort():", list1)

list1.sort(reverse=True)
print("Descending Order using sort():", list1)

print("Ascending Order using sorted():", sorted(list1))
print("Descending Order using sorted():", sorted(list1, reverse=True))

# (c) Add, insert, and remove student names
list1.append("Sakshi")
print("After adding : ", list1)
list1.insert(3,'Leela')
print("After inserting : ", list1)


list1.remove('Sakshi')
print("After removing : ", list1)


# (d) Display all student records using a loop
print("\nAll Student Records:")
for student in list2:
    print("Name:", student[0], "| Marks:", student[1])
# (e) Find student with highest marks and calculate average
highest = max(student[1] for student in list2)

for student in list2:
    if student[1] == highest:
        print("Student with highest marks:", student[0])
        print("Highest marks:", highest)

# Calculate average marks
total = sum(student[1] for student in list2)
average = total / len(list2)

print("Average marks:", average)

# (f) Display number of student records
print("\nNumber of Student Records:", len(list2))
