class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0
        self.__dead = False

    @property
    def age(self): 
        print('getter method called')
        return self._age

    @age.setter
    def age(self, a):
        print('setter method called')
        self._age = a
        if (a > 100):
            self.__dead = True

    @property
    def dead(self):
        return self.__dead

    



alice = Person('alice')

# print(alice.name)
# print(alice.age)

alice.age = 101

print(alice.age)
# print(alice.dead)

# alice.dead = False    #does not work

# alice.name = 'zaynab'
# print(alice.dead)
# print(vars(alice))
# print(alice.name)