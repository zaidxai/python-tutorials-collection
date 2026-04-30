# Python Class and Object Demonstration with Constructor and Methods
class Employee:
    lang="Python" #class attribute
    salary=1200000 #class attribute
    
    #constructor
    def __init__(self,name,salary,lang): #dunder method and init is called automatically whenever an object is created
        self.name=name
        self.salary=salary
        self.lang=lang
        print("Init is called!")

    #method
    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}.")
    
    @staticmethod #there is no use of object in this method so we are not passing any argument to it, thus used @staticmethod
    def greet():
        print("Good Morning!")
        
zaid=Employee("Zaid", 1200000, "Python")

# zaid.name="Zaid" #instance attribute
print(zaid.name,zaid.lang,zaid.salary)
zaid.greet()

aoun=Employee()
aoun.name="Aoun" #instance attribute
aoun.lang="Javascript" #instance  attributes take precedence over class attributes
print(aoun.name,aoun.lang,aoun.salary)
aoun.getinfo()
# or it can be weitten as Employee.getinfo(aoun)

wahab=Employee("Wahab", 1000000, "C++")
print(wahab.name,wahab.salary,wahab.lang)