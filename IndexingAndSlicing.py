'''Pythn supports indexing and negative indexing, Negative indexing reverse the strings'''
sent="Python is very easy"
print(sent[3])
print(sent[-1])  # will print reverse order when providing nagative number
# Slicing
name="MynameisSeema"
print(name[2:6])#Start From 2 stop on 6
name="PythonIsVeryEasy"
print(name[6:8])
print(name[::2])#By default starting from 0, skipping change the step counts
print(name[::-1])#will print the entire string with double coln
