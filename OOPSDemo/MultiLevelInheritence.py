class classA:
    def methodA(self):
        print("Coming from class A")

    def Hello_world(self):
        print("Hello_World from class A")


class classB(classA):
    def methodB(self):
        print("Coming from class B")

    def Hello_world(self):
        print("Hello_World from class B, Method overriding")
        super().Hello_world()

class classC(classB):
    def methodC(self):
        print("Coming from class C")

    def Hello_world(self):
        print("Hello_World from class C, Method overriding")


obj1 = classC()
obj1.Hello_world()
obj1.methodA()
obj1.methodB()
obj1.methodC()
