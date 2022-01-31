'''Tuple are immutable,Idexxing, Slicing, Ordered
tup1=(1,"Seema",98.0, True, 1, 1, 1, "QA", 2, 2, 2, )
print(tup1)
print(tup1[1])
print(tup1[-2])
print(tup1.count(1))
print(tup1.index(98.0))
print(tup1[0:4])
print(tup1[::5]) # Skipping 5 indexing '''

# Is possible to convert tuple into list/set - yes
tup1=(1,"Seema",98.0, True, 1, 1, 1, "QA", 2, 2, 2, )
print(tup1)
l1=list(tup1)
#print("Converting tuple to list: ", type(l1))
print(l1)
s1=set(tup1) # doesn't allow duplicate, unordered and not index based
#print("Converting tuple to Set: ",type(s1))
print(s1)
print("******************************************")
tup2=("SeemaKumar", )  # ("SeemaKumar") It will return all chars, Strings are sequence of chars, seperate by coma
print(tup2)
print(len(tup2))
print("*******************************")
'''List of Tuples'''
l3=[(1, 3, 5,), (2, 4, 6), (10, 20, 30)]
print(l3[1][2])
'''Tuple class constructor'''
t4=tuple(["Java", "Python", "Automation"])
print(type(t4))
print(t4[1])
print("-------------Tuple Un-Packaging------------------")
x,y,z=t4
print("Assigning values to variables: ",x, y, z)
print("--------------------------------------------------")
#tuples
t1=(3, 5, 10)
t2=(10, 20, 30)
t3=(100, 200, 300)
tupl=[t1, t2, t3]
'''for x in tupl:
    print("t1: ", x[0])
    print("t2: ", x[1])
    print("t3: ", x[2])'''
for x, y, z in tupl:
    print(x)
    print(y)
    print(z)
