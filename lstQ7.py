nums=[0,1,0,3,12]
result=[]
for num in nums:
    if num!=0:
        result.append(num)
for n in nums:
    if n==0:
        result.append(n)
print(result)