def can_drink(age, country):
    if age >= 21 or age >= 18 and country != 'USA' :
        return True
    elif country == 'Antarctica' :
        return True
    elif age != 21:
        print('not 21')
    else: 
        return False

print(can_drink(20, 'USA'))
print(can_drink(21, 'USA'))
print(can_drink(18, 'UK'))
print(can_drink(4, 'Antarctica'))


# for loops

my_list = ['a', 'b', 'c']
for item in my_list:
    print(item)


# Range
l = range(4)
print(type(l))

for x in range(10):
    print(x)

for x in range(2,6):
    print(x)

print('step range')

for x in range(6, 2,-1 ):
    print(x)


# enumerate
for index, element in enumerate(my_list):
    print(index, element)
    
    if index == 1:
        break #to end loop early

    
# looping over dictionaries

person = {
            'name': 'alice',
            'age': 44,
            'jobs': {'internship':'hiudhsf','1stjob': 'uhdifhsdpo'}
        }

for key in person:
    print(person[key])

for val in person.values():
    print(val)


# while loops
x = 9
while x > 0:
    print(x)
    x -= 1  # same as x= x-1

# destructive and non destructive methods
string = 'something'
string2 = string.capitalize()           #non-destructive
replaced = string.replace('m','123' )   #non-destructive
print(string)
print(replaced)



my_list.append('r') # destructive

print(my_list)

my_input = input("please enter your name: \n ")

print(my_input)