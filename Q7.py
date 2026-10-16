def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b 
def division(a,b):
    return a / b

print("----Menu----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice : "))
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))  

if choice==1:
    print("Addition = ",addition(num1,num2))
elif choice==2:
    print("Subtraction = ",subtraction(num1,num2))
elif choice==3:
    print("Multiplication = ",multiplication(num1,num2))
elif choice==4:
    if(num2!=0):
        print("Division = ",division(num1,num2))
    else:
        print("Division by zero is not allowed")    
else:
    print("Invalid choice")