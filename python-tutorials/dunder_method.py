class Employee:
    name="Zaid"
    def __len__(self):
        return len(self.name)
e=Employee
print(e.name)
print(len(e.name))
    

# from emp import Employee

# e = Employee("Harry")
# print(str(e))
# print(repr(e))
# print(e.name)
# print(len(e))
# e()