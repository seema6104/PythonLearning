'''Collections of items,each item have key and value pairs
Dynamic in nature, unordered, can fetch the value by key
keys should be unique but values can be duplicate, can use dict() constructor

emp = {"QA": ["Seema", "Marian", "Allison"], "Dev": "David", "DevOps":"John", "SecurityCode": 89, 67: "Python"}  #Can have any kind data
print(emp)
print(type(emp))
print(emp["Dev"])  #Pass the Key,fetch the value
#  print(emp["Developer"]) KeyError: 'Developer'
print(emp.get("QA"))
print(emp["QA"][2])  #Fetching the value by index
emp1=emp["QA"]
print(emp1[0])
emp={"QA":["Seema", "Marian", "Allison"], "Dev": {"Frontend": "Mike", "Backend": "Willi"}} # Dictionary inside dictionary
print(emp.get("QA"))
print(emp.get("Dev").get("Frontend"))
print(emp["Dev"]["Backend"]) # Cant use .get() method when using [] brackets
#myDict=dict([()])
emp1=emp.get("Dev")
emp_name=emp1.get("Backend")
print(emp_name)
print(emp["Dev"]["Backend"])
emp["Manager"]="xyz"
print(emp)
emp["Manager"]="Sat"
print(emp)
#  emp.pop("QA")
emp.popitem()  # Last In First Out remove
print(emp)
print(len(emp))
print(emp.keys())
print(emp.values())
print(emp.items())
print("**********************************")
del emp # NameError name 'emp' is not defined.
print(emp)
'''
empDict= dict(QA= "Seema", Dev="Mike", qa="Smantha", Qa="Roger")  #Case-sensitive, no need quote when assigning key, cant use same key
print(empDict)
#New dictionary / List of Tuple
newemp = dict([(1, "Python"), (2, "Java"), (3, "Java Script")])
print('Printing new emp: ', newemp)
