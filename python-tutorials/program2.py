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
