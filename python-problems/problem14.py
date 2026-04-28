# Functions and Recursion in Python: Greeting, Factorial, and Summation
def greet(user, ending="Thank You"):
    # user=input("Enter username:")
    print(f"Good Morning! " + user)
    print(ending)
    return user
a=greet("Zaid", "Thank you")
print(a)

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
number=int(input("Enter a number for factorial:"))
print(f"The factorial of {number} is: {factorial(number)}")

def sum(n):
    if n==1:
        return n
    return sum(n-1)+n
number=int(input("Enter a number for sum from 1 to that number:"))
print(f"The sum is: {sum(number)}")