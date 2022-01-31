#  Arbitrary Arguments
#  how to print multiple values, Can pass the index to retrieve
#  specific value
def print_name(*args):
    # print(args)
    # print(args[4])
    print(type(args))  # Return type is tuple
    for name in args:
        print(name)


print_name("Python", "Java", "#C", "JavaScript", "Ruby");


def get_sum_of_all_Num(*args):
    print(sum(args))


def get_min_Num(*args):
    print(min(args))


def get_max_Num(*args):
    print(max(args))


def hello_world(fname,*args, **kwargs):
    print(fname)
    print(args)
    print(kwargs)


get_min_Num(20, 90, 80, 70)
get_max_Num(890, 70, 60, 70)
get_sum_of_all_Num(10, 20, 30, 70)
hello_world(12, 39, 90, name="Seema", Phone=12345, country="India")
