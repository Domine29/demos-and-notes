def gimme_five( ):
    return 5

print(gimme_five())

def add_one(n):
    return n+1

print(add_one( 5))

def describe_berries(n:int, color:str):
    print(f'I have {n} {color}berries')

def describe_berries(n=2, color='blue'):
    print(f'second function: I have {n} {color}berries')

describe_berries(3, 'orange')
describe_berries(3, 'blue')
describe_berries( 'blue', 3)  # wrong order
describe_berries( color='red',n= 3)

# def describe_berries2(n=2, color='blue'):
#     print(f'I have {n} {color}berries')

# describe_berries2(color="red",  n=4)


def print_all_args(*args):  #can args be capped at a certain number?
    print(args[1:3])

print_all_args('red', 'blue', 'green')

def who_am_i(**kwargs):
    print(type(kwargs))

    for kw in kwargs:
        print(f'{kw} : {kwargs[kw]}')

who_am_i(name='dan', age=20, job='skydiving instructor')


