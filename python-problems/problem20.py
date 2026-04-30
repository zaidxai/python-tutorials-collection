# Inheritance and Method Overriding in Python (2D & 3D Vectors + Animal Hierarchy)
class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
        
obj1=TwoDvector(1,2)
obj1.show()

obj2=ThreeDvector(3,4,5)
obj2.show()


class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Wow Wow!")
        
d=Dogs()
d.bark()