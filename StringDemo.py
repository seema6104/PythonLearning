first_name="Seema"
last_name='kumar'
print(first_name,last_name)
print("Concatenate Strings: "+first_name+last_name)
name="Can' have single quote under double quote but not double quote"
print(name)
prog='cant have single quote under single quote'
print(prog)
#for tab = \t, \n= new line

escape= "\"python\""
print(escape)
print(type(escape))
'''String len method will include white spaces
'''
print(len(escape))
print(escape.index('t'))
print(escape.replace('t', 'l'))
print(escape.split('h'))
print(escape.upper())
print(escape.lower())
print("***********************************************8")
print(escape.title())
print(escape.isdigit())
print(escape.isprintable())
print(escape.isdecimal())
print(escape.isalpha())
print(escape.isidentifier())
print(escape.__init_subclass__())
'''curly braces will be replace with python, multiple curly brace and index, same variable have Dynamic typing'''
myName="I know {}".format('python')
print(myName)
multRep="I know {2}{1}{0}".format('python','java','JS')
print(multRep)
multRep="I know {}{}{}".format('python','java','JS')
print(multRep)
multRep="I know {p}{j}{js}".format(p='python',j='java',js='Java Script')
print(type(multRep))
indexOutRange="I know {p}{j}{js}".format(p='python',j='java',js='Java Script')# indexOutRange
print(type(indexOutRange))
'''Formatting String litres'''
strLitName = 'Seema'
print("My name is {strLitName}")#will print variable in quote
print(f"My name is {strLitName}")# f will print variable value in quote
pyLang="I know python"
print(f"I know java {strLitName} {pyLang}")