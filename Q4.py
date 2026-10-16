languages = ["Python", "JavaScript", "Java", "C++"]
print("Original List : ",languages)

languages.insert(1,"C")
print("After insert() : ",languages)

languages.remove("C++")
print("After remove() : ",languages)

languages.append("C#")
print("After append() : ",languages)

print("Length of list : ",len(languages))

languages.pop()
print("After pop() : ",languages)

del languages[1]
print("After delete (del) : ",languages)

languages.clear()
print("After clear() : ",languages)