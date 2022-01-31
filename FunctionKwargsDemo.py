def print_name(**kwargs):
    print(kwargs)
    print(type(kwargs)) # return type is dictionary
    print(kwargs["address"]) # Can pass the spesific vales


print_name(name="Seema", address="US", phone=2342341234)
