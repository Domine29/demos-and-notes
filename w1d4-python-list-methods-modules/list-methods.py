# Switch case

from audioop import add

# lang = input("What's your favorite programming lang?")
#using if -else
# if (lang == 'python'):
#     print('you can do data stuff with that')

# elif (lang == 'javascript'):
#     print('you can do frontend stuff with that')

# else:
#     print('all languages are cool anyways')

## match and case
# match lang:
    # case 'python'|'Python':
    #     print('you can do data stuff with that')
    # case 'javascript':
    #     x = 4-4
    #     print(x)
    #     print('you can do frontend stuff with that')
    # case _:
    #     print('all languages are cool anyways')


# Lambda function - temporary , unamed (anonymous) function

def add_one(x):
    return x+1

add_two = lambda x : lambda y : x+y

func = add_two(7)
print(func(2))

# list methods
# 

my_list = [1,2,3,4,5,6,7,8,9,10]

# map - creates new list using a function
new_list = map(lambda item : item+2 , my_list)
print(list(new_list))

# filter
new_list = filter(lambda item: item % 3 == 0, my_list)

print(list(new_list))

def computeSum(aggr, item):
    return aggr+item


# reduce
# import functools
from functools import reduce
x_list = ['s', 'e', 'a']

product = reduce(lambda agg, item: agg+item, x_list)
# print(product)


#sort
people = [
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'bob',
        'age': 49,
        'job': 'dog walker',
    },
    {
        'name': 'carol',
        'age': 35,
        'job': 'life coach',
    },
]

sorted_people = sorted(people, key=lambda p: p['age'], reverse=True)
# print(sorted_people)
# print(people)

people.sort(key=lambda p: p['name'])
# print(people)


# zip
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

zipped = zip(numbers, letters)
# print(list(zipped))

dictionary = dict(zipped)

print(dictionary)


