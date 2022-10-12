

class Mammal:
    def __init__(self):
        self.is_mammal = True
        self.has_teeth = True

class Animal(Mammal):
    animals = []
    def __init__(self, name):

        super().__init__()

        self._name = name
        self._legs = 2

    def eat(self, food):
        print(f"{self.name} eats a {food}.")

    def speak(self):
        print('I''m an animal')

    @property
    def name(self):
        print('in getter')
        return self._name

    @name.setter
    def name(self, n):
        print('in setter')
        self._name = n

    @property
    def legs(self):
        return self._legs

    @legs.setter
    def legs(self, x):
        self._legs = x

    

class Dog(Animal):
    def __init__(self, name, is_service_animal, legs):
        # parent_temp_instance = super()
        # parent_temp_instance.__init__(self, name)

        super().__init__(name)
        
        self.is_service_animal = is_service_animal
        self.legs = legs
        # super().animals.append(self)
    
    def speak(self):
        super().speak()
        print('Bark! Bark!')
    

class Cat(Animal):
   def speak(self):

        print('Meow! Meow!')
        super().speak()

   

spot = Dog('Spot', False, 4)
# print(spot.is_mammal)
# print(spot.has_teeth)
# print(spot.name)
# spot.name = 'bibo'
# print(spot.name)
# spot.speak()

# print(spot.is_service_animal)
# print(spot.legs)
# print(spot.animals)
# print(spot.mammal)

# fido = Dog('fido', True, 3)
# print

# garfield = Cat('Garfield')
# print(garfield.name)
# garfield.speak()
# garfield.eat('tuna')