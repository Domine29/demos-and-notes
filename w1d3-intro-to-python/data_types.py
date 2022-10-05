a_small_number = 4
x = 5

a_string = "hi\"hivuz"
another_string = 'jd\'diuh'


number = 4


# print(type(a_string))
# print(a_string, another_string)

# print( "This is my formatted string {0}  {1} ".format(a_string, number) )
print( f"This is my formatted string {a_string} " )

boolean = True

# print(type(boolean))
# print(type(a_small_number))

# lists

berries = ['grape', 'tomato', 'cucumber', 'eggplant', 'banana', 'watermelon', 'pumpkin']

# print(type(berries))

# print(berries[-1])
# print(berries[0])
# print(berries[1:4])
# print(berries[:3])
# print(berries[2:])

# print(berries[::-1])


berries.append(5)
# print(berries)
berries.extend([3, 'strawberry'])
# print(berries)

popped = berries.pop()

# print(popped)
# print (berries)
popped = berries.pop(1)  # removes item at index and returns it

removed = berries.remove('watermelon') #removes item with specifies value

berries.insert(2, 'hello')

# print(berries)
berries[0] = 'hi'
# print(berries)

#tuples

days_of_the_week = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')

# days_of_the_week[6] = 'something'  #This will not work



#dictionary
my_dictionary = {'key': 'value', 'key2':'value2'}

user = {
    'name': 'jeff',
    'age': '40',
    'job': 'dev'
}

print(user['name'])


user['address'] = 'address 21343'
print(user)

people = [
    {
        'name': 'alice',
        'age': 44,
        'jobs': {'internship':'hiudhsf','1stjob': 'uhdifhsdpo'}
    },
    {
        'name': 'bob',
        'age': 31,
        'job': 'dog walker',
    },
    {
        'name': 'carol',
        'age': 65,
        'job': 'life coach',
    },
]

print(people[1]['age'])

print(people[0]['jobs']['1stjob'])

people[0]['address'] = 'some address'
print (people)

print(user.values())
