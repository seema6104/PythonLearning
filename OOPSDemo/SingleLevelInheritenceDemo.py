class Base:
    name="Seema"
    def baseMethod(self):
        print("I am in base class")


class Child(Base):
    company="Selenium"
    def childMethod(self):
        print("I am in child class")


""" without inheritance
c = Child()
c.childMethod()
b = Base
b.baseMethod()"""
c=Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.company)