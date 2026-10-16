print("---MENU---")
print("1. Area of Circle")
print("2. Area of Triangle")
print("3. Area of Square") 
print("4. Area of Rectangle") 
print("5. Simple Interest")

choice = int(input("Enter the choice : "))

if choice==1:
    radius= float(input("Enter radius of circle : "))
    area= 3.14*radius*radius
    print("Area of circle : ",area)
elif choice==2:
    base=float(input("Enter base of triangle : "))
    height=float(input("Enter height of triangle : "))
    area=0.5*base*height
    print("Area of triangle : ",area)
elif choice==3:
    side=float(input("Enter side of square : "))
    area=side*side
    print("Area of square : ",area)
elif choice==4:
    length=float(input("Enter length of rectangle : "))
    breadth=float(input("Enter breadth of rectangle : "))
    area=length*breadth
    print("Area of rectangle : ",area)
elif choice==5:
    principal=float(input("Enter principal amout : "))
    rate=float(input("Enter rate of interest : "))
    time=float(input("Enter time in years : ")) 
    si=(principal*rate*time)/100
    print("Simple Interest : ",si)
else:
    print("Invalid choice")