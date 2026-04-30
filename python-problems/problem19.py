# Programmer Class Implementation in Python (OOP Basics)
class programmer:
    
    def __init__(self,name,salary,lang):
        self.name=name
        self.salary=salary
        self.lang=lang
    def getinfo(self):
        print(f"The name of programmer is {self.name}\nThe salary is {self.salary}\nWorking language is {self.lang}")
        
p1=programmer("Zaid",100000,"Python")
p1.getinfo()