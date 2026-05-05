# Implementing Complex Numbers with Magic Methods in Python
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return Complex(self.r+c2.r , self.i+c2.i)
    def __mul__(self,c2):
        return Complex(self.r*c2.r , self.i*c2.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1=Complex(2,3)
c2=Complex(4,6)
print(c1+c2)
print(c1*c2)