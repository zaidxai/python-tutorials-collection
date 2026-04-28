# Name Filtering and Factorial Calculation in Python
name=["Zaid", "Zain", "Wahab", "Aoun", "Zohaib"]
for i in name:
    if (i.startswith("Z")):
        print(f"Hello, {i}")

# factorial  of number 5 is = 1 x 2 x 3 x 4 x 5
n=int(input("Enter a number:"))
product=1
for i in range (1,n+1):
    product=product*i
print(f"The factorial of the {n} is {product}")