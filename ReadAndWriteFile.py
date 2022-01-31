import os

"""f = open("Demo1.txt")
data = f.read()
print(f.name)
print(f.mode)
print(data)  # FileNotFoundError
print(f.closed)  #Closed or not
f.close()"""

filePath = os.getcwd()  # Current working directory
print(filePath)
with open(os.path.dirname(filePath)+ "\\Demon1.txt") as f:
    # with open("Demo1.txt") as f:
    print("Current state is", f.closed)
    data = f.read()
    print(data)
print("State of the file is ", f.closed)
