number=list(range(1,11))
#a) Display the list and access its elements using positive indexing, negative indexing,and slicing.
print("list : ",number)
print("positive indexing : ",number[1])
print("negative indexing : ",number[-1])
print("slicing : ",number[2:5])

#b) Update an element at a specified index entered by the user.
index=int(input("Enter index to update (0-9) : "))
if 0 <= index < len(number):
    value = int(input("Enter new value: "))
    number[index] = value
    print("Updated List:", number)
else:
    print("Invalid index!")

#c) Perform list concatenation using + and repetition using *.

print("Concation using + : ", number + [7,9])
print("Repitation using * : ", number * 5) 

#d) Check whether a number exists in the list using in and not in.


num = int(input("Enter number for search : "))
print("Number exits : ", num in number)
print("Number does not exist : ", num not in number)

#e) Perform the following list methods: append(), insert(), remove(), pop(), reverse(), and count().

number.append(20)
print("After append(20) : ", number)

number.insert(7,67)
print("After insert(7,67) : ", number)


number.remove(67)
print("After remove(67) : ", number)

removed=number.pop()
print("Popped element : ", removed)
print("After pop : ", number)

number.reverse()
print("After reverse() : ", number)

count_n = int(input("Enter number for counting : "))
print("Count of ", count_n,":",number.count(count_n))
#f) Display the list in ascending and descending order using sort() and sorted().

number.sort()
print("ascending order using sort() : ",number)
number.sort(reverse=True)
print("Descending order using sort() : ",number)


print("ascending order using sorted() : ",sorted(number))
print("descending order using sort() : ",sorted(number,reverse=True))
#g) Create an alias and a clone of the list, modify one element, and demonstrate the difference between aliasing and cloning.

alias = number
clone = number.copy()

alias[0]=10
print("after modifying alias :")
print("original list : ",number)
print("alias list : ",alias)
print("clone list : ",clone)

#h) Display the maximum, minimum, and length of the list using max(), min(), and len().

print("maximun : ",max(number))
print("minimun : ",min(number))
print("length : ",len(number))