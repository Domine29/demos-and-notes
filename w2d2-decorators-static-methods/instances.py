from dog_class import Dog
from methods import Pizza

bibo = Dog('bibo', 'huskey', 3)
    
# print(bibo.name)
# print(vars(bibo))

# print(Dog.species)
# print(Dog.legs)
# print(bibo.legs)

fifo = Dog('fifo','huskey' )
print(vars(fifo))
print(fifo.list_of_dogs)
# print(fifo.email)
# print(Dog.legs)
# print(fifo.legs)

for d in Dog.list_of_dogs:
    print(f'{d.name}  {d.breed} ')


print(Pizza.circle_area(5))