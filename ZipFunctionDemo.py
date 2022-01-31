#calling the zip function
name=["Seema", "Mike", "Peter", "Python"] #List
marks=[70, 90, 80]
address=["abc", "xyz", "Demo"]
data=zip(name, marks, address)
print(data)
mydata=list(data)
print(mydata) # returning list of tuples, will return only pair single will not
l1=[1, 2, 3, 5]
print(list(zip(l1)))
name1={"Seema", "Mike", "Peter", "Python"} #set
mark={70, 90, 80, 90}
mydata=zip(name1, mark)
myData=list(mydata)
#unzipping
a, b=zip(*myData)
print(a)
print(b)




