class Dog:
    # class attributes
    species = "Canis Lupus Familiaris" 
    legs = 4
    list_of_dogs = []

    def __init__(self, name, breed, l=4):
        self.name = name        #instance attributes
        self.breed = breed
        if l != 4:
            self.legs= l

        self.email = self.create_email() 

        Dog.list_of_dogs.append(self)

    def create_email(self):
        return f'{self.name}@cp.com'

    def __str__(self):
        return f'{self.name}  {self.breed}  {self.email}'

    
