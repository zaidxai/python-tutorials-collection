# There are four types of arguments:
#    Default arguments, Keyword arguments, Variable length arguments, Required arguments
def average(a,b):
    # a abd b are required arguments
    print("The average is:", (a+b)/2)
average(4,7)

def average(a=3,b=9):
    # a abd b are default arguments
    print("The average is:", (a+b)/2)
average(b=7)

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(7,8,9,1)
print(c)

def name(**name):
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="Zaid", lname="Mehmood", fname="Rao")
