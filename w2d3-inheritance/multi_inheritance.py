
import math 
class Bug():
    def __init__(self):
        self.name = 'George' 


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def work(self):
        print(f"{self.name} is working hard as they can at {self.job}.")


class Computer:
    def __init__(self, number_of_cores):
        self.number_of_cores = number_of_cores

    def compute(self):
        print(round(math.pi, self.number_of_cores))

toaster = Computer(6)
toaster.compute()

class Cyborg(Person, Computer):
    def __init__(self, name, job, number_of_cores):
        Person.__init__(self, name, job)
        Computer.__init__(self, number_of_cores)

        ## another way of calling both init functions
        # super().__init__(name, job)
        # super(Person, self).__init__(number_of_cores)

    def work(self):
        for code in range(self.number_of_cores):
            Person.work(self)

    def create_something(self):
        self.bug = Bug()



terminator = Cyborg('Arnold', 'terminatior', 16)
print(terminator.name)
print(terminator.job)
print(terminator.number_of_cores)


terminator.work()
# print(terminator.bug.name)
terminator.create_something()
print(terminator.bug.name)

