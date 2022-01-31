x = 1
while x < 10:
    print(x)
    x = x + 1
'''x=5  #infinite loop
while x<10:
    print("Python")'''
'''num=100
while num<15:
    print(num)
    num=num+1
else:
    print("Condition not met")'''
print("***********Break Statement************")
num = 10
while num < 15:
    print(num)
    num = num + 1
    if num == 10:
        print("")
        break
else:
    print("Condition not true")
print("***********Continue Statement*******************")
a=10
while a<20:
    a=a+1
    if a==5:
        continue
    print(a)