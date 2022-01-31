name = "SeemaKumar"
# for a in name:
#   print(a)
marks = [70, 80, 90, 100]
totalMarks = 0
for m in marks:  # another way can pass values directly [70, 80, 90, 100]
    totalMarks = totalMarks + m
print("Final value is " + str(totalMarks))  # type cast int type  variable
print("Final value is ", totalMarks)

print("***********************************")
sent = {10, 30, 90, "Seema", 90.0, "Python", 10, 10}  # set don't allow duplicate
# for abc in sent:
#   print(abc)

mydict = {1: "Seema", 2: "Python", "Name": "Kumar"}
# for d in mydict.items(): # items method will fetch all key and values
'''for d, b in mydict.items():
    print(d)
    print(b)
for a in mydict.values():  # will fetch only values
    print(a)
for b in mydict.keys():
    print(b)'''
for x in range(30):  # range() is a predefined class, by default starting from 0
    print(x)
# How to print even and odd numbers by mod % operator
evenList = []
oddList = []
for x in range(40):
    if x % 2 == 0:
        evenList.append(x)
    else:
        oddList.append(x)
print(evenList)
print(oddList)
