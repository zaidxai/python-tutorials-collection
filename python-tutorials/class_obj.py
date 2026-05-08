# Self means the object on which method being called!
class Person:
    name="Zaid"
    occupation="Software Engineer"
    salary="100k"
    def info(self):
        print(f"{self.name} is a {self.occupation} with salary of {self.salary}")

p1=Person()
p1.info()
p2=Person()
p2.name="Zain"
p2.occupation="Graphic Designer"
p2.info()
p3=Person()
p3.name="Wahab"
p3.occupation="Web Developer"
p3.salary="50k"
p3.info()