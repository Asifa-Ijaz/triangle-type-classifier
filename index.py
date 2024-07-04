side1 = float(input("Enter the length of side1: "))
side2 = float(input("Enter the length of side2: "))
side3 = float(input("Enter the length of side3: "))

if side1 == side2 ==side3:
    print("This is Equilateral triangle")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("This is Isosceles triangle")

else: 
    print("This is Scalene triangle")