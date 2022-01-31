# Swaping numbers
x = 50
y = 60
'''tem=x
x=y
y=tem
print(x, y)'''
# Find largest number
num1 = 100
num2 = 140
num3 = 120
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)
