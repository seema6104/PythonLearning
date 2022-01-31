def helloworld():
    print("Hello Python")
    c = 10 + 90
    return c
    print(c)
    print("Bye")


print("*************************")


def sum(num1, num2):
    result = num1 + num2
    print("Sum function result Inside fun: ", result)
    return result


# print(sum(10, 30))
print("*****************************")


def sumFun(n1, n2):
    sumResult = n1 + n2
    return sumResult


def deafultValFun(n1, n2, n3=0, n4=9):
    r = n1 + n2
    return r


# Called as keyword arguments
def greeting(fname, lname, marks):
    print("Welcome " + fname + " " + lname + "", marks)


def check_even_num(list1):
    even_num = []

    for x in list1:
        if x % 2 == 0:
            even_num.append(x)
        else:
            pass
        return even_num


print("check_even_num: ")

helloFun = helloworld()
print("HelloWord Function: ", helloFun)
sunRes = sum(10, 30)
print("Sum Outside Function: ", sunRes)
newResult = sumFun(12, 94)
print("SunFun Function: ", newResult)
defaulResult = deafultValFun(23, 90, 14)
print("defaultValFun: ", defaulResult)
greetingFun = greeting("Seema", "Kumar", 90)  # Returning none also after printing
greetingFun2 = greeting(fname="John", lname="Smith", marks=90)  # Returning none also after printing
print(greetingFun)
print(greetingFun2)
resu_list = check_even_num([2, 80, 20])
if len(resu_list) >0:
    print(resu_list)
else:
    print("Sorry not found")