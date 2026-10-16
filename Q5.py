languages=("C++","Java","PHP")

languages=("React",)+languages+("Java",)
print("After adding elements in tuple : ",languages)

if"React" in languages:
    print("React is present in the tuple")

print("Length of tuple : ",len(languages))

print("First item of the tuple : ",languages[0])
print("Second item of the tuple : ",languages[1])
print("Last item of the tuple : ",languages[-1])