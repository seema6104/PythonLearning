class Person:

    def welcome(self):
        print("Hello python")

    def hello_world(self):
        print("Hello world")

    def sum(self, num1, num2):
        print(num1 + num2)


def hello_world():
    print("Hello world outside the class")


p = Person()
p.welcome()
p.hello_world()
hello_world()
print(hello_world)  # without () output
print(p.welcome)  # without () output
p.sum(12, 34)
# setting the properties as variables using p object
p.name="Seema"
p.phone=90909090
p.country="India"
p.city="Banglore"

q=Person()
q.name="Rihana"
q.phone=90909090
q.country="USA"
q.city="Michigan"

print(p.name)
print(q.name)
print(p.city)
print(q.city)

