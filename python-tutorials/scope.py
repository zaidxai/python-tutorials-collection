x = 10  # global variable
def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 4  # local variable
  print(y)
my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function



# single word name for this file
# Global Variable
f='Zaid Mehmood'
print(f)
def myfunction():
    # Global Variable
    # global f
    # print(f)
    # Local Variable
    f='I Love learning Python'
    print(f)
myfunction()
# Global Variable
print(f)

# Deletion of a variable
g=23
print(g)
del g
print(g)  # This will raise a NameError because g is deleted
