numbers=[1,2,3,4,5]
n=2
while n>0:
    last = numbers.pop()
    numbers.insert(0, last)
    n = n - 1
print(numbers)