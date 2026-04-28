# Greatest Number Finder and Temperature Converter in Python
def greatest(n1,n2,n3,n4):
    if(n1>n2 and n1>n3 and n1>n4):
        return n1
    elif (n2>n1 and n2>n3 and n2>n4):
        return n2
    elif (n3>n1 and n3>n2 and n3>n4):
        return n3
    else:
        return n4
n1=int(input("Enter no1:"))
n2=int(input("Enter no2:"))
n3=int(input("Enter no3:"))
n4=int(input("Enter no4:"))
print(f"The greatest number among all the entered numbers is:{greatest(n1,n2,n3,n4)}")


def f_to_c(temp):
    return 5*(temp-32)/9
temp=int(input("Enter temprature in farenhite:"))
c=f_to_c(temp)
print("The temprature in celcius is:", round(c,2))