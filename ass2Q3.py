# Create a tuple with repeated values
t = (10, 20, 30, 40, 20, 50, 60, 20, 70, 80)

# a) Display tuple and access elements
print("Tuple:", t)
print("Positive indexing:", t[2])
print("Negative indexing:", t[-1])
print("Slicing:", t[2:6])

# b) Concatenation and repetition
t2 = (90, 100)
print("Concatenation:", t + t2)
print("Repetition:", t * 2)

# c) Membership operations
print("20 in tuple:", 20 in t)
print("25 not in tuple:", 25 not in t)

# d) Maximum, minimum and length
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Length:", len(t))

# e) Count occurrences
value = int(input("Enter value to count: "))
print("Occurrences:", t.count(value))

# f) Search for an element
value = int(input("Enter value to search: "))

if value in t:
    print("Element found at index:", t.index(value))
else:
    print("Element not found")