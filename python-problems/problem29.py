# Program to calculate the area and perimeter of a rectangle

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)

print(f"The area of rectangle is: {area_rectangle:.2f}")
print(f"The perimeter of rectangle is: {perimeter_rectangle:.2f}")