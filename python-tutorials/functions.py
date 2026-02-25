# Python Functions: Basics & Operations

# 1. Function definition and calling
def greet():
    print("Hello! Welcome to Python functions.")

greet()  # Calling the function

# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Zaid")

# 3. Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum of 5 and 3:", result)

# 4. Function with default arguments
def power(base, exponent=2):
    return base ** exponent

print("5 squared:", power(5))
print("2 cubed:", power(2, 3))

# 5. Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=22, name="Zaid")  # Using keyword arguments

# 6. Function with variable-length arguments (*args and **kwargs)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nUser info:")
print_info(name="Zaid", age=22, major="CS")

# 7. Nested functions
def outer():
    print("\nThis is the outer function.")
    def inner():
        print("This is the inner function.")
    inner()

outer()

# 8. Lambda (anonymous) functions
square = lambda x: x**2
print("\nSquare of 5 using lambda:", square(5))

# 9. Recursion example (factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 10. Returning multiple values
def arithmetic(a, b):
    return a + b, a - b, a * b, a / b

sum_val, diff, prod, div = arithmetic(10, 5)
print("\nArithmetic operations on 10 and 5:")
print("Sum:", sum_val, "Difference:", diff, "Product:", prod, "Division:", div)