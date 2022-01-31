status = False
names = ["Python", "Java", "JS", "CSharp"]

for name in names:
    if name == "JS":
        status = True
        break
    else:
        print("Wait we are still searching")
if status:
    print("We glad we found")
else:
    print("Sorry  we could not found ")
