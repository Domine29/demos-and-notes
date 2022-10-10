class Dog:
    
    def __init__(self, name, breed, color, sound='woof'):   # Dunder
        if type(name) == str:
            self.name = name 
        else: 
            self.name = 'random'
            print('issue')
        self.__breed = breed
        self.color = color
        self.sound = sound
        self.email = self.__create_email()
        
    
    def speak(self):
        print(f' >> hello my name is {self.name} {self.sound}')

    def fetch(self, item):
        print(f'>> {self.name} is fetching {item}')

    def __create_email(self):
        self.email = self.name+'@canine.com'
        return self.email

    def __str__(self):
        try:
            if self.email: 
                print('using email')
                return f'name: {self.name}, email: {self.email}'

        except:
            print('creating email')
            return f'name: {self.name}, email: {self.create_email()}'

    
    def __add__(self, other):
        return f'{self.name}, {other.name}'

