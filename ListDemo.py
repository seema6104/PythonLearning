list1=[10,50,60,90]
print(list1)
list2 = ["Seema", 10, 50, 60, True]
print(list2)
list3=list1+list2
print(list3)
print(len(list3))
list3 = [91, 2, 91, 10, 7, 8]
print(list3[::-1])
print(list3.count(91))
print(list3[1:5])#start count and end count
print(type(list3))
list3[3]=666  # Replacing/Override the value
#  print(list3)
list1.append("Seema Kumar")  #Append the value at the last
print(list1)
list1.insert(0, 555)  # replacing the indexed value
print(list1)
'''List will append char by char, list is Iterable '''
myName= "Seema"
myLname = "Kumar"
list4=["Seema", "Kumar", "Pyton"]
list4.extend(myName)
list4.extend(myLname)
print(list4)
popObj=["Python", "Java", "JS", "QFT"]
popObj.pop(1) # Indexed  value will be removed
print(popObj)
# Removing the element by value
popObj.remove("Python")
print(popObj)
listSort=[10,50,60,90, 120, 200, 1000]
listSort.sort()# Will print value in accending order
print(listSort)
listSort.reverse()
print(listSort) # Will print value in descending order
mylist=[10, 90, 80, ["Seema", "Selenium", "TestNG"]]
print(mylist)
print(mylist[2][1])