"""l1=[1,2 ,3, 5]
def sqr(num):
    print(num*num)
for x in l1:
    sqr(4)"""
data = lambda num: num * num
result = data(5)
print(result)

newData = lambda num1, num2, num3: num1 * 2 + num2 * 3 + num3 * 4
print(newData(1, 2, 3))
