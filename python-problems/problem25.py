# Program to calculate the surface area and volume of a sphere

import math

radius = float(input("Enter the radius of Sphere: "))

surface_area = 4 * math.pi * (radius ** 2)
volume = (4 / 3) * math.pi * (radius ** 3)

print(f"The surface area of sphere is: {surface_area:.2f}")
print(f"The volume of sphere is: {volume:.2f}")