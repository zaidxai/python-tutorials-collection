# Python Conditions: Basics & Operations

# 1. Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")

# 2. if-else statement
num = 7
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# 3. if-elif-else ladder
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Nested if statements
num = 15
if num > 0:
    print("Positive number")
    if num % 5 == 0:
        print(f"{num} is divisible by 5")
    else:
        print(f"{num} is not divisible by 5")
else:
    print("Non-positive number")

# 5. Multiple conditions using logical operators
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are True")
if x > 5 or y < 15:
    print("At least one condition is True")
if not x < 5:
    print("Negation example: x is not less than 5")

# 6. Conditional (ternary) operator
a, b = 10, 20
max_val = a if a > b else b
print(f"Maximum value between {a} and {b} is {max_val}")

# 7. Membership test in conditions
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list of fruits")
if "orange" not in fruits:
    print("Orange is not in the list of fruits")

# 8. Identity test
x = [1, 2, 3]
y = x
z = [1, 2, 3]
if x is y:
    print("x and y refer to the same object")
if x is not z:
    print("x and z do not refer to the same object")