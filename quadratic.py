import math

a = float(input("Enter the 1st value: "))
b = float(input("Enter the 2nd value: "))
c = float(input("Enter the 3rd value: "))
d = (b**2 - 4*a*c)
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("The root1 value is:", r1)
    print("The root2 value is:", r2)
elif d == 0:
    r1 = -b / (2*a)
    print("One real solution is:", r1)
else:
    print("No real solution")
