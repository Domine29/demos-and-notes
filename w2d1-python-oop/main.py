from classDog import Dog

bibo = Dog('bibo','grey', 'Huskey' ) #instantiate class
print(bibo)
# print(bibo.color)
# bibo.speak()
# print(bibo.breed)


print(bibo)


fifo = Dog('fifo', 'blond', 'golden retreiver', 'bork bork')
# print(fifo.name)
# fifo.fetch('ball')

# print(bibo + fifo)

# print(3+'7')
# print(fifo)

dogs = [bibo, fifo]

for dog in dogs:
    print(dog.name)