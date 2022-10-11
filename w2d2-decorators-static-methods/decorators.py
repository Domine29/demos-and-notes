from datetime import datetime

def add_one(num):
    return num +1

def multiply_by_two(num):
    return num * 2


def print_time_and_also(func):

    def wrapper_function(*args, **kwargs):
        print(datetime.now())
        result = func(*args, **kwargs)
        print(datetime.now())
        return result

    return wrapper_function

print_time_and_also_add_one  = print_time_and_also(add_one)
# one_plus_one = print_time_and_also_add_one(1)
# print(one_plus_one)

print_time_multiply = print_time_and_also(multiply_by_two)
# result = print_time_multiply(2)
# print(result)

@print_time_and_also
def subrtact_three(num):
    return num - 3

@print_time_and_also
def multiply_by_two(num):
    return num * 2


print(multiply_by_two(subrtact_three(7)))
    
