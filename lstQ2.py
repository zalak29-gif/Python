lst=list(range(1,10))
print("Original list : ",lst)
for i in lst[:]:
    if i%2!=0:
        lst.remove(i)
        print("Final list :")
