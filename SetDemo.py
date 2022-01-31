
''' Sets - set - Unordered and  no duplicates {"M", 10.90}, values are unique  '''
mySet={98, 89, 76, 12, 2, 888, 98, 98}
'''print(mySet)
mySet.add(777)
print(mySet)
mySet.pop()
print(mySet)
mySet.remove(888)
print(mySet)
# mySet.remove(8888) KeyError: 8888, element is not there
mySet.discard(7775) # If dont found the element will not throw an error
print(mySet)'''
mySet2={98, 89, 76, 12, 2, 888, 98,"Seema",  98}
print(mySet2)
myset3=mySet2.copy() # Will copy all elements from mySet2
#mySet2.clear()
print(myset3) # Clear all the values in set
set1=set({"Seema", 1, 4, 6, 8}) #will get new set another way to create set
print(set1)
set2=set(("Python", "Java", "JS"))
print(set2)