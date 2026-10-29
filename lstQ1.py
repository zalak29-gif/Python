lst=[10,20,10,30,20,40,30]
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print("Original List : ",lst)
print("List after removing duplicates : ",new_lst)