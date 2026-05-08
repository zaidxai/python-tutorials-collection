# Program to calculate the area of a triangle using Heron's Formula

import math

a = float(input("Enter side a of triangle: "))
b = float(input("Enter side b of triangle: "))
c = float(input("Enter side c of triangle: "))

# Check if valid triangle
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area_of_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"The area of triangle is: {area_of_triangle:.3f}")
else:
    print("Invalid triangle sides!")