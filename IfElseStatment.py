marks = 97
print("A+") if marks > 90 else print("A")
salary = input("Please enter your salary for loan: ")  # Input statment is always strings
print(type(salary))
sal = int(salary)  # Convert Salary string in to int (type cast)
if sal > 40000:
    print("Eligible for car loan")
    if sal > 60000:
        print("Eligible for home loan")
        if sal > 90000:
            print("Premium customer, eligible for all kind of loans")
        else:
            print("Not eligible")
